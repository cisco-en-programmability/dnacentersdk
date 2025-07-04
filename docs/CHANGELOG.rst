Changelog
=========

All notable changes to this project will be documented in this file.

The format is based on `Keep a
Changelog <https://keepachangelog.com/en/1.0.0/>`__, and this project
adheres to `Semantic
Versioning <https://semver.org/spec/v2.0.0.html>`__.

`Unreleased <https://github.com/cisco-en-programmability/dnacentersdk/compare/v2.10.1...develop>`__
---------------------------------------------------------------------------------------------------

`2.10.1 <https://github.com/cisco-en-programmability/dnacentersdk/compare/v2.10.0...v2.10.1>`__ - 2025-07-04
------------------------------------------------------------------------------------------------------------

Fixed
~~~~~

- Fixed a bug that occurred when the response was empty.
- Fixed validation for the ``value`` field in filters of the function
  ``retrieves_the_list_of_clients_by_applying_complex_filters_while_also_supporting_aggregate_attributes``
  to accept ``string``, ``integer``, and ``number`` types as supported
  by the API.
- Fixed function name from
  ``download_unmaskedraw_device_configuration_as_z_ip`` to
  ``download_unmaskedraw_device_configuration_as_zip``.

.. _section-1:

`2.10.0 <https://github.com/cisco-en-programmability/dnacentersdk/compare/v2.9.1...v2.10.0>`__ - 2025-06-09
-----------------------------------------------------------------------------------------------------------

Added
~~~~~

- Backup service.
- Industrial configuratiom service.
- Know your network service.
- Restore service.
- Wired service. ### Changed
- Renamed ``get_auditlog_summary`` to ``get_audit_log_summary``
- Renamed ``get_auditlog_parent_records`` to
  ``get_audit_log_parent_records``
- Renamed ``get_eventartifacts`` to ``get_event_artifacts``
- Renamed ``get_auditlog_records`` to ``get_audit_log_records``
- Renamed
  ``gets_the_total_network_device_interface_counts_in_the_specified_time_range_when_there_is_no_start_and_end_time_specified_returns_the_latest_interfaces_total_count``\ to
  ``gets_the_total_network_device_interface_counts``.
- Moved ``get_port_channels`` to LAN Automation service ### Removed
- The v1 alias functions were all removed. Example… if your using
  “application_v1” you must be able to change it to “application”.

.. _section-2:

`2.9.1 <https://github.com/cisco-en-programmability/dnacentersdk/compare/v2.9.0...v2.9.1>`__ - 2025-05-09
---------------------------------------------------------------------------------------------------------

Fix
~~~

- Modification of the get_reserve_ip_subpool_v1 function.

.. _section-3:

`2.9.0 <https://github.com/cisco-en-programmability/dnacentersdk/compare/v2.8.14...v2.9.0>`__ - 2025-05-09
----------------------------------------------------------------------------------------------------------

.. _added-1:

Added
~~~~~

- Add support of DNA Center versions (‘3.1.3.0’)
- Adds modules for v3_1_3_0
- Modules 2_2_2_3, 2_2_3_3, 2_3_3_0 were removed

.. _section-4:

`2.8.14 <https://github.com/cisco-en-programmability/dnacentersdk/compare/v2.8.13...v2.8.14>`__ - 2025-05-05
------------------------------------------------------------------------------------------------------------

.. _fix-1:

Fix
~~~

- This release allows the
  download_unmaskedraw_device_configuration_as_z_ip_v1 function to
  correctly respond with a binary.

.. _section-5:

`2.8.13 <https://github.com/cisco-en-programmability/dnacentersdk/compare/v2.8.12...v2.8.13>`__ - 2025-04-25
------------------------------------------------------------------------------------------------------------

.. _fix-2:

Fix
~~~

- Correction in error handling.
- Added function aliases that have been renamed due to fixes.
- Deprecated functions were established that would disappear in the
  future.
- Deprecated functions (export_projects_v1, clone_given_template
  get_projects_v1, export_projects, clone_given_template_v1,
  get_projects, get_all_keywords_of_clis_accepted,
  get_all_keywords_of_clis_accepted_v1,
  run_read_only_commands_on_devices_v1,
  run_read_only_commands_on_devices,
  cisco_dna_center_packages_summary_v1, release_summary_v1,
  cisco_dna_center_packages_summary, nodes_configuration_summary_v1,
  release_summary , nodes_configuration_summary,
  get_all_mobility_groups, get_all80211be_profiles_v1,
  get_all80211be_profiles, get_all_mobility_groups_v1,
  gets_interfaces_along_with_statistics_data_from_all_network_devices_v1,
  gets_interfaces_along_with_statistics_data_from_all_network_devices,
  get_the_interface_data_for_the_given_interface_idinstance_uuid_along_with_the_statistics_data_v1
  )

.. _section-6:

`2.8.12 <https://github.com/cisco-en-programmability/dnacentersdk/compare/v2.8.11...v2.8.12>`__ - 2025-04-08
------------------------------------------------------------------------------------------------------------

.. _fix-3:

Fix
~~~

- Fix in ignore_the_given_list_of_issues_v1 function in versions 2.3.7.6
  and 2.3.7.9.

.. _section-7:

`2.8.11 <https://github.com/cisco-en-programmability/dnacentersdk/compare/v2.8.10...v2.8.11>`__ - 2025-04-03
------------------------------------------------------------------------------------------------------------

.. _fix-4:

Fix
~~~

- Resolution of issues #206 and #205.
- sync_devices functionality has been added to devices.
- Adjusted function names to avoid looping.

.. _section-8:

`2.8.10 <https://github.com/cisco-en-programmability/dnacentersdk/compare/v2.8.9...v2.8.10>`__ - 2025-04-01
-----------------------------------------------------------------------------------------------------------

.. _fix-5:

Fix
~~~

- This release allows the
  downloads_a_specific_i_cap_packet_capture_file_v1 function to
  correctly respond with a binary.

.. _section-9:

`2.8.9 <https://github.com/cisco-en-programmability/dnacentersdk/compare/v2.8.8...v2.8.9>`__ - 2025-03-13
---------------------------------------------------------------------------------------------------------

.. _fix-6:

Fix
~~~

- Correction in the functions set_banner_settings_for_a_site,
  set_dhcp_settings_for_a_site, set_n_t_p_settings_for_a_site,
  set_time_zone_for_a_site, set_d_n_s_settings_for_a_site,
  set_telemetry_settings_for_a_site, set_aaa_settings_for_a_site. #174

.. _section-10:

`2.8.8 <https://github.com/cisco-en-programmability/dnacentersdk/compare/v2.8.7...v2.8.8>`__ - 2025-03-10
---------------------------------------------------------------------------------------------------------

.. _fix-7:

Fix
~~~

- Modification of the data type in offset and limit. In the
  get_ap_profiles function of the wireless family.

.. _section-11:

`2.8.7 <https://github.com/cisco-en-programmability/dnacentersdk/compare/v2.8.6...v2.8.7>`__ - 2025-03-05
---------------------------------------------------------------------------------------------------------

.. _fix-8:

Fix
~~~

- Error correction in the user_and_roles module

.. _section-12:

`2.8.6 <https://github.com/cisco-en-programmability/dnacentersdk/compare/v2.8.5...v2.8.6>`__ - 2025-02-27
---------------------------------------------------------------------------------------------------------

.. _added-2:

Added
~~~~~

- Add support of DNA Center versions (‘2.3.7.7’)

.. _section-13:

`2.8.5 <https://github.com/cisco-en-programmability/dnacentersdk/compare/v2.8.4...v2.8.5>`__ - 2025-02-21
---------------------------------------------------------------------------------------------------------

.. _fix-9:

Fix
~~~

- correction in the request validation structures. In the
  deploy_template functions in version 1 and 2. In 2.3.5.3, 2.3.7.6 and
  2.3.7.9.

.. _section-14:

`2.8.4 <https://github.com/cisco-en-programmability/dnacentersdk/compare/v2.8.3...v2.8.4>`__ - 2025-02-17
---------------------------------------------------------------------------------------------------------

.. _fix-10:

Fix
~~~

- fix in create_webhook_destination, update_webhook_destination,
  get_webhook_destination functions. In versions 2.3.7.6 and 2.3.7.9.

.. _section-15:

`2.8.3 <https://github.com/cisco-en-programmability/dnacentersdk/compare/v2.8.2...v2.8.3>`__ - 2025-01-23
---------------------------------------------------------------------------------------------------------

.. _fix-11:

Fix
~~~

- Issues #188 and #189 have been resolved.
- Alias have been adjusted for backward compatibility.
- Some functions were changed in versions 2.3.7.6 and 2.3.7.9 to handle
  files.

.. _added-3:

Added
~~~~~

- Cisco_IMC module added

.. _section-16:

`2.8.2 <https://github.com/cisco-en-programmability/dnacentersdk/compare/v2.8.1...v2.8.2>`__ - 2025-01-15
---------------------------------------------------------------------------------------------------------

.. _fix-12:

Fix
~~~

- A new alias function has been added to maintain compatibility with
  event_management in versions 2.3.7.6 and 2.3.7.9.
- The new function is get_eventartifacts which was already present in
  previous versions but was changed to get_event_artifacts in 2.3.7.6
  and 2.3.7.9.
- issues #186

.. _section-17:

`2.8.1 <https://github.com/cisco-en-programmability/dnacentersdk/compare/v2.8.0...v2.8.1>`__ - 2025-01-13
---------------------------------------------------------------------------------------------------------

.. _fix-13:

Fix
~~~

- changing the api version in the configuration files
- Resolved issue #174
- removal of -v1 from reference urls in the documentation
- Fixed a bug in site_design in the uploads_floor_image function in
  versions 2.3.7.6 and 2.3.7.9.

.. _section-18:

`2.8.0 <https://github.com/cisco-en-programmability/dnacentersdk/compare/v2.7.7...v2.8.0>`__ - 2024-12-11
---------------------------------------------------------------------------------------------------------

.. _added-4:

Added
~~~~~

- Add support of DNA Center versions (‘2.3.7.9’)
- Adds modules for v2_3_7_9

.. _section-19:

`2.7.7 <https://github.com/cisco-en-programmability/dnacentersdk/compare/v2.7.6...v2.7.7>`__ - 2024-11-19
---------------------------------------------------------------------------------------------------------

Bug fix
~~~~~~~

- The get_templates_details function was added because it was named
  incorrectly.There was an “s” missing from the word templates.

.. _section-20:

`2.7.6 <https://github.com/cisco-en-programmability/dnacentersdk/compare/v2.7.5...v2.7.6>`__ - 2024-11-12
---------------------------------------------------------------------------------------------------------

ADD
~~~

- authentication_management module added

.. _section-21:

`2.7.5 <https://github.com/cisco-en-programmability/dnacentersdk/compare/v2.7.4...v2.7.5>`__ - 2024-11-11
---------------------------------------------------------------------------------------------------------

.. _add-1:

ADD
~~~

- The use of alias in the functions was implemented
- The User Agent parameter was added
- New Modules Such As (ai_endpoint_analytics,
  cisco_trusted_certificates, disaster_revery) were Added

.. _section-22:

`2.7.4 <https://github.com/cisco-en-programmability/dnacentersdk/compare/v2.7.3...v2.7.4>`__ - 2024-09-17
---------------------------------------------------------------------------------------------------------

- Add multipart parameter for file upload in
  site_design:uploads_floor_image.

.. _section-23:

`2.7.3 <https://github.com/cisco-en-programmability/dnacentersdk/compare/v2.7.2...v2.7.3>`__ - 2024-08-19
---------------------------------------------------------------------------------------------------------

- Refactor error message construction in ApiError class
- Injection for requests.Session ### Fixed
- Fixed a problem when exporting the environment variable verify
- Update offset and limit parameter type to support int and str value
- ``accept_cisco_ise_server_certificate_for_cisco_ise_server_integration``
  accept empty payload {} to retry
- Update memberToTags from list to object in ``updates_tag_membership``
- Update offset and limit parameter type to support int and str value

.. _section-24:

`2.7.2 <https://github.com/cisco-en-programmability/dnacentersdk/compare/v2.7.1...v2.7.2>`__ - 2024-08-09
---------------------------------------------------------------------------------------------------------

- Update User-Agent header in RestSession
- Update requirements:

  - python = “^3.8”
  - requests = “^2.32.0”
  - readthedocs-sphinx-search = “^0.3.2” ### Fixed

- Fix function names in 2.3.7.6 ``user_and_roles``

  - From add_role_ap_i to add_role_api
  - From get_a_a_a_attribute_ap_i to get_aaa_attribute_api
  - From get_permissions_ap_i to get_permissions_api
  - From delete_role_ap_i to delete_role_api
  - From get_roles_ap_i to get_roles_api
  - From get_users_ap_i to get_users_api
  - From add_user_ap_i to add_user_api
  - From update_user_ap_i to update_user_api
  - From delete_user_ap_i to delete_user_api
  - From get_external_authentication_setting_ap_i to
    get_external_authentication_setting_api
  - From manage_external_authentication_setting_ap_i to
    manage_external_authentication_setting_api
  - From get_external_authentication_servers_ap_i to
    get_external_authentication_servers_api
  - From add_and_update_a_a_a_attribute_ap_i to
    add_and_update_aaa_attribute_api
  - From delete_a_a_a_attribute_ap_i to delete_aaa_attribute_api
  - From get_a_a_a_attribute_ap_i to get_aaa_attribute_api

.. _section-25:

`2.7.1 <https://github.com/cisco-en-programmability/dnacentersdk/compare/v2.7.0...v2.7.1>`__ - 2024-05-31
---------------------------------------------------------------------------------------------------------

.. _fixed-1:

Fixed
~~~~~

- Updated package version retrieval method from pkg_resources to
  importlib.metadata.

.. _section-26:

`2.7.0 <https://github.com/cisco-en-programmability/dnacentersdk/compare/v2.6.11...v2.7.0>`__ - 2024-05-31
----------------------------------------------------------------------------------------------------------

.. _added-5:

Added
~~~~~

- Add support of DNA Center versions (‘2.3.7.6’)
- Adds modules for v2_3_7_6 ### Changed
- The future library was removed
- The past library was removed
- Changed str to str
- Requirements updated ### Fixed
- Fix headers in ``create_webhook_destination`` and
  ``update_webhook_destination``

.. _section-27:

`2.6.11 <https://github.com/cisco-en-programmability/dnacentersdk/compare/v2.6.10...v2.6.11>`__ - 2023-01-10
------------------------------------------------------------------------------------------------------------

.. _fixed-2:

Fixed
~~~~~

- Configuration template import template - check_type error #142 -
  Fixing required schema.
- Updating request version. Issue #132

.. _section-28:

`2.6.10 <https://github.com/cisco-en-programmability/dnacentersdk/compare/v2.6.9...v2.6.10>`__ - 2023-11-10
-----------------------------------------------------------------------------------------------------------

.. _fixed-3:

Fixed
~~~~~

- Fixed params in 2.3.5.3 claim_a_device_to_a_site from interfaceName to
  ipInterfaceName
- Fixed params in 2.3.5.3 claim_a_device_to_a_site from vlanID to vlanId

.. _section-29:

`2.6.9 <https://github.com/cisco-en-programmability/dnacentersdk/compare/v2.6.8...v2.6.9>`__ - 2023-09-20
---------------------------------------------------------------------------------------------------------

Changed
~~~~~~~

- AP port assignment API not working with DNAC APIs of 2.3.3.0 #126,
  Documetion bug, extra-space in enum.

.. _section-30:

`2.6.8 <https://github.com/cisco-en-programmability/dnacentersdk/compare/v2.6.7...v2.6.8>`__ - 2023-09-12
---------------------------------------------------------------------------------------------------------

.. _changed-1:

Changed
~~~~~~~

- 2_3_3_0 sda sevice ``add_vn`` method update.

.. _section-31:

`2.6.7 <https://github.com/cisco-en-programmability/dnacentersdk/compare/v2.6.6...v2.6.7>`__ - 2023-08-25
---------------------------------------------------------------------------------------------------------

.. _changed-2:

Changed
~~~~~~~

- Update readthedocs settings

.. _section-32:

`2.6.6 <https://github.com/cisco-en-programmability/dnacentersdk/compare/v2.6.5...v2.6.6>`__ - 2023-07-10
---------------------------------------------------------------------------------------------------------

.. _changed-3:

Changed
~~~~~~~

- Change requests-toolbelt minimum version #101

.. _section-33:

`2.6.5 <https://github.com/cisco-en-programmability/dnacentersdk/compare/v2.6.4...v2.6.5>`__ - 2023-05-29
---------------------------------------------------------------------------------------------------------

.. _changed-4:

Changed
~~~~~~~

- user_and_roles::Unable to use user and roles module. #112

.. _section-34:

`2.6.4 <https://github.com/cisco-en-programmability/dnacentersdk/compare/v2.6.3...v2.6.4>`__ - 2023-05-25
---------------------------------------------------------------------------------------------------------

.. _changed-5:

Changed
~~~~~~~

- SDK implementation for API Add Edge Device to Sda fabric on DNAC
  Version 2.3.3.0 inconsistent with previous DNAC versions
  implementation #90
- Documentatin links updated.
- EoX turns to Eox
- SDK function for version 2.3.3.x (v2_3_3_0 /device_onboarding_pnp.py)
  input requirment does not match with API schema from dnac, #103
- Function name changed to assign_device_credential_to_site in
  DNAC2.3.5.0(dnacentersdk/api/v2_3_5_3/network_settings.py) #107
- Function names changed in v2.3.5.0 libs all function got added with 2
  though no change in DNAC APIs #106
- 2.3.3.0 LAN Automation function names are incorrect #105
- Function name changed in 2.3.3.0 from update_ssid_to_ip_pool_mapping
  to update_ssid_to_ip_pool_mapping2 #104
- SDK function for version 2.3.3.x (v2_3_3_0 /device_onboarding_pnp.py)
  input requirment does not match with API schema from dnac, #103
- Poor naming of function: v2_3_5_3/authentication_management.py :
  ``authentication_ap_i( #102``

.. _section-35:

`2.6.3 <https://github.com/cisco-en-programmability/dnacentersdk/compare/v2.6.2...v2.6.3>`__ - 2023-04-28
---------------------------------------------------------------------------------------------------------

.. _changed-6:

Changed
~~~~~~~

- SDK implementation for API Add Edge Device to Sda fabric on DNAC
  Version 2.3.3.0 inconsistent with previous DNAC versions
  implementation #90

- Actual error message was not being used in case of exceptions #98

- SDA :: add_default_authentication_profile #97

- DNA_CENTER_VERIFY not being imported correctly from the environment
  #92, now you can export this as:

  .. code:: zsh

       export DNA_CENTER_VERIFY=false
       export DNA_CENTER_VERIFY=true

  .. rubric:: `2.6.2 <https://github.com/cisco-en-programmability/dnacentersdk/compare/v2.6.1...v2.6.2>`__
     - 2023-04-25
     :name: section-36

  .. rubric:: Changed
     :name: changed-7

- Add ``issue`` family on 2.3.3.0

.. _section-37:

`2.6.1 <https://github.com/cisco-en-programmability/dnacentersdk/compare/v2.6.0...v2.6.1>`__ - 2023-04-12
---------------------------------------------------------------------------------------------------------

.. _changed-8:

Changed
~~~~~~~

- Remove some families bug in 2.3.3.0
- Correct families names in 2.3.5.3
- Removing duplicate params

.. _section-38:

`2.6.0 <https://github.com/cisco-en-programmability/dnacentersdk/compare/v2.5.6...v2.6.0>`__ - 2023-04-12
---------------------------------------------------------------------------------------------------------

.. _added-6:

Added
~~~~~

- Add support of DNA Center versions (‘2.3.5.3’)
- Adds modules for v2_3_5_3

.. _section-39:

`2.5.6 <https://github.com/cisco-en-programmability/dnacentersdk/compare/v2.5.5...v2.5.6>`__ - 2023-01-10
---------------------------------------------------------------------------------------------------------

.. _added-7:

Added
~~~~~

- Compatibility matrix added in ``readme.rst``

.. _fixed-4:

Fixed
~~~~~

- Offset and limit now support str and int

  - dnacentersdk.api.v2_3_3_0.application_policy
  - dnacentersdk.api.v2_3_3_0.applications
  - dnacentersdk.api.v2_3_3_0.compliance
  - dnacentersdk.api.v2_3_3_0.configuration_templates
  - dnacentersdk.api.v2_3_3_0.device_onboarding_pnp
  - dnacentersdk.api.v2_3_3_0.device_replacement
  - dnacentersdk.api.v2_3_3_0.devices
  - dnacentersdk.api.v2_3_3_0.discovery
  - dnacentersdk.api.v2_3_3_0.event_management
  - dnacentersdk.api.v2_3_3_0.health_and_performance
  - dnacentersdk.api.v2_3_3_0.lan_automation
  - dnacentersdk.api.v2_3_3_0.licenses
  - dnacentersdk.api.v2_3_3_0.network_settings
  - dnacentersdk.api.v2_3_3_0.path_trace
  - dnacentersdk.api.v2_3_3_0.site_design
  - dnacentersdk.api.v2_3_3_0.sites
  - dnacentersdk.api.v2_3_3_0.software_image_management_swim
  - dnacentersdk.api.v2_3_3_0.tag
  - dnacentersdk.api.v2_3_3_0.task

.. _section-40:

`2.5.5 <https://github.com/cisco-en-programmability/dnacentersdk/compare/v2.5.4...v2.5.5>`__ - 2022-11-17
---------------------------------------------------------------------------------------------------------

.. _fixed-5:

Fixed
~~~~~

- Removed enum in
  ``dnacentersdk.api.v2_3_3_0.sda.add_default_authentication_profile``:

  - authenticateTemplateName

- Added Dict_of_str function call in custom_caller headers

.. _section-41:

`2.5.4 <https://github.com/cisco-en-programmability/dnacentersdk/compare/v2.5.3...v2.5.4>`__ - 2022-08-11
---------------------------------------------------------------------------------------------------------

.. _added-8:

Added
~~~~~

- New function on ``fabric_wireless`` for v2_3_3_0.

  - ``add_ssid_to_ip_pool_mapping``

.. _section-42:

`2.5.3 <https://github.com/cisco-en-programmability/dnacentersdk/compare/v2.5.2...v2.5.3>`__ - 2022-08-09
---------------------------------------------------------------------------------------------------------

.. _fixed-6:

Fixed
~~~~~

- ``virtualNetwork`` on ``sda.adds_border_device`` parameter comes from
  ``array`` to ``object``.
- Parameters ``borderWithExternalConnectivity`` and
  ``connectedToInternet`` on ``sda.adds_border_device`` comes from
  ``boolean`` to ``string``.

.. _section-43:

`2.5.2 <https://github.com/cisco-en-programmability/dnacentersdk/compare/v2.5.1...v2.5.2>`__ - 2022-07-29
---------------------------------------------------------------------------------------------------------

.. _fixed-7:

Fixed
~~~~~

- Removed enum in ``sda``.\ ``adds_border_device``:

  - externalDomainRoutingProtocolName

- Removed enum in ``sda``.\ ``add_multicast_in_sda_fabric``:

  - multicastMethod

- Removed enum in ``site_design``.\ ``provision_nfv``:

  - linkType

- Removed enum in ``sda``.\ ``add_transit_peer_network``:

  - routingProtocolName

- Removed enum in ``network_settings``.\ ``update_network`` and
  ``network_settings``.\ ``create_network``:

  - ipAddress
  - sharedSecret
  - domainName
  - primaryIpAddress
  - secondaryIpAddress
  - network
  - servers

.. _section-44:

`2.5.1 <https://github.com/cisco-en-programmability/dnacentersdk/compare/v2.5.0...v2.5.1>`__ - 2022-07-12
---------------------------------------------------------------------------------------------------------

.. _fixed-8:

Fixed
~~~~~

- Fixed enum in ``network_global``.\ ``create_global_pool``:

  - IpAddressSpace

.. _section-45:

`2.5.0 <https://github.com/cisco-en-programmability/dnacentersdk/compare/v2.4.11...v2.5.0>`__ - 2022-06-20
----------------------------------------------------------------------------------------------------------

.. _added-9:

Added
~~~~~

- Add support of DNA Center versions (‘2.3.3.0’)
- Adds modules for v2_3_3_0

.. _section-46:

`2.4.11 <https://github.com/cisco-en-programmability/dnacentersdk/compare/v2.4.10...v2.4.11>`__ - 2022-06-15
------------------------------------------------------------------------------------------------------------

.. _fixed-9:

Fixed
~~~~~

- Improved the way of reading the following env variables:

  - wait_on_rate_limit
  - verify
  - debug

.. _section-47:

`2.4.10 <https://github.com/cisco-en-programmability/dnacentersdk/compare/v2.4.9...v2.4.10>`__ - 2022-05-12
-----------------------------------------------------------------------------------------------------------

.. _added-10:

Added
~~~~~

- Add following parameters to
  ``delete_ip_pool_from_sda_virtual_network`` and
  ``get_ip_pool_from_sda_virtual_network``:

  - site_name_hierarchy

.. _section-48:

`2.4.9 <https://github.com/cisco-en-programmability/dnacentersdk/compare/v2.4.8...v2.4.9>`__ - 2022-04-20
---------------------------------------------------------------------------------------------------------

.. _added-11:

Added
~~~~~

- Add following parameters to ``claim_a_device_to_a_site``:

  - gateway
  - imageId
  - ipInterfaceName
  - rfProfile
  - staticIP
  - subnetMask
  - vlanId

.. _section-49:

`2.4.8 <https://github.com/cisco-en-programmability/dnacentersdk/compare/v2.4.7...v2.4.8>`__ - 2022-03-23
---------------------------------------------------------------------------------------------------------

.. _added-12:

Added
~~~~~

- Add ``DownloadResponse`` class that wraps the
  ``urllib3.response.HTTPResponse``.
- Add ``filename`` optional parameter to the following functions:

  - dnacentersdk.api.v1_2_10.file.File.download_a_file_by_fileid
  - dnacentersdk.api.v1_3_0.file.File.download_a_file_by_fileid
  - dnacentersdk.api.v1_3_1.file.File.download_a_file_by_fileid
  - dnacentersdk.api.v1_3_3.file.File.download_a_file_by_fileid
  - dnacentersdk.api.v2_1_1.file.File.download_a_file_by_fileid
  - dnacentersdk.api.v2_1_2.file.File.download_a_file_by_fileid
  - dnacentersdk.api.v2_1_2.reports.Reports.download_report_content
  - dnacentersdk.api.v2_2_2_3.file.File.download_a_file_by_fileid
  - dnacentersdk.api.v2_2_2_3.reports.Reports.download_report_content
  - dnacentersdk.api.v2_2_3_3.file.File.download_a_file_by_fileid
  - dnacentersdk.api.v2_2_3_3.reports.Reports.download_report_content

.. _changed-9:

Changed
~~~~~~~

- Change the response of the following funtions from
  ``urllib3.response.HTTPResponse`` to a wrapper ``DownloadResponse``.

  - dnacentersdk.api.v1_2_10.file.File.download_a_file_by_fileid
  - dnacentersdk.api.v1_3_0.file.File.download_a_file_by_fileid
  - dnacentersdk.api.v1_3_1.file.File.download_a_file_by_fileid
  - dnacentersdk.api.v1_3_3.file.File.download_a_file_by_fileid
  - dnacentersdk.api.v2_1_1.file.File.download_a_file_by_fileid
  - dnacentersdk.api.v2_1_2.file.File.download_a_file_by_fileid
  - dnacentersdk.api.v2_1_2.reports.Reports.download_report_content
  - dnacentersdk.api.v2_2_2_3.file.File.download_a_file_by_fileid
  - dnacentersdk.api.v2_2_2_3.reports.Reports.download_report_content
  - dnacentersdk.api.v2_2_3_3.file.File.download_a_file_by_fileid
  - dnacentersdk.api.v2_2_3_3.reports.Reports.download_report_content

.. _section-50:

`2.4.7 <https://github.com/cisco-en-programmability/dnacentersdk/compare/v2.4.6...v2.4.7>`__ - 2022-03-22
---------------------------------------------------------------------------------------------------------

.. _added-13:

Added
~~~~~

- Add ``rfProfile`` parameter for request body struct of
  ``claim_a_device_to_a_site``.

.. _section-51:

`2.4.6 <https://github.com/cisco-en-programmability/dnacentersdk/compare/v2.4.5...v2.4.6>`__ - 2022-03-14
---------------------------------------------------------------------------------------------------------

.. _changed-10:

Changed
~~~~~~~

- Update the type of the ``externalConnectivitySettings``\ from object
  to list in sda.adds_border_device
- ``interfaceName`` is now part of the structure of
  ``externalConnectivitySettings`` in sda.adds_border_device
- ``externalAutonomouSystemNumber`` is now part of the structure of
  ``externalConnectivitySettings`` in sda.adds_border_device
- ``l3Handoff`` is now part of the structure of
  ``externalConnectivitySettings`` in sda.adds_border_device
- Update the type of the ``l3Handoff``\ from object to list in
  sda.adds_border_device
- ``virtualNetwork`` is now part of the structure of ``l3Handoff`` in
  sda.adds_border_device
- ``virtualNetworkName`` is now part of the structure of
  ``virtualNetwork`` in sda.adds_border_device
- ``vlanId`` is now part of the structure of ``virtualNetwork`` in
  sda.adds_border_device
- Update models validators of Cisco DNA Center API v2.2.3.3 files for
  the following functions:

  - sda.adds_border_device

.. _section-52:

`2.4.5 <https://github.com/cisco-en-programmability/dnacentersdk/compare/v2.4.4...v2.4.5>`__ - 2022-02-01
---------------------------------------------------------------------------------------------------------

.. _changed-11:

Changed
~~~~~~~

- Adds parameter ``id`` to devices.sync_devices for Cisco DNA Center API
  v2.2.3.3

- Update response documentation of Cisco DNA Center API v2.2.3.3 files

  - fabric_wireless.add_ssid_to_ip_pool_mapping
  - fabric_wireless.update_ssid_to_ip_pool_mapping
  - fabric_wireless.add_w_l_c_to_fabric_domain
  - wireless.ap_provision
  - wireless.create_update_dynamic_interface

- Update models validators of Cisco DNA Center API v2.2.3.3 files for
  the following functions:

  - devices.sync_devices

.. _section-53:

`2.4.4 <https://github.com/cisco-en-programmability/dnacentersdk/compare/v2.4.3...v2.4.4>`__ - 2022-01-31
---------------------------------------------------------------------------------------------------------

.. _changed-12:

Changed
~~~~~~~

- Update response documentation of Cisco DNA Center API v2.2.3.3 files

  - application_policy.get_applications
  - device_onboarding_pnp.get_device_list

- Adds parameters ``payload`` and ``active_validation`` to the following
  functions for Cisco DNA Center API v2.2.3.3:

  - site_design.create_floormap
  - site_design.update_floormap

- Update models validators of Cisco DNA Center API v2.2.3.3 files for
  the following functions:

  - site_design.create_floormap
  - site_design.update_floormap
  - application_policy.create_application

.. _fixed-10:

Fixed
~~~~~

- Removed an extra parameter in the call of
  ``VERIFY_STRING_ENVIRONMENT_VARIABLE``

.. _added-14:

Added
~~~~~

- Adds parameters ``hostname``, ``imageInfo`` and ``configInfo`` to
  device_onboarding_pnp.pnp_device_claim_to_site

.. _section-54:

`2.4.3 <https://github.com/cisco-en-programmability/dnacentersdk/compare/v2.4.2...v2.4.3>`__ - 2022-01-19
---------------------------------------------------------------------------------------------------------

.. _fixed-11:

Fixed
~~~~~

- DNACenterAPI constructor allows for optional arguments
  `#37 <https://github.com/cisco-en-programmability/dnacentersdk/issues/37>`__

.. _changed-13:

Changed
~~~~~~~

- Update requirements
- Adds env variables support for import before/after importing
  DNACenterAPI
- Adds tests for env variables before/after DNACenterAPI import

.. _section-55:

`2.4.2 <https://github.com/cisco-en-programmability/dnacentersdk/compare/v2.4.1...v2.4.2>`__ - 2021-12-14
---------------------------------------------------------------------------------------------------------

.. _fixed-12:

Fixed
~~~~~

- Fix add_members_to_the_tag and retrieves_all_network_devices json
  schemas. ### Updated
- Update json schemas for models/validators and
  tests/models/models/validators

.. _section-56:

`2.4.1 <https://github.com/cisco-en-programmability/dnacentersdk/compare/v2.4.0...v2.4.1>`__ - 2021-12-01
---------------------------------------------------------------------------------------------------------

.. _changed-14:

Changed
~~~~~~~

- Update to match checksum

.. _section-57:

`2.4.0 <https://github.com/cisco-en-programmability/dnacentersdk/compare/v2.3.3...v2.4.0>`__ - 2021-12-01
---------------------------------------------------------------------------------------------------------

.. _added-15:

Added
~~~~~

- Add support of DNA Center versions (‘2.2.3.3’)
- Add ``retrieves_all_network_devices`` funtion

.. _changed-15:

Changed
~~~~~~~

- Included support for DNAC 2.2.3.3 files
- Update function names:

  - Rename ``devices.add_device2`` to ``devices.add_device``
  - Rename ``devices.is_valid_add_device2`` to
    ``devices.is_valid_add_device`` in tests
  - Rename ``devices.test_add_device2`` to ``devices.test_add_device``
    in tests
  - Rename ``devices.add_device2_default_val`` to
    ``devices.add_device_default_val`` in tests

- Update missing dnac 2.2.3.3 files

.. _section-58:

`2.3.3 <https://github.com/cisco-en-programmability/dnacentersdk/compare/v2.3.2...v2.3.3>`__ - 2021-11-24
---------------------------------------------------------------------------------------------------------

.. _changed-16:

Changed
~~~~~~~

- Changes to ``configuration_templates`` functions:

  - Add ``payload`` and ``active_validation`` parameters to
    ``clone_given_template`` function
  - Change type from ``dict`` to ``list`` for parameter ``templates`` in
    ``create_project``
  - Change type from ``dict`` to ``list`` for parameter ``templates`` in
    ``update_project``
  - Change type from ``(list, dict)`` to ``basesting`` for parameter
    ``payload`` in ``imports_the_projects_provided``
  - Change type from ``object`` to ``list`` for parameter
    ``resourceParams`` in ``preview_template``
  - Removed ``active_validation`` parameter in
    ``imports_the_projects_provided`` function

- Changes to ``sda`` functions:

  - Add ``isGuestVirtualNetwork`` parameter to
    ``add_virtual_network_with_scalable_groups`` function
  - Add ``isGuestVirtualNetwork`` parameter to
    ``update_virtual_network_with_scalable_groups`` function

.. _section-59:

`2.3.2 <https://github.com/cisco-en-programmability/dnacentersdk/compare/v2.3.1...v2.3.2>`__ - 2021-09-14
---------------------------------------------------------------------------------------------------------

.. _changed-17:

Changed
~~~~~~~

- Disable verify=False warnings of urllib3

.. _section-60:

`2.3.1 <https://github.com/cisco-en-programmability/dnacentersdk/compare/v2.3.0...v2.3.1>`__ - 2021-08-10
---------------------------------------------------------------------------------------------------------

.. _fixed-13:

Fixed
~~~~~

- Fix devices param definition & schemas [``aba32f3``]
- Remove unnecesary path_params [``25c4e99``]

.. _section-61:

`2.3.0 <https://github.com/cisco-en-programmability/dnacentersdk/compare/v2.2.5...v2.3.0>`__ - 2021-08-09
---------------------------------------------------------------------------------------------------------

.. _added-16:

Added
~~~~~

- Add support of DNA Center versions (‘2.2.2.3’)
- Adds modules for v2_2_2_3

.. _changed-18:

Changed
~~~~~~~

- Updates download_report_content of v2_2_1 function to handle response
  body and save it as a file.
- Updates exceptions.py file to check if self.details is dict before
  attempting access
- Updates restsession.py to handle downloads using Content-Disposition
  header rather than custom fileName header

.. _section-62:

`2.2.5 <https://github.com/cisco-en-programmability/dnacentersdk/compare/v2.2.4...v2.2.5>`__ - 2021-08-05
---------------------------------------------------------------------------------------------------------

.. _changed-19:

Changed
~~~~~~~

- Fixes #34 by:

  - Removing enum that contain descriptions rather than actual values.
  - Adding ``primaryIpAddress`` and ``secondaryIpAddress`` for v2_2_1
    the ``"format": "ipv4"`` JSON schema property.

- Removes minus char from docstrings.
- Adds check_type conditions for ‘X-Auth-Token’ for v2_2_1 operations.

.. _section-63:

`2.2.4 <https://github.com/cisco-en-programmability/dnacentersdk/compare/v2.2.3...v2.2.4>`__ - 2021-06-08
---------------------------------------------------------------------------------------------------------

.. _fixed-14:

Fixed
~~~~~

- Fixes download_a_file_by_fileid and import_local_software_image for
  v2_2_1

.. _section-64:

`2.2.3 <https://github.com/cisco-en-programmability/dnacentersdk/compare/v2.2.2...v2.2.3>`__ - 2021-06-08
---------------------------------------------------------------------------------------------------------

.. _changed-20:

Changed
~~~~~~~

- Update project dependencies & settings
- Update LICENSE
- Update tests (lint, mock server order, validators)
- Update docs for v2_2_1
- Fix functions args for 2_2_1
- Update LICENSE reference
- Removed unused code in ``dnacentersdk/generator_containers.py``
- Remove description from validators
- Update comments & args’ types
- Patch changes some parameters in v2_2_1 that were causing NameError
- Patch adds one function that was missing from previous release
- Patch adds models/validators for v2_2_1 with new ids

.. _section-65:

`2.2.2 <https://github.com/cisco-en-programmability/dnacentersdk/compare/v2.0.2...v2.2.2>`__ - 2021-05-10
---------------------------------------------------------------------------------------------------------

.. _added-17:

Added
~~~~~

- Add support of DNA Center versions (‘2.2.1’)

.. _changed-21:

Changed
~~~~~~~

- Updates requirements files

.. _section-66:

`2.0.2 <https://github.com/cisco-en-programmability/dnacentersdk/compare/v2.0.0...v2.0.2>`__ - 2020-11-01
---------------------------------------------------------------------------------------------------------

.. _added-18:

Added
~~~~~

- Add support of DNA Center versions (‘2.1.2’)
- Included sphinx_search in Pipfile
- Included sphinx_search in requirements-dev.txt
- Requirements-docs.txt
- Added requirements.lock

.. _changed-22:

Changed
~~~~~~~

- Migrated to poetry for publishing and managing the project
- Generated requirements.txt from poetry export

Removed
~~~~~~~

- Removed requirements.lock

.. _section-67:

`2.0.0 <https://github.com/cisco-en-programmability/dnacentersdk/compare/v1.3.0...v2.0.0>`__ - 2020-07-17
---------------------------------------------------------------------------------------------------------

.. _added-19:

Added
~~~~~

- Add support of DNA Center versions (‘1.3.1’, ‘1.3.3’, ‘2.1.1’)
- Included setuptools_scm in the requirements

.. _changed-23:

Changed
~~~~~~~

- Changed repo URLs to current repository
- Changed versioneer style from pep440 to pep440-post
- Changed setup from versioneer to setuptools_scm
- Changed version management to include patch (major, minor, patch)

.. _fixed-15:

Fixed
~~~~~

- Fixed link to github organization
- Fixed dict limit error with python < 3.7
- Fixed (``json **kwargs``) handling

.. _removed-1:

Removed
~~~~~~~

- Removed Webex Teams Space Community reference from README
- Removed Token refresh when changing base_url

.. _section-68:

`1.3.0 <https://github.com/cisco-en-programmability/dnacentersdk/compare/v1.2.10...v1.3.0>`__ - 2019-08-19
----------------------------------------------------------------------------------------------------------

.. _added-20:

Added
~~~~~

- Add support for multiple versions of DNA Center (‘1.2.10’, ‘1.3.0’)

.. _fixed-16:

Fixed
~~~~~

- Fix code example in README
- Fix error in setter in ``api/__init__.py``
- Fix errors for readthedocs

.. _section-69:

`1.2.10 <https://github.com/cisco-en-programmability/dnacentersdk/releases/v1.2.10>`__ - 2019-07-18
---------------------------------------------------------------------------------------------------

.. _added-21:

Added
~~~~~

- Add support for DNA Center version 1.2.10

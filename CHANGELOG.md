# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
## [2.5.0] - 2022-mm-dd

### Added
- Add support of DNA Center API version ('2.3.2.0')

### Changed
- Update requirements files.

- Major changes between versions 2.2.3.3 and 2.3.2.0
  + Removed functions in v2.3.2.0
    * site_design.create_floormap
    * site_design.delete_floormap
    * site_design.get_floormap
    * site_design.get_floormaps
    * site_design.update_floormap
  + New modules `lan_automation` and `system_settings` in v2.3.2.0, and their new functions
    * lan_automation.lan_automation_log
    * lan_automation.lan_automation_log_by_id
    * lan_automation.lan_automation_session_count
    * lan_automation.lan_automation_start
    * lan_automation.lan_automation_status
    * lan_automation.lan_automation_status_by_id
    * lan_automation.lan_automation_stop
    * system_settings.custom_prompt_post_api
    * system_settings.custom_prompt_support_get_api
  + New functions for existent modules in v2.3.2.0
    * devices.clear_mac_address_table
    * devices.get_connected_device_detail
    * devices.get_planned_access_points_for_building
    * devices.get_planned_access_points_for_floor
    * devices.legit_operations_for_interface
    * devices.update_interface_details
    * event_management.create_email_destination
    * event_management.create_syslog_destination
    * event_management.create_webhook_destination
    * event_management.get_connector_types
    * event_management.update_email_destination
    * event_management.update_syslog_destination
    * event_management.update_webhook_destination
    * file.upload_file
## [2.4.4] - 2022-01-31
### Changed
- Update response documentation of DNA Center API v2.2.3.3 files
  + application_policy.get_applications
  + device_onboarding_pnp.get_device_list

- Adds parameters `payload` and `active_validation` to the following functions:
  + site_design.create_floormap
  + site_design.update_floormap

- Update models validators of DNA Center API v2.2.3.3 files for the following functions:
  + site_design.create_floormap
  + site_design.update_floormap
  + application_policy.create_application


## [2.4.3] - 2022-01-19

### Fixed
- DNACenterAPI constructor allows for optional arguments [#37](https://github.com/cisco-en-programmability/dnacentersdk/issues/37)

### Changed
- Update requirements
- Adds env variables support for import before/after importing DNACenterAPI
- Adds tests for env variables before/after DNACenterAPI import 

## [2.4.2] - 2021-12-14

### Fixed
- Fix add_members_to_the_tag and retrieves_all_network_devices json schemas.
### Updated
- Update json schemas for models/validators and tests/models/models/validators

## [2.4.1] - 2021-12-01

### Changed
- Update to match checksum

## [2.4.0] - 2021-12-01

### Added
- Add support of DNA Center versions ('2.2.3.3')
- Add `retrieves_all_network_devices` funtion

### Changed
- Included support for DNAC 2.2.3.3 files
- Update function names:
  + Rename `devices.add_device2` to `devices.add_device`
  + Rename `devices.is_valid_add_device2` to `devices.is_valid_add_device` in tests
  + Rename `devices.test_add_device2` to `devices.test_add_device` in tests
  + Rename `devices.add_device2_default_val` to `devices.add_device_default_val` in tests
- Update missing dnac 2.2.3.3 files

## [2.3.3] - 2021-11-24

### Changed
- Changes to `configuration_templates` functions:
  + Add `payload` and `active_validation` parameters to `clone_given_template` function
  + Change type from `dict` to `list` for parameter `templates` in `create_project`
  + Change type from `dict` to `list` for parameter `templates` in `update_project`
  + Change type from `(list, dict)` to `basesting` for parameter `payload` in `imports_the_projects_provided`
  + Change type from `object` to `list` for parameter `resourceParams` in `preview_template`
  + Removed `active_validation` parameter in `imports_the_projects_provided` function
- Changes to `sda` functions:
  + Add `isGuestVirtualNetwork` parameter to `add_virtual_network_with_scalable_groups` function
  + Add `isGuestVirtualNetwork` parameter to `update_virtual_network_with_scalable_groups` function

## [2.3.2] - 2021-09-14

### Changed
- Disable verify=False warnings of urllib3

## [2.3.1] - 2021-08-10

### Fixed
- Fix devices param definition & schemas [`aba32f3`]
- Remove unnecesary path_params [`25c4e99`]

## [2.3.0] - 2021-08-09

### Added
- Add support of DNA Center versions ('2.2.2.3')
- Adds modules for v2_2_2_3

### Changed
- Updates download_report_content of v2_2_1 function to handle response body and save it as a file.
- Updates exceptions.py file to check if self.details is dict before attempting access
- Updates restsession.py to handle downloads using Content-Disposition header rather than custom fileName header

## [2.2.5] - 2021-08-05

### Changed
- Fixes #34 by:
  + Removing enum that contain descriptions rather than actual values.
  + Adding `primaryIpAddress` and `secondaryIpAddress` for v2_2_1 the `"format": "ipv4"` JSON schema property.
- Removes minus char from docstrings.
- Adds check_type conditions for 'X-Auth-Token' for v2_2_1 operations.

## [2.2.4] - 2021-06-08

### Fixed
- Fixes download_a_file_by_fileid and import_local_software_image for v2_2_1

## [2.2.3] - 2021-06-08

### Changed
- Update project dependencies & settings
- Update LICENSE
- Update tests (lint, mock server order, validators)
- Update docs for v2_2_1
- Fix functions args for 2_2_1
- Update LICENSE reference
- Removed unused code in `dnacentersdk/generator_containers.py`
- Remove description from validators
- Update comments & args' types
- Patch changes some parameters in v2_2_1 that were causing NameError
- Patch adds one function that was missing from previous release
- Patch adds models/validators for v2_2_1 with new ids

## [2.2.2] - 2021-05-10

### Added
- Add support of DNA Center versions ('2.2.1')

### Changed
- Updates requirements files

## [2.0.2] - 2020-11-01

### Added
- Add support of DNA Center versions ('2.1.2')
- Included sphinx_search in Pipfile
- Included sphinx_search in requirements-dev.txt
- Requirements-docs.txt
- Added requirements.lock

### Changed
- Migrated to poetry for publishing and managing the project
- Generated requirements.txt from poetry export

### Removed
- Removed requirements.lock

## [2.0.0] - 2020-07-17

### Added
- Add support of DNA Center versions ('1.3.1', '1.3.3', '2.1.1')
- Included setuptools_scm in the requirements

### Changed
- Changed repo URLs to current repository
- Changed versioneer style from pep440 to pep440-post
- Changed setup from versioneer to setuptools_scm
- Changed version management to include patch (major, minor, patch)

### Fixed
- Fixed link to github organization
- Fixed dict limit error with python < 3.7
- Fixed (`json **kwargs`) handling

### Removed
- Removed Webex Teams Space Community reference from README
- Removed Token refresh when changing base_url


## [1.3.0] - 2019-08-19

### Added
- Add support for multiple versions of DNA Center ('1.2.10', '1.3.0')

### Fixed
- Fix code example in README
- Fix error in setter in `api/__init__.py`
- Fix errors for readthedocs

## [1.2.10] - 2019-07-18

### Added
- Add support for DNA Center version 1.2.10


[1.2.10]: https://github.com/cisco-en-programmability/dnacentersdk/releases/v1.2.10
[1.3.0]: https://github.com/cisco-en-programmability/dnacentersdk/compare/v1.2.10...v1.3.0
[2.0.0]: https://github.com/cisco-en-programmability/dnacentersdk/compare/v1.3.0...v2.0.0
[2.0.2]: https://github.com/cisco-en-programmability/dnacentersdk/compare/v2.0.0...v2.0.2
[2.2.2]: https://github.com/cisco-en-programmability/dnacentersdk/compare/v2.0.2...v2.2.2
[2.2.3]: https://github.com/cisco-en-programmability/dnacentersdk/compare/v2.2.2...v2.2.3
[2.2.4]: https://github.com/cisco-en-programmability/dnacentersdk/compare/v2.2.3...v2.2.4
[2.2.5]: https://github.com/cisco-en-programmability/dnacentersdk/compare/v2.2.4...v2.2.5
[2.3.0]: https://github.com/cisco-en-programmability/dnacentersdk/compare/v2.2.5...v2.3.0
[2.3.1]: https://github.com/cisco-en-programmability/dnacentersdk/compare/v2.3.0...v2.3.1
[2.3.2]: https://github.com/cisco-en-programmability/dnacentersdk/compare/v2.3.1...v2.3.2
[2.3.3]: https://github.com/cisco-en-programmability/dnacentersdk/compare/v2.3.2...v2.3.3
[2.4.0]: https://github.com/cisco-en-programmability/dnacentersdk/compare/v2.3.3...v2.4.0
[2.4.1]: https://github.com/cisco-en-programmability/dnacentersdk/compare/v2.4.0...v2.4.1
[2.4.2]: https://github.com/cisco-en-programmability/dnacentersdk/compare/v2.4.1...v2.4.2
[2.4.3]: https://github.com/cisco-en-programmability/dnacentersdk/compare/v2.4.2...v2.4.3
[2.4.4]: https://github.com/cisco-en-programmability/dnacentersdk/compare/v2.4.3...v2.4.4
[2.5.0]: https://github.com/cisco-en-programmability/dnacentersdk/compare/v2.4.4...v2.5.0
[Unreleased]: https://github.com/cisco-en-programmability/dnacentersdk/compare/v2.5.0...master

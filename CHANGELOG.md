# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]


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
[2.4.0]: https://github.com/cisco-en-programmability/dnacentersdk/compare/v2.4.0...v2.4.1
[Unreleased]: https://github.com/cisco-en-programmability/dnacentersdk/compare/v2.4.1...master

# -*- coding: utf-8 -*-
"""Cisco Catalyst Center System Software Upgrade API wrapper.

Copyright (c) 2025 Cisco Systems.

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

from builtins import *


from ...restsession import RestSession
from ...utils import (
    apply_path_params,
    check_type,
    dict_from_items_with_values,
    dict_of_str,
    deprecated,
)


class SystemSoftwareUpgrade(object):
    """Cisco Catalyst Center System Software Upgrade API (version: 3.1.6.0).

    Wraps the Catalyst Center System Software Upgrade
    API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new SystemSoftwareUpgrade
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Catalyst Center service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(SystemSoftwareUpgrade, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def delete_downloaded_release(
        self, release_name, release_version, headers=None, **request_parameters
    ):
        """This api is used to trigger the workflow to delete the downloaded release.

        Args:
            release_name(str): releaseName query parameter. The releaseName of the downloaded release to be deleted.
            release_version(str): releaseVersion query parameter. The releaseVersion of the downloaded release to be
                deleted.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            MyDict: JSON response. Access the object's properties by using
            the dot notation or the bracket notation.

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!delete-downloaded-release
        """
        check_type(headers, dict)
        check_type(release_name, str, may_be_none=False)
        check_type(release_version, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "releaseName": release_name,
            "releaseVersion": release_version,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/system/api/v1/downloadSoftwareRelease"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_b57f9a355d58e4a951d3db3f293_v3_1_6_0", json_data
        )

    def download_release(
        self,
        optionalPackages=None,
        releaseName=None,
        releaseVersion=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This api is used to trigger download workflow of a specific release.

        Args:
            optionalPackages(list): System Software Upgrade's Provide the list of optional package's id to be
                downloaded.Obtain the `id` from the `packages[n].id` attribute where
                `packages[n].optional` is true from the `/dna/system/api/v1/releases/releaseSummary` API
                where the `releaseName` and `releaseVersion` is the requested download version. (list of
                strings).
            releaseName(string): System Software Upgrade's The `releaseName` of the release to be downloaded.Obtain
                the releaseName from the `name` attribute in the response of the
                `/dna/system/api/v1/releases` API.
            releaseVersion(string): System Software Upgrade's The `releaseVersion` of the release to be
                downloaded.Obtain the releaseVersion from the `version` attribute in the response of the
                `/dna/system/api/v1/releases` API.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(dict): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            MyDict: JSON response. Access the object's properties by using
            the dot notation or the bracket notation.

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!download-release
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = {
            "optionalPackages": optionalPackages,
            "releaseName": releaseName,
            "releaseVersion": releaseVersion,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_f57dc44184564cb97a6573a44ad394_v3_1_6_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/system/api/v1/downloadSoftwareRelease"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(
                endpoint_full_url, params=_params, json=_payload, headers=_headers
            )
        else:
            json_data = self._session.post(
                endpoint_full_url, params=_params, json=_payload
            )

        return self._object_factory(
            "bpm_f57dc44184564cb97a6573a44ad394_v3_1_6_0", json_data
        )

    def update_downloaded_release(
        self,
        optionalPackages=None,
        releaseName=None,
        releaseVersion=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """After the specified release has been downloaded successfully, users can download additional optional packages
        using this API.

        Args:
            optionalPackages(list): System Software Upgrade's Provide the list of optional package's id to be
                downloaded.Obtain the `id` from the `packages[n].id` attribute where
                `packages[n].optional` is true from the `/dna/system/api/v1/releases/releaseSummary` API
                where the `releaseName` and `releaseVersion` is the requested download version. (list of
                strings).
            releaseName(string): System Software Upgrade's The `releaseName` of the downloaded release to be
                updated.
            releaseVersion(string): System Software Upgrade's The `releaseVersion` of the downloaded release to be
                updated.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(dict): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            MyDict: JSON response. Access the object's properties by using
            the dot notation or the bracket notation.

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!update-downloaded-release
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = {
            "optionalPackages": optionalPackages,
            "releaseName": releaseName,
            "releaseVersion": releaseVersion,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_e4ddf9b60efb59ac8f6a200a563d9d72_v3_1_6_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/system/api/v1/downloadSoftwareRelease"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(
                endpoint_full_url, params=_params, json=_payload, headers=_headers
            )
        else:
            json_data = self._session.put(
                endpoint_full_url, params=_params, json=_payload
            )

        return self._object_factory(
            "bpm_e4ddf9b60efb59ac8f6a200a563d9d72_v3_1_6_0", json_data
        )

    def install_optional_packages(
        self,
        optionalPackages=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This API is used to trigger the workflow for installing optional packages.

        Args:
            optionalPackages(list): System Software Upgrade's Provide the list of optional package's id to be
                installed .Use the /dna/system/api/v1/releases/releaseSummary API to obtain the optional
                package IDs. The `releaseName` and `releaseVersion` should correspond to the installed
                release name and version, which can be obtained from the `name` and `version` attributes
                in the response of the `/dna/system/api/v1/installedRelease` API. In the releaseSummary
                API response, optional packages can be identified by the attribute
                `packages[n].optional` is true. Provide the `packages[n].id` of these optional packages.
                (list of strings).
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(dict): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            MyDict: JSON response. Access the object's properties by using
            the dot notation or the bracket notation.

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!install-optional-packages
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = {
            "optionalPackages": optionalPackages,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_f2dc0b2dd265d3bb69c5aeb5cff2f13_v3_1_6_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/system/api/v1/installOptionalPackages"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(
                endpoint_full_url, params=_params, json=_payload, headers=_headers
            )
        else:
            json_data = self._session.post(
                endpoint_full_url, params=_params, json=_payload
            )

        return self._object_factory(
            "bpm_f2dc0b2dd265d3bb69c5aeb5cff2f13_v3_1_6_0", json_data
        )

    def get_installed_release_details(self, headers=None, **request_parameters):
        """This api is used to get the installed release details.

        Args:
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            MyDict: JSON response. Access the object's properties by using
            the dot notation or the bracket notation.

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-installed-release-details
        """
        check_type(headers, dict)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/system/api/v1/installedRelease"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_af1fd1bd1557b880106f71c5db9f66_v3_1_6_0", json_data
        )

    def get_all_release(self, headers=None, **request_parameters):
        """This api is used to get all available release.

        Args:
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            MyDict: JSON response. Access the object's properties by using
            the dot notation or the bracket notation.

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-all-release
        """
        check_type(headers, dict)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/system/api/v1/releases"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_fc2a12b907a35a92a47b7877b5207c4d_v3_1_6_0", json_data
        )

    def get_release_detail(
        self, release_name, release_version, headers=None, **request_parameters
    ):
        """This API is used to retrieve a specific release and the list of packages available in that release.

        Args:
            release_name(str): releaseName query parameter. The releaseName of the release to be retrieved.
            release_version(str): releaseVersion query parameter. The releaseVersion of the release to be retrieved.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            MyDict: JSON response. Access the object's properties by using
            the dot notation or the bracket notation.

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-release-detail
        """
        check_type(headers, dict)
        check_type(release_name, str, may_be_none=False)
        check_type(release_version, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "releaseName": release_name,
            "releaseVersion": release_version,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/system/api/v1/releases/releaseSummary"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a0c33ecb0a475f55b3518736d8a9c601_v3_1_6_0", json_data
        )

    def get_software_management_execution_details(
        self, id, headers=None, **request_parameters
    ):
        """This api is used to get execution status and task details of a specific software management workflows.

        Args:
            id(str): id path parameter. The id of the execution detail to be retrieved.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            MyDict: JSON response. Access the object's properties by using
            the dot notation or the bracket notation.

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-software-management-execution-details
        """
        check_type(headers, dict)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/system/api/v1/softwareManagementExecutions/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_fc20a7cd31655bf1ae775e4bf645a9e1_v3_1_6_0", json_data
        )

    def uninstall_optional_packages(
        self,
        optionalPackages=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This API is used to trigger the workflow for uninstalling optional packages.

        Args:
            optionalPackages(list): System Software Upgrade's Provide the list of optional package's id to be
                uninstalled. Use the `/dna/system/api/v1/installedRelease` API to obtain the optional
                package IDs. In the installedRelease API response, installed optional packages can be
                identified by the attributes `packages[n].optional` is true. and `packages[n].status` is
                DEPLOYED. Provide the `packages[n].id` of these optional packages. (list of strings).
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(dict): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            MyDict: JSON response. Access the object's properties by using
            the dot notation or the bracket notation.

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!uninstall-optional-packages
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = {
            "optionalPackages": optionalPackages,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_d0456ad1d5bda99f7d9254f8a1ec3_v3_1_6_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/system/api/v1/uninstallOptionalPackages"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(
                endpoint_full_url, params=_params, json=_payload, headers=_headers
            )
        else:
            json_data = self._session.post(
                endpoint_full_url, params=_params, json=_payload
            )

        return self._object_factory(
            "bpm_d0456ad1d5bda99f7d9254f8a1ec3_v3_1_6_0", json_data
        )

    def upgrade_release(
        self,
        optionalPackages=None,
        releaseName=None,
        releaseVersion=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This api is used to trigger the workflow to upgrade the downloaded release.

        Args:
            optionalPackages(list): System Software Upgrade's Provide the list of optional package's id to be
                downloaded and upgraded . Use the `/dna/system/api/v1/releases/releaseSummary` API to
                obtain the optional package IDs. The `releaseName` and `releaseVersion` should
                correspond to the downloaded release.In the releases summary API response, optional
                packages can be identified by the attribute `packages[n].optional` is true. Provide the
                `packages[n].id` of these optional packages. (list of strings).
            releaseName(string): System Software Upgrade's The `releaseName` of the downloaded release to be
                upgraded.
            releaseVersion(string): System Software Upgrade's The `releaseVersion` of the downloaded release to be
                upgraded.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(dict): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            MyDict: JSON response. Access the object's properties by using
            the dot notation or the bracket notation.

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!upgrade-release
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = {
            "optionalPackages": optionalPackages,
            "releaseName": releaseName,
            "releaseVersion": releaseVersion,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_c90586f562b8fc0451b7e71b35a_v3_1_6_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/system/api/v1/upgradeSoftwareRelease"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(
                endpoint_full_url, params=_params, json=_payload, headers=_headers
            )
        else:
            json_data = self._session.post(
                endpoint_full_url, params=_params, json=_payload
            )

        return self._object_factory(
            "bpm_c90586f562b8fc0451b7e71b35a_v3_1_6_0", json_data
        )


# Alias Functions

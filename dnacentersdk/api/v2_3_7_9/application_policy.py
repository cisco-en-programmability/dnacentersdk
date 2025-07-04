# -*- coding: utf-8 -*-
"""Cisco Catalyst Center Application Policy API wrapper.

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
)


class ApplicationPolicy(object):
    """Cisco Catalyst Center Application Policy API (version: 2.3.7.9).

    Wraps the Catalyst Center Application Policy
    API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new ApplicationPolicy
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Catalyst Center service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(ApplicationPolicy, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def get_application_policy(
        self, policy_scope=None, headers=None, **request_parameters
    ):
        """Get all existing application policies .

        Args:
            policy_scope(str): policyScope query parameter. policy scope name .
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
            https://developer.cisco.com/docs/dna-center/#!get-application-policy
        """
        check_type(headers, dict)
        check_type(policy_scope, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "policyScope": policy_scope,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/app-policy"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_fae4378ef4e2503f9fef4f3a4ddd4de4_v2_3_7_9", json_data
        )

    def get_application_policy_default(self, headers=None, **request_parameters):
        """Get default application policy .

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
            https://developer.cisco.com/docs/dna-center/#!get-application-policy-default
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

        e_url = "/dna/intent/api/v1/app-policy-default"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_d1b2e541bb85dea8192cd474be4e3ad_v2_3_7_9", json_data
        )

    def application_policy_intent(
        self,
        createList=None,
        deleteList=None,
        updateList=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Create/Update/Delete application policy .

        Args:
            createList(list): Application Policy's createList (list of objects).
            deleteList(list): Application Policy's Delete list of Group Based Policy ids  (list of strings).
            updateList(list): Application Policy's updateList (list of objects).
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
            https://developer.cisco.com/docs/dna-center/#!application-policy-intent
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
            "createList": createList,
            "updateList": updateList,
            "deleteList": deleteList,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_fa27ccbaf55711849381a707e1edfa_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/app-policy-intent"
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
            "bpm_fa27ccbaf55711849381a707e1edfa_v2_3_7_9", json_data
        )

    def get_application_policy_queuing_profile(
        self, name=None, headers=None, **request_parameters
    ):
        """Get all or by name, existing application policy queuing profiles .

        Args:
            name(str): name query parameter. queuing profile name .
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
            https://developer.cisco.com/docs/dna-center/#!get-application-policy-queuing-profile
        """
        check_type(headers, dict)
        check_type(name, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "name": name,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/app-policy-queuing-profile"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_d47102747c9e50ed9e365b1297e4188d_v2_3_7_9", json_data
        )

    def update_application_policy_queuing_profile(
        self, headers=None, payload=None, active_validation=True, **request_parameters
    ):
        """Update existing custom application queuing profile .

        Args:
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(list): A JSON serializable Python object to send in the
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
            https://developer.cisco.com/docs/dna-center/#!update-application-policy-queuing-profile
        """
        check_type(headers, dict)
        check_type(payload, list)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = payload or []
        if active_validation:
            self._request_validator(
                "jsd_b11aa4de387251c794665e030fa815da_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/app-policy-queuing-profile"
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
            "bpm_b11aa4de387251c794665e030fa815da_v2_3_7_9", json_data
        )

    def create_application_policy_queuing_profile(
        self, headers=None, payload=None, active_validation=True, **request_parameters
    ):
        """Create new custom application queuing profile .

        Args:
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(list): A JSON serializable Python object to send in the
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
            https://developer.cisco.com/docs/dna-center/#!create-application-policy-queuing-profile
        """
        check_type(headers, dict)
        check_type(payload, list)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = payload or []
        if active_validation:
            self._request_validator(
                "jsd_bd31fcbd1ecd5a2c8b812088b27bfcea_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/app-policy-queuing-profile"
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
            "bpm_bd31fcbd1ecd5a2c8b812088b27bfcea_v2_3_7_9", json_data
        )

    def get_application_policy_queuing_profile_count(
        self, headers=None, **request_parameters
    ):
        """Get the number of all existing  application policy queuing profile .

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
            https://developer.cisco.com/docs/dna-center/#!get-application-policy-queuing-profile-count
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

        e_url = "/dna/intent/api/v1/app-policy-queuing-profile-count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a22faef865d55fe48dd2467bee214518_v2_3_7_9", json_data
        )

    def delete_application_policy_queuing_profile(
        self, id, headers=None, **request_parameters
    ):
        """Delete existing custom application policy queuing profile by id .

        Args:
            id(str): id path parameter. Id of custom queuing profile to delete .
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
            https://developer.cisco.com/docs/dna-center/#!delete-application-policy-queuing-profile
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

        e_url = "/dna/intent/api/v1/app-policy-queuing-profile/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ac547ee07c2c5aff983d90cf4306619d_v2_3_7_9", json_data
        )

    def get_application_sets(
        self, limit=None, name=None, offset=None, headers=None, **request_parameters
    ):
        """Get appllication-sets by offset/limit or by name .

        Args:
            offset(int): offset query parameter.
            limit(int): limit query parameter.
            name(str): name query parameter.
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
            https://developer.cisco.com/docs/dna-center/#!get-application-sets
        """
        check_type(headers, dict)
        check_type(offset, int)
        check_type(limit, int)
        check_type(name, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "offset": offset,
            "limit": limit,
            "name": name,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/application-policy-application-set"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_b60dbd805b95030bc2caf345a44b504_v2_3_7_9", json_data
        )

    def delete_application_set(self, id, headers=None, **request_parameters):
        """Delete existing application-set by it's id .

        Args:
            id(str): id query parameter.
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
            https://developer.cisco.com/docs/dna-center/#!delete-application-set
        """
        check_type(headers, dict)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "id": id,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/application-policy-application-set"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a59a448c5c25f1e8246d6827e6e3215_v2_3_7_9", json_data
        )

    def create_application_set(
        self, headers=None, payload=None, active_validation=True, **request_parameters
    ):
        """Create new custom application-set/s .

        Args:
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(list): A JSON serializable Python object to send in the
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
            https://developer.cisco.com/docs/dna-center/#!create-application-set
        """
        check_type(headers, dict)
        check_type(payload, list)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = payload or []
        if active_validation:
            self._request_validator(
                "jsd_cb7563a5058c4801eb842a74ff61c_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/application-policy-application-set"
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
            "bpm_cb7563a5058c4801eb842a74ff61c_v2_3_7_9", json_data
        )

    def get_application_sets_count(self, headers=None, **request_parameters):
        """Get the number of existing application-sets .

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
            https://developer.cisco.com/docs/dna-center/#!get-application-sets-count
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

        e_url = "/dna/intent/api/v1/application-policy-application-set-" + "count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ebc5880945305adb41253c6e4ffec_v2_3_7_9", json_data
        )

    def retrieve_the_list_of_network_devices_with_their_application_visibility_status(
        self,
        app_telemetry_deployment_status=None,
        app_telemetry_readiness_status=None,
        application_registry_sync_status=None,
        cbar_deployment_status=None,
        cbar_readiness_status=None,
        hostname=None,
        ids=None,
        limit=None,
        management_address=None,
        offset=None,
        order=None,
        protocol_pack_status=None,
        protocol_pack_update_status=None,
        site_id=None,
        sort_by=None,
        headers=None,
        **request_parameters
    ):
        """This API retrieves the list of network devices with their application visibility status. The list can be
        filtered using the query parameters. Multiple filters can be applied. .

        Args:
            ids(str): ids query parameter. List of network devices ids. If this parameter is not provided, all
                network devices will be included in the response. Multiple network device IDs can be
                provided. .
            management_address(str): managementAddress query parameter. The management address for the network
                device. This is normally IP address of the device. But it could be hostname in some
                cases like Meraki devices. Partial search is supported. For example, searching for `25.`
                would include `10.25.1.1`, `25.5.10.1`, `225.225.1.0`, `10.10.10.125`, etc. .
            hostname(str): hostname query parameter. The host name of the network device. Partial search is
                supported. For example, searching for `switch` will include `edge-switch1.domain.com`,
                `switch25`, etc. .
            site_id(str): siteId query parameter. The site ID where the network device is assigned. .
            app_telemetry_deployment_status(str): appTelemetryDeploymentStatus query parameter. Status of the
                application telemetry deployment on the network device. Available values: SCHEDULED,
                IN_PROGRESS, COMPLETED, FAILED, NOT_DEPLOYED. .
            app_telemetry_readiness_status(str): appTelemetryReadinessStatus query parameter. Indicates whether the
                network device is ready for application telemetry enablement or not. Available values:
                ENABLED, READY, NOT_READY, NOT_SUPPORTED .
            cbar_deployment_status(str): cbarDeploymentStatus query parameter. Status of the CBAR deployment on the
                network device. Available values: SCHEDULED, IN_PROGRESS, COMPLETED, FAILED,
                NOT_DEPLOYED .
            cbar_readiness_status(str): cbarReadinessStatus query parameter. Indicates whether the network device is
                ready for CBAR enablement or not. Available values: ENABLED, READY, NOT_READY,
                NOT_SUPPORTED .
            protocol_pack_status(str): protocolPackStatus query parameter. Indicates whether the NBAR protocol pack
                is up-to-date or not on the network device. Available values: LATEST, OUTDATED, UNKNOWN
                .
            protocol_pack_update_status(str): protocolPackUpdateStatus query parameter. Status of the NBAR protocol
                pack update on the network device. Available values: SCHEDULED, IN_PROGRESS, SUCCESS,
                FAILED, NONE .
            application_registry_sync_status(str): applicationRegistrySyncStatus query parameter. Indicates whether
                the latest definitions from application registry have been synchronized with the network
                device or not. Available values: SYNCING, IN_SYNC, OUT_OF_SYNC, NOT_APPLICABLE .
            offset(str): offset query parameter. The first record to show for this page; the first record is
                numbered 1. Default value is: 1. .
            limit(str): limit query parameter. The number of records to show for this page. Minimum value is: 1,
                Maximum value is: 500 .
            sort_by(str): sortBy query parameter. A property within the response to sort by. .
            order(str): order query parameter. Whether ascending or descending order should be used to sort the
                response. Available values are: asc, desc. Default value is: asc .
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
            https://developer.cisco.com/docs/dna-center/#!retrieve-the-list-of-network-devices-with-their-application-visibility-status
        """
        check_type(headers, dict)
        check_type(ids, str)
        check_type(management_address, str)
        check_type(hostname, str)
        check_type(site_id, str)
        check_type(app_telemetry_deployment_status, str)
        check_type(app_telemetry_readiness_status, str)
        check_type(cbar_deployment_status, str)
        check_type(cbar_readiness_status, str)
        check_type(protocol_pack_status, str)
        check_type(protocol_pack_update_status, str)
        check_type(application_registry_sync_status, str)
        check_type(offset, str)
        check_type(limit, str)
        check_type(sort_by, str)
        check_type(order, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "ids": ids,
            "managementAddress": management_address,
            "hostname": hostname,
            "siteId": site_id,
            "appTelemetryDeploymentStatus": app_telemetry_deployment_status,
            "appTelemetryReadinessStatus": app_telemetry_readiness_status,
            "cbarDeploymentStatus": cbar_deployment_status,
            "cbarReadinessStatus": cbar_readiness_status,
            "protocolPackStatus": protocol_pack_status,
            "protocolPackUpdateStatus": protocol_pack_update_status,
            "applicationRegistrySyncStatus": application_registry_sync_status,
            "offset": offset,
            "limit": limit,
            "sortBy": sort_by,
            "order": order,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/applicationVisibility/networkDevices"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory("bpm_a5b7b549ba686b2c5c1091157_v2_3_7_9", json_data)

    def retrieve_the_count_of_network_devices_for_the_given_application_visibility_status_filters(
        self,
        app_telemetry_deployment_status=None,
        app_telemetry_readiness_status=None,
        application_registry_sync_status=None,
        cbar_deployment_status=None,
        cbar_readiness_status=None,
        hostname=None,
        ids=None,
        management_address=None,
        protocol_pack_status=None,
        protocol_pack_update_status=None,
        site_id=None,
        headers=None,
        **request_parameters
    ):
        """This API retrieves the count of network devices for the given application visibility status filters. .

        Args:
            ids(str): ids query parameter. List of network devices ids. If this parameter is not provided, all
                network devices will be included in the response. Multiple network device IDs can be
                provided. .
            management_address(str): managementAddress query parameter. The management address for the network
                device. This is normally IP address of the device. But it could be hostname in some
                cases like Meraki devices. Partial search is supported. For example, searching for `25.`
                would include `10.25.1.1`, `25.5.10.1`, `225.225.1.0`, `10.10.10.125`, etc. .
            hostname(str): hostname query parameter. The host name of the network device. Partial search is
                supported. For example, searching for `switch` will include `edge-switch1.domain.com`,
                `switch25`, etc. .
            site_id(str): siteId query parameter. The site ID where the network device is assigned. .
            app_telemetry_deployment_status(str): appTelemetryDeploymentStatus query parameter. Status of the
                application telemetry deployment on the network device. Available values: SCHEDULED,
                IN_PROGRESS, COMPLETED, FAILED, NOT_DEPLOYED .
            app_telemetry_readiness_status(str): appTelemetryReadinessStatus query parameter. Indicates whether the
                network device is ready for application telemetry enablement or not. Available values:
                ENABLED, READY, NOT_READY, NOT_SUPPORTED .
            cbar_deployment_status(str): cbarDeploymentStatus query parameter. Status of the CBAR deployment on the
                network device. Available values: SCHEDULED, IN_PROGRESS, COMPLETED, FAILED,
                NOT_DEPLOYED .
            cbar_readiness_status(str): cbarReadinessStatus query parameter. Indicates whether the network device is
                ready for CBAR enablement or not. Available values: ENABLED, READY, NOT_READY,
                NOT_SUPPORTED .
            protocol_pack_status(str): protocolPackStatus query parameter. Indicates whether the NBAR protocol pack
                is up-to-date or not on the network device. Available values: LATEST, OUTDATED, UNKNOWN
                .
            protocol_pack_update_status(str): protocolPackUpdateStatus query parameter. Status of the NBAR protocol
                pack update on the network device. Available values: SCHEDULED, IN_PROGRESS, SUCCESS,
                FAILED, NONE .
            application_registry_sync_status(str): applicationRegistrySyncStatus query parameter. Indicates whether
                the latest definitions from application registry have been synchronized with the network
                device or not. Available values: SYNCING, IN_SYNC, OUT_OF_SYNC, NOT_APPLICABLE .
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
            https://developer.cisco.com/docs/dna-center/#!retrieve-the-count-of-network-devices-for-the-given-application-visibility-status-filters
        """
        check_type(headers, dict)
        check_type(ids, str)
        check_type(management_address, str)
        check_type(hostname, str)
        check_type(site_id, str)
        check_type(app_telemetry_deployment_status, str)
        check_type(app_telemetry_readiness_status, str)
        check_type(cbar_deployment_status, str)
        check_type(cbar_readiness_status, str)
        check_type(protocol_pack_status, str)
        check_type(protocol_pack_update_status, str)
        check_type(application_registry_sync_status, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "ids": ids,
            "managementAddress": management_address,
            "hostname": hostname,
            "siteId": site_id,
            "appTelemetryDeploymentStatus": app_telemetry_deployment_status,
            "appTelemetryReadinessStatus": app_telemetry_readiness_status,
            "cbarDeploymentStatus": cbar_deployment_status,
            "cbarReadinessStatus": cbar_readiness_status,
            "protocolPackStatus": protocol_pack_status,
            "protocolPackUpdateStatus": protocol_pack_update_status,
            "applicationRegistrySyncStatus": application_registry_sync_status,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/applicationVisibility/networkDevices/" + "count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c378266e951b51b6b15818086b9ea97a_v2_3_7_9", json_data
        )

    def disable_application_telemetry_feature_on_multiple_network_devices(
        self,
        networkDeviceIds=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This API can be used to disable application telemetry feature on multiple network devices. Request payload
        should include the list of network devices where it has to be disabled. This operation pushes
        configuration to the network devices, and is only permitted if the provisioning settings do not mandate
        a config preview for application telemetry disablement. In cases where such settings are active,
        attempting to use this endpoint will result in `422 Unprocessable Content` error. .

        Args:
            networkDeviceIds(list): Application Policy's List of network device ids where Application Telemetry has
                to be disabled  (list of strings).
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
            https://developer.cisco.com/docs/dna-center/#!disable-application-telemetry-feature-on-multiple-network-devices
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
            "networkDeviceIds": networkDeviceIds,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_dda852745acd5ce5a97b0cfdf0de2fd2_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/applicationVisibility/networkDevices/"
            + "disableAppTelemetry"
        )
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
            "bpm_dda852745acd5ce5a97b0cfdf0de2fd2_v2_3_7_9", json_data
        )

    def disable_c_b_a_r_feature_on_multiple_network_devices(
        self,
        networkDeviceIds=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This API can be used to disable CBAR feature on multiple network devices. Request payload should include the
        list of network devices where it has to be disabled. This operation pushes configuration to the network
        devices, and is only permitted if the provisioning settings do not mandate a config preview for CBAR
        disablement. In cases where such settings are active, attempting to use this endpoint will result in
        `422 Unprocessable Content` error. .

        Args:
            networkDeviceIds(list): Application Policy's List of network device ids where CBAR has to be disabled
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
            https://developer.cisco.com/docs/dna-center/#!disable-c-b-a-r-feature-on-multiple-network-devices
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
            "networkDeviceIds": networkDeviceIds,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_b4635c45c3b5e44a30d84daa1d5fb69_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/applicationVisibility/networkDevices/" + "disableCbar"
        )
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
            "bpm_b4635c45c3b5e44a30d84daa1d5fb69_v2_3_7_9", json_data
        )

    def enable_application_telemetry_feature_on_multiple_network_devices(
        self,
        networkDevices=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This API can be used to enable application telemetry feature on multiple network devices. Request payload should
        include the list of network devices where application telemetry has to be enabled. For wireless
        controllers, it also needs the WLAN modes / SSID details to be included for enablement. Please note that
        this operation can be performed even if the feature is already enabled on the network device. It would
        push the updated configurations to the network device. This operation pushes configuration to the
        network devices, and is only permitted if the provisioning settings do not mandate a config preview for
        application telemetry enablement. In cases where such settings are active, attempting to use this
        endpoint will result in `422 Unprocessable Content` error. .

        Args:
            networkDevices(list): Application Policy's networkDevices (list of objects).
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
            https://developer.cisco.com/docs/dna-center/#!enable-application-telemetry-feature-on-multiple-network-devices
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
            "networkDevices": networkDevices,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator("jsd_d73cd5be487a36d0a01d6cdc3_v2_3_7_9").validate(
                _payload
            )

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/applicationVisibility/networkDevices/"
            + "enableAppTelemetry"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(
                endpoint_full_url, params=_params, json=_payload, headers=_headers
            )
        else:
            json_data = self._session.post(
                endpoint_full_url, params=_params, json=_payload
            )

        return self._object_factory("bpm_d73cd5be487a36d0a01d6cdc3_v2_3_7_9", json_data)

    def enable_c_b_a_r_feature_on_multiple_network_devices(
        self,
        networkDevices=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This API can be used to enable CBAR feature on multiple network devices. Request payload should include the list
        of network devices where CBAR has to be enabled. It can optionally include list of interfaces (wired) or
        WLAN modes (wireless) to be excluded from CBAR enablement. Please note that this operation can be
        performed even if the feature is already enabled on the network device. It would push the updated
        configurations to the network device. This operation is only permitted if the provisioning settings do
        not mandate a configuration preview for CBAR enablement. In cases where such settings are active,
        attempting to use this endpoint will result in `422 Unprocessable Content` error. .

        Args:
            networkDevices(list): Application Policy's networkDevices (list of objects).
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
            https://developer.cisco.com/docs/dna-center/#!enable-c-b-a-r-feature-on-multiple-network-devices
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
            "networkDevices": networkDevices,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_e62749061c5aae8ecd1ccc2d315153_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/applicationVisibility/networkDevices/" + "enableCbar"
        )
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
            "bpm_e62749061c5aae8ecd1ccc2d315153_v2_3_7_9", json_data
        )

    def create_application(
        self, headers=None, payload=None, active_validation=True, **request_parameters
    ):
        """Create new Custom application .

        Args:
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(list): A JSON serializable Python object to send in the
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
            https://developer.cisco.com/docs/dna-center/#!create-application
        """
        check_type(headers, dict)
        check_type(payload, list)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = payload or []
        if active_validation:
            self._request_validator(
                "jsd_e1781a990c6b5a4b895d56bcfda2b7cb_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/applications"
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
            "bpm_e1781a990c6b5a4b895d56bcfda2b7cb_v2_3_7_9", json_data
        )

    def edit_application(
        self, headers=None, payload=None, active_validation=True, **request_parameters
    ):
        """Edit the attributes of an existing application .

        Args:
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(list): A JSON serializable Python object to send in the
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
            https://developer.cisco.com/docs/dna-center/#!edit-application
        """
        check_type(headers, dict)
        check_type(payload, list)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = payload or []
        if active_validation:
            self._request_validator(
                "jsd_a3b37dcbe2a150bea06d9dcde1837281_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/applications"
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
            "bpm_a3b37dcbe2a150bea06d9dcde1837281_v2_3_7_9", json_data
        )

    def delete_application(self, id, headers=None, **request_parameters):
        """Delete existing application by its id .

        Args:
            id(str): id query parameter. Application's Id .
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
            https://developer.cisco.com/docs/dna-center/#!delete-application
        """
        check_type(headers, dict)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "id": id,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/applications"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_d11d35f3505652b68905ddf1ee2f7e66_v2_3_7_9", json_data
        )

    def get_applications(
        self, limit=None, name=None, offset=None, headers=None, **request_parameters
    ):
        """Get applications by offset/limit or by name .

        Args:
            offset(int): offset query parameter. The offset of the first application to be returned .
            limit(int): limit query parameter. The maximum number of applications to be returned .
            name(str): name query parameter. Application's name .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            list: JSON response. A list of MyDict objects.
            Access the object's properties by using the dot notation
            or the bracket notation.

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-applications
        """
        check_type(headers, dict)
        check_type(offset, int)
        check_type(limit, int)
        check_type(name, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "offset": offset,
            "limit": limit,
            "name": name,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/applications"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_b12cdd3a75c51258c9e051e84189f92_v2_3_7_9", json_data
        )

    def get_applications_count(self, headers=None, **request_parameters):
        """Get the number of all existing applications .

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
            https://developer.cisco.com/docs/dna-center/#!get-applications-count
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

        e_url = "/dna/intent/api/v1/applications-count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_af5f0aa1ed56ab9b98eb602dbd8366_v2_3_7_9", json_data
        )

    def get_qos_device_interface_info(
        self, network_device_id=None, headers=None, **request_parameters
    ):
        """Get all or by network device id, existing qos device interface infos .

        Args:
            network_device_id(str): networkDeviceId query parameter. network device id .
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
            https://developer.cisco.com/docs/dna-center/#!get-qos-device-interface-info
        """
        check_type(headers, dict)
        check_type(network_device_id, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "networkDeviceId": network_device_id,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/qos-device-interface-info"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c37a46857f0bee5eba0a514091c_v2_3_7_9", json_data
        )

    def update_qos_device_interface_info(
        self, headers=None, payload=None, active_validation=True, **request_parameters
    ):
        """Update existing qos device interface infos associate with network device id .

        Args:
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(list): A JSON serializable Python object to send in the
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
            https://developer.cisco.com/docs/dna-center/#!update-qos-device-interface-info
        """
        check_type(headers, dict)
        check_type(payload, list)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = payload or []
        if active_validation:
            self._request_validator(
                "jsd_ea59df3daf2a57a0b48044cc49c8a1ca_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/qos-device-interface-info"
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
            "bpm_ea59df3daf2a57a0b48044cc49c8a1ca_v2_3_7_9", json_data
        )

    def create_qos_device_interface_info(
        self, headers=None, payload=None, active_validation=True, **request_parameters
    ):
        """Create qos device interface infos associate with network device id to allow the user to mark specific interfaces
        as WAN, to associate WAN interfaces with specific SP Profile and to be able to define a shaper on WAN
        interfaces .

        Args:
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(list): A JSON serializable Python object to send in the
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
            https://developer.cisco.com/docs/dna-center/#!create-qos-device-interface-info
        """
        check_type(headers, dict)
        check_type(payload, list)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = payload or []
        if active_validation:
            self._request_validator(
                "jsd_d045d18062ad5ae59c6f446beb17d675_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/qos-device-interface-info"
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
            "bpm_d045d18062ad5ae59c6f446beb17d675_v2_3_7_9", json_data
        )

    def get_qos_device_interface_info_count(self, headers=None, **request_parameters):
        """Get the number of all existing qos device interface infos group by network device id .

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
            https://developer.cisco.com/docs/dna-center/#!get-qos-device-interface-info-count
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

        e_url = "/dna/intent/api/v1/qos-device-interface-info-count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_b98fe15b531dbb7e20c0f5fa61ab_v2_3_7_9", json_data
        )

    def delete_qos_device_interface_info(self, id, headers=None, **request_parameters):
        """Delete all qos device interface infos associate with network device id .

        Args:
            id(str): id path parameter. Id of the qos device info, this object holds all qos device interface infos
                associate with network device id .
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
            https://developer.cisco.com/docs/dna-center/#!delete-qos-device-interface-info
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

        e_url = "/dna/intent/api/v1/qos-device-interface-info/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a6a5bb5935709b03d0fc37a1d47d4_v2_3_7_9", json_data
        )

    def retrieves_the_application_qo_s_policy_setting(
        self, headers=None, **request_parameters
    ):
        """API to retrieve the application QoS policy setting. .

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
            https://developer.cisco.com/docs/dna-center/#!retrieves-the-application-qo-s-policy-setting
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

        e_url = "/dna/intent/api/v1/qosPolicySetting"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_d3c8a459b787b55338701d8b33_v2_3_7_9", json_data
        )

    def updates_the_application_qo_s_policy_setting(
        self,
        deployByDefaultOnWiredDevices=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """API to update the application QoS policy setting. .

        Args:
            deployByDefaultOnWiredDevices(boolean): Application Policy's Flag to indicate whether QoS policy should
                be deployed automatically on wired network device when it is provisioned. This would be
                only applicable for cases where the network device is assigned to a site where a QoS
                policy has been configured. .
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
            https://developer.cisco.com/docs/dna-center/#!updates-the-application-qo-s-policy-setting
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = {
            "deployByDefaultOnWiredDevices": deployByDefaultOnWiredDevices,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_bc9716ed6eb5c6e9ecb0380501d6138_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/qosPolicySetting"
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
            "bpm_bc9716ed6eb5c6e9ecb0380501d6138_v2_3_7_9", json_data
        )

    def create_application_sets(
        self, headers=None, payload=None, active_validation=True, **request_parameters
    ):
        """Create new custom application set/s .

        Args:
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(list): A JSON serializable Python object to send in the
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
            https://developer.cisco.com/docs/dna-center/#!create-application-sets
        """
        check_type(headers, dict)
        check_type(payload, list)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = payload or []
        if active_validation:
            self._request_validator(
                "jsd_e4d208b5545f66bf0f94a155c81f46_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v2/application-policy-application-set"
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
            "bpm_e4d208b5545f66bf0f94a155c81f46_v2_3_7_9", json_data
        )

    def get_application_sets_v2(
        self, attributes, limit, offset, name=None, headers=None, **request_parameters
    ):
        """Get application set/s by offset/limit or by name .

        Args:
            attributes(str): attributes query parameter. Attributes to retrieve, valid value applicationSet .
            name(str): name query parameter. Application set name .
            offset(int): offset query parameter. The starting point or index from where the paginated results should
                begin. .
            limit(int): limit query parameter. The limit which is the maximum number of items to include in a single
                page of results, max value 500 .
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
            https://developer.cisco.com/docs/dna-center/#!get-application-sets-v2
        """
        check_type(headers, dict)
        check_type(attributes, str, may_be_none=False)
        check_type(name, str)
        check_type(offset, int, may_be_none=False)
        check_type(limit, int, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "attributes": attributes,
            "name": name,
            "offset": offset,
            "limit": limit,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v2/application-policy-application-set"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_b399a8f895b65f3d91926da8508a9295_v2_3_7_9", json_data
        )

    def get_application_set_count(
        self, scalable_group_type, headers=None, **request_parameters
    ):
        """Get the number of all existing application sets .

        Args:
            scalable_group_type(str): scalableGroupType query parameter. Scalable group type to retrieve, valid
                value APPLICATION_GROUP .
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
            https://developer.cisco.com/docs/dna-center/#!get-application-set-count
        """
        check_type(headers, dict)
        check_type(scalable_group_type, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "scalableGroupType": scalable_group_type,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v2/application-policy-application-set-" + "count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c3f0e5c233a5cc39969fdcff6e0288e_v2_3_7_9", json_data
        )

    def delete_application_set_v2(self, id, headers=None, **request_parameters):
        """Delete existing custom application set by id .

        Args:
            id(str): id path parameter. Id of custom application set to delete .
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
            https://developer.cisco.com/docs/dna-center/#!delete-application-set-v2
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

        e_url = "/dna/intent/api/v2/application-policy-application-" + "set/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_fbef625d3225c1eb6db93289a11a33e_v2_3_7_9", json_data
        )

    def edit_applications(
        self, headers=None, payload=None, active_validation=True, **request_parameters
    ):
        """Edit the attributes of an existing application .

        Args:
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(list): A JSON serializable Python object to send in the
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
            https://developer.cisco.com/docs/dna-center/#!edit-applications
        """
        check_type(headers, dict)
        check_type(payload, list)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = payload or []
        if active_validation:
            self._request_validator(
                "jsd_b46a141650debf5946262e8a0961_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v2/applications"
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
            "bpm_b46a141650debf5946262e8a0961_v2_3_7_9", json_data
        )

    def create_applications(
        self, headers=None, payload=None, active_validation=True, **request_parameters
    ):
        """Create new custom application/s .

        Args:
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(list): A JSON serializable Python object to send in the
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
            https://developer.cisco.com/docs/dna-center/#!create-applications
        """
        check_type(headers, dict)
        check_type(payload, list)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = payload or []
        if active_validation:
            self._request_validator(
                "jsd_a14e71c1b98e51eea41255720025b519_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v2/applications"
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
            "bpm_a14e71c1b98e51eea41255720025b519_v2_3_7_9", json_data
        )

    def get_applications_v2(
        self, attributes, limit, offset, name=None, headers=None, **request_parameters
    ):
        """Get application/s by offset/limit or by name .

        Args:
            attributes(str): attributes query parameter. Attributes to retrieve, valid value application .
            name(str): name query parameter. The application name .
            offset(int): offset query parameter. The starting point or index from where the paginated results should
                begin. .
            limit(int): limit query parameter. The limit which is the maximum number of items to include in a single
                page of results, max value 500 .
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
            https://developer.cisco.com/docs/dna-center/#!get-applications-v2
        """
        check_type(headers, dict)
        check_type(attributes, str, may_be_none=False)
        check_type(name, str)
        check_type(offset, int, may_be_none=False)
        check_type(limit, int, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "attributes": attributes,
            "name": name,
            "offset": offset,
            "limit": limit,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v2/applications"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_f8a81055328e2c77f0dcb60a68_v2_3_7_9", json_data
        )

    def get_application_count(
        self, scalable_group_type, headers=None, **request_parameters
    ):
        """Get the number of all existing applications .

        Args:
            scalable_group_type(str): scalableGroupType query parameter. scalable group type to retrieve, valid
                value APPLICATION .
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
            https://developer.cisco.com/docs/dna-center/#!get-application-count
        """
        check_type(headers, dict)
        check_type(scalable_group_type, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "scalableGroupType": scalable_group_type,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v2/applications-count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_d4d0a63b02ed518a95fe297b2a566f1d_v2_3_7_9", json_data
        )

    def delete_application_v2(self, id, headers=None, **request_parameters):
        """Delete existing custom application by id .

        Args:
            id(str): id path parameter. Id of custom application to delete .
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
            https://developer.cisco.com/docs/dna-center/#!delete-application-v2
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

        e_url = "/dna/intent/api/v2/applications/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ef849b2f5415501086635693a458e69b_v2_3_7_9", json_data
        )


# Alias Functions

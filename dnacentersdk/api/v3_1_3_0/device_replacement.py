# -*- coding: utf-8 -*-
"""Cisco Catalyst Center Device Replacement API wrapper.

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


class DeviceReplacement(object):
    """Cisco Catalyst Center Device Replacement API (version: 3.1.3.0).

    Wraps the Catalyst Center Device Replacement
    API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new DeviceReplacement
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Catalyst Center service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(DeviceReplacement, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def return_replacement_devices_with_details(
        self,
        family=None,
        faulty_device_name=None,
        faulty_device_platform=None,
        faulty_device_serial_number=None,
        limit=None,
        offset=None,
        replacement_device_platform=None,
        replacement_device_serial_number=None,
        replacement_status=None,
        sort_by=None,
        sort_order=None,
        headers=None,
        **request_parameters
    ):
        """Get list of replacement devices with replacement details and it can filter replacement devices based on Faulty
        Device Name,Faulty Device Platform, Replacement Device Platform, Faulty Device Serial Number,Replacement
        Device Serial Number, Device Replacement status, Product Family. .

        Args:
            faulty_device_name(str): faultyDeviceName query parameter. Faulty Device Name .
            faulty_device_platform(str): faultyDevicePlatform query parameter. Faulty Device Platform .
            replacement_device_platform(str): replacementDevicePlatform query parameter. Replacement Device Platform
                .
            faulty_device_serial_number(str): faultyDeviceSerialNumber query parameter. Faulty Device Serial Number
                .
            replacement_device_serial_number(str): replacementDeviceSerialNumber query parameter. Replacement Device
                Serial Number .
            replacement_status(list, set, str, tuple): replacementStatus query parameter. Device Replacement status
                [READY-FOR-REPLACEMENT, REPLACEMENT-IN-PROGRESS, REPLACEMENT-SCHEDULED, REPLACED, ERROR,
                NETWORK_READINESS_REQUESTED, NETWORK_READINESS_FAILED] .
            family(list, set, str, tuple): family query parameter. List of families[Routers, Switches and Hubs, AP]
                .
            sort_by(str): sortBy query parameter. SortBy this field. SortBy is mandatory when order is used. .
            sort_order(str): sortOrder query parameter. Order on displayName[ASC,DESC] .
            offset(int): offset query parameter. The first record to show for this page; the first record is
                numbered 1. .
            limit(int): limit query parameter. The number of records to show for this page. .
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
            https://developer.cisco.com/docs/dna-center/#!return-list-of-replacement-devices-with-replacement-details
        """
        check_type(headers, dict)
        check_type(faulty_device_name, str)
        check_type(faulty_device_platform, str)
        check_type(replacement_device_platform, str)
        check_type(faulty_device_serial_number, str)
        check_type(replacement_device_serial_number, str)
        check_type(replacement_status, (list, set, str, tuple))
        check_type(family, (list, set, str, tuple))
        check_type(sort_by, str)
        check_type(sort_order, str)
        check_type(offset, int)
        check_type(limit, int)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "faultyDeviceName": faulty_device_name,
            "faultyDevicePlatform": faulty_device_platform,
            "replacementDevicePlatform": replacement_device_platform,
            "faultyDeviceSerialNumber": faulty_device_serial_number,
            "replacementDeviceSerialNumber": replacement_device_serial_number,
            "replacementStatus": replacement_status,
            "family": family,
            "sortBy": sort_by,
            "sortOrder": sort_order,
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

        e_url = "/dna/intent/api/v1/device-replacement"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_e89f8ba4965853b3a075c7401c564477_v3_1_3_0", json_data
        )

    def unmark_device_for_replacement(
        self, headers=None, payload=None, active_validation=True, **request_parameters
    ):
        """UnMarks device for replacement .

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
            https://developer.cisco.com/docs/dna-center/#!un-mark-device-for-replacement
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
                "jsd_b60f9f312235959812d49dc4c469e83_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/device-replacement"
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
            "bpm_b60f9f312235959812d49dc4c469e83_v3_1_3_0", json_data
        )

    def mark_device_for_replacement(
        self, headers=None, payload=None, active_validation=True, **request_parameters
    ):
        """Marks device for replacement .

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
            https://developer.cisco.com/docs/dna-center/#!mark-device-for-replacement
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
                "jsd_ac6e63199fb05bcf89106a22502c2197_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/device-replacement"
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
            "bpm_ac6e63199fb05bcf89106a22502c2197_v3_1_3_0", json_data
        )

    def return_replacement_devices_count(
        self, replacement_status=None, headers=None, **request_parameters
    ):
        """Get replacement devices count .

        Args:
            replacement_status(list, set, str, tuple): replacementStatus query parameter. Device Replacement status
                list[READY-FOR-REPLACEMENT, REPLACEMENT-IN-PROGRESS, REPLACEMENT-SCHEDULED, REPLACED,
                ERROR] .
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
            https://developer.cisco.com/docs/dna-center/#!return-replacement-devices-count
        """
        check_type(headers, dict)
        check_type(replacement_status, (list, set, str, tuple))
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "replacementStatus": replacement_status,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/device-replacement/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c2b2882c8fb65284bfc9d781e9ddd07f_v3_1_3_0", json_data
        )

    def deploy_device_replacement_workflow(
        self,
        faultyDeviceSerialNumber=None,
        replacementDeviceSerialNumber=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """API to trigger RMA workflow that will replace faulty device with replacement device with same configuration and
        images .

        Args:
            faultyDeviceSerialNumber(string): Device Replacement's Faulty device serial number .
            replacementDeviceSerialNumber(string): Device Replacement's Replacement device serial number .
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
            https://developer.cisco.com/docs/dna-center/#!deploy-device-replacement-workflow
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
            "faultyDeviceSerialNumber": faultyDeviceSerialNumber,
            "replacementDeviceSerialNumber": replacementDeviceSerialNumber,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_f256e33af7501a8bdae2742ca9f6d6_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/device-replacement/workflow"
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
            "bpm_f256e33af7501a8bdae2742ca9f6d6_v3_1_3_0", json_data
        )

    def retrieve_the_status_of_all_the_device_replacement_workflows(
        self,
        family=None,
        faulty_device_name=None,
        faulty_device_platform=None,
        faulty_device_serial_number=None,
        limit=None,
        offset=None,
        replacement_device_platform=None,
        replacement_device_serial_number=None,
        replacement_status=None,
        sort_by=None,
        sort_order=None,
        headers=None,
        **request_parameters
    ):
        """Retrieve the list of device replacements with replacement details. Filters can be applied based on faulty device
        name, faulty device platform, faulty device serial number, replacement device platform, replacement
        device serial number, device replacement status, device family. .

        Args:
            family(str): family query parameter. Faulty device family. .
            faulty_device_name(str): faultyDeviceName query parameter. Faulty device name. .
            faulty_device_platform(str): faultyDevicePlatform query parameter. Faulty device platform. .
            faulty_device_serial_number(str): faultyDeviceSerialNumber query parameter. Faulty device serial number.
                .
            replacement_device_platform(str): replacementDevicePlatform query parameter. Replacement device
                platform. .
            replacement_device_serial_number(str): replacementDeviceSerialNumber query parameter. Replacement device
                serial number. .
            replacement_status(str): replacementStatus query parameter. Device replacement status. Available values
                : MARKED_FOR_REPLACEMENT, NETWORK_READINESS_REQUESTED, NETWORK_READINESS_FAILED,
                READY_FOR_REPLACEMENT, REPLACEMENT_SCHEDULED, REPLACEMENT_IN_PROGRESS, REPLACED, ERROR.
                Replacement status: 'MARKED_FOR_REPLACEMENT' The faulty device has been marked for
                replacement. 'NETWORK_READINESS_REQUESTED' Initiated steps to shut down neighboring
                device interfaces and create a DHCP server on the uplink neighbor if the faulty device
                is part of a fabric setup. 'NETWORK_READINESS_FAILED' Preparation of the network failed.
                Neighboring device interfaces were not shut down, and the DHCP server on the uplink
                neighbor was not created. 'READY_FOR_REPLACEMENT' The network is prepared for the faulty
                device replacement. Neighboring device interfaces are shut down, and the DHCP server on
                the uplink neighbor is set up. 'REPLACEMENT_SCHEDULED' Device replacement has been
                scheduled. 'REPLACEMENT_IN_PROGRESS' Device replacement is currently in progress.
                'REPLACED' Device replacement was successful. 'ERROR' Device replacement has failed. .
            offset(int): offset query parameter. The first record to show for this page; the first record is
                numbered 1. .
            limit(int): limit query parameter. The number of records to show for this page. Maximum value can be
                500. .
            sort_by(str): sortBy query parameter. A property within the response to sort by. Available values : id,
                creationTime, family, faultyDeviceId, fautyDeviceName, faultyDevicePlatform,
                faultyDeviceSerialNumber, replacementDevicePlatform, replacementDeviceSerialNumber,
                replacementTime. .
            sort_order(str): sortOrder query parameter. Whether ascending or descending order should be used to sort
                the response. Available values : ASC, DESC .
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
            https://developer.cisco.com/docs/dna-center/#!retrieve-the-status-of-all-the-device-replacement-workflows
        """
        check_type(headers, dict)
        check_type(family, str)
        check_type(faulty_device_name, str)
        check_type(faulty_device_platform, str)
        check_type(faulty_device_serial_number, str)
        check_type(replacement_device_platform, str)
        check_type(replacement_device_serial_number, str)
        check_type(replacement_status, str)
        check_type(offset, int)
        check_type(limit, int)
        check_type(sort_by, str)
        check_type(sort_order, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "family": family,
            "faultyDeviceName": faulty_device_name,
            "faultyDevicePlatform": faulty_device_platform,
            "faultyDeviceSerialNumber": faulty_device_serial_number,
            "replacementDevicePlatform": replacement_device_platform,
            "replacementDeviceSerialNumber": replacement_device_serial_number,
            "replacementStatus": replacement_status,
            "offset": offset,
            "limit": limit,
            "sortBy": sort_by,
            "sortOrder": sort_order,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/networkDeviceReplacements"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_baf2f1fbbb9456c79497cb324764a3d0_v3_1_3_0", json_data
        )

    def retrieve_the_status_of_device_replacement_workflow_that_replaces_a_faulty_device_with_a_replacement_device(
        self, id, headers=None, **request_parameters
    ):
        """Fetches the status of the device replacement workflow for a given device replacement `id`. Invoke the API
        `/dna/intent/api/v1/networkDeviceReplacements` to `GET` the list of all device replacements and use the
        `id` field data as input to this API. .

        Args:
            id(str): id path parameter. Instance UUID of the device replacement .
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
            https://developer.cisco.com/docs/dna-center/#!retrieve-the-status-of-device-replacement-workflow-that-replaces-a-faulty-device-with-a-replacement-device
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

        e_url = "/dna/intent/api/v1/networkDeviceReplacements/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_babae5a4f2275df0aa468da4a268375e_v3_1_3_0", json_data
        )


# Alias Functions

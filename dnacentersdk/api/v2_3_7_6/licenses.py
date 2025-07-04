# -*- coding: utf-8 -*-
"""Cisco DNA Center Licenses API wrapper.

Copyright (c) 2024 Cisco Systems.

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


class Licenses(object):
    """Cisco DNA Center Licenses API (version: 2.3.7.6).

    Wraps the DNA Center Licenses
    API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new Licenses
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the DNA Center service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(Licenses, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def retrieve_license_setting_v1(self, headers=None, **request_parameters):
        """Retrieves license setting Default smart account id and virtual account id for auto registration of devices for
        smart license flow. If default smart account is not configured, 'defaultSmartAccountId' is 'null'.
        Similarly, if auto registration of devices for smart license flow is not enabled,
        'autoRegistrationVirtualAccountId' is 'null'. For smart proxy connection mode,
        'autoRegistrationVirtualAccountId' is always 'null'. .

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
            ApiError: If the DNA Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!retrieve-license-setting
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

        e_url = "/dna/intent/api/v1/licenseSetting"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_b5ef334945074a609698223cf05db_v2_3_7_6", json_data
        )

    def update_license_setting_v1(
        self,
        autoRegistrationVirtualAccountId=None,
        defaultSmartAccountId=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Update license setting Configure default smart account id  and/or virtual account id for auto registration of
        devices for smart license flow. Virtual account should be part of default smart account. Default smart
        account id cannot be set to 'null'. Auto registration of devices for smart license flow is applicable
        only for direct or on-prem SSM connection mode. .

        Args:
            autoRegistrationVirtualAccountId(string): Licenses's Virtual account id .
            defaultSmartAccountId(string): Licenses's Default smart account id .
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
            ApiError: If the DNA Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!update-license-setting
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
            "defaultSmartAccountId": defaultSmartAccountId,
            "autoRegistrationVirtualAccountId": autoRegistrationVirtualAccountId,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_d9bd7c527d254ecb63d2b709c428043_v2_3_7_6"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/licenseSetting"
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
            "bpm_d9bd7c527d254ecb63d2b709c428043_v2_3_7_6", json_data
        )

    def device_count_details_v1(
        self,
        device_type=None,
        dna_level=None,
        registration_status=None,
        smart_account_id=None,
        virtual_account_name=None,
        headers=None,
        **request_parameters
    ):
        """Get total number of managed device(s). .

        Args:
            device_type(str): device_type query parameter. Type of device .
            registration_status(str): registration_status query parameter. Smart license registration status
                of device .
            dna_level(str): dna_level query parameter. Device Cisco DNA License Level .
            virtual_account_name(str): virtual_account_name query parameter. Virtual account name .
            smart_account_id(str): smart_account_id query parameter. Smart account id .
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
            ApiError: If the DNA Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!device-count-details
        """
        check_type(headers, dict)
        check_type(device_type, str)
        check_type(registration_status, str)
        check_type(dna_level, str)
        check_type(virtual_account_name, str)
        check_type(smart_account_id, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "device_type": device_type,
            "registration_status": registration_status,
            "dna_level": dna_level,
            "virtual_account_name": virtual_account_name,
            "smart_account_id": smart_account_id,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/licenses/device/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c0cf04bdc758b29bb11abbdacbd921_v2_3_7_6", json_data
        )

    def device_license_summary_v1(
        self,
        limit,
        order,
        page_number,
        device_type=None,
        device_uuid=None,
        dna_level=None,
        registration_status=None,
        smart_account_id=None,
        sort_by=None,
        virtual_account_name=None,
        headers=None,
        **request_parameters
    ):
        """Show license summary of device(s). .

        Args:
            page_number(int): page_number query parameter. Page number of response .
            order(str): order query parameter. Sorting order .
            sort_by(str): sort_by query parameter. Sort result by field .
            dna_level(str): dna_level query parameter. Device Cisco DNA license level. The valid values are
                Advantage, Essentials .
            device_type(str): device_type query parameter. Type of device. The valid values are Routers,
                Switches and Hubs, Wireless Controller .
            limit(int): limit query parameter.
            registration_status(str): registration_status query parameter. Smart license registration status
                of device. The valid values are Unknown, NA, Unregistered, Registered,
                Registration_expired, Reservation_in_progress, Registered_slr, Registered_plr,
                Registered_satellite .
            virtual_account_name(str): virtual_account_name query parameter. Name of virtual account .
            smart_account_id(str): smart_account_id query parameter. Id of smart account .
            device_uuid(str): device_uuid query parameter. Id of device .
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
            ApiError: If the DNA Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!device-license-summary
        """
        check_type(headers, dict)
        check_type(page_number, int, may_be_none=False)
        check_type(order, str, may_be_none=False)
        check_type(sort_by, str)
        check_type(dna_level, str)
        check_type(device_type, str)
        check_type(limit, int, may_be_none=False)
        check_type(registration_status, str)
        check_type(virtual_account_name, str)
        check_type(smart_account_id, str)
        check_type(device_uuid, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "page_number": page_number,
            "order": order,
            "sort_by": sort_by,
            "dna_level": dna_level,
            "device_type": device_type,
            "limit": limit,
            "registration_status": registration_status,
            "virtual_account_name": virtual_account_name,
            "smart_account_id": smart_account_id,
            "device_uuid": device_uuid,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/licenses/device/summary"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_f4ba64eef4085d518a612835e128fe3c_v2_3_7_6", json_data
        )

    def device_license_details_v1(
        self, device_uuid, headers=None, **request_parameters
    ):
        """Get detailed license information of a device. .

        Args:
            device_uuid(str): device_uuid path parameter. Id of device .
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
            ApiError: If the DNA Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!device-license-details
        """
        check_type(headers, dict)
        check_type(device_uuid, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "device_uuid": device_uuid,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/licenses/device/{device_uuid}/details"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_f04f865c01d5c17a5f0cb5abe620dd8_v2_3_7_6", json_data
        )

    def device_deregistration_v1(
        self,
        device_uuids=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Deregister device(s) from CSSM(Cisco Smart Software Manager). .

        Args:
            device_uuids(list): Licenses's Comma separated device ids  (list of strings).
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
            ApiError: If the DNA Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!device-deregistration
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = {
            "device_uuids": device_uuids,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_b2f15d0c54c2862a60a904289ddd_v2_3_7_6"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/licenses/smartAccount/virtualAccount/" + "deregister"
        )
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
            "bpm_b2f15d0c54c2862a60a904289ddd_v2_3_7_6", json_data
        )

    def device_registration_v1(
        self,
        virtual_account_name,
        device_uuids=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Register device(s) in CSSM(Cisco Smart Software Manager). .

        Args:
            device_uuids(list): Licenses's Comma separated device ids  (list of strings).
            virtual_account_name(str): virtual_account_name path parameter. Name of virtual account .
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
            ApiError: If the DNA Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!device-registration
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(virtual_account_name, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "virtual_account_name": virtual_account_name,
        }
        _payload = {
            "device_uuids": device_uuids,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_df26f516755a50b5b5477324cf5cb649_v2_3_7_6"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/licenses/smartAccount/virtualAccount/"
            + "{virtual_account_name}/register"
        )
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
            "bpm_df26f516755a50b5b5477324cf5cb649_v2_3_7_6", json_data
        )

    def change_virtual_account_v1(
        self,
        smart_account_id,
        virtual_account_name,
        device_uuids=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Transfer device(s) from one virtual account to another within same smart account. .

        Args:
            device_uuids(list): Licenses's Comma separated device ids  (list of strings).
            smart_account_id(str): smart_account_id path parameter. Id of smart account .
            virtual_account_name(str): virtual_account_name path parameter. Name of target virtual account .
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
            ApiError: If the DNA Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!change-virtual-account
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(smart_account_id, str, may_be_none=False)
        check_type(virtual_account_name, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "smart_account_id": smart_account_id,
            "virtual_account_name": virtual_account_name,
        }
        _payload = {
            "device_uuids": device_uuids,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_bd5b507f58a50aab614e3d7409eec4c_v2_3_7_6"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/licenses/smartAccount/{smart_account_"
            + "id}/virtualAccount/{virtual_account_name}/device/transfe"
            + "r"
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
            "bpm_bd5b507f58a50aab614e3d7409eec4c_v2_3_7_6", json_data
        )

    def virtual_account_details_v1(
        self, smart_account_id, headers=None, **request_parameters
    ):
        """Get virtual account details of a smart account. .

        Args:
            smart_account_id(str): smart_account_id path parameter. Id of smart account .
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
            ApiError: If the DNA Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!virtual-account-details
        """
        check_type(headers, dict)
        check_type(smart_account_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "smart_account_id": smart_account_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/licenses/smartAccount/{smart_account_"
            + "id}/virtualAccounts"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ab450b197375fa9bcd95219113a3075_v2_3_7_6", json_data
        )

    def smart_account_details_v1(self, headers=None, **request_parameters):
        """Retrieve details of all smart accounts. .

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
            ApiError: If the DNA Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!smart-account-details
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

        e_url = "/dna/intent/api/v1/licenses/smartAccounts"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ea3fdbde23325051a76b9d062c2962a0_v2_3_7_6", json_data
        )

    def license_term_details_v1(
        self,
        device_type,
        smart_account_id,
        virtual_account_name,
        headers=None,
        **request_parameters
    ):
        """Get license term details. .

        Args:
            smart_account_id(str): smart_account_id path parameter. Id of smart account .
            virtual_account_name(str): virtual_account_name path parameter. Name of virtual account. Putting
                "All" will give license term detail for all virtual accounts. .
            device_type(str): device_type query parameter. Type of device like router, switch, wireless or
                ise .
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
            ApiError: If the DNA Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!license-term-details
        """
        check_type(headers, dict)
        check_type(device_type, str, may_be_none=False)
        check_type(smart_account_id, str, may_be_none=False)
        check_type(virtual_account_name, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "device_type": device_type,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "smart_account_id": smart_account_id,
            "virtual_account_name": virtual_account_name,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/licenses/term/smartAccount/{smart_acc"
            + "ount_id}/virtualAccount/{virtual_account_name}"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_df2d278e89b45c8ea0ca0a945c001f08_v2_3_7_6", json_data
        )

    def license_usage_details_v1(
        self,
        device_type,
        smart_account_id,
        virtual_account_name,
        headers=None,
        **request_parameters
    ):
        """Get count of purchased and in use Cisco DNA and Network licenses. .

        Args:
            smart_account_id(str): smart_account_id path parameter. Id of smart account .
            virtual_account_name(str): virtual_account_name path parameter. Name of virtual account. Putting
                "All" will give license term detail for all virtual accounts. .
            device_type(str): device_type query parameter. Type of device like router, switch, wireless or
                ise .
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
            ApiError: If the DNA Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!license-usage-details
        """
        check_type(headers, dict)
        check_type(device_type, str, may_be_none=False)
        check_type(smart_account_id, str, may_be_none=False)
        check_type(virtual_account_name, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "device_type": device_type,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "smart_account_id": smart_account_id,
            "virtual_account_name": virtual_account_name,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/licenses/usage/smartAccount/{smart_ac"
            + "count_id}/virtualAccount/{virtual_account_name}"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_e55ecbbda454c6a01d905e6f4cce16_v2_3_7_6", json_data
        )

    # Alias Function
    def virtual_account_details(
        self, smart_account_id, headers=None, **request_parameters
    ):
        """This function is an alias of virtual_account_details_v1 .
        Args:
            smart_account_id(basestring): smart_account_id path parameter. Id of smart account .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of virtual_account_details_v1 .
        """
        return self.virtual_account_details_v1(
            smart_account_id=smart_account_id, headers=headers, **request_parameters
        )

    # Alias Function
    def license_term_details(
        self,
        device_type,
        smart_account_id,
        virtual_account_name,
        headers=None,
        **request_parameters
    ):
        """This function is an alias of license_term_details_v1 .
        Args:
            smart_account_id(basestring): smart_account_id path parameter. Id of smart account .
            virtual_account_name(basestring): virtual_account_name path parameter. Name of virtual account. Putting
                "All" will give license term detail for all virtual accounts. .
            device_type(basestring): device_type query parameter. Type of device like router, switch, wireless or
                ise .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of license_term_details_v1 .
        """
        return self.license_term_details_v1(
            device_type=device_type,
            smart_account_id=smart_account_id,
            virtual_account_name=virtual_account_name,
            headers=headers,
            **request_parameters
        )

    # Alias Function
    def device_count_details(
        self,
        device_type=None,
        dna_level=None,
        registration_status=None,
        smart_account_id=None,
        virtual_account_name=None,
        headers=None,
        **request_parameters
    ):
        """This function is an alias of device_count_details_v1 .
        Args:
            device_type(basestring): device_type query parameter. Type of device .
            registration_status(basestring): registration_status query parameter. Smart license registration status
                of device .
            dna_level(basestring): dna_level query parameter. Device Cisco DNA License Level .
            virtual_account_name(basestring): virtual_account_name query parameter. Virtual account name .
            smart_account_id(basestring): smart_account_id query parameter. Smart account id .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of device_count_details_v1 .
        """
        return self.device_count_details_v1(
            device_type=device_type,
            dna_level=dna_level,
            registration_status=registration_status,
            smart_account_id=smart_account_id,
            virtual_account_name=virtual_account_name,
            headers=headers,
            **request_parameters
        )

    # Alias Function
    def retrieve_license_setting(self, headers=None, **request_parameters):
        """This function is an alias of retrieve_license_setting_v1 .
        Args:
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of retrieve_license_setting_v1 .
        """
        return self.retrieve_license_setting_v1(headers=headers, **request_parameters)

    # Alias Function
    def device_license_summary(
        self,
        limit,
        order,
        page_number,
        device_type=None,
        device_uuid=None,
        dna_level=None,
        registration_status=None,
        smart_account_id=None,
        sort_by=None,
        virtual_account_name=None,
        headers=None,
        **request_parameters
    ):
        """This function is an alias of device_license_summary_v1 .
        Args:
            page_number(int): page_number query parameter. Page number of response .
            order(basestring): order query parameter. Sorting order .
            sort_by(basestring): sort_by query parameter. Sort result by field .
            dna_level(basestring): dna_level query parameter. Device Cisco DNA license level. The valid values are
                Advantage, Essentials .
            device_type(basestring): device_type query parameter. Type of device. The valid values are Routers,
                Switches and Hubs, Wireless Controller .
            limit(int): limit query parameter.
            registration_status(basestring): registration_status query parameter. Smart license registration status
                of device. The valid values are Unknown, NA, Unregistered, Registered,
                Registration_expired, Reservation_in_progress, Registered_slr, Registered_plr,
                Registered_satellite .
            virtual_account_name(basestring): virtual_account_name query parameter. Name of virtual account .
            smart_account_id(basestring): smart_account_id query parameter. Id of smart account .
            device_uuid(basestring): device_uuid query parameter. Id of device .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of device_license_summary_v1 .
        """
        return self.device_license_summary_v1(
            limit=limit,
            order=order,
            page_number=page_number,
            device_type=device_type,
            device_uuid=device_uuid,
            dna_level=dna_level,
            registration_status=registration_status,
            smart_account_id=smart_account_id,
            sort_by=sort_by,
            virtual_account_name=virtual_account_name,
            headers=headers,
            **request_parameters
        )

    # Alias Function
    def change_virtual_account(
        self,
        smart_account_id,
        virtual_account_name,
        device_uuids=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This function is an alias of change_virtual_account_v1 .
        Args:
            device_uuids(list): Licenses's Comma separated device ids  (list of strings).
            smart_account_id(basestring): smart_account_id path parameter. Id of smart account .
            virtual_account_name(basestring): virtual_account_name path parameter. Name of target virtual account .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of change_virtual_account_v1 .
        """
        return self.change_virtual_account_v1(
            smart_account_id=smart_account_id,
            virtual_account_name=virtual_account_name,
            device_uuids=device_uuids,
            headers=headers,
            payload=payload,
            active_validation=active_validation,
            **request_parameters
        )

    # Alias Function
    def device_registration(
        self,
        virtual_account_name,
        device_uuids=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This function is an alias of device_registration_v1 .
        Args:
            device_uuids(list): Licenses's Comma separated device ids  (list of strings).
            virtual_account_name(basestring): virtual_account_name path parameter. Name of virtual account .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of device_registration_v1 .
        """
        return self.device_registration_v1(
            virtual_account_name=virtual_account_name,
            device_uuids=device_uuids,
            headers=headers,
            payload=payload,
            active_validation=active_validation,
            **request_parameters
        )

    # Alias Function
    def smart_account_details(self, headers=None, **request_parameters):
        """This function is an alias of smart_account_details_v1 .
        Args:
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of smart_account_details_v1 .
        """
        return self.smart_account_details_v1(headers=headers, **request_parameters)

    # Alias Function
    def update_license_setting(
        self,
        autoRegistrationVirtualAccountId=None,
        defaultSmartAccountId=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This function is an alias of update_license_setting_v1 .
        Args:
            autoRegistrationVirtualAccountId(string): Licenses's Virtual account id .
            defaultSmartAccountId(string): Licenses's Default smart account id .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of update_license_setting_v1 .
        """
        return self.update_license_setting_v1(
            autoRegistrationVirtualAccountId=autoRegistrationVirtualAccountId,
            defaultSmartAccountId=defaultSmartAccountId,
            headers=headers,
            payload=payload,
            active_validation=active_validation,
            **request_parameters
        )

    # Alias Function
    def device_license_details(self, device_uuid, headers=None, **request_parameters):
        """This function is an alias of device_license_details_v1 .
        Args:
            device_uuid(basestring): device_uuid path parameter. Id of device .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of device_license_details_v1 .
        """
        return self.device_license_details_v1(
            device_uuid=device_uuid, headers=headers, **request_parameters
        )

    # Alias Function
    def device_deregistration(
        self,
        device_uuids=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This function is an alias of device_deregistration_v1 .
        Args:
            device_uuids(list): Licenses's Comma separated device ids  (list of strings).
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of device_deregistration_v1 .
        """
        return self.device_deregistration_v1(
            device_uuids=device_uuids,
            headers=headers,
            payload=payload,
            active_validation=active_validation,
            **request_parameters
        )

    # Alias Function
    def license_usage_details(
        self,
        device_type,
        smart_account_id,
        virtual_account_name,
        headers=None,
        **request_parameters
    ):
        """This function is an alias of license_usage_details_v1 .
        Args:
            smart_account_id(basestring): smart_account_id path parameter. Id of smart account .
            virtual_account_name(basestring): virtual_account_name path parameter. Name of virtual account. Putting
                "All" will give license term detail for all virtual accounts. .
            device_type(basestring): device_type query parameter. Type of device like router, switch, wireless or
                ise .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of license_usage_details_v1 .
        """
        return self.license_usage_details_v1(
            device_type=device_type,
            smart_account_id=smart_account_id,
            virtual_account_name=virtual_account_name,
            headers=headers,
            **request_parameters
        )

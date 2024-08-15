# -*- coding: utf-8 -*-
"""Cisco DNA Center Device Onboarding (PnP) API wrapper.

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


from builtins import *


from ...restsession import RestSession
from ...utils import (
    apply_path_params,
    check_type,
    dict_from_items_with_values,
    dict_of_str,
)


class DeviceOnboardingPnp(object):
    """Cisco DNA Center Device Onboarding (PnP) API (version: 2.3.7.6).

    Wraps the DNA Center Device Onboarding (PnP)
    API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new DeviceOnboardingPnp
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the DNA Center service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(DeviceOnboardingPnp, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def authorize_device(self,
                         deviceIdList=None,
                         headers=None,
                         payload=None,
                         active_validation=True,
                         **request_parameters):
        """Authorizes one of more devices. A device can only be authorized if Authorization is set in Device Settings. .

        Args:
            deviceIdList(list): Device Onboarding (PnP)'s Device Id List (list of strings).
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
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if 'Content-Type' in headers:
                check_type(headers.get('Content-Type'),
                           str)
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }
        _payload = {
            'deviceIdList':
                deviceIdList,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_d9227adc5f02b7cd264af7255d19_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/api/v1/onboarding/pnp-device/authorize')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_d9227adc5f02b7cd264af7255d19_v2_3_7_6', json_data)

    def add_device(self,
                   deviceInfo=None,
                   headers=None,
                   payload=None,
                   active_validation=True,
                   **request_parameters):
        """Adds a device to the PnP database. .

        Args:
            deviceInfo(object): Device Onboarding (PnP)'s deviceInfo.
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
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if 'Content-Type' in headers:
                check_type(headers.get('Content-Type'),
                           str, may_be_none=False)
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }
        _payload = {
            'deviceInfo':
                deviceInfo,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_f04b76067507b9384e409e9431ef3_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/onboarding/pnp-device')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_f04b76067507b9384e409e9431ef3_v2_3_7_6', json_data)

    def get_device_list(self,
                        hostname=None,
                        last_contact=None,
                        limit=None,
                        mac_address=None,
                        name=None,
                        offset=None,
                        onb_state=None,
                        pid=None,
                        serial_number=None,
                        site_name=None,
                        smart_account_id=None,
                        sort=None,
                        sort_order=None,
                        source=None,
                        state=None,
                        virtual_account_id=None,
                        workflow_id=None,
                        workflow_name=None,
                        headers=None,
                        **request_parameters):
        """Returns list of devices from Plug & Play based on filter criteria. Returns 50 devices by default. This endpoint
        supports Pagination and Sorting. .

        Args:
            limit(int,str): limit query parameter. Limits number of results .
            offset(int,str): offset query parameter. Index of first result .
            sort(str, list, set, tuple): sort query parameter. Comma seperated list of fields to sort on .
            sort_order(str): sortOrder query parameter. Sort Order Ascending (asc) or Descending (des) .
            serial_number(str, list, set, tuple): serialNumber query parameter. Device Serial Number .
            state(str, list, set, tuple): state query parameter. Device State .
            onb_state(str, list, set, tuple): onbState query parameter. Device Onboarding State .
            name(str, list, set, tuple): name query parameter. Device Name .
            pid(str, list, set, tuple): pid query parameter. Device ProductId .
            source(str, list, set, tuple): source query parameter. Device Source .
            workflow_id(str, list, set, tuple): workflowId query parameter. Device Workflow Id .
            workflow_name(str, list, set, tuple): workflowName query parameter. Device Workflow Name .
            smart_account_id(str, list, set, tuple): smartAccountId query parameter. Device Smart Account .
            virtual_account_id(str, list, set, tuple): virtualAccountId query parameter. Device Virtual
                Account .
            last_contact(bool): lastContact query parameter. Device Has Contacted lastContact > 0 .
            mac_address(str): macAddress query parameter. Device Mac Address .
            hostname(str): hostname query parameter. Device Hostname .
            site_name(str): siteName query parameter. Device Site Name .
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
            ApiError: If the DNA Center cloud returns an error.
        """
        check_type(headers, dict)
        check_type(limit, (int, str))
        check_type(offset, (int, str))
        check_type(sort, (str, list, set, tuple))
        check_type(sort_order, str)
        check_type(serial_number, (str, list, set, tuple))
        check_type(state, (str, list, set, tuple))
        check_type(onb_state, (str, list, set, tuple))
        check_type(name, (str, list, set, tuple))
        check_type(pid, (str, list, set, tuple))
        check_type(source, (str, list, set, tuple))
        check_type(workflow_id, (str, list, set, tuple))
        check_type(workflow_name, (str, list, set, tuple))
        check_type(smart_account_id, (str, list, set, tuple))
        check_type(virtual_account_id, (str, list, set, tuple))
        check_type(last_contact, bool)
        check_type(mac_address, str)
        check_type(hostname, str)
        check_type(site_name, str)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'limit':
                limit,
            'offset':
                offset,
            'sort':
                sort,
            'sortOrder':
                sort_order,
            'serialNumber':
                serial_number,
            'state':
                state,
            'onbState':
                onb_state,
            'name':
                name,
            'pid':
                pid,
            'source':
                source,
            'workflowId':
                workflow_id,
            'workflowName':
                workflow_name,
            'smartAccountId':
                smart_account_id,
            'virtualAccountId':
                virtual_account_id,
            'lastContact':
                last_contact,
            'macAddress':
                mac_address,
            'hostname':
                hostname,
            'siteName':
                site_name,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/onboarding/pnp-device')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_c033291ec4591886bd6ed25f900c1b_v2_3_7_6', json_data)

    def claim_device(self,
                     configFileUrl=None,
                     configId=None,
                     deviceClaimList=None,
                     fileServiceId=None,
                     imageId=None,
                     imageUrl=None,
                     populateInventory=None,
                     projectId=None,
                     workflowId=None,
                     headers=None,
                     payload=None,
                     active_validation=True,
                     **request_parameters):
        """Claims one of more devices with specified workflow .

        Args:
            configFileUrl(string): Device Onboarding (PnP)'s configFileUrl.
            configId(string): Device Onboarding (PnP)'s configId.
            deviceClaimList(list): Device Onboarding (PnP)'s deviceClaimList (list of objects).
            fileServiceId(string): Device Onboarding (PnP)'s fileServiceId.
            imageId(string): Device Onboarding (PnP)'s imageId.
            imageUrl(string): Device Onboarding (PnP)'s imageUrl.
            populateInventory(boolean): Device Onboarding (PnP)'s populateInventory.
            projectId(string): Device Onboarding (PnP)'s projectId.
            workflowId(string): Device Onboarding (PnP)'s workflowId.
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
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if 'Content-Type' in headers:
                check_type(headers.get('Content-Type'),
                           str, may_be_none=False)
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }
        _payload = {
            'configFileUrl':
                configFileUrl,
            'configId':
                configId,
            'deviceClaimList':
                deviceClaimList,
            'fileServiceId':
                fileServiceId,
            'imageId':
                imageId,
            'imageUrl':
                imageUrl,
            'populateInventory':
                populateInventory,
            'projectId':
                projectId,
            'workflowId':
                workflowId,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_e722e05046d5262b55c125237e9b67d_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/onboarding/pnp-device/claim')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_e722e05046d5262b55c125237e9b67d_v2_3_7_6', json_data)

    def get_device_count(self,
                         last_contact=None,
                         name=None,
                         onb_state=None,
                         pid=None,
                         serial_number=None,
                         smart_account_id=None,
                         source=None,
                         state=None,
                         virtual_account_id=None,
                         workflow_id=None,
                         workflow_name=None,
                         headers=None,
                         **request_parameters):
        """Returns the device count based on filter criteria. This is useful for pagination .

        Args:
            serial_number(str, list, set, tuple): serialNumber query parameter. Device Serial Number .
            state(str, list, set, tuple): state query parameter. Device State .
            onb_state(str, list, set, tuple): onbState query parameter. Device Onboarding State .
            name(str, list, set, tuple): name query parameter. Device Name .
            pid(str, list, set, tuple): pid query parameter. Device ProductId .
            source(str, list, set, tuple): source query parameter. Device Source .
            workflow_id(str, list, set, tuple): workflowId query parameter. Device Workflow Id .
            workflow_name(str, list, set, tuple): workflowName query parameter. Device Workflow Name .
            smart_account_id(str, list, set, tuple): smartAccountId query parameter. Device Smart Account .
            virtual_account_id(str, list, set, tuple): virtualAccountId query parameter. Device Virtual
                Account .
            last_contact(bool): lastContact query parameter. Device Has Contacted lastContact > 0 .
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
        """
        check_type(headers, dict)
        check_type(serial_number, (str, list, set, tuple))
        check_type(state, (str, list, set, tuple))
        check_type(onb_state, (str, list, set, tuple))
        check_type(name, (str, list, set, tuple))
        check_type(pid, (str, list, set, tuple))
        check_type(source, (str, list, set, tuple))
        check_type(workflow_id, (str, list, set, tuple))
        check_type(workflow_name, (str, list, set, tuple))
        check_type(smart_account_id, (str, list, set, tuple))
        check_type(virtual_account_id, (str, list, set, tuple))
        check_type(last_contact, bool)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'serialNumber':
                serial_number,
            'state':
                state,
            'onbState':
                onb_state,
            'name':
                name,
            'pid':
                pid,
            'source':
                source,
            'workflowId':
                workflow_id,
            'workflowName':
                workflow_name,
            'smartAccountId':
                smart_account_id,
            'virtualAccountId':
                virtual_account_id,
            'lastContact':
                last_contact,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/onboarding/pnp-device/count')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_ce6d91900556839c09184d8a11c04d_v2_3_7_6', json_data)

    def get_device_history(self,
                           serial_number,
                           sort=None,
                           sort_order=None,
                           headers=None,
                           **request_parameters):
        """Returns history for a specific device. Serial number is a required parameter .

        Args:
            serial_number(str): serialNumber query parameter. Device Serial Number .
            sort(str, list, set, tuple): sort query parameter. Comma seperated list of fields to sort on .
            sort_order(str): sortOrder query parameter. Sort Order Ascending (asc) or Descending (des) .
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
        """
        check_type(headers, dict)
        check_type(serial_number, str,
                   may_be_none=False)
        check_type(sort, (str, list, set, tuple))
        check_type(sort_order, str)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'serialNumber':
                serial_number,
            'sort':
                sort,
            'sortOrder':
                sort_order,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/onboarding/pnp-device/history')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_f03966978a7f5cd4b3228dcae71373fe_v2_3_7_6', json_data)

    def import_devices_in_bulk(self,
                               headers=None,
                               payload=None,
                               active_validation=True,
                               **request_parameters):
        """Add devices to PnP in bulk .

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
            ApiError: If the DNA Center cloud returns an error.
        """
        check_type(headers, dict)
        check_type(payload, list)
        if headers is not None:
            if 'Content-Type' in headers:
                check_type(headers.get('Content-Type'),
                           str, may_be_none=False)
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }
        _payload = payload or []
        if active_validation:
            self._request_validator('jsd_a7d6d604f38f5f849af79d8768bddfc1_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/onboarding/pnp-device/import')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_a7d6d604f38f5f849af79d8768bddfc1_v2_3_7_6', json_data)

    def reset_device(self,
                     deviceResetList=None,
                     projectId=None,
                     workflowId=None,
                     headers=None,
                     payload=None,
                     active_validation=True,
                     **request_parameters):
        """Recovers a device from a Workflow Execution Error state .

        Args:
            deviceResetList(list): Device Onboarding (PnP)'s deviceResetList (list of objects).
            projectId(string): Device Onboarding (PnP)'s projectId.
            workflowId(string): Device Onboarding (PnP)'s workflowId.
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
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if 'Content-Type' in headers:
                check_type(headers.get('Content-Type'),
                           str, may_be_none=False)
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }
        _payload = {
            'deviceResetList':
                deviceResetList,
            'projectId':
                projectId,
            'workflowId':
                workflowId,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_f5a13405ba69f3957b98db8663a_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/onboarding/pnp-device/reset')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_f5a13405ba69f3957b98db8663a_v2_3_7_6', json_data)

    def get_sync_result_for_virtual_account(self,
                                            domain,
                                            name,
                                            headers=None,
                                            **request_parameters):
        """Returns the summary of devices synced from the given smart account & virtual account with PnP (Deprecated) .

        Args:
            domain(str): domain path parameter. Smart Account Domain .
            name(str): name path parameter. Virtual Account Name .
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
        """
        check_type(headers, dict)
        check_type(domain, str,
                   may_be_none=False)
        check_type(name, str,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'domain': domain,
            'name': name,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/onboarding/pnp-'
                 + 'device/sacct/{domain}/vacct/{name}/sync-result')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_b34f9daa98735533a61287ce30d216b6_v2_3_7_6', json_data)

    def claim_a_device_to_a_site(self,
                                 configInfo=None,
                                 deviceId=None,
                                 gateway=None,
                                 imageInfo=None,
                                 ipInterfaceName=None,
                                 rfProfile=None,
                                 sensorProfile=None,
                                 siteId=None,
                                 staticIP=None,
                                 subnetMask=None,
                                 type=None,
                                 vlanId=None,
                                 headers=None,
                                 payload=None,
                                 active_validation=True,
                                 **request_parameters):
        """Claim a device based on Catalyst Center Site-based design process. Some required parameters differ based on
        device platform: Default/StackSwitch: imageInfo, configInfo.   AccessPoints: rfProfile.   Sensors:
        sensorProfile.   CatalystWLC/MobilityExpress/EWC: staticIP, subnetMask, gateway. vlanId and
        ipInterfaceName are also allowed for Catalyst 9800 WLCs. .

        Args:
            configInfo(object): Device Onboarding (PnP)'s configInfo.
            deviceId(string): Device Onboarding (PnP)'s Device Id.
            gateway(string): Device Onboarding (PnP)'s for CatalystWLC/MobilityExpress .
            imageInfo(object): Device Onboarding (PnP)'s imageInfo.
            ipInterfaceName(string): Device Onboarding (PnP)'s for Catalyst 9800 WLC .
            rfProfile(string): Device Onboarding (PnP)'s for Access Points .
            sensorProfile(string): Device Onboarding (PnP)'s for Sensors .
            siteId(string): Device Onboarding (PnP)'s Site Id.
            staticIP(string): Device Onboarding (PnP)'s for CatalystWLC/MobilityExpress .
            subnetMask(string): Device Onboarding (PnP)'s for CatalystWLC/MobilityExpress .
            type(string): Device Onboarding (PnP)'s Type. Available values are 'Default', 'StackSwitch',
                'AccessPoint', 'Sensor', 'CatalystWLC' and 'MobilityExpress'.
            vlanId(string): Device Onboarding (PnP)'s for Catalyst 9800 WLC .
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
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if 'Content-Type' in headers:
                check_type(headers.get('Content-Type'),
                           str, may_be_none=False)
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }
        _payload = {
            'deviceId':
                deviceId,
            'siteId':
                siteId,
            'type':
                type,
            'imageInfo':
                imageInfo,
            'configInfo':
                configInfo,
            'rfProfile':
                rfProfile,
            'staticIP':
                staticIP,
            'subnetMask':
                subnetMask,
            'gateway':
                gateway,
            'vlanId':
                vlanId,
            'ipInterfaceName':
                ipInterfaceName,
            'sensorProfile':
                sensorProfile,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_e11daa984f535a08bc1eb01bc84bc399_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/onboarding/pnp-device/site-claim')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_e11daa984f535a08bc1eb01bc84bc399_v2_3_7_6', json_data)

    def preview_config(self,
                       deviceId=None,
                       siteId=None,
                       type=None,
                       headers=None,
                       payload=None,
                       active_validation=True,
                       **request_parameters):
        """Triggers a preview for site-based Day 0 Configuration .

        Args:
            deviceId(string): Device Onboarding (PnP)'s deviceId.
            siteId(string): Device Onboarding (PnP)'s siteId.
            type(string): Device Onboarding (PnP)'s type. Available values are 'Default', 'AccessPoint',
                'StackSwitch', 'Sensor' and 'MobilityExpress'.
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
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if 'Content-Type' in headers:
                check_type(headers.get('Content-Type'),
                           str, may_be_none=False)
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }
        _payload = {
            'deviceId':
                deviceId,
            'siteId':
                siteId,
            'type':
                type,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_fc416739f3c655ed911884aec0130e83_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/onboarding/pnp-device/site-config-'
                 + 'preview')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_fc416739f3c655ed911884aec0130e83_v2_3_7_6', json_data)

    def un_claim_device(self,
                        deviceIdList=None,
                        headers=None,
                        payload=None,
                        active_validation=True,
                        **request_parameters):
        """Un-Claims one of more devices with specified workflow (Deprecated). .

        Args:
            deviceIdList(list): Device Onboarding (PnP)'s deviceIdList (list of strings).
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
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if 'Content-Type' in headers:
                check_type(headers.get('Content-Type'),
                           str, may_be_none=False)
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }
        _payload = {
            'deviceIdList':
                deviceIdList,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_97e350a7a690cdfeffa5eaca_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/onboarding/pnp-device/unclaim')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_97e350a7a690cdfeffa5eaca_v2_3_7_6', json_data)

    def sync_virtual_account_devices(self,
                                     autoSyncPeriod=None,
                                     ccoUser=None,
                                     expiry=None,
                                     lastSync=None,
                                     profile=None,
                                     smartAccountId=None,
                                     syncResult=None,
                                     syncResultStr=None,
                                     syncStartTime=None,
                                     syncStatus=None,
                                     tenantId=None,
                                     token=None,
                                     virtualAccountId=None,
                                     headers=None,
                                     payload=None,
                                     active_validation=True,
                                     **request_parameters):
        """Synchronizes the device info from the given smart account & virtual account with the PnP database. The response
        payload returns a list of synced devices (Deprecated). .

        Args:
            autoSyncPeriod(integer): Device Onboarding (PnP)'s autoSyncPeriod.
            ccoUser(string): Device Onboarding (PnP)'s ccoUser.
            expiry(integer): Device Onboarding (PnP)'s expiry.
            lastSync(integer): Device Onboarding (PnP)'s lastSync.
            profile(object): Device Onboarding (PnP)'s profile.
            smartAccountId(string): Device Onboarding (PnP)'s smartAccountId.
            syncResult(object): Device Onboarding (PnP)'s syncResult.
            syncResultStr(string): Device Onboarding (PnP)'s syncResultStr.
            syncStartTime(integer): Device Onboarding (PnP)'s syncStartTime.
            syncStatus(string): Device Onboarding (PnP)'s syncStatus. Available values are 'NOT_SYNCED', 'SYNCING',
                'SUCCESS' and 'FAILURE'.
            tenantId(string): Device Onboarding (PnP)'s tenantId.
            token(string): Device Onboarding (PnP)'s token.
            virtualAccountId(string): Device Onboarding (PnP)'s virtualAccountId.
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
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if 'Content-Type' in headers:
                check_type(headers.get('Content-Type'),
                           str, may_be_none=False)
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }
        _payload = {
            'autoSyncPeriod':
                autoSyncPeriod,
            'ccoUser':
                ccoUser,
            'expiry':
                expiry,
            'lastSync':
                lastSync,
            'profile':
                profile,
            'smartAccountId':
                smartAccountId,
            'syncResult':
                syncResult,
            'syncResultStr':
                syncResultStr,
            'syncStartTime':
                syncStartTime,
            'syncStatus':
                syncStatus,
            'tenantId':
                tenantId,
            'token':
                token,
            'virtualAccountId':
                virtualAccountId,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_ad0cce45817862bebfc839bf5ae_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/onboarding/pnp-device/vacct-sync')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_ad0cce45817862bebfc839bf5ae_v2_3_7_6', json_data)

    def update_device(self,
                      id,
                      deviceInfo=None,
                      headers=None,
                      payload=None,
                      active_validation=True,
                      **request_parameters):
        """Updates device details specified by device id in PnP database .

        Args:
            deviceInfo(object): Device Onboarding (PnP)'s deviceInfo.
            id(string): Device Onboarding (PnP)'s Id.
            id(str): id path parameter.
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
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(id, str,
                   may_be_none=False)
        if headers is not None:
            if 'Content-Type' in headers:
                check_type(headers.get('Content-Type'),
                           str, may_be_none=False)
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'id': id,
        }
        _payload = {
            'id':
                id,
            'deviceInfo':
                deviceInfo,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_cec8139f6b1c5e5991d12197206029a0_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/onboarding/pnp-device/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload,
                                          headers=_headers)
        else:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload)

        return self._object_factory('bpm_cec8139f6b1c5e5991d12197206029a0_v2_3_7_6', json_data)

    def delete_device_by_id_from_pnp(self,
                                     id,
                                     headers=None,
                                     **request_parameters):
        """Deletes specified device from PnP database .

        Args:
            id(str): id path parameter.
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
        """
        check_type(headers, dict)
        check_type(id, str,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'id': id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/onboarding/pnp-device/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(endpoint_full_url, params=_params,
                                             headers=_headers)
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_cfec9657be95cac9679e5a808e95124_v2_3_7_6', json_data)

    def get_device_by_id(self,
                         id,
                         headers=None,
                         **request_parameters):
        """Returns device details specified by device id .

        Args:
            id(str): id path parameter.
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
        """
        check_type(headers, dict)
        check_type(id, str,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'id': id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/onboarding/pnp-device/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_d2ead8063ab552ea4abcb3e947a092a_v2_3_7_6', json_data)

    def update_pnp_global_settings(self,
                                   acceptEula=None,
                                   defaultProfile=None,
                                   id=None,
                                   savaMappingList=None,
                                   headers=None,
                                   payload=None,
                                   active_validation=True,
                                   **request_parameters):
        """Updates the user's list of global PnP settings .

        Args:
            acceptEula(string): Device Onboarding (PnP)'s Accept Eula.
            defaultProfile(object): Device Onboarding (PnP)'s defaultProfile.
            id(string): Device Onboarding (PnP)'s Id.
            savaMappingList(list): Device Onboarding (PnP)'s savaMappingList (list of objects).
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
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if 'Content-Type' in headers:
                check_type(headers.get('Content-Type'),
                           str, may_be_none=False)
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }
        _payload = {
            'id':
                id,
            'acceptEula':
                acceptEula,
            'defaultProfile':
                defaultProfile,
            'savaMappingList':
                savaMappingList,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_fc8410781af357b6be17a2104ce5efb1_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/onboarding/pnp-settings')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload,
                                          headers=_headers)
        else:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload)

        return self._object_factory('bpm_fc8410781af357b6be17a2104ce5efb1_v2_3_7_6', json_data)

    def get_pnp_global_settings(self,
                                headers=None,
                                **request_parameters):
        """Returns global PnP settings of the user .

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
        """
        check_type(headers, dict)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/onboarding/pnp-settings')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_b37eb826a4ad5283ae85dc4628045b40_v2_3_7_6', json_data)

    def get_smart_account_list(self,
                               headers=None,
                               **request_parameters):
        """Returns the list of Smart Account domains .

        Args:
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
            ApiError: If the DNA Center cloud returns an error.
        """
        check_type(headers, dict)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/onboarding/pnp-settings/sacct')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_e433c01ec815f18af40dcf05481ef52_v2_3_7_6', json_data)

    def get_virtual_account_list(self,
                                 domain,
                                 headers=None,
                                 **request_parameters):
        """Returns list of virtual accounts associated with the specified smart account .

        Args:
            domain(str): domain path parameter. Smart Account Domain .
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
            ApiError: If the DNA Center cloud returns an error.
        """
        check_type(headers, dict)
        check_type(domain, str,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'domain': domain,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/onboarding/pnp-'
                 + 'settings/sacct/{domain}/vacct')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_c1a9d2c14ac255fd812d6e7aa20a57cc_v2_3_7_6', json_data)

    def add_virtual_account(self,
                            autoSyncPeriod=None,
                            ccoUser=None,
                            expiry=None,
                            lastSync=None,
                            profile=None,
                            smartAccountId=None,
                            syncResult=None,
                            syncResultStr=None,
                            syncStartTime=None,
                            syncStatus=None,
                            tenantId=None,
                            token=None,
                            virtualAccountId=None,
                            headers=None,
                            payload=None,
                            active_validation=True,
                            **request_parameters):
        """Registers a Smart Account, Virtual Account and the relevant server profile info with the PnP System & database.
        The devices present in the registered virtual account are synced with the PnP database as well. The
        response payload returns the new profile .

        Args:
            autoSyncPeriod(integer): Device Onboarding (PnP)'s autoSyncPeriod.
            ccoUser(string): Device Onboarding (PnP)'s ccoUser.
            expiry(integer): Device Onboarding (PnP)'s expiry.
            lastSync(integer): Device Onboarding (PnP)'s lastSync.
            profile(object): Device Onboarding (PnP)'s profile.
            smartAccountId(string): Device Onboarding (PnP)'s smartAccountId.
            syncResult(object): Device Onboarding (PnP)'s syncResult.
            syncResultStr(string): Device Onboarding (PnP)'s syncResultStr.
            syncStartTime(integer): Device Onboarding (PnP)'s syncStartTime.
            syncStatus(string): Device Onboarding (PnP)'s syncStatus. Available values are 'NOT_SYNCED', 'SYNCING',
                'SUCCESS' and 'FAILURE'.
            tenantId(string): Device Onboarding (PnP)'s tenantId.
            token(string): Device Onboarding (PnP)'s token.
            virtualAccountId(string): Device Onboarding (PnP)'s virtualAccountId.
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
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if 'Content-Type' in headers:
                check_type(headers.get('Content-Type'),
                           str, may_be_none=False)
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }
        _payload = {
            'autoSyncPeriod':
                autoSyncPeriod,
            'ccoUser':
                ccoUser,
            'expiry':
                expiry,
            'lastSync':
                lastSync,
            'profile':
                profile,
            'smartAccountId':
                smartAccountId,
            'syncResult':
                syncResult,
            'syncResultStr':
                syncResultStr,
            'syncStartTime':
                syncStartTime,
            'syncStatus':
                syncStatus,
            'tenantId':
                tenantId,
            'token':
                token,
            'virtualAccountId':
                virtualAccountId,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_c6774ff9549a53d4b41fdd2d88f1d0f5_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/onboarding/pnp-settings/savacct')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_c6774ff9549a53d4b41fdd2d88f1d0f5_v2_3_7_6', json_data)

    def update_pnp_server_profile(self,
                                  ccoUser=None,
                                  profile=None,
                                  smartAccountId=None,
                                  virtualAccountId=None,
                                  headers=None,
                                  payload=None,
                                  active_validation=True,
                                  **request_parameters):
        """Updates the PnP Server profile in a registered Virtual Account in the PnP database. The response payload returns
        the updated smart & virtual account info .

        Args:
            ccoUser(string): Device Onboarding (PnP)'s Cco User.
            profile(object): Device Onboarding (PnP)'s profile.
            smartAccountId(string): Device Onboarding (PnP)'s Smart Account Id.
            virtualAccountId(string): Device Onboarding (PnP)'s Virtual Account Id.
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
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }
        _payload = {
            'smartAccountId':
                smartAccountId,
            'virtualAccountId':
                virtualAccountId,
            'profile':
                profile,
            'ccoUser':
                ccoUser,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_bc3cb471beaf5bfeb47201993c023068_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/onboarding/pnp-settings/savacct')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload,
                                          headers=_headers)
        else:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload)

        return self._object_factory('bpm_bc3cb471beaf5bfeb47201993c023068_v2_3_7_6', json_data)

    def deregister_virtual_account(self,
                                   domain,
                                   name,
                                   headers=None,
                                   **request_parameters):
        """Deregisters the specified smart account & virtual account info and the associated device information from the
        PnP System & database. The devices associated with the deregistered virtual account are removed from the
        PnP database as well. The response payload contains the deregistered smart & virtual account information
        .

        Args:
            domain(str): domain query parameter. Smart Account Domain .
            name(str): name query parameter. Virtual Account Name .
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
        """
        check_type(headers, dict)
        check_type(domain, str,
                   may_be_none=False)
        check_type(name, str,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'domain':
                domain,
            'name':
                name,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/onboarding/pnp-settings/vacct')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(endpoint_full_url, params=_params,
                                             headers=_headers)
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_f785e5c9b1c5690b29a65d96f6a601a_v2_3_7_6', json_data)

    def get_workflows(self,
                      limit=None,
                      name=None,
                      offset=None,
                      sort=None,
                      sort_order=None,
                      type=None,
                      headers=None,
                      **request_parameters):
        """Returns the list of workflows based on filter criteria. If a limit is not specified, it will default to return
        50 workflows. Pagination and sorting are also supported by this endpoint .

        Args:
            limit(int,str): limit query parameter. Limits number of results .
            offset(int,str): offset query parameter. Index of first result .
            sort(str, list, set, tuple): sort query parameter. Comma seperated lost of fields to sort on .
            sort_order(str): sortOrder query parameter. Sort Order Ascending (asc) or Descending (des) .
            type(str, list, set, tuple): type query parameter. Workflow Type .
            name(str, list, set, tuple): name query parameter. Workflow Name .
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
            ApiError: If the DNA Center cloud returns an error.
        """
        check_type(headers, dict)
        check_type(limit, (int, str))
        check_type(offset, (int, str))
        check_type(sort, (str, list, set, tuple))
        check_type(sort_order, str)
        check_type(type, (str, list, set, tuple))
        check_type(name, (str, list, set, tuple))
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'limit':
                limit,
            'offset':
                offset,
            'sort':
                sort,
            'sortOrder':
                sort_order,
            'type':
                type,
            'name':
                name,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/onboarding/pnp-workflow')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_df400c60659589599f2a0e3e1171985_v2_3_7_6', json_data)

    def add_a_workflow(self,
                       _id=None,
                       addToInventory=None,
                       addedOn=None,
                       configId=None,
                       currTaskIdx=None,
                       description=None,
                       endTime=None,
                       execTime=None,
                       imageId=None,
                       instanceType=None,
                       lastupdateOn=None,
                       name=None,
                       startTime=None,
                       state=None,
                       tasks=None,
                       tenantId=None,
                       type=None,
                       useState=None,
                       version=None,
                       headers=None,
                       payload=None,
                       active_validation=True,
                       **request_parameters):
        """Adds a PnP Workflow along with the relevant tasks in the workflow into the PnP database .

        Args:
            _id(string): Device Onboarding (PnP)'s _id.
            addToInventory(boolean): Device Onboarding (PnP)'s addToInventory.
            addedOn(integer): Device Onboarding (PnP)'s addedOn.
            configId(string): Device Onboarding (PnP)'s configId.
            currTaskIdx(integer): Device Onboarding (PnP)'s currTaskIdx.
            description(string): Device Onboarding (PnP)'s description.
            endTime(integer): Device Onboarding (PnP)'s endTime.
            execTime(integer): Device Onboarding (PnP)'s execTime.
            imageId(string): Device Onboarding (PnP)'s imageId.
            instanceType(string): Device Onboarding (PnP)'s instanceType. Available values are 'SystemWorkflow',
                'UserWorkflow' and 'SystemResetWorkflow'.
            lastupdateOn(integer): Device Onboarding (PnP)'s lastupdateOn.
            name(string): Device Onboarding (PnP)'s name.
            startTime(integer): Device Onboarding (PnP)'s startTime.
            state(string): Device Onboarding (PnP)'s state.
            tasks(list): Device Onboarding (PnP)'s tasks (list of objects).
            tenantId(string): Device Onboarding (PnP)'s tenantId.
            type(string): Device Onboarding (PnP)'s type.
            useState(string): Device Onboarding (PnP)'s useState.
            version(integer): Device Onboarding (PnP)'s version.
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
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }
        _payload = {
            '_id':
                _id,
            'addToInventory':
                addToInventory,
            'addedOn':
                addedOn,
            'configId':
                configId,
            'currTaskIdx':
                currTaskIdx,
            'description':
                description,
            'endTime':
                endTime,
            'execTime':
                execTime,
            'imageId':
                imageId,
            'instanceType':
                instanceType,
            'lastupdateOn':
                lastupdateOn,
            'name':
                name,
            'startTime':
                startTime,
            'state':
                state,
            'tasks':
                tasks,
            'tenantId':
                tenantId,
            'type':
                type,
            'useState':
                useState,
            'version':
                version,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_d967a378b43457ad8c6a6de7bc1845d1_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/onboarding/pnp-workflow')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_d967a378b43457ad8c6a6de7bc1845d1_v2_3_7_6', json_data)

    def get_workflow_count(self,
                           name=None,
                           headers=None,
                           **request_parameters):
        """Returns the workflow count .

        Args:
            name(str, list, set, tuple): name query parameter. Workflow Name .
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
        """
        check_type(headers, dict)
        check_type(name, (str, list, set, tuple))
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'name':
                name,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/onboarding/pnp-workflow/count')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_da8a788940fe59519facc6327e988922_v2_3_7_6', json_data)

    def get_workflow_by_id(self,
                           id,
                           headers=None,
                           **request_parameters):
        """Returns a workflow specified by id .

        Args:
            id(str): id path parameter.
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
        """
        check_type(headers, dict)
        check_type(id, str,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'id': id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/onboarding/pnp-workflow/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_a2b8f2239f5ef5b2e749f1b85d6508_v2_3_7_6', json_data)

    def delete_workflow_by_id(self,
                              id,
                              headers=None,
                              **request_parameters):
        """Deletes a workflow specified by id .

        Args:
            id(str): id path parameter.
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
        """
        check_type(headers, dict)
        check_type(id, str,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'id': id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/onboarding/pnp-workflow/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(endpoint_full_url, params=_params,
                                             headers=_headers)
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_ccaae97d6564e9a29fa5170ccd2a3_v2_3_7_6', json_data)

    def update_workflow(self,
                        id,
                        _id=None,
                        addToInventory=None,
                        addedOn=None,
                        configId=None,
                        currTaskIdx=None,
                        description=None,
                        endTime=None,
                        execTime=None,
                        imageId=None,
                        instanceType=None,
                        lastupdateOn=None,
                        name=None,
                        startTime=None,
                        state=None,
                        tasks=None,
                        tenantId=None,
                        type=None,
                        useState=None,
                        version=None,
                        headers=None,
                        payload=None,
                        active_validation=True,
                        **request_parameters):
        """Updates an existing workflow .

        Args:
            _id(string): Device Onboarding (PnP)'s _id.
            addToInventory(boolean): Device Onboarding (PnP)'s addToInventory.
            addedOn(integer): Device Onboarding (PnP)'s addedOn.
            configId(string): Device Onboarding (PnP)'s configId.
            currTaskIdx(integer): Device Onboarding (PnP)'s currTaskIdx.
            description(string): Device Onboarding (PnP)'s description.
            endTime(integer): Device Onboarding (PnP)'s endTime.
            execTime(integer): Device Onboarding (PnP)'s execTime.
            imageId(string): Device Onboarding (PnP)'s imageId.
            instanceType(string): Device Onboarding (PnP)'s instanceType. Available values are 'SystemWorkflow',
                'UserWorkflow' and 'SystemResetWorkflow'.
            lastupdateOn(integer): Device Onboarding (PnP)'s lastupdateOn.
            name(string): Device Onboarding (PnP)'s name.
            startTime(integer): Device Onboarding (PnP)'s startTime.
            state(string): Device Onboarding (PnP)'s state.
            tasks(list): Device Onboarding (PnP)'s tasks (list of objects).
            tenantId(string): Device Onboarding (PnP)'s tenantId.
            type(string): Device Onboarding (PnP)'s type.
            useState(string): Device Onboarding (PnP)'s useState.
            version(integer): Device Onboarding (PnP)'s version.
            id(str): id path parameter.
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
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(id, str,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'id': id,
        }
        _payload = {
            '_id':
                _id,
            'addToInventory':
                addToInventory,
            'addedOn':
                addedOn,
            'configId':
                configId,
            'currTaskIdx':
                currTaskIdx,
            'description':
                description,
            'endTime':
                endTime,
            'execTime':
                execTime,
            'imageId':
                imageId,
            'instanceType':
                instanceType,
            'lastupdateOn':
                lastupdateOn,
            'name':
                name,
            'startTime':
                startTime,
            'state':
                state,
            'tasks':
                tasks,
            'tenantId':
                tenantId,
            'type':
                type,
            'useState':
                useState,
            'version':
                version,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_fdd2af215b9b8327a3e24a3dea89_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/onboarding/pnp-workflow/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload,
                                          headers=_headers)
        else:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload)

        return self._object_factory('bpm_fdd2af215b9b8327a3e24a3dea89_v2_3_7_6', json_data)

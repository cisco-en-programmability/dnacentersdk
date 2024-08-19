# -*- coding: utf-8 -*-
"""Cisco DNA Center Licenses API wrapper.

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


class Licenses(object):
    """Cisco DNA Center Licenses API (version: 2.2.2.3).

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

    def device_count_details(self,
                             device_type=None,
                             dna_level=None,
                             registration_status=None,
                             smart_account_id=None,
                             virtual_account_name=None,
                             headers=None,
                             **request_parameters):
        """Get total number of managed device(s). .

        Args:
            device_type(str): device_type query parameter. Type of device .
            registration_status(str): registration_status query parameter. Smart license registration status
                of device .
            dna_level(str): dna_level query parameter. Device Cisco DNA license level .
            virtual_account_name(str): virtual_account_name query parameter. Name of virtual account .
            smart_account_id(str): smart_account_id query parameter. Id of smart account .
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
        check_type(device_type, str)
        check_type(registration_status, str)
        check_type(dna_level, str)
        check_type(virtual_account_name, str)
        check_type(smart_account_id, str)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'device_type':
                device_type,
            'registration_status':
                registration_status,
            'dna_level':
                dna_level,
            'virtual_account_name':
                virtual_account_name,
            'smart_account_id':
                smart_account_id,
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

        e_url = ('/dna/intent/api/v1/licenses/device/count')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_c0cf04bdc758b29bb11abbdacbd921_v2_2_2_3', json_data)

    def device_license_summary(self,
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
                               **request_parameters):
        """Show license summary of device(s). .

        Args:
            page_number(int): page_number query parameter. Page number of response .
            order(str): order query parameter. Sorting order .
            sort_by(str): sort_by query parameter. Sort result by field .
            dna_level(str): dna_level query parameter. Device Cisco DNA license level .
            device_type(str): device_type query parameter. Type of device .
            limit(int,str): limit query parameter.
            registration_status(str): registration_status query parameter. Smart license registration status
                of device .
            virtual_account_name(str): virtual_account_name query parameter. Name of virtual account .
            smart_account_id(int): smart_account_id query parameter. Id of smart account .
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
        """
        check_type(headers, dict)
        check_type(page_number, int,
                   may_be_none=False)
        check_type(order, str,
                   may_be_none=False)
        check_type(sort_by, str)
        check_type(dna_level, str)
        check_type(device_type, str)
        check_type(limit, int,
                   may_be_none=False)
        check_type(registration_status, str)
        check_type(virtual_account_name, str)
        check_type(smart_account_id, int)
        check_type(device_uuid, str)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'page_number':
                page_number,
            'order':
                order,
            'sort_by':
                sort_by,
            'dna_level':
                dna_level,
            'device_type':
                device_type,
            'limit':
                limit,
            'registration_status':
                registration_status,
            'virtual_account_name':
                virtual_account_name,
            'smart_account_id':
                smart_account_id,
            'device_uuid':
                device_uuid,
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

        e_url = ('/dna/intent/api/v1/licenses/device/summary')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_f4ba64eef4085d518a612835e128fe3c_v2_2_2_3', json_data)

    def device_license_details(self,
                               device_uuid,
                               headers=None,
                               **request_parameters):
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
        """
        check_type(headers, dict)
        check_type(device_uuid, str,
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
            'device_uuid': device_uuid,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/licenses/device/{device_uuid}/details')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_f04f865c01d5c17a5f0cb5abe620dd8_v2_2_2_3', json_data)

    def device_deregistration(self,
                              device_uuids=None,
                              headers=None,
                              payload=None,
                              active_validation=True,
                              **request_parameters):
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
            'device_uuids':
                device_uuids,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_b2f15d0c54c2862a60a904289ddd_v2_2_2_3')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/licenses/smartAccount/virtualAccount/'
                 + 'deregister')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload,
                                          headers=_headers)
        else:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload)

        return self._object_factory('bpm_b2f15d0c54c2862a60a904289ddd_v2_2_2_3', json_data)

    def device_registration(self,
                            virtual_account_name,
                            device_uuids=None,
                            headers=None,
                            payload=None,
                            active_validation=True,
                            **request_parameters):
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
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(virtual_account_name, str,
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
            'virtual_account_name': virtual_account_name,
        }
        _payload = {
            'device_uuids':
                device_uuids,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_df26f516755a50b5b5477324cf5cb649_v2_2_2_3')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/licenses/smartAccount/virtualAccount/'
                 + '{virtual_account_name}/register')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload,
                                          headers=_headers)
        else:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload)

        return self._object_factory('bpm_df26f516755a50b5b5477324cf5cb649_v2_2_2_3', json_data)

    def change_virtual_account(self,
                               smart_account_id,
                               virtual_account_name,
                               device_uuids=None,
                               headers=None,
                               payload=None,
                               active_validation=True,
                               **request_parameters):
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
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(smart_account_id, str,
                   may_be_none=False)
        check_type(virtual_account_name, str,
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
            'smart_account_id': smart_account_id,
            'virtual_account_name': virtual_account_name,
        }
        _payload = {
            'device_uuids':
                device_uuids,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_bd5b507f58a50aab614e3d7409eec4c_v2_2_2_3')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/licenses/smartAccount/{smart_account_'
                 + 'id}/virtualAccount/{virtual_account_name}/device/transfe'
                 + 'r')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_bd5b507f58a50aab614e3d7409eec4c_v2_2_2_3', json_data)

    def virtual_account_details(self,
                                smart_account_id,
                                headers=None,
                                **request_parameters):
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
        """
        check_type(headers, dict)
        check_type(smart_account_id, str,
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
            'smart_account_id': smart_account_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/licenses/smartAccount/{smart_account_'
                 + 'id}/virtualAccounts')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_ab450b197375fa9bcd95219113a3075_v2_2_2_3', json_data)

    def smart_account_details(self,
                              headers=None,
                              **request_parameters):
        """Get detail of all smart accounts. .

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

        e_url = ('/dna/intent/api/v1/licenses/smartAccounts')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_ea3fdbde23325051a76b9d062c2962a0_v2_2_2_3', json_data)

    def license_term_details(self,
                             device_type,
                             smart_account_id,
                             virtual_account_name,
                             headers=None,
                             **request_parameters):
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
        """
        check_type(headers, dict)
        check_type(device_type, str,
                   may_be_none=False)
        check_type(smart_account_id, str,
                   may_be_none=False)
        check_type(virtual_account_name, str,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'device_type':
                device_type,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'smart_account_id': smart_account_id,
            'virtual_account_name': virtual_account_name,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/licenses/term/smartAccount/{smart_acc'
                 + 'ount_id}/virtualAccount/{virtual_account_name}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_df2d278e89b45c8ea0ca0a945c001f08_v2_2_2_3', json_data)

    def license_usage_details(self,
                              device_type,
                              smart_account_id,
                              virtual_account_name,
                              headers=None,
                              **request_parameters):
        """Get count of purchased and in use DNA and Network licenses. .

        Args:
            smart_account_id(str): smart_account_id path parameter. Id of smart account .
            virtual_account_name(str): virtual_account_name path parameter. Name of virtual account. Putting
                "All" will give license usage detail for all virtual accounts. .
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
        """
        check_type(headers, dict)
        check_type(device_type, str,
                   may_be_none=False)
        check_type(smart_account_id, str,
                   may_be_none=False)
        check_type(virtual_account_name, str,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'device_type':
                device_type,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'smart_account_id': smart_account_id,
            'virtual_account_name': virtual_account_name,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/licenses/usage/smartAccount/{smart_ac'
                 + 'count_id}/virtualAccount/{virtual_account_name}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_e55ecbbda454c6a01d905e6f4cce16_v2_2_2_3', json_data)

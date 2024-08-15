# -*- coding: utf-8 -*-
"""Cisco DNA Center Compliance API wrapper.

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


class Compliance(object):
    """Cisco DNA Center Compliance API (version: 2.2.3.3).

    Wraps the DNA Center Compliance
    API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new Compliance
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the DNA Center service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(Compliance, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def get_compliance_status_(self,
                               compliance_status=None,
                               device_uuid=None,
                               limit=None,
                               offset=None,
                               headers=None,
                               **request_parameters):
        """Return compliance status of device(s). .

        Args:
            compliance_status(str): complianceStatus query parameter. Compliance status can be have value
                among 'COMPLIANT','NON_COMPLIANT','IN_PROGRESS', 'ERROR' .
            device_uuid(str): deviceUuid query parameter. Comma separated deviceUuids .
            offset(int,str): offset query parameter. offset/starting row .
            limit(int,str): limit query parameter. Number of records to be retrieved .
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
        return self.get_compliance_status(compliance_status=compliance_status,
                                          device_uuid=device_uuid,
                                          limit=limit,
                                          offset=offset,
                                          headers=headers,
                                          **request_parameters)

    def get_compliance_status(self,
                              compliance_status=None,
                              device_uuid=None,
                              limit=None,
                              offset=None,
                              headers=None,
                              **request_parameters):
        """Return compliance status of device(s). .

        Args:
            compliance_status(str): complianceStatus query parameter. Compliance status can be have value
                among 'COMPLIANT','NON_COMPLIANT','IN_PROGRESS', 'ERROR' .
            device_uuid(str): deviceUuid query parameter. Comma separated deviceUuids .
            offset(int,str): offset query parameter. offset/starting row .
            limit(int,str): limit query parameter. Number of records to be retrieved .
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
        check_type(compliance_status, str)
        check_type(device_uuid, str)
        check_type(offset, (int, str))
        check_type(limit, (int, str))
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'complianceStatus':
                compliance_status,
            'deviceUuid':
                device_uuid,
            'offset':
                offset,
            'limit':
                limit,
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

        e_url = ('/dna/intent/api/v1/compliance')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_a1de7ff46fa5da09c5051c06ad07f2c_v2_2_3_3', json_data)

    def run_compliance(self,
                       categories=None,
                       deviceUuids=None,
                       triggerFull=None,
                       headers=None,
                       payload=None,
                       active_validation=True,
                       **request_parameters):
        """Run compliance check for device(s). .

        Args:
            categories(list): Compliance's categories (list of strings).
            deviceUuids(list): Compliance's deviceUuids (list of strings).
            triggerFull(boolean): Compliance's triggerFull.
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
            'triggerFull':
                triggerFull,
            'categories':
                categories,
            'deviceUuids':
                deviceUuids,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_a0a8d545698d1d59a9be90e51_v2_2_3_3')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/compliance/')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_a0a8d545698d1d59a9be90e51_v2_2_3_3', json_data)

    def get_compliance_status_count(self,
                                    compliance_status=None,
                                    headers=None,
                                    **request_parameters):
        """Return Compliance Status Count .

        Args:
            compliance_status(str): complianceStatus query parameter. Compliance status can have value among
                'COMPLIANT', 'NON_COMPLIANT', 'IN_PROGRESS', 'NOT_AVAILABLE', 'NOT_APPLICABLE', 'ERROR'
                .
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
        check_type(compliance_status, str)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'complianceStatus':
                compliance_status,
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

        e_url = ('/dna/intent/api/v1/compliance/count')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_c37ce8136584f9e2ed471fc896ef9_v2_2_3_3', json_data)

    def get_compliance_detail(self,
                              compliance_status=None,
                              compliance_type=None,
                              device_uuid=None,
                              limit=None,
                              offset=None,
                              headers=None,
                              **request_parameters):
        """Return Compliance Detail  .

        Args:
            compliance_type(str): complianceType query parameter. complianceType can have any value among
                'NETWORK_PROFILE', 'IMAGE', 'APPLICATION_VISIBILITY', 'FABRIC', 'PSIRT',
                'RUNNING_CONFIG', 'WORKFLOW' .
            compliance_status(str): complianceStatus query parameter. Compliance status can have value among
                'COMPLIANT', 'NON_COMPLIANT', 'IN_PROGRESS', 'NOT_AVAILABLE', 'NOT_APPLICABLE', 'ERROR'
                .
            device_uuid(str): deviceUuid query parameter. Comma separated deviceUuids .
            offset(str,int): offset query parameter. offset/starting row .
            limit(str,int): limit query parameter. Number of records to be retrieved .
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
        check_type(compliance_type, str)
        check_type(compliance_status, str)
        check_type(device_uuid, str)
        check_type(offset, (int, str))
        check_type(limit, (int, str))
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'complianceType':
                compliance_type,
            'complianceStatus':
                compliance_status,
            'deviceUuid':
                device_uuid,
            'offset':
                offset,
            'limit':
                limit,
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

        e_url = ('/dna/intent/api/v1/compliance/detail')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_adeaeb8157da972efb7b91e1e2cb_v2_2_3_3', json_data)

    def get_compliance_detail_count(self,
                                    compliance_status=None,
                                    compliance_type=None,
                                    headers=None,
                                    **request_parameters):
        """Return  Compliance Count Detail .

        Args:
            compliance_type(str): complianceType query parameter. complianceType can have any value among
                'NETWORK_PROFILE', 'IMAGE', 'APPLICATION_VISIBILITY', 'FABRIC', 'PSIRT',
                'RUNNING_CONFIG', 'WORKFLOW'. .
            compliance_status(str): complianceStatus query parameter. Compliance status can have value among
                'COMPLIANT', 'NON_COMPLIANT', 'IN_PROGRESS', 'NOT_AVAILABLE', 'NOT_APPLICABLE', 'ERROR'
                .
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
        check_type(compliance_type, str)
        check_type(compliance_status, str)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'complianceType':
                compliance_type,
            'complianceStatus':
                compliance_status,
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

        e_url = ('/dna/intent/api/v1/compliance/detail/count')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_d3d38fed534f5aeaa80f5a8c63694708_v2_2_3_3', json_data)

    def device_compliance_status(self,
                                 device_uuid,
                                 headers=None,
                                 **request_parameters):
        """Return compliance status of a device. .

        Args:
            device_uuid(str): deviceUuid path parameter.
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
            'deviceUuid': device_uuid,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/compliance/{deviceUuid}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_da8e5cdd435db0b1da1684be8f15b8_v2_2_3_3', json_data)

    def compliance_details_of_device(self,
                                     device_uuid,
                                     category=None,
                                     compliance_type=None,
                                     diff_list=None,
                                     key=None,
                                     value=None,
                                     headers=None,
                                     **request_parameters):
        """Return compliance detailed report for a device. .

        Args:
            device_uuid(str): deviceUuid path parameter.
            category(str): category query parameter. complianceCategory can have any value among 'INTENT',
                'RUNNING_CONFIG' .
            compliance_type(str): complianceType query parameter. complianceType can have any value among
                'NETWORK_DESIGN', 'NETWORK_PROFILE', 'FABRIC', 'POLICY', 'RUNNING_CONFIG' .
            diff_list(bool): diffList query parameter. diff list [ pass true to fetch the diff list ] .
            key(str): key query parameter. extended attribute key .
            value(str): value query parameter. extended attribute value .
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
        check_type(category, str)
        check_type(compliance_type, str)
        check_type(diff_list, bool)
        check_type(key, str)
        check_type(value, str)
        check_type(device_uuid, str,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'category':
                category,
            'complianceType':
                compliance_type,
            'diffList':
                diff_list,
            'key':
                key,
            'value':
                value,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'deviceUuid': device_uuid,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/compliance/{deviceUuid}/detail')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_b70e1b6a2f51a59690669a4b2fd3f0_v2_2_3_3', json_data)

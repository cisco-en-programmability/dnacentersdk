# -*- coding: utf-8 -*-
"""Cisco Catalyst Center ITSM Integration API wrapper.

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


class ItsmIntegration(object):
    """Cisco Catalyst Center ITSM Integration API (version: 2.3.7.9).

    Wraps the Catalyst Center ITSM Integration
    API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new ItsmIntegration
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Catalyst Center service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(ItsmIntegration, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def create_itsm_integration_setting_v1(self,
                                           data=None,
                                           description=None,
                                           dypName=None,
                                           name=None,
                                           headers=None,
                                           payload=None,
                                           active_validation=True,
                                           **request_parameters):
        """Creates ITSM Integration setting .

        Args:
            data(object): ITSM Integration's data.
            description(string): ITSM Integration's Description of the setting instance .
            dypName(string): ITSM Integration's It can be ServiceNowConnection .
            name(string): ITSM Integration's Name of the setting instance .
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
            https://developer.cisco.com/docs/dna-center/#!create-i-t-s-m-integration-setting
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
            'name':
                name,
            'description':
                description,
            'data':
                data,
            'dypName':
                dypName,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_bb01b6bd31b53bfb12bbe327320392e_v2_3_7_9')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/integration-settings/instances/itsm')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_bb01b6bd31b53bfb12bbe327320392e_v2_3_7_9', json_data)

    def update_itsm_integration_setting_v1(self,
                                           instance_id,
                                           data=None,
                                           description=None,
                                           dypName=None,
                                           name=None,
                                           headers=None,
                                           payload=None,
                                           active_validation=True,
                                           **request_parameters):
        """Updates the ITSM Integration setting .

        Args:
            data(object): ITSM Integration's data.
            description(string): ITSM Integration's Description of the setting instance .
            dypName(string): ITSM Integration's It can be ServiceNowConnection .
            name(string): ITSM Integration's Name of the setting instance .
            instance_id(str): instanceId path parameter. Instance Id of the Integration setting instance .
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
            https://developer.cisco.com/docs/dna-center/#!update-i-t-s-m-integration-setting
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(instance_id, str,
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
            'instanceId': instance_id,
        }
        _payload = {
            'name':
                name,
            'description':
                description,
            'data':
                data,
            'dypName':
                dypName,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_c9b5b83e67195b649077a05e42897cc4_v2_3_7_9')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/integration-'
                 + 'settings/instances/itsm/{instanceId}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload,
                                          headers=_headers)
        else:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload)

        return self._object_factory('bpm_c9b5b83e67195b649077a05e42897cc4_v2_3_7_9', json_data)

    def get_itsm_integration_setting_by_id_v1(self,
                                              instance_id,
                                              headers=None,
                                              **request_parameters):
        """Fetches ITSM Integration setting by ID .

        Args:
            instance_id(str): instanceId path parameter. Instance Id of the Integration setting instance .
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
            https://developer.cisco.com/docs/dna-center/#!get-i-t-s-m-integration-setting-by-id
        """
        check_type(headers, dict)
        check_type(instance_id, str,
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
            'instanceId': instance_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/integration-'
                 + 'settings/instances/itsm/{instanceId}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_ca7a97d4665bca9634b6fb41cd7d29_v2_3_7_9', json_data)

    def delete_itsm_integration_setting_v1(self,
                                           instance_id,
                                           headers=None,
                                           **request_parameters):
        """Deletes the ITSM Integration setting .

        Args:
            instance_id(str): instanceId path parameter. Instance Id of the Integration setting instance .
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
            https://developer.cisco.com/docs/dna-center/#!delete-i-t-s-m-integration-setting
        """
        check_type(headers, dict)
        check_type(instance_id, str,
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
            'instanceId': instance_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/integration-'
                 + 'settings/instances/itsm/{instanceId}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(endpoint_full_url, params=_params,
                                             headers=_headers)
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_ae71ae83f7f530c81e650c1455567e8_v2_3_7_9', json_data)

    def get_all_itsm_integration_settings_v1(self,
                                             order=None,
                                             page=None,
                                             page_size=None,
                                             sort_by=None,
                                             headers=None,
                                             **request_parameters):
        """Fetches all ITSM Integration settings .

        Args:
            page_size(int): page_size query parameter. Specifies the number of records to display per page. .
            page(int): page query parameter. Indicates the current page number to display. .
            sort_by(str): sortBy query parameter. The field name used to sort the records. .
            order(str): order query parameter. Specify the sorting order asc for ascending or desc for
                descending .
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
            https://developer.cisco.com/docs/dna-center/#!get-all-i-t-s-m-integration-settings
        """
        check_type(headers, dict)
        check_type(page_size, int)
        check_type(page, int)
        check_type(sort_by, str)
        check_type(order, str)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'page_size':
                page_size,
            'page':
                page,
            'sortBy':
                sort_by,
            'order':
                order,
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

        e_url = ('/dna/intent/api/v1/integration-settings/itsm/instances')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_ac54638bea4157f2bbd03f329ac25e27_v2_3_7_9', json_data)

    def get_itsm_integration_status_v1(self,
                                       headers=None,
                                       **request_parameters):
        """Fetches ITSM Integration status .

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
            https://developer.cisco.com/docs/dna-center/#!get-i-t-s-m-integration-status
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

        e_url = ('/dna/intent/api/v1/integration-settings/status')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_e8398520e0aa5a549ddb60c11581b93d_v2_3_7_9', json_data)



    # Alias Function
    def create_itsm_integration_setting(self,
                                           data=None,
                                           description=None,
                                           dypName=None,
                                           name=None,
                                           headers=None,
                                           payload=None,
                                           active_validation=True,
                                           **request_parameters):
        """ This function is an alias of create_itsm_integration_setting_v1 .
        Args:
            data(object): ITSM Integration's data.
            description(string): ITSM Integration's Description of the setting instance .
            dypName(string): ITSM Integration's It can be ServiceNowConnection .
            name(string): ITSM Integration's Name of the setting instance .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of create_itsm_integration_setting_v1 .
        """
        return self.create_itsm_integration_setting_v1(
                    data=data,
                    description=description,
                    dypName=dypName,
                    name=name,
                    headers=headers,
                    payload=payload,
                    active_validation=active_validation,
                    **request_parameters
        )


    # Alias Function
    def get_all_itsm_integration_settings(self,
                                             order=None,
                                             page=None,
                                             page_size=None,
                                             sort_by=None,
                                             headers=None,
                                             **request_parameters):
        """ This function is an alias of get_all_itsm_integration_settings_v1 .
        Args:
            page_size(int): page_size query parameter. Specifies the number of records to display per page. .
            page(int): page query parameter. Indicates the current page number to display. .
            sort_by(str): sortBy query parameter. The field name used to sort the records. .
            order(str): order query parameter. Specify the sorting order asc for ascending or desc for
                descending .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_all_itsm_integration_settings_v1 .
        """
        return self.get_all_itsm_integration_settings_v1(
                    order=order,
                    page=page,
                    page_size=page_size,
                    sort_by=sort_by,
                    headers=headers,
                    **request_parameters
        )


    # Alias Function
    def get_itsm_integration_status(self,
                                       headers=None,
                                       **request_parameters):
        """ This function is an alias of get_itsm_integration_status_v1 .
        Args:
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_itsm_integration_status_v1 .
        """
        return self.get_itsm_integration_status_v1(
                    headers=headers,
                    **request_parameters
        )


    # Alias Function
    def update_itsm_integration_setting(self,
                                           instance_id,
                                           data=None,
                                           description=None,
                                           dypName=None,
                                           name=None,
                                           headers=None,
                                           payload=None,
                                           active_validation=True,
                                           **request_parameters):
        """ This function is an alias of update_itsm_integration_setting_v1 .
        Args:
            data(object): ITSM Integration's data.
            description(string): ITSM Integration's Description of the setting instance .
            dypName(string): ITSM Integration's It can be ServiceNowConnection .
            name(string): ITSM Integration's Name of the setting instance .
            instance_id(str): instanceId path parameter. Instance Id of the Integration setting instance .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of update_itsm_integration_setting_v1 .
        """
        return self.update_itsm_integration_setting_v1(
                    instance_id=instance_id,
                    data=data,
                    description=description,
                    dypName=dypName,
                    name=name,
                    headers=headers,
                    payload=payload,
                    active_validation=active_validation,
                    **request_parameters
        )


    # Alias Function
    def get_itsm_integration_setting_by_id(self,
                                              instance_id,
                                              headers=None,
                                              **request_parameters):
        """ This function is an alias of get_itsm_integration_setting_by_id_v1 .
        Args:
            instance_id(str): instanceId path parameter. Instance Id of the Integration setting instance .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_itsm_integration_setting_by_id_v1 .
        """
        return self.get_itsm_integration_setting_by_id_v1(
                    instance_id=instance_id,
                    headers=headers,
                    **request_parameters
        )


    # Alias Function
    def delete_itsm_integration_setting(self,
                                           instance_id,
                                           headers=None,
                                           **request_parameters):
        """ This function is an alias of delete_itsm_integration_setting_v1 .
        Args:
            instance_id(str): instanceId path parameter. Instance Id of the Integration setting instance .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of delete_itsm_integration_setting_v1 .
        """
        return self.delete_itsm_integration_setting_v1(
                    instance_id=instance_id,
                    headers=headers,
                    **request_parameters
        )



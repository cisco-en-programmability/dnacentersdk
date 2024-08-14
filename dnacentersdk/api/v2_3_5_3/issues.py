# -*- coding: utf-8 -*-
"""Cisco DNA Center Issues API wrapper.

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


class Issues(object):
    """Cisco DNA Center Issues API (version: 2.3.5.3).

    Wraps the DNA Center Issues
    API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new Issues
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the DNA Center service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(Issues, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def execute_suggested_actions_commands(self,
                                           entity_type=None,
                                           entity_value=None,
                                           headers=None,
                                           payload=None,
                                           active_validation=True,
                                           **request_parameters):
        """This API triggers the execution of the suggested actions for an issue, given the Issue Id. It will return an
        execution Id. At the completion of the execution, the output of the commands associated with the
        suggested actions will be provided Invoking this API would provide the execution id. Execute the 'Get
        Business API Execution Details' API with this execution id, to receive the suggested actions commands
        output. .

        Args:
            entity_type(string): Issues's Commands provided as part of the suggested actions for an issue can be
                executed based on issue id. The value here must be issue_id .
            entity_value(string): Issues's Contains the actual value for the entity type that has been defined .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(dict): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
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
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!execute-suggested-actions-commands
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
            'entity_type':
                entity_type,
            'entity_value':
                entity_value,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_bc55e6552fac58cc0aaacd773a_v2_3_5_3')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/execute-suggested-actions-commands')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_bc55e6552fac58cc0aaacd773a_v2_3_5_3', json_data)

    def get_issue_enrichment_details(self,
                                     headers=None,
                                     **request_parameters):
        """Enriches a given network issue context (an issue id or end user’s Mac Address) with details about the issue(s),
        impacted hosts and suggested actions for remediation .

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
            https://developer.cisco.com/docs/dna-center/#!get-issue-enrichment-details
        """
        check_type(headers, dict)
        if headers is not None:
            if 'entity_type' in headers:
                check_type(headers.get('entity_type'),
                           str, may_be_none=False)
            if 'entity_value' in headers:
                check_type(headers.get('entity_value'),
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

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/issue-enrichment-details')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_f2f039811951c0af53e3381ae91225_v2_3_5_3', json_data)

    def issues(self,
               ai_driven=None,
               device_id=None,
               end_time=None,
               issue_status=None,
               mac_address=None,
               priority=None,
               site_id=None,
               start_time=None,
               headers=None,
               **request_parameters):
        """Intent API to get a list of global issues, issues for a specific device, or issue for a specific client device's
        MAC address. .

        Args:
            start_time(int): startTime query parameter. Starting epoch time in milliseconds of query time window .
            end_time(int): endTime query parameter. Ending epoch time in milliseconds of query time window .
            site_id(str): siteId query parameter. Assurance UUID value of the site in the issue content .
            device_id(str): deviceId query parameter. Assurance UUID value of the device in the issue content
                .
            mac_address(str): macAddress query parameter. Client's device MAC address of the issue (format
                xx:xx:xx:xx:xx:xx) .
            priority(str): priority query parameter. The issue's priority value (One of P1, P2, P3, or
                P4)(Use only when macAddress and deviceId are not provided) .
            ai_driven(str): aiDriven query parameter. The issue's AI driven value (Yes or No)(Use only when
                macAddress and deviceId are not provided) .
            issue_status(str): issueStatus query parameter. The issue's status value (One of ACTIVE, IGNORED,
                RESOLVED) .
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
            https://developer.cisco.com/docs/dna-center/#!issues
        """
        check_type(headers, dict)
        check_type(start_time, int)
        check_type(end_time, int)
        check_type(site_id, str)
        check_type(device_id, str)
        check_type(mac_address, str)
        check_type(priority, str)
        check_type(ai_driven, str)
        check_type(issue_status, str)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'startTime':
                start_time,
            'endTime':
                end_time,
            'siteId':
                site_id,
            'deviceId':
                device_id,
            'macAddress':
                mac_address,
            'priority':
                priority,
            'aiDriven':
                ai_driven,
            'issueStatus':
                issue_status,
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

        e_url = ('/dna/intent/api/v1/issues')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_aaef3b519ba8b9fb2cbf43b985_v2_3_5_3', json_data)

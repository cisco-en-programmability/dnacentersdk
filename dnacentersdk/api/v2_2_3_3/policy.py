# -*- coding: utf-8 -*-
"""Cisco DNA Center Policy API wrapper.

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


class Policy(object):
    """Cisco DNA Center Policy API (version: 2.2.3.3).

    Wraps the DNA Center Policy
    API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new Policy
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the DNA Center service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(Policy, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def create_a_profiling_rule(self,
                                clusterId=None,
                                conditionGroups=None,
                                isDeleted=None,
                                lastModifiedBy=None,
                                lastModifiedOn=None,
                                pluginId=None,
                                rejected=None,
                                result=None,
                                ruleId=None,
                                ruleName=None,
                                rulePriority=None,
                                ruleType=None,
                                ruleVersion=None,
                                sourcePriority=None,
                                usedAttributes=None,
                                headers=None,
                                payload=None,
                                active_validation=True,
                                **request_parameters):
        """Creates profiling rule from the request body. .

        Args:
            clusterId(string): Policy's Unique identifier for ML cluster. Only applicable for 'ML Rule'. .
            conditionGroups(object): Policy's conditionGroups.
            isDeleted(boolean): Policy's Flag to indicate whether the rule was deleted. .
            lastModifiedBy(string): Policy's User that last modified the rule. It is read-only, and is ignored if
                provided as part of input request. .
            lastModifiedOn(integer): Policy's Timestamp (in epoch milliseconds) of last modification. It is read-
                only, and is ignored if provided as part of input request. .
            pluginId(string): Policy's Plugin for the rule. Only applicable for 'Cisco Default' rules. .
            rejected(boolean): Policy's Flag to indicate whether rule has been rejected by user or not. Only
                applicable for 'ML Rule'. .
            result(object): Policy's result.
            ruleId(string): Policy's Unique identifier for the rule. This is normally generated by the system, and
                client does not need to provide it for rules that need to be newly created. .
            ruleName(string): Policy's Human readable name for the rule. .
            rulePriority(integer): Policy's Priority for the rule. .
            ruleType(string): Policy's Type of the rule. Allowed values are 'Cisco Default Static', 'Cisco Default
                Dynamic', 'Custom Rule', 'ML Rule'. .
            ruleVersion(integer): Policy's Version of the rule. .
            sourcePriority(integer): Policy's Source priority for the rule. .
            usedAttributes(list): Policy's List of attributes used in the rule. Only applicable for 'Cisco Default'
                rules.  (list of strings).
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
            'ruleId':
                ruleId,
            'ruleName':
                ruleName,
            'ruleType':
                ruleType,
            'ruleVersion':
                ruleVersion,
            'rulePriority':
                rulePriority,
            'sourcePriority':
                sourcePriority,
            'isDeleted':
                isDeleted,
            'lastModifiedBy':
                lastModifiedBy,
            'lastModifiedOn':
                lastModifiedOn,
            'pluginId':
                pluginId,
            'clusterId':
                clusterId,
            'rejected':
                rejected,
            'result':
                result,
            'conditionGroups':
                conditionGroups,
            'usedAttributes':
                usedAttributes,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_bf80823752baba63a8849fd521cd_v2_2_3_3')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/endpoint-analytics/profiling-rules')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_bf80823752baba63a8849fd521cd_v2_2_3_3', json_data)

    def get_list_of_profiling_rules(self,
                                    include_deleted=None,
                                    limit=None,
                                    offset=None,
                                    order=None,
                                    rule_type=None,
                                    sort_by=None,
                                    headers=None,
                                    **request_parameters):
        """This API fetches the list of profiling rules. It can be used to show profiling rules in client applications, or
        export those from an environment. 'POST /profiling-rules/bulk' API can be used to import such exported
        rules into another environment. If this API is used to export rules to be imported into another Cisco
        DNA Center system, then ensure that 'includeDeleted' parameter is 'true', so that deleted rules get
        synchronized correctly. Use query parameters to filter the data, as required. If no filter is provided,
        then it will include only rules of type 'Custom Rule' in the response. By default, the response is
        limited to 500 records. Use 'limit' parameter to fetch higher number of records, if required. 'GET
        /profiling-rules/count' API can be used to find out the total number of rules in the system. .

        Args:
            rule_type(str): ruleType query parameter. Use comma-separated list of rule types to filter the
                data. Defaults to 'Custom Rule'. .
            include_deleted(bool): includeDeleted query parameter. Flag to indicate whether deleted rules should be
                part of the records fetched. .
            limit(int,str): limit query parameter. Maximum number of records to be fetched. If not provided, 500 records
                will be fetched by default. To fetch all the records in the system, provide a large
                value for this parameter. .
            offset(int,str): offset query parameter. Record offset to start data fetch at. Offset starts at zero. .
            sort_by(str): sortBy query parameter. Name of the column to sort the results on. Please note that
                fetch might take more time if sorting is requested. .
            order(str): order query parameter. Order to be used for sorting. .
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
        check_type(rule_type, str)
        check_type(include_deleted, bool)
        check_type(limit, (int, str))
        check_type(offset, (int, str))
        check_type(sort_by, str)
        check_type(order, str)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'ruleType':
                rule_type,
            'includeDeleted':
                include_deleted,
            'limit':
                limit,
            'offset':
                offset,
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

        e_url = ('/dna/intent/api/v1/endpoint-analytics/profiling-rules')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_a4571194a9e05664ad348f72d7651bb0_v2_2_3_3', json_data)

    def import_profiling_rules_in_bulk(self,
                                       profilingRules=None,
                                       headers=None,
                                       payload=None,
                                       active_validation=True,
                                       **request_parameters):
        """This API imports the given list of profiling rules. For each record, 1) If 'ruleType' for a record is not
        'Custom Rule', then it is rejected. 2) If 'ruleId' is provided in the input record,   2a) Record with
        same 'ruleId' exists in the system, then it is replaced with new data.   2b) Record with same 'ruleId'
        does not exist, then it is inserted in the database. 3) If 'ruleId' is not provided in the input record,
        then new 'ruleId' is generated by the system, and record is inserted. .

        Args:
            profilingRules(list): Policy's profilingRules (list of objects).
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
            'profilingRules':
                profilingRules,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_b4155d6f885a53ad0e47b1a4_v2_2_3_3')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/endpoint-analytics/profiling-'
                 + 'rules/bulk')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_b4155d6f885a53ad0e47b1a4_v2_2_3_3', json_data)

    def get_count_of_profiling_rules(self,
                                     include_deleted=None,
                                     rule_type=None,
                                     headers=None,
                                     **request_parameters):
        """This API fetches the count of profiling rules based on the filter values provided in the query parameters. The
        filter parameters are same as that of 'GET /profiling-rules' API, excluding the pagination and sort
        parameters. .

        Args:
            rule_type(str): ruleType query parameter. Use comma-separated list of rule types to filter the
                data. Defaults to 'Custom Rule'. .
            include_deleted(bool): includeDeleted query parameter. Flag to indicate whether deleted rules should be
                part of the records fetched. .
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
        check_type(rule_type, str)
        check_type(include_deleted, bool)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'ruleType':
                rule_type,
            'includeDeleted':
                include_deleted,
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

        e_url = ('/dna/intent/api/v1/endpoint-analytics/profiling-'
                 + 'rules/count')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_ec43ed2e44c5f3ea7a904d39af66899_v2_2_3_3', json_data)

    def update_an_existing_profiling_rule(self,
                                          rule_id,
                                          clusterId=None,
                                          conditionGroups=None,
                                          isDeleted=None,
                                          lastModifiedBy=None,
                                          lastModifiedOn=None,
                                          pluginId=None,
                                          rejected=None,
                                          result=None,
                                          ruleId=None,
                                          ruleName=None,
                                          rulePriority=None,
                                          ruleType=None,
                                          ruleVersion=None,
                                          sourcePriority=None,
                                          usedAttributes=None,
                                          headers=None,
                                          payload=None,
                                          active_validation=True,
                                          **request_parameters):
        """Updates the profiling rule for the given 'ruleId'. .

        Args:
            clusterId(string): Policy's Unique identifier for ML cluster. Only applicable for 'ML Rule'. .
            conditionGroups(object): Policy's conditionGroups.
            isDeleted(boolean): Policy's Flag to indicate whether the rule was deleted. .
            lastModifiedBy(string): Policy's User that last modified the rule. It is read-only, and is ignored if
                provided as part of input request. .
            lastModifiedOn(integer): Policy's Timestamp (in epoch milliseconds) of last modification. It is read-
                only, and is ignored if provided as part of input request. .
            pluginId(string): Policy's Plugin for the rule. Only applicable for 'Cisco Default' rules. .
            rejected(boolean): Policy's Flag to indicate whether rule has been rejected by user or not. Only
                applicable for 'ML Rule'. .
            result(object): Policy's result.
            ruleId(string): Policy's Unique identifier for the rule. This is normally generated by the system, and
                client does not need to provide it for rules that need to be newly created. .
            ruleName(string): Policy's Human readable name for the rule. .
            rulePriority(integer): Policy's Priority for the rule. .
            ruleType(string): Policy's Type of the rule. Allowed values are 'Cisco Default Static', 'Cisco Default
                Dynamic', 'Custom Rule', 'ML Rule'. .
            ruleVersion(integer): Policy's Version of the rule. .
            sourcePriority(integer): Policy's Source priority for the rule. .
            usedAttributes(list): Policy's List of attributes used in the rule. Only applicable for 'Cisco Default'
                rules.  (list of strings).
            rule_id(str): ruleId path parameter. Unique rule identifier .
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
        check_type(rule_id, str,
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
            'ruleId': rule_id,
        }
        _payload = {
            'ruleId':
                ruleId,
            'ruleName':
                ruleName,
            'ruleType':
                ruleType,
            'ruleVersion':
                ruleVersion,
            'rulePriority':
                rulePriority,
            'sourcePriority':
                sourcePriority,
            'isDeleted':
                isDeleted,
            'lastModifiedBy':
                lastModifiedBy,
            'lastModifiedOn':
                lastModifiedOn,
            'pluginId':
                pluginId,
            'clusterId':
                clusterId,
            'rejected':
                rejected,
            'result':
                result,
            'conditionGroups':
                conditionGroups,
            'usedAttributes':
                usedAttributes,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_a4dab79d54829548004029a91ba1_v2_2_3_3')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/endpoint-analytics/profiling-'
                 + 'rules/{ruleId}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload,
                                          headers=_headers)
        else:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload)

        return self._object_factory('bpm_a4dab79d54829548004029a91ba1_v2_2_3_3', json_data)

    def get_details_of_a_single_profiling_rule(self,
                                               rule_id,
                                               headers=None,
                                               **request_parameters):
        """Fetches details of the profiling rule for the given 'ruleId'. .

        Args:
            rule_id(str): ruleId path parameter. Unique rule identifier .
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
        check_type(rule_id, str,
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
            'ruleId': rule_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/endpoint-analytics/profiling-'
                 + 'rules/{ruleId}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_fbea90831e6e57e79062edab0c76f8a1_v2_2_3_3', json_data)

    def delete_an_existing_profiling_rule(self,
                                          rule_id,
                                          headers=None,
                                          **request_parameters):
        """Deletes the profiling rule for the given 'ruleId'. .

        Args:
            rule_id(str): ruleId path parameter. Unique rule identifier .
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
        check_type(rule_id, str,
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
            'ruleId': rule_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/endpoint-analytics/profiling-'
                 + 'rules/{ruleId}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(endpoint_full_url, params=_params,
                                             headers=_headers)
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_a3f7b6780725e83beed53d6ce2256e4_v2_2_3_3', json_data)

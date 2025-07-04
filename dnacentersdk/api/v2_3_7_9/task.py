# -*- coding: utf-8 -*-
"""Cisco Catalyst Center Task API wrapper.

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


class Task(object):
    """Cisco Catalyst Center Task API (version: 2.3.7.9).

    Wraps the Catalyst Center Task
    API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new Task
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Catalyst Center service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(Task, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def retrieve_a_list_of_assurance_tasks(
        self,
        limit=None,
        offset=None,
        order=None,
        sort_by=None,
        status=None,
        headers=None,
        **request_parameters
    ):
        """returns all existing tasks in a paginated list default sorting of list is `startTime`, `asc` valid field to sort
        by are [`startTime`,`endTime`,`updateTime`,`status`] For detailed information about the usage of the
        API, please refer to the Open API specification document https://github.com/cisco-en-
        programmability/catalyst-center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-
        AssuranceTasks-1.0.0-resolved.yaml .

        Args:
            limit(int): limit query parameter. Maximum number of records to return .
            offset(int): offset query parameter. Specifies the starting point within all records returned by the
                API. It's one based offset. The starting value is 1. .
            sort_by(str): sortBy query parameter. A field within the response to sort by. .
            order(str): order query parameter. The sort order of the field ascending or descending. .
            status(str): status query parameter. used to get a subset of tasks by their status .
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
            https://developer.cisco.com/docs/dna-center/#!retrieve-a-list-of-assurance-tasks
        """
        check_type(headers, dict)
        check_type(limit, int)
        check_type(offset, int)
        check_type(sort_by, str)
        check_type(order, str)
        check_type(status, str)
        if headers is not None:
            if "X-CALLER-ID" in headers:
                check_type(headers.get("X-CALLER-ID"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "limit": limit,
            "offset": offset,
            "sortBy": sort_by,
            "order": order,
            "status": status,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/assuranceTasks"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory("bpm_49d65b4492fff74d2a84d710_v2_3_7_9", json_data)

    def retrieve_a_count_of_the_number_of_assurance_tasks_that_currently_exist(
        self, status=None, headers=None, **request_parameters
    ):
        """returns a count of the number of assurance tasks that are not expired For detailed information about the usage
        of the API, please refer to the Open API specification document https://github.com/cisco-en-
        programmability/catalyst-center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-
        AssuranceTasks-1.0.0-resolved.yaml .

        Args:
            status(str): status query parameter. used to get a subset of tasks by their status .
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
            https://developer.cisco.com/docs/dna-center/#!retrieve-a-count-of-the-number-of-assurance-tasks-that-currently-exist
        """
        check_type(headers, dict)
        check_type(status, str)
        if headers is not None:
            if "X-CALLER-ID" in headers:
                check_type(headers.get("X-CALLER-ID"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "status": status,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/assuranceTasks/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_cb42937f005b9980039bb76b1b04bc_v2_3_7_9", json_data
        )

    def retrieve_a_specific_assurance_task_by_id(
        self, id, headers=None, **request_parameters
    ):
        """returns a task given a specific task id For detailed information about the usage of the API, please refer to the
        Open API specification document https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-AssuranceTasks-1.0.0-resolved.yaml .

        Args:
            id(str): id path parameter. unique task id .
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
            https://developer.cisco.com/docs/dna-center/#!retrieve-a-specific-assurance-task-by-id
        """
        check_type(headers, dict)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-CALLER-ID" in headers:
                check_type(headers.get("X-CALLER-ID"), str)
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

        e_url = "/dna/data/api/v1/assuranceTasks/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_f8a9bff28df85f64bdf060731d66dc7c_v2_3_7_9", json_data
        )

    def get_activities(
        self,
        description=None,
        end_time=None,
        limit=None,
        offset=None,
        order=None,
        recurring=None,
        sort_by=None,
        start_time=None,
        status=None,
        type=None,
        headers=None,
        **request_parameters
    ):
        """Returns activity(s) based on filter criteria .

        Args:
            description(str): description query parameter. The description of the activity .
            status(str): status query parameter. The status of the activity .
            type(str): type query parameter. The type of the activity .
            recurring(bool): recurring query parameter. If the activity is recurring .
            start_time(str): startTime query parameter. This is the epoch millisecond start time from which
                activities need to be fetched .
            end_time(str): endTime query parameter. This is the epoch millisecond end time upto which activities
                need to be fetched .
            offset(int): offset query parameter. The first record to show for this page; the first record is
                numbered 1. .
            limit(int): limit query parameter. The number of records to show for this page. .
            sort_by(str): sortBy query parameter. A property within the response to sort by. .
            order(str): order query parameter. Whether ascending or descending order should be used to sort the
                response. .
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
            https://developer.cisco.com/docs/dna-center/#!get-activities
        """
        check_type(headers, dict)
        check_type(description, str)
        check_type(status, str)
        check_type(type, str)
        check_type(recurring, bool)
        check_type(start_time, str)
        check_type(end_time, str)
        check_type(offset, int)
        check_type(limit, int)
        check_type(sort_by, str)
        check_type(order, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "description": description,
            "status": status,
            "type": type,
            "recurring": recurring,
            "startTime": start_time,
            "endTime": end_time,
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

        e_url = "/dna/intent/api/v1/activities"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c6a291ea9c5d5423af5ac96894c7f8b0_v2_3_7_9", json_data
        )

    def retrieves_the_count_of_activities(
        self,
        description=None,
        end_time=None,
        recurring=None,
        start_time=None,
        status=None,
        type=None,
        headers=None,
        **request_parameters
    ):
        """Retrieves the count of activities .

        Args:
            description(str): description query parameter. The description provided when creating the activity .
            status(str): status query parameter. Status of the activity .
            type(str): type query parameter. Type of the activity .
            recurring(bool): recurring query parameter. Denotes whether an activity is recurring or not .
            start_time(str): startTime query parameter. This is the epoch millisecond start time from which
                activities need to be fetched .
            end_time(str): endTime query parameter. This is the epoch millisecond end time upto which activities
                need to be fetched .
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-the-count-of-activities
        """
        check_type(headers, dict)
        check_type(description, str)
        check_type(status, str)
        check_type(type, str)
        check_type(recurring, bool)
        check_type(start_time, str)
        check_type(end_time, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "description": description,
            "status": status,
            "type": type,
            "recurring": recurring,
            "startTime": start_time,
            "endTime": end_time,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/activities/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_eab67fb962e55baea864b1bb17fd78e3_v2_3_7_9", json_data
        )

    def get_triggered_jobs_by_activity_id(
        self,
        activity_id,
        limit=None,
        offset=None,
        order=None,
        sort_by=None,
        headers=None,
        **request_parameters
    ):
        """Returns the triggered jobs by the activity with the given activity id .

        Args:
            activity_id(str): activityId path parameter. The id of the activity .
            offset(int): offset query parameter. The first record to show for this page; the first record is
                numbered 1. .
            limit(int): limit query parameter. The number of records to show for this page. .
            sort_by(str): sortBy query parameter. A property within the response to sort by. .
            order(str): order query parameter. Whether ascending or descending order should be used to sort the
                response. .
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
            https://developer.cisco.com/docs/dna-center/#!get-triggered-jobs-by-activity-id
        """
        check_type(headers, dict)
        check_type(offset, int)
        check_type(limit, int)
        check_type(sort_by, str)
        check_type(order, str)
        check_type(activity_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "offset": offset,
            "limit": limit,
            "sortBy": sort_by,
            "order": order,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "activityId": activity_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/activities/{activityId}/triggeredJobs"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_affaf286eb455fc8869939066990765_v2_3_7_9", json_data
        )

    def retrieves_the_count_of_triggered_jobs_by_activity_id(
        self, activity_id, headers=None, **request_parameters
    ):
        """Retrieves the count of triggered jobs by activity id. .

        Args:
            activity_id(str): activityId path parameter. The id of the activity .
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-the-count-of-triggered-jobs-by-activity-id
        """
        check_type(headers, dict)
        check_type(activity_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "activityId": activity_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/activities/{activityId}/triggeredJobs" + "/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_d235a8436ddd5bb1add2c7bf04940a99_v2_3_7_9", json_data
        )

    def get_business_api_execution_details(
        self, execution_id, headers=None, **request_parameters
    ):
        """Retrieves the execution details of a Business API .

        Args:
            execution_id(str): executionId path parameter. Execution Id of API .
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
            https://developer.cisco.com/docs/dna-center/#!get-business-a-p-i-execution-details
        """
        check_type(headers, dict)
        check_type(execution_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "executionId": execution_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/dnacaap/management/execution-" + "status/{executionId}"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ffc19ddea705526b7d9db01baf4997e_v2_3_7_9", json_data
        )

    def get_tasks_operational_tasks(
        self,
        data=None,
        end_time=None,
        error_code=None,
        failure_reason=None,
        is_error=None,
        limit=None,
        offset=None,
        order=None,
        parent_id=None,
        progress=None,
        service_type=None,
        sort_by=None,
        start_time=None,
        username=None,
        headers=None,
        **request_parameters
    ):
        """Returns task(s) based on filter criteria .

        Args:
            start_time(str): startTime query parameter. This is the epoch start time from which tasks need to be
                fetched .
            end_time(str): endTime query parameter. This is the epoch end time upto which audit records need to be
                fetched .
            data(str): data query parameter. Fetch tasks that contains this data .
            error_code(str): errorCode query parameter. Fetch tasks that have this error code .
            service_type(str): serviceType query parameter. Fetch tasks with this service type .
            username(str): username query parameter. Fetch tasks with this username .
            progress(str): progress query parameter. Fetch tasks that contains this progress .
            is_error(str): isError query parameter. Fetch tasks ended as success or failure. Valid values: true,
                false .
            failure_reason(str): failureReason query parameter. Fetch tasks that contains this failure reason .
            parent_id(str): parentId query parameter. Fetch tasks that have this parent Id .
            offset(int): offset query parameter. The first record to show for this page; the first record is
                numbered 1. .
            limit(int): limit query parameter. The number of records to show for this page;The minimum is 1, and the
                maximum is 500. .
            sort_by(str): sortBy query parameter. Sort results by this field .
            order(str): order query parameter. Sort order asc or dsc .
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
            https://developer.cisco.com/docs/dna-center/#!get-tasks-operational-tasks
        """
        check_type(headers, dict)
        check_type(start_time, str)
        check_type(end_time, str)
        check_type(data, str)
        check_type(error_code, str)
        check_type(service_type, str)
        check_type(username, str)
        check_type(progress, str)
        check_type(is_error, str)
        check_type(failure_reason, str)
        check_type(parent_id, str)
        check_type(offset, int)
        check_type(limit, int)
        check_type(sort_by, str)
        check_type(order, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "startTime": start_time,
            "endTime": end_time,
            "data": data,
            "errorCode": error_code,
            "serviceType": service_type,
            "username": username,
            "progress": progress,
            "isError": is_error,
            "failureReason": failure_reason,
            "parentId": parent_id,
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

        e_url = "/dna/intent/api/v1/task"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ff485556f6504d8443789f42098be7_v2_3_7_9", json_data
        )

    def get_task_count(
        self,
        data=None,
        end_time=None,
        error_code=None,
        failure_reason=None,
        is_error=None,
        parent_id=None,
        progress=None,
        service_type=None,
        start_time=None,
        username=None,
        headers=None,
        **request_parameters
    ):
        """Returns Task count .

        Args:
            start_time(str): startTime query parameter. This is the epoch start time from which tasks need to be
                fetched .
            end_time(str): endTime query parameter. This is the epoch end time upto which audit records need to be
                fetched .
            data(str): data query parameter. Fetch tasks that contains this data .
            error_code(str): errorCode query parameter. Fetch tasks that have this error code .
            service_type(str): serviceType query parameter. Fetch tasks with this service type .
            username(str): username query parameter. Fetch tasks with this username .
            progress(str): progress query parameter. Fetch tasks that contains this progress .
            is_error(str): isError query parameter. Fetch tasks ended as success or failure. Valid values: true,
                false .
            failure_reason(str): failureReason query parameter. Fetch tasks that contains this failure reason .
            parent_id(str): parentId query parameter. Fetch tasks that have this parent Id .
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
            https://developer.cisco.com/docs/dna-center/#!get-task-count
        """
        check_type(headers, dict)
        check_type(start_time, str)
        check_type(end_time, str)
        check_type(data, str)
        check_type(error_code, str)
        check_type(service_type, str)
        check_type(username, str)
        check_type(progress, str)
        check_type(is_error, str)
        check_type(failure_reason, str)
        check_type(parent_id, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "startTime": start_time,
            "endTime": end_time,
            "data": data,
            "errorCode": error_code,
            "serviceType": service_type,
            "username": username,
            "progress": progress,
            "isError": is_error,
            "failureReason": failure_reason,
            "parentId": parent_id,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/task/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_d0586946be75e0f9f2c170217d45a28_v2_3_7_9", json_data
        )

    def get_task_by_operation_id(
        self, limit, offset, operation_id, headers=None, **request_parameters
    ):
        """Returns root tasks associated with an Operationid .

        Args:
            operation_id(str): operationId path parameter.
            offset(int): offset path parameter. Index, minimum value is 0 .
            limit(int): limit path parameter. The maximum value of {limit} supported is 500.               Base 1
                indexing for {limit}, minimum value is 1 .
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
            https://developer.cisco.com/docs/dna-center/#!get-task-by-operation-id
        """
        check_type(headers, dict)
        check_type(operation_id, str, may_be_none=False)
        check_type(offset, int, may_be_none=False)
        check_type(limit, int, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "operationId": operation_id,
            "offset": offset,
            "limit": limit,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/task/operation/{operationId}/{offset}" + "/{limit}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_d95c21e41dce5a9dbee07d33eefef2b2_v2_3_7_9", json_data
        )

    def get_task_by_id(self, task_id, headers=None, **request_parameters):
        """Returns a task by specified id .

        Args:
            task_id(str): taskId path parameter. UUID of the Task .
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
            https://developer.cisco.com/docs/dna-center/#!get-task-by-id
        """
        check_type(headers, dict)
        check_type(task_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "taskId": task_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/task/{taskId}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory("bpm_99a75ba5a6bae1d568700bd3_v2_3_7_9", json_data)

    def get_task_tree(self, task_id, headers=None, **request_parameters):
        """Returns a task with its children tasks by based on their id .

        Args:
            task_id(str): taskId path parameter. UUID of the Task .
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
            https://developer.cisco.com/docs/dna-center/#!get-task-tree
        """
        check_type(headers, dict)
        check_type(task_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "taskId": task_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/task/{taskId}/tree"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_fa2865e229b536aacd59585a1d29704_v2_3_7_9", json_data
        )

    def get_tasks(
        self,
        end_time=None,
        limit=None,
        offset=None,
        order=None,
        parent_id=None,
        root_id=None,
        sort_by=None,
        start_time=None,
        status=None,
        headers=None,
        **request_parameters
    ):
        """Returns task(s) based on filter criteria .

        Args:
            offset(int): offset query parameter. The first record to show for this page; the first record is
                numbered 1. .
            limit(int): limit query parameter. The number of records to show for this page;The minimum is 1, and the
                maximum is 500. .
            sort_by(str): sortBy query parameter. A property within the response to sort by. .
            order(str): order query parameter. Whether ascending or descending order should be used to sort the
                response. .
            start_time(int): startTime query parameter. This is the epoch millisecond start time from which tasks
                need to be fetched .
            end_time(int): endTime query parameter. This is the epoch millisecond end time upto which task records
                need to be fetched .
            parent_id(str): parentId query parameter. Fetch tasks that have this parent Id .
            root_id(str): rootId query parameter. Fetch tasks that have this root Id .
            status(str): status query parameter. Fetch tasks that have this status. Available values : PENDING,
                FAILURE, SUCCESS .
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
            https://developer.cisco.com/docs/dna-center/#!get-tasks
        """
        check_type(headers, dict)
        check_type(offset, int)
        check_type(limit, int)
        check_type(sort_by, str)
        check_type(order, str)
        check_type(start_time, int)
        check_type(end_time, int)
        check_type(parent_id, str)
        check_type(root_id, str)
        check_type(status, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "offset": offset,
            "limit": limit,
            "sortBy": sort_by,
            "order": order,
            "startTime": start_time,
            "endTime": end_time,
            "parentId": parent_id,
            "rootId": root_id,
            "status": status,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/tasks"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_b485e8aa7d9150ddb5048aa3b0617866_v2_3_7_9", json_data
        )

    def get_tasks_count(
        self,
        end_time=None,
        parent_id=None,
        root_id=None,
        start_time=None,
        status=None,
        headers=None,
        **request_parameters
    ):
        """Returns the number of tasks that meet the filter criteria .

        Args:
            start_time(int): startTime query parameter. This is the epoch millisecond start time from which tasks
                need to be fetched .
            end_time(int): endTime query parameter. This is the epoch millisecond end time upto which task records
                need to be fetched .
            parent_id(str): parentId query parameter. Fetch tasks that have this parent Id .
            root_id(str): rootId query parameter. Fetch tasks that have this root Id .
            status(str): status query parameter. Fetch tasks that have this status. Available values : PENDING,
                FAILURE, SUCCESS .
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
            https://developer.cisco.com/docs/dna-center/#!get-tasks-count
        """
        check_type(headers, dict)
        check_type(start_time, int)
        check_type(end_time, int)
        check_type(parent_id, str)
        check_type(root_id, str)
        check_type(status, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "startTime": start_time,
            "endTime": end_time,
            "parentId": parent_id,
            "rootId": root_id,
            "status": status,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/tasks/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ff937b756f5eec9f5cd519ea6e9fec_v2_3_7_9", json_data
        )

    def get_tasks_by_id(self, id, headers=None, **request_parameters):
        """Returns the task with the given ID .

        Args:
            id(str): id path parameter. the `id` of the task to retrieve .
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
            https://developer.cisco.com/docs/dna-center/#!get-tasks-by-i-d
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

        e_url = "/dna/intent/api/v1/tasks/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ffc437c17db355ae92597ce411cec6c8_v2_3_7_9", json_data
        )

    def get_task_details_by_id(self, id, headers=None, **request_parameters):
        """Returns the task details for the given task ID .

        Args:
            id(str): id path parameter. the `id` of the task to retrieve details for .
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
            https://developer.cisco.com/docs/dna-center/#!get-task-details-by-i-d
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

        e_url = "/dna/intent/api/v1/tasks/{id}/detail"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a48eee2b20065722ba9688176af178c1_v2_3_7_9", json_data
        )

    def get_activity_by_id(self, id, headers=None, **request_parameters):
        """Returns the activity with the given ID .

        Args:
            id(str): id path parameter. The id of the activity to retrieve .
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
            https://developer.cisco.com/docs/dna-center/#!get-activity-by-i-d
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

        e_url = "/intent/api/v1/activities/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c8c7108e4f52c783a2703cf19e6c8c_v2_3_7_9", json_data
        )

    # Alias Functions
    @deprecated
    def get_task_by_operationid(
        self, limit, offset, operation_id, headers=None, **request_parameters
    ):
        """alias for get_task_by_operation_id"""
        return self.get_task_by_operation_id(
            limit=limit,
            offset=offset,
            operation_id=operation_id,
            headers=headers,
            **request_parameters
        )

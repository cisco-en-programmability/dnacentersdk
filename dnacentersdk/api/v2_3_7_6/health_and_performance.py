# -*- coding: utf-8 -*-
"""Cisco DNA Center Health and Performance API wrapper.

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


class HealthAndPerformance(object):
    """Cisco DNA Center Health and Performance API (version: 2.3.7.6).

    Wraps the DNA Center Health and Performance
    API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new HealthAndPerformance
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the DNA Center service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(HealthAndPerformance, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def retrieves_all_the_validation_sets_v1(
        self, view=None, headers=None, **request_parameters
    ):
        """Retrieves all the validation sets and optionally the contained validations .

        Args:
            view(str): view query parameter. When the query parameter `view=DETAIL` is passed, all validation
                sets and associated validations will be returned. When the query parameter
                `view=DEFAULT` is passed, only validation sets metadata will be returned. .
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-all-the-validation-sets
        """
        check_type(headers, dict)
        check_type(view, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "view": view,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/diagnosticValidationSets"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_d6fc1397d48d52449923716aff009d3c_v2_3_7_6", json_data
        )

    def retrieves_validation_details_for_a_validation_set_v1(
        self, id, headers=None, **request_parameters
    ):
        """Retrieves validation details for the given validation set id .

        Args:
            id(str): id path parameter. Validation set id .
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-validation-details-for-a-validation-set
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

        e_url = "/dna/intent/api/v1/diagnosticValidationSets/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_d95307fdbf5b169d9d05e3151f61ac_v2_3_7_6", json_data
        )

    def retrieves_the_list_of_validation_workflows_v1(
        self,
        end_time=None,
        limit=None,
        offset=None,
        run_status=None,
        start_time=None,
        headers=None,
        **request_parameters
    ):
        """Retrieves the workflows that have been successfully submitted and are currently available. This is sorted by
        `submitTime` .

        Args:
            start_time(int): startTime query parameter. Workflows started after the given time (as milliseconds
                since UNIX epoch). .
            end_time(int): endTime query parameter. Workflows started before the given time (as milliseconds since
                UNIX epoch). .
            run_status(str): runStatus query parameter. Execution status of the workflow. If the workflow is
                successfully submitted, runStatus is `PENDING`. If the workflow execution has started,
                runStatus is `IN_PROGRESS`. If the workflow executed is completed with all validations
                executed, runStatus is `COMPLETED`. If the workflow execution fails while running
                validations, runStatus is `FAILED`. .
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
            ApiError: If the DNA Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!retrieves-the-list-of-validation-workflows
        """
        check_type(headers, dict)
        check_type(start_time, int)
        check_type(end_time, int)
        check_type(run_status, str)
        check_type(offset, int)
        check_type(limit, int)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "startTime": start_time,
            "endTime": end_time,
            "runStatus": run_status,
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

        e_url = "/dna/intent/api/v1/diagnosticValidationWorkflows"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a53d325f85e5549b7c5957c6ecbd891_v2_3_7_6", json_data
        )

    def submits_the_workflow_for_executing_validations_v1(
        self,
        description=None,
        name=None,
        validationSetIds=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Submits the workflow for executing the validations for the given validation specifications .

        Args:
            description(string): Health and Performance's Description of the workflow to run .
            name(string): Health and Performance's Name of the workflow to run. It must be unique. .
            validationSetIds(list): Health and Performance's List of validation set ids  (list of strings).
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
            https://developer.cisco.com/docs/dna-center/#!submits-the-workflow-for-executing-validations
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
            "name": name,
            "description": description,
            "validationSetIds": validationSetIds,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_cf9d39cef5e95bb9bd48d5f86e094c99_v2_3_7_6"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/diagnosticValidationWorkflows"
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
            "bpm_cf9d39cef5e95bb9bd48d5f86e094c99_v2_3_7_6", json_data
        )

    def retrieves_the_count_of_validation_workflows_v1(
        self,
        end_time=None,
        run_status=None,
        start_time=None,
        headers=None,
        **request_parameters
    ):
        """Retrieves the count of workflows that have been successfully submitted and are currently available.  .

        Args:
            start_time(int): startTime query parameter. Workflows started after the given time (as milliseconds
                since UNIX epoch). .
            end_time(int): endTime query parameter. Workflows started before the given time (as milliseconds since
                UNIX epoch). .
            run_status(str): runStatus query parameter. Execution status of the workflow. If the workflow is
                successfully submitted, runStatus is `PENDING`. If the workflow execution has started,
                runStatus is `IN_PROGRESS`. If the workflow executed is completed with all validations
                executed, runStatus is `COMPLETED`. If the workflow execution fails while running
                validations, runStatus is `FAILED`. .
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-the-count-of-validation-workflows
        """
        check_type(headers, dict)
        check_type(start_time, int)
        check_type(end_time, int)
        check_type(run_status, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "startTime": start_time,
            "endTime": end_time,
            "runStatus": run_status,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/diagnosticValidationWorkflows/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_b174a2fc5171520d9423c9a50f7394e7_v2_3_7_6", json_data
        )

    def deletes_a_validation_workflow_v1(self, id, headers=None, **request_parameters):
        """Deletes the workflow for the given id .

        Args:
            id(str): id path parameter. Workflow id .
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
            https://developer.cisco.com/docs/dna-center/#!deletes-a-validation-workflow
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

        e_url = "/dna/intent/api/v1/diagnosticValidationWorkflows/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_b3ab76a74dae51fabf39b2ad85c3c58f_v2_3_7_6", json_data
        )

    def retrieves_validation_workflow_details_v1(
        self, id, headers=None, **request_parameters
    ):
        """Retrieves workflow details for a workflow id .

        Args:
            id(str): id path parameter. Workflow id .
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-validation-workflow-details
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

        e_url = "/dna/intent/api/v1/diagnosticValidationWorkflows/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c36c30b8c5ddfbf9ccf36db5dd68a_v2_3_7_6", json_data
        )

    def system_health_v1(
        self,
        domain=None,
        limit=None,
        offset=None,
        subdomain=None,
        summary=None,
        headers=None,
        **request_parameters
    ):
        """This API retrieves the latest system events  .

        Args:
            summary(bool): summary query parameter. Fetch the latest high severity event .
            domain(str): domain query parameter. Fetch system events with this domain. Possible values of
                domain are listed here : /dna/platform/app/consumer-portal/developer-toolkit/events .
            subdomain(str): subdomain query parameter. Fetch system events with this subdomain. Possible
                values of subdomain are listed here : /dna/platform/app/consumer-portal/developer-
                toolkit/events .
            limit(int): limit query parameter.
            offset(int): offset query parameter.
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
            https://developer.cisco.com/docs/dna-center/#!system-health-api
        """
        check_type(headers, dict)
        check_type(summary, bool)
        check_type(domain, str)
        check_type(subdomain, str)
        check_type(limit, int)
        check_type(offset, int)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "summary": summary,
            "domain": domain,
            "subdomain": subdomain,
            "limit": limit,
            "offset": offset,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/diagnostics/system/health"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_d0acccfae6885bc28f8f39c67f4acfc1_v2_3_7_6", json_data
        )

    def system_health_count_v1(
        self, domain=None, subdomain=None, headers=None, **request_parameters
    ):
        """This API gives the count of the latest system events .

        Args:
            domain(str): domain query parameter. Fetch system events with this domain. Possible values of
                domain are listed here : /dna/platform/app/consumer-portal/developer-toolkit/events .
            subdomain(str): subdomain query parameter. Fetch system events with this subdomain. Possible
                values of subdomain are listed here : /dna/platform/app/consumer-portal/developer-
                toolkit/events .
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
            https://developer.cisco.com/docs/dna-center/#!system-health-count-api
        """
        check_type(headers, dict)
        check_type(domain, str)
        check_type(subdomain, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "domain": domain,
            "subdomain": subdomain,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/diagnostics/system/health/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_f6dd603bc35db1948f31c782a37647_v2_3_7_6", json_data
        )

    def system_performance_v1(
        self,
        end_time=None,
        function=None,
        kpi=None,
        start_time=None,
        headers=None,
        **request_parameters
    ):
        """Retrieves the aggregated metrics (total, average or maximum) of cluster key performance indicators (KPIs), such
        as CPU utilization, memory utilization or network rates recorded within a specified time period. The
        data will be available from the past 24 hours. .

        Args:
            kpi(str): kpi query parameter. Valid values: cpu,memory,network .
            function(str): function query parameter. Valid values: sum,average,max .
            start_time(int): startTime query parameter. This is the epoch start time in milliseconds from which
                performance indicator need to be fetched .
            end_time(int): endTime query parameter. This is the epoch end time in milliseconds upto which
                performance indicator need to be fetched .
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
            https://developer.cisco.com/docs/dna-center/#!system-performance-api
        """
        check_type(headers, dict)
        check_type(kpi, str)
        check_type(function, str)
        check_type(start_time, int)
        check_type(end_time, int)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "kpi": kpi,
            "function": function,
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

        e_url = "/dna/intent/api/v1/diagnostics/system/performance"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_cfcb7a875f215cb4ba59be38abb871e6_v2_3_7_6", json_data
        )

    def system_performance_historical_v1(
        self,
        end_time=None,
        kpi=None,
        start_time=None,
        headers=None,
        **request_parameters
    ):
        """Retrieves the average values of cluster key performance indicators (KPIs), like CPU utilization, memory
        utilization or network rates grouped by time intervals within a specified time range. The data will be
        available from the past 24 hours. .

        Args:
            kpi(str): kpi query parameter. Fetch historical data for this kpi. Valid values:
                cpu,memory,network .
            start_time(int): startTime query parameter. This is the epoch start time in milliseconds from which
                performance indicator need to be fetched .
            end_time(int): endTime query parameter. This is the epoch end time in milliseconds upto which
                performance indicator need to be fetched .
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
            https://developer.cisco.com/docs/dna-center/#!system-performance-historical-api
        """
        check_type(headers, dict)
        check_type(kpi, str)
        check_type(start_time, int)
        check_type(end_time, int)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "kpi": kpi,
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

        e_url = "/dna/intent/api/v1/diagnostics/system/performance/histor" + "y"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_f131d712dc253dca528c0298b3e41c6_v2_3_7_6", json_data
        )

    # Alias Function
    def system_performance(
        self,
        end_time=None,
        function=None,
        kpi=None,
        start_time=None,
        headers=None,
        **request_parameters
    ):
        """This function is an alias of system_performance_v1 .
        Args:
            kpi(basestring): kpi query parameter. Valid values: cpu,memory,network .
            function(basestring): function query parameter. Valid values: sum,average,max .
            start_time(int): startTime query parameter. This is the epoch start time in milliseconds from which
                performance indicator need to be fetched .
            end_time(int): endTime query parameter. This is the epoch end time in milliseconds upto which
                performance indicator need to be fetched .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of system_performance_v1 .
        """
        return self.system_performance_v1(
            end_time=end_time,
            function=function,
            kpi=kpi,
            start_time=start_time,
            headers=headers,
            **request_parameters
        )

    # Alias Function
    def system_performance_historical(
        self,
        end_time=None,
        kpi=None,
        start_time=None,
        headers=None,
        **request_parameters
    ):
        """This function is an alias of system_performance_historical_v1 .
        Args:
            kpi(basestring): kpi query parameter. Fetch historical data for this kpi. Valid values:
                cpu,memory,network .
            start_time(int): startTime query parameter. This is the epoch start time in milliseconds from which
                performance indicator need to be fetched .
            end_time(int): endTime query parameter. This is the epoch end time in milliseconds upto which
                performance indicator need to be fetched .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of system_performance_historical_v1 .
        """
        return self.system_performance_historical_v1(
            end_time=end_time,
            kpi=kpi,
            start_time=start_time,
            headers=headers,
            **request_parameters
        )

    # Alias Function
    def system_health(
        self,
        domain=None,
        limit=None,
        offset=None,
        subdomain=None,
        summary=None,
        headers=None,
        **request_parameters
    ):
        """This function is an alias of system_health_v1 .
        Args:
            summary(bool): summary query parameter. Fetch the latest high severity event .
            domain(basestring): domain query parameter. Fetch system events with this domain. Possible values of
                domain are listed here : /dna/platform/app/consumer-portal/developer-toolkit/events .
            subdomain(basestring): subdomain query parameter. Fetch system events with this subdomain. Possible
                values of subdomain are listed here : /dna/platform/app/consumer-portal/developer-
                toolkit/events .
            limit(int): limit query parameter.
            offset(int): offset query parameter.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of system_health_v1 .
        """
        return self.system_health_v1(
            domain=domain,
            limit=limit,
            offset=offset,
            subdomain=subdomain,
            summary=summary,
            headers=headers,
            **request_parameters
        )

    # Alias Function
    def deletes_a_validation_workflow(self, id, headers=None, **request_parameters):
        """This function is an alias of deletes_a_validation_workflow_v1 .
        Args:
            id(basestring): id path parameter. Workflow id .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of deletes_a_validation_workflow_v1 .
        """
        return self.deletes_a_validation_workflow_v1(
            id=id, headers=headers, **request_parameters
        )

    # Alias Function
    def retrieves_validation_details_for_a_validation_set(
        self, id, headers=None, **request_parameters
    ):
        """This function is an alias of retrieves_validation_details_for_a_validation_set_v1 .
        Args:
            id(basestring): id path parameter. Validation set id .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of retrieves_validation_details_for_a_validation_set_v1 .
        """
        return self.retrieves_validation_details_for_a_validation_set_v1(
            id=id, headers=headers, **request_parameters
        )

    # Alias Function
    def retrieves_the_count_of_validation_workflows(
        self,
        end_time=None,
        run_status=None,
        start_time=None,
        headers=None,
        **request_parameters
    ):
        """This function is an alias of retrieves_the_count_of_validation_workflows_v1 .
        Args:
            start_time(int): startTime query parameter. Workflows started after the given time (as milliseconds
                since UNIX epoch). .
            end_time(int): endTime query parameter. Workflows started before the given time (as milliseconds since
                UNIX epoch). .
            run_status(basestring): runStatus query parameter. Execution status of the workflow. If the workflow is
                successfully submitted, runStatus is `PENDING`. If the workflow execution has started,
                runStatus is `IN_PROGRESS`. If the workflow executed is completed with all validations
                executed, runStatus is `COMPLETED`. If the workflow execution fails while running
                validations, runStatus is `FAILED`. .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of retrieves_the_count_of_validation_workflows_v1 .
        """
        return self.retrieves_the_count_of_validation_workflows_v1(
            end_time=end_time,
            run_status=run_status,
            start_time=start_time,
            headers=headers,
            **request_parameters
        )

    # Alias Function
    def retrieves_the_list_of_validation_workflows(
        self,
        end_time=None,
        limit=None,
        offset=None,
        run_status=None,
        start_time=None,
        headers=None,
        **request_parameters
    ):
        """This function is an alias of retrieves_the_list_of_validation_workflows_v1 .
        Args:
            start_time(int): startTime query parameter. Workflows started after the given time (as milliseconds
                since UNIX epoch). .
            end_time(int): endTime query parameter. Workflows started before the given time (as milliseconds since
                UNIX epoch). .
            run_status(basestring): runStatus query parameter. Execution status of the workflow. If the workflow is
                successfully submitted, runStatus is `PENDING`. If the workflow execution has started,
                runStatus is `IN_PROGRESS`. If the workflow executed is completed with all validations
                executed, runStatus is `COMPLETED`. If the workflow execution fails while running
                validations, runStatus is `FAILED`. .
            offset(int): offset query parameter. The first record to show for this page; the first record is
                numbered 1. .
            limit(int): limit query parameter. The number of records to show for this page. .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of retrieves_the_list_of_validation_workflows_v1 .
        """
        return self.retrieves_the_list_of_validation_workflows_v1(
            end_time=end_time,
            limit=limit,
            offset=offset,
            run_status=run_status,
            start_time=start_time,
            headers=headers,
            **request_parameters
        )

    # Alias Function
    def system_health_count(
        self, domain=None, subdomain=None, headers=None, **request_parameters
    ):
        """This function is an alias of system_health_count_v1 .
        Args:
            domain(basestring): domain query parameter. Fetch system events with this domain. Possible values of
                domain are listed here : /dna/platform/app/consumer-portal/developer-toolkit/events .
            subdomain(basestring): subdomain query parameter. Fetch system events with this subdomain. Possible
                values of subdomain are listed here : /dna/platform/app/consumer-portal/developer-
                toolkit/events .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of system_health_count_v1 .
        """
        return self.system_health_count_v1(
            domain=domain, subdomain=subdomain, headers=headers, **request_parameters
        )

    # Alias Function
    def retrieves_validation_workflow_details(
        self, id, headers=None, **request_parameters
    ):
        """This function is an alias of retrieves_validation_workflow_details_v1 .
        Args:
            id(basestring): id path parameter. Workflow id .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of retrieves_validation_workflow_details_v1 .
        """
        return self.retrieves_validation_workflow_details_v1(
            id=id, headers=headers, **request_parameters
        )

    # Alias Function
    def submits_the_workflow_for_executing_validations(
        self,
        description=None,
        name=None,
        validationSetIds=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This function is an alias of submits_the_workflow_for_executing_validations_v1 .
        Args:
            description(string): Health and Performance's Description of the workflow to run .
            name(string): Health and Performance's Name of the workflow to run. It must be unique. .
            validationSetIds(list): Health and Performance's List of validation set ids  (list of strings).
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of submits_the_workflow_for_executing_validations_v1 .
        """
        return self.submits_the_workflow_for_executing_validations_v1(
            description=description,
            name=name,
            validationSetIds=validationSetIds,
            headers=headers,
            payload=payload,
            active_validation=active_validation,
            **request_parameters
        )

    # Alias Function
    def retrieves_all_the_validation_sets(
        self, view=None, headers=None, **request_parameters
    ):
        """This function is an alias of retrieves_all_the_validation_sets_v1 .
        Args:
            view(basestring): view query parameter. When the query parameter `view=DETAIL` is passed, all validation
                sets and associated validations will be returned. When the query parameter
                `view=DEFAULT` is passed, only validation sets metadata will be returned. .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of retrieves_all_the_validation_sets_v1 .
        """
        return self.retrieves_all_the_validation_sets_v1(
            view=view, headers=headers, **request_parameters
        )

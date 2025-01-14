# -*- coding: utf-8 -*-
"""Cisco Catalyst Center Reports API wrapper.

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


class Reports(object):
    """Cisco Catalyst Center Reports API (version: 2.3.7.9).

    Wraps the Catalyst Center Reports
    API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new Reports
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Catalyst Center service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(Reports, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def download_flexible_report_v1(self,
                                    execution_id,
                                    report_id,
                                    headers=None,
                                    **request_parameters):
        """This is used to download the flexible report. The API returns report content. Save the response to a file by
        converting the response data as a blob and setting the file format available from content-disposition
        response header. .

        Args:
            report_id(str): reportId path parameter. Id of the report .
            execution_id(str): executionId path parameter. Id of execution .
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!download-flexible-report
        """
        check_type(headers, dict)
        check_type(report_id, str,
                   may_be_none=False)
        check_type(execution_id, str,
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
            'reportId': report_id,
            'executionId': execution_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/data/api/v1/flexible-'
                 + 'report/report/content/{reportId}/{executionId}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_fc4acf45953f5b68be682c3c5906bf14_v2_3_7_9', json_data)

    def executing_the_flexible_report_v1(self,
                                         report_id,
                                         headers=None,
                                         **request_parameters):
        """This API is used for executing the report .

        Args:
            report_id(str): reportId path parameter. Id of the Report .
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
            https://developer.cisco.com/docs/dna-center/#!executing-the-flexible-report
        """
        check_type(headers, dict)
        check_type(report_id, str,
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
            'reportId': report_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/data/api/v1/flexible-'
                 + 'report/report/{reportId}/execute')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params)

        return self._object_factory('bpm_c2c0c5f9fa208985865f05eca_v2_3_7_9', json_data)

    def get_execution_id_by_report_id_v1(self,
                                         report_id,
                                         headers=None,
                                         **request_parameters):
        """Get Execution Id by Report Id .

        Args:
            report_id(str): reportId path parameter. Id of the report .
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
            https://developer.cisco.com/docs/dna-center/#!get-execution-id-by-report-id
        """
        check_type(headers, dict)
        check_type(report_id, str,
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
            'reportId': report_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/data/api/v1/flexible-'
                 + 'report/report/{reportId}/executions')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_edf3c4d58586fb15a5b62256f94a6_v2_3_7_9', json_data)

    def update_schedule_of_flexible_report_v1(self,
                                              report_id,
                                              schedule=None,
                                              headers=None,
                                              payload=None,
                                              active_validation=True,
                                              **request_parameters):
        """Update schedule of flexible report .

        Args:
            schedule(object): Reports's Schedule information .
            report_id(str): reportId path parameter. Id of the report .
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
            https://developer.cisco.com/docs/dna-center/#!update-schedule-of-flexible-report
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(report_id, str,
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
            'reportId': report_id,
        }
        _payload = {
            'schedule':
                schedule,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_a93d01238de0537dbb3d358f9cce0bd2_v2_3_7_9')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/data/api/v1/flexible-report/schedule/{reportId}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload,
                                          headers=_headers)
        else:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload)

        return self._object_factory('bpm_a93d01238de0537dbb3d358f9cce0bd2_v2_3_7_9', json_data)

    def get_flexible_report_schedule_by_report_id_v1(self,
                                                     report_id,
                                                     headers=None,
                                                     **request_parameters):
        """Get flexible report schedule by report id .

        Args:
            report_id(str): reportId path parameter. Id of the report .
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
            https://developer.cisco.com/docs/dna-center/#!get-flexible-report-schedule-by-report-id
        """
        check_type(headers, dict)
        check_type(report_id, str,
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
            'reportId': report_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/data/api/v1/flexible-report/schedule/{reportId}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_a2a4b5bdcace5b55a5962ae85ff59d87_v2_3_7_9', json_data)

    def get_all_flexible_report_schedules_v1(self,
                                             headers=None,
                                             **request_parameters):
        """Get all flexible report schedules .

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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-all-flexible-report-schedules
        """
        check_type(headers, dict)
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

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/data/api/v1/flexible-report/schedules')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_dfd5cfd8a985505aaa606be4599319f_v2_3_7_9', json_data)

    def create_or_schedule_a_report_v1(self,
                                       dataCategory=None,
                                       deliveries=None,
                                       name=None,
                                       schedule=None,
                                       tags=None,
                                       view=None,
                                       viewGroupId=None,
                                       viewGroupVersion=None,
                                       headers=None,
                                       payload=None,
                                       active_validation=True,
                                       **request_parameters):
        """Create/Schedule a report configuration. Use "Get view details for a given view group & view" API to get the
        metadata required to configure a report. .

        Args:
            dataCategory(string): Reports's category of viewgroup for the report .
            deliveries(list): Reports's Array of available delivery channels  (list of objects).
            name(string): Reports's report name .
            schedule(object): Reports's schedule.
            tags(list): Reports's array of tags for report  (list of strings).
            view(object): Reports's view.
            viewGroupId(string): Reports's viewGroupId of the viewgroup for the report .
            viewGroupVersion(string): Reports's version of viewgroup for the report .
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
            https://developer.cisco.com/docs/dna-center/#!create-or-schedule-a-report
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
            'tags':
                tags,
            'deliveries':
                deliveries,
            'name':
                name,
            'schedule':
                schedule,
            'view':
                view,
            'viewGroupId':
                viewGroupId,
            'viewGroupVersion':
                viewGroupVersion,
            'dataCategory':
                dataCategory,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_fa310ab095148bdb00d7d3d5e1676_v2_3_7_9')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/data/reports')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_fa310ab095148bdb00d7d3d5e1676_v2_3_7_9', json_data)

    def get_list_of_scheduled_reports_v1(self,
                                         view_group_id=None,
                                         view_id=None,
                                         headers=None,
                                         **request_parameters):
        """Get list of scheduled report configurations. .

        Args:
            view_group_id(str): viewGroupId query parameter. viewGroupId of viewgroup for report .
            view_id(str): viewId query parameter. viewId of view for report .
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-list-of-scheduled-reports
        """
        check_type(headers, dict)
        check_type(view_group_id, str)
        check_type(view_id, str)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'viewGroupId':
                view_group_id,
            'viewId':
                view_id,
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

        e_url = ('/dna/intent/api/v1/data/reports')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_d89e1c3e150ef9faaff44fa483de5_v2_3_7_9', json_data)

    def get_a_scheduled_report_v1(self,
                                  report_id,
                                  headers=None,
                                  **request_parameters):
        """Get scheduled report configuration by reportId .

        Args:
            report_id(str): reportId path parameter. reportId of report .
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
            https://developer.cisco.com/docs/dna-center/#!get-a-scheduled-report
        """
        check_type(headers, dict)
        check_type(report_id, str,
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
            'reportId': report_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/data/reports/{reportId}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_f9cb7c424b5502b4ad54ccbb1ca4f4_v2_3_7_9', json_data)

    def delete_a_scheduled_report_v1(self,
                                     report_id,
                                     headers=None,
                                     **request_parameters):
        """Delete a scheduled report configuration. Deletes the report executions also. .

        Args:
            report_id(str): reportId path parameter. reportId of report .
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
            https://developer.cisco.com/docs/dna-center/#!delete-a-scheduled-report
        """
        check_type(headers, dict)
        check_type(report_id, str,
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
            'reportId': report_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/data/reports/{reportId}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(endpoint_full_url, params=_params,
                                             headers=_headers)
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_a6a151b68d450dfaf1e8a92e0f5cc68_v2_3_7_9', json_data)

    def get_all_execution_details_for_a_given_report_v1(self,
                                                        report_id,
                                                        headers=None,
                                                        **request_parameters):
        """Get details of all executions for a given report .

        Args:
            report_id(str): reportId path parameter. reportId of report .
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
            https://developer.cisco.com/docs/dna-center/#!get-all-execution-details-for-a-given-report
        """
        check_type(headers, dict)
        check_type(report_id, str,
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
            'reportId': report_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/data/reports/{reportId}/executions')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_a4b1ca0320185570bc12da238f0e88bb_v2_3_7_9', json_data)

    def download_report_content_v1(self,
                                   execution_id,
                                   report_id,
                                   headers=None,
                                   **request_parameters):
        """Returns report content. Save the response to a file by converting the response data as a blob and setting the
        file format available from content-disposition response header. .

        Args:
            report_id(str): reportId path parameter. reportId of report .
            execution_id(str): executionId path parameter. executionId of report execution .
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!download-report-content
        """
        check_type(headers, dict)
        check_type(report_id, str,
                   may_be_none=False)
        check_type(execution_id, str,
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
            'reportId': report_id,
            'executionId': execution_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/data/reports/{reportId}/executions/{e'
                 + 'xecutionId}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_b2790cdb5abf98c8e00011de86a4_v2_3_7_9', json_data)

    def get_all_view_groups_v1(self,
                               headers=None,
                               **request_parameters):
        """Gives a list of summary of all view groups. .

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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-all-view-groups
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

        e_url = ('/dna/intent/api/v1/data/view-groups')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_bbff833d5d5756698f4764a9d488cc98_v2_3_7_9', json_data)

    def get_views_for_a_given_view_group_v1(self,
                                            view_group_id,
                                            headers=None,
                                            **request_parameters):
        """Gives a list of summary of all views in a viewgroup. Use "Get all view groups" API to get the viewGroupIds
        (required as a query param for this API) for available viewgroups. .

        Args:
            view_group_id(str): viewGroupId path parameter. viewGroupId of viewgroup. .
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
            https://developer.cisco.com/docs/dna-center/#!get-views-for-a-given-view-group
        """
        check_type(headers, dict)
        check_type(view_group_id, str,
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
            'viewGroupId': view_group_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/data/view-groups/{viewGroupId}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_c5879612ddc05cd0a0de09d29da4907e_v2_3_7_9', json_data)

    def get_view_details_for_a_given_view_group_and_view_v1(self,
                                                         view_group_id,
                                                         view_id,
                                                         headers=None,
                                                         **request_parameters):
        """Gives complete information of the view that is required to configure a report. Use "Get views for a given view
        group" API to get the viewIds  (required as a query param for this API) for available views. .

        Args:
            view_group_id(str): viewGroupId path parameter. viewGroupId of viewgroup .
            view_id(str): viewId path parameter. view id of view .
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
            https://developer.cisco.com/docs/dna-center/#!get-view-details-for-a-given-view-group_-view
        """
        check_type(headers, dict)
        check_type(view_group_id, str,
                   may_be_none=False)
        check_type(view_id, str,
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
            'viewGroupId': view_group_id,
            'viewId': view_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/data/view-'
                 + 'groups/{viewGroupId}/views/{viewId}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_d1944177c95598ebd1986582dc8069a_v2_3_7_9', json_data)



    # Alias Function
    def create_or_schedule_a_report(self,
                                       dataCategory=None,
                                       deliveries=None,
                                       name=None,
                                       schedule=None,
                                       tags=None,
                                       view=None,
                                       viewGroupId=None,
                                       viewGroupVersion=None,
                                       headers=None,
                                       payload=None,
                                       active_validation=True,
                                       **request_parameters):
        """ This function is an alias of create_or_schedule_a_report_v1 .
        Args:
            dataCategory(string): Reports's category of viewgroup for the report .
            deliveries(list): Reports's Array of available delivery channels  (list of objects).
            name(string): Reports's report name .
            schedule(object): Reports's schedule.
            tags(list): Reports's array of tags for report  (list of strings).
            view(object): Reports's view.
            viewGroupId(string): Reports's viewGroupId of the viewgroup for the report .
            viewGroupVersion(string): Reports's version of viewgroup for the report .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of create_or_schedule_a_report_v1 .
        """
        return self.create_or_schedule_a_report_v1(
                    dataCategory=dataCategory,
                    deliveries=deliveries,
                    name=name,
                    schedule=schedule,
                    tags=tags,
                    view=view,
                    viewGroupId=viewGroupId,
                    viewGroupVersion=viewGroupVersion,
                    headers=headers,
                    payload=payload,
                    active_validation=active_validation,
                    **request_parameters
        )


    # Alias Function
    def get_execution_id_by_report_id(self,
                                         report_id,
                                         headers=None,
                                         **request_parameters):
        """ This function is an alias of get_execution_id_by_report_id_v1 .
        Args:
            report_id(str): reportId path parameter. Id of the report .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_execution_id_by_report_id_v1 .
        """
        return self.get_execution_id_by_report_id_v1(
                    report_id=report_id,
                    headers=headers,
                    **request_parameters
        )


    # Alias Function
    def get_all_view_groups(self,
                               headers=None,
                               **request_parameters):
        """ This function is an alias of get_all_view_groups_v1 .
        Args:
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_all_view_groups_v1 .
        """
        return self.get_all_view_groups_v1(
                    headers=headers,
                    **request_parameters
        )


    # Alias Function
    def executing_the_flexible_report(self,
                                         report_id,
                                         headers=None,
                                         **request_parameters):
        """ This function is an alias of executing_the_flexible_report_v1 .
        Args:
            report_id(str): reportId path parameter. Id of the Report .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of executing_the_flexible_report_v1 .
        """
        return self.executing_the_flexible_report_v1(
                    report_id=report_id,
                    headers=headers,
                    **request_parameters
        )


    # Alias Function
    def get_a_scheduled_report(self,
                                  report_id,
                                  headers=None,
                                  **request_parameters):
        """ This function is an alias of get_a_scheduled_report_v1 .
        Args:
            report_id(str): reportId path parameter. reportId of report .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_a_scheduled_report_v1 .
        """
        return self.get_a_scheduled_report_v1(
                    report_id=report_id,
                    headers=headers,
                    **request_parameters
        )


    # Alias Function
    def update_schedule_of_flexible_report(self,
                                              report_id,
                                              schedule=None,
                                              headers=None,
                                              payload=None,
                                              active_validation=True,
                                              **request_parameters):
        """ This function is an alias of update_schedule_of_flexible_report_v1 .
        Args:
            schedule(object): Reports's Schedule information .
            report_id(str): reportId path parameter. Id of the report .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of update_schedule_of_flexible_report_v1 .
        """
        return self.update_schedule_of_flexible_report_v1(
                    report_id=report_id,
                    schedule=schedule,
                    headers=headers,
                    payload=payload,
                    active_validation=active_validation,
                    **request_parameters
        )


    # Alias Function
    def get_all_execution_details_for_a_given_report(self,
                                                        report_id,
                                                        headers=None,
                                                        **request_parameters):
        """ This function is an alias of get_all_execution_details_for_a_given_report_v1 .
        Args:
            report_id(str): reportId path parameter. reportId of report .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_all_execution_details_for_a_given_report_v1 .
        """
        return self.get_all_execution_details_for_a_given_report_v1(
                    report_id=report_id,
                    headers=headers,
                    **request_parameters
        )


    # Alias Function
    def get_all_flexible_report_schedules(self,
                                             headers=None,
                                             **request_parameters):
        """ This function is an alias of get_all_flexible_report_schedules_v1 .
        Args:
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_all_flexible_report_schedules_v1 .
        """
        return self.get_all_flexible_report_schedules_v1(
                    headers=headers,
                    **request_parameters
        )


    # Alias Function
    def download_flexible_report(self,
                                    execution_id,
                                    report_id,
                                    headers=None,
                                    **request_parameters):
        """ This function is an alias of download_flexible_report_v1 .
        Args:
            report_id(str): reportId path parameter. Id of the report .
            execution_id(str): executionId path parameter. Id of execution .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of download_flexible_report_v1 .
        """
        return self.download_flexible_report_v1(
                    execution_id=execution_id,
                    report_id=report_id,
                    headers=headers,
                    **request_parameters
        )


    # Alias Function
    def get_list_of_scheduled_reports(self,
                                         view_group_id=None,
                                         view_id=None,
                                         headers=None,
                                         **request_parameters):
        """ This function is an alias of get_list_of_scheduled_reports_v1 .
        Args:
            view_group_id(str): viewGroupId query parameter. viewGroupId of viewgroup for report .
            view_id(str): viewId query parameter. viewId of view for report .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_list_of_scheduled_reports_v1 .
        """
        return self.get_list_of_scheduled_reports_v1(
                    view_group_id=view_group_id,
                    view_id=view_id,
                    headers=headers,
                    **request_parameters
        )


    # Alias Function
    def download_report_content(self,
                                   execution_id,
                                   report_id,
                                   headers=None,
                                   **request_parameters):
        """ This function is an alias of download_report_content_v1 .
        Args:
            report_id(str): reportId path parameter. reportId of report .
            execution_id(str): executionId path parameter. executionId of report execution .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of download_report_content_v1 .
        """
        return self.download_report_content_v1(
                    execution_id=execution_id,
                    report_id=report_id,
                    headers=headers,
                    **request_parameters
        )


    # Alias Function
    def get_views_for_a_given_view_group(self,
                                            view_group_id,
                                            headers=None,
                                            **request_parameters):
        """ This function is an alias of get_views_for_a_given_view_group_v1 .
        Args:
            view_group_id(str): viewGroupId path parameter. viewGroupId of viewgroup. .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_views_for_a_given_view_group_v1 .
        """
        return self.get_views_for_a_given_view_group_v1(
                    view_group_id=view_group_id,
                    headers=headers,
                    **request_parameters
        )


    # Alias Function
    def delete_a_scheduled_report(self,
                                     report_id,
                                     headers=None,
                                     **request_parameters):
        """ This function is an alias of delete_a_scheduled_report_v1 .
        Args:
            report_id(str): reportId path parameter. reportId of report .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of delete_a_scheduled_report_v1 .
        """
        return self.delete_a_scheduled_report_v1(
                    report_id=report_id,
                    headers=headers,
                    **request_parameters
        )


    # Alias Function
    def get_flexible_report_schedule_by_report_id(self,
                                                     report_id,
                                                     headers=None,
                                                     **request_parameters):
        """ This function is an alias of get_flexible_report_schedule_by_report_id_v1 .
        Args:
            report_id(str): reportId path parameter. Id of the report .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_flexible_report_schedule_by_report_id_v1 .
        """
        return self.get_flexible_report_schedule_by_report_id_v1(
                    report_id=report_id,
                    headers=headers,
                    **request_parameters
        )

    def get_view_details_for_a_given_view_group_and_view(self,
                                                         view_group_id,
                                                         view_id,
                                                         headers=None,
                                                         **request_parameters):
        """ This function is an alias of get_view_details_for_a_given_view_group_and_view_v1 .
        Args:
            view_group_id(str): viewGroupId path parameter. viewGroupId of viewgroup .
            view_id(str): viewId path parameter. view id of view .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_view_details_for_a_given_view_group_and_view_v1 .
        """
        return self.get_view_details_for_a_given_view_group_and_view_v1(
                                                         view_group_id,
                                                         view_id,
                                                         headers,
                                                         **request_parameters)


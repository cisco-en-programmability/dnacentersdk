# -*- coding: utf-8 -*-
"""Cisco Catalyst Center Sensors API wrapper.

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
)


class Sensors(object):
    """Cisco Catalyst Center Sensors API (version: 2.3.7.9).

    Wraps the Catalyst Center Sensors
    API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new Sensors
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Catalyst Center service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(Sensors, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def lists_i_cap_packet_capture_files_matching_specified_criteria(
        self,
        type,
        ap_mac=None,
        client_mac=None,
        end_time=None,
        limit=None,
        offset=None,
        order=None,
        sort_by=None,
        start_time=None,
        headers=None,
        **request_parameters
    ):
        """Lists the ICAP packet capture (pcap) files matching the specified criteria. For detailed information about the
        usage of the API, please refer to the Open API specification document https://github.com/cisco-en-
        programmability/catalyst-center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-icap-1.0.0-resolved.yaml
        .

        Args:
            type(str): type query parameter. Capture Type .
            client_mac(str): clientMac query parameter. The macAddress of client .
            ap_mac(str): apMac query parameter. The base radio macAddress of the access point .
            start_time(int): startTime query parameter. Start time from which API queries the data set related to
                the resource. It must be specified in UNIX epochtime in milliseconds. Value is
                inclusive. .
            end_time(int): endTime query parameter. End time to which API queries the data set related to the
                resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive. .
            limit(int): limit query parameter. Maximum number of records to return .
            offset(int): offset query parameter. Specifies the starting point within all records returned by the
                API. It's one based offset. The starting value is 1. .
            sort_by(str): sortBy query parameter. A field within the response to sort by. .
            order(str): order query parameter. The sort order of the field ascending or descending. .
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
            https://developer.cisco.com/docs/dna-center/#!lists-i-c-a-p-packet-capture-files-matching-specified-criteria
        """
        check_type(headers, dict)
        check_type(type, str, may_be_none=False)
        check_type(client_mac, str)
        check_type(ap_mac, str)
        check_type(start_time, int)
        check_type(end_time, int)
        check_type(limit, int)
        check_type(offset, int)
        check_type(sort_by, str)
        check_type(order, str)
        if headers is not None:
            if "X-CALLER-ID" in headers:
                check_type(headers.get("X-CALLER-ID"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "type": type,
            "clientMac": client_mac,
            "apMac": ap_mac,
            "startTime": start_time,
            "endTime": end_time,
            "limit": limit,
            "offset": offset,
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

        e_url = "/dna/data/api/v1/icap/captureFiles"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_dbaeabc535e1a8587c92b593cefc3_v2_3_7_9", json_data
        )

    def retrieves_the_total_number_of_packet_capture_files_matching_specified_criteria(
        self,
        type,
        ap_mac=None,
        client_mac=None,
        end_time=None,
        start_time=None,
        headers=None,
        **request_parameters
    ):
        """Retrieves the total number of packet capture files matching the specified criteria. For detailed information
        about the usage of the API, please refer to the Open API specification document
        https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-icap-1.0.0-resolved.yaml .

        Args:
            type(str): type query parameter. Capture Type .
            client_mac(str): clientMac query parameter. The macAddress of client .
            ap_mac(str): apMac query parameter. The base radio macAddress of the access point .
            start_time(int): startTime query parameter. Start time from which API queries the data set related to
                the resource. It must be specified in UNIX epochtime in milliseconds. Value is
                inclusive. .
            end_time(int): endTime query parameter. End time to which API queries the data set related to the
                resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive. .
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-the-total-number-of-packet-capture-files-matching-specified-criteria
        """
        check_type(headers, dict)
        check_type(type, str, may_be_none=False)
        check_type(client_mac, str)
        check_type(ap_mac, str)
        check_type(start_time, int)
        check_type(end_time, int)
        if headers is not None:
            if "X-CALLER-ID" in headers:
                check_type(headers.get("X-CALLER-ID"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "type": type,
            "clientMac": client_mac,
            "apMac": ap_mac,
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

        e_url = "/dna/data/api/v1/icap/captureFiles/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_cbb6ff54e6605629a0a8a3555be72613_v2_3_7_9", json_data
        )

    def retrieves_details_of_a_specific_i_cap_packet_capture_file(
        self, id, headers=None, **request_parameters
    ):
        """Retrieves details of a specific ICAP packet capture file. For detailed information about the usage of the API,
        please refer to the Open API specification document https://github.com/cisco-en-
        programmability/catalyst-center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-icap-1.0.0-resolved.yaml
        .

        Args:
            id(str): id path parameter. The name of the packet capture file, as given by the GET /captureFiles API
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-details-of-a-specific-i-c-a-p-packet-capture-file
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

        e_url = "/dna/data/api/v1/icap/captureFiles/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_be18fdce21365e3ab6833963fefbaa96_v2_3_7_9", json_data
        )

    def downloads_a_specific_i_cap_packet_capture_file(
        self, id, headers=None, **request_parameters
    ):
        """Downloads a specific ICAP packet capture file. For detailed information about the usage of the API, please refer
        to the Open API specification document https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-icap-1.0.0-resolved.yaml .

        Args:
            id(str): id path parameter. The name of the packet capture file, as given by the GET /captureFiles API
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
            https://developer.cisco.com/docs/dna-center/#!downloads-a-specific-i-c-a-p-packet-capture-file
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

        e_url = "/dna/data/api/v1/icap/captureFiles/{id}/download"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_aeb8cee149c55a4a49506e07b6c4385_v2_3_7_9", json_data
        )

    def retrieves_specific_client_statistics_over_specified_period_of_time(
        self,
        id,
        endTime=None,
        filters=None,
        page=None,
        startTime=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Retrieves the time series statistics of a specific client by applying complex filters. If startTime and endTime
        are not provided, the API defaults to the last 24 hours. For detailed information about the usage of the
        API, please refer to the Open API specification document https://github.com/cisco-en-
        programmability/catalyst-center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-icap-1.0.0-resolved.yaml
        .

        Args:
            endTime(integer): Sensors's End Time.
            filters(list): Sensors's filters (list of objects).
            page(object): Sensors's page.
            startTime(integer): Sensors's Start Time.
            id(str): id path parameter. id is the client mac address. It can be specified in one of the notational
                conventions 01:23:45:67:89:AB or 01-23-45-67-89-AB or 0123.4567.89AB and is case
                insensitive .
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-specific-client-statistics-over-specified-period-of-time
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
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
        _payload = {
            "startTime": startTime,
            "endTime": endTime,
            "filters": filters,
            "page": page,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_cca68e89d0545dac01a8c7a461ac6e_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/icap/clients/{id}/stats"
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
            "bpm_cca68e89d0545dac01a8c7a461ac6e_v2_3_7_9", json_data
        )

    def retrieves_specific_radio_statistics_over_specified_period_of_time(
        self,
        id,
        endTime=None,
        filters=None,
        page=None,
        startTime=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Retrieves the time series statistics of a specific radio by applying complex filters. If startTime and endTime
        are not provided, the API defaults to the last 24 hours. For detailed information about the usage of the
        API, please refer to the Open API specification document https://github.com/cisco-en-
        programmability/catalyst-center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-icap-1.0.0-resolved.yaml
        .

        Args:
            endTime(integer): Sensors's End Time.
            filters(list): Sensors's filters (list of objects).
            page(object): Sensors's page.
            startTime(integer): Sensors's Start Time.
            id(str): id path parameter. id is the composite key made of AP Base Ethernet macAddress and Radio Slot
                Id. Format apMac_RadioId .
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-specific-radio-statistics-over-specified-period-of-time
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
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
        _payload = {
            "startTime": startTime,
            "endTime": endTime,
            "filters": filters,
            "page": page,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_f71d0b2527b8cd13123f9a68cf3_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/icap/radios/{id}/stats"
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
            "bpm_f71d0b2527b8cd13123f9a68cf3_v2_3_7_9", json_data
        )

    def retrieves_the_spectrum_interference_devices_reports_sent_by_w_l_c_for_provided_ap_mac(
        self,
        ap_mac,
        end_time=None,
        limit=None,
        offset=None,
        start_time=None,
        time_sort_order=None,
        headers=None,
        **request_parameters
    ):
        """Retrieves the spectrum interference devices reports sent by WLC for provided AP Mac. For detailed information
        about the usage of the API, please refer to the Open API specification document
        https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-icap-1.0.0-resolved.yaml .

        Args:
            start_time(int): startTime query parameter. Start time from which API queries the data set related to
                the resource. It must be specified in UNIX epochtime in milliseconds. Value is
                inclusive. .
            end_time(int): endTime query parameter. End time to which API queries the data set related to the
                resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive. .
            ap_mac(str): apMac query parameter. The base ethernet macAddress of the access point .
            limit(int): limit query parameter. Maximum number of records to return .
            offset(int): offset query parameter. Specifies the starting point within all records returned by the
                API. It's one based offset. The starting value is 1. .
            time_sort_order(str): timeSortOrder query parameter. The sort order of the field ascending or
                descending. .
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-the-spectrum-interference-devices-reports-sent-by-w-l-c-for-provided-a-p-mac
        """
        check_type(headers, dict)
        check_type(start_time, int)
        check_type(end_time, int)
        check_type(ap_mac, str, may_be_none=False)
        check_type(limit, int)
        check_type(offset, int)
        check_type(time_sort_order, str)
        if headers is not None:
            if "X-CALLER-ID" in headers:
                check_type(headers.get("X-CALLER-ID"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "startTime": start_time,
            "endTime": end_time,
            "apMac": ap_mac,
            "limit": limit,
            "offset": offset,
            "timeSortOrder": time_sort_order,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/icap/spectrumInterferenceDeviceReports"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_d1233df7e65d6b93c17b6568a9be4f_v2_3_7_9", json_data
        )

    def retrieves_the_spectrum_sensor_reports_sent_by_w_l_c_for_provided_ap_mac(
        self,
        ap_mac,
        data_type=None,
        end_time=None,
        limit=None,
        offset=None,
        start_time=None,
        time_sort_order=None,
        headers=None,
        **request_parameters
    ):
        """Retrieves the spectrum sensor reports sent by WLC for provided AP Mac. For detailed information about the usage
        of the API, please refer to the Open API specification document https://github.com/cisco-en-
        programmability/catalyst-center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-icap-1.0.0-resolved.yaml
        .

        Args:
            start_time(int): startTime query parameter. Start time from which API queries the data set related to
                the resource. It must be specified in UNIX epochtime in milliseconds. Value is
                inclusive. .
            end_time(int): endTime query parameter. End time to which API queries the data set related to the
                resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive. .
            ap_mac(str): apMac query parameter. The base ethernet macAddress of the access point .
            data_type(int): dataType query parameter. Data type reported by the sensor (Data Type: Description: `0`:
                Duty Cycle: `1`: Max Power: `2`: Average Power: `3`: Max Power in dBm with adjusted base
                of +48: `4`: Average Power in dBm with adjusted base of +48),  .
            limit(int): limit query parameter. Maximum number of records to return .
            offset(int): offset query parameter. Specifies the starting point within all records returned by the
                API. It's one based offset. The starting value is 1. .
            time_sort_order(str): timeSortOrder query parameter. The sort order of the field ascending or
                descending. .
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-the-spectrum-sensor-reports-sent-by-w-l-c-for-provided-a-p-mac
        """
        check_type(headers, dict)
        check_type(start_time, int)
        check_type(end_time, int)
        check_type(ap_mac, str, may_be_none=False)
        check_type(data_type, int)
        check_type(limit, int)
        check_type(offset, int)
        check_type(time_sort_order, str)
        if headers is not None:
            if "X-CALLER-ID" in headers:
                check_type(headers.get("X-CALLER-ID"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "startTime": start_time,
            "endTime": end_time,
            "apMac": ap_mac,
            "dataType": data_type,
            "limit": limit,
            "offset": offset,
            "timeSortOrder": time_sort_order,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/icap/spectrumSensorReports"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ba6a51cf3055d0da0ba65e43b3030b6_v2_3_7_9", json_data
        )

    def edit_sensor_test_template(
        self,
        _id=None,
        actionInProgress=None,
        apCoverage=None,
        connection=None,
        encryptionMode=None,
        frequency=None,
        lastModifiedTime=None,
        location=None,
        locationInfoList=None,
        modelVersion=None,
        name=None,
        numAssociatedSensor=None,
        numNeighborAPThreshold=None,
        profiles=None,
        radioAsSensorRemoved=None,
        rssiThreshold=None,
        runNow=None,
        scheduleInDays=None,
        sensors=None,
        showWlcUpgradeBanner=None,
        siteHierarchy=None,
        ssids=None,
        startTime=None,
        status=None,
        templateName=None,
        testScheduleMode=None,
        version=None,
        wlans=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Intent API to deploy, schedule, or edit and existing SENSOR test template .

        Args:
            _id(string): Sensors's The sensor test template unique identifier, generated at test creation time .
            actionInProgress(string): Sensors's Indication of inprogress action .
            apCoverage(list): Sensors's apCoverage (list of objects).
            connection(string): Sensors's connection type of test: WIRED, WIRELESS, BOTH .
            encryptionMode(string): Sensors's Encryption mode .
            frequency(object): Sensors's frequency.
            lastModifiedTime(integer): Sensors's Last modify time .
            location(string): Sensors's Location string .
            locationInfoList(list): Sensors's locationInfoList (list of objects).
            modelVersion(integer): Sensors's Test template object model version (must be 2) .
            name(string): Sensors's The sensor test template name, which is the same as in 'templateName' .
            numAssociatedSensor(integer): Sensors's Number of associated sensor .
            numNeighborAPThreshold(integer): Sensors's Number of neighboring AP threshold .
            profiles(list): Sensors's profiles (list of objects).
            radioAsSensorRemoved(boolean): Sensors's Radio as sensor removed .
            rssiThreshold(integer): Sensors's RSSI threshold .
            runNow(string): Sensors's Run now (YES, NO) .
            scheduleInDays(integer): Sensors's Bit-wise value of scheduled test days .
            sensors(list): Sensors's sensors (list of objects).
            showWlcUpgradeBanner(boolean): Sensors's Show WLC upgrade banner .
            siteHierarchy(string): Sensors's Site hierarchy .
            ssids(list): Sensors's ssids (list of objects).
            startTime(integer): Sensors's Start time .
            status(string): Sensors's Status of the test (RUNNING, NOTRUNNING) .
            templateName(string): Sensors's The test template name that is to be edited .
            testScheduleMode(string): Sensors's Test schedule mode (ONDEMAND, DEDICATED, SCHEDULED, CONTINUOUS,
                RUNNOW) .
            version(integer): Sensors's The sensor test template version (must be 2) .
            wlans(list): Sensors's WLANs list  (list of strings).
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
            https://developer.cisco.com/docs/dna-center/#!edit-sensor-test-template
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
            "templateName": templateName,
            "name": name,
            "_id": _id,
            "version": version,
            "modelVersion": modelVersion,
            "startTime": startTime,
            "lastModifiedTime": lastModifiedTime,
            "numAssociatedSensor": numAssociatedSensor,
            "location": location,
            "siteHierarchy": siteHierarchy,
            "status": status,
            "connection": connection,
            "actionInProgress": actionInProgress,
            "frequency": frequency,
            "rssiThreshold": rssiThreshold,
            "numNeighborAPThreshold": numNeighborAPThreshold,
            "scheduleInDays": scheduleInDays,
            "wlans": wlans,
            "ssids": ssids,
            "profiles": profiles,
            "testScheduleMode": testScheduleMode,
            "showWlcUpgradeBanner": showWlcUpgradeBanner,
            "radioAsSensorRemoved": radioAsSensorRemoved,
            "encryptionMode": encryptionMode,
            "runNow": runNow,
            "locationInfoList": locationInfoList,
            "sensors": sensors,
            "apCoverage": apCoverage,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_e2f9718de3d050819cdc6355a3a43200_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/AssuranceScheduleSensorTest"
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
            "bpm_e2f9718de3d050819cdc6355a3a43200_v2_3_7_9", json_data
        )

    def retrieves_deployed_i_cap_configurations_while_supporting_basic_filtering(
        self,
        capture_status,
        apid=None,
        capture_type=None,
        client_mac=None,
        limit=None,
        offset=None,
        wlc_id=None,
        headers=None,
        **request_parameters
    ):
        """Retrieves deployed ICAP configurations while supporting basic filtering. For detailed information about the
        usage of the API, please refer to the Open API specification document https://github.com/cisco-en-
        programmability/catalyst-center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-
        ICAP_APIs-1.0.0-resolved.yaml .

        Args:
            capture_status(str): captureStatus query parameter. Catalyst Center ICAP status .
            capture_type(str): captureType query parameter. Catalyst Center ICAP type .
            client_mac(str): clientMac query parameter. The client device MAC address in ICAP configuration .
            apid(str): apId query parameter. The AP device's UUID. .
            wlc_id(str): wlcId query parameter. The wireless controller device's UUID .
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!retrieves-deployed-i-c-a-p-configurations-while-supporting-basic-filtering
        """
        check_type(headers, dict)
        check_type(capture_status, str, may_be_none=False)
        check_type(capture_type, str)
        check_type(client_mac, str)
        check_type(apid, str)
        check_type(wlc_id, str)
        check_type(offset, int)
        check_type(limit, int)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "captureStatus": capture_status,
            "captureType": capture_type,
            "clientMac": client_mac,
            "apId": apid,
            "wlcId": wlc_id,
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

        e_url = "/dna/intent/api/v1/icapSettings"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_fdb9138f5aea88430fda95cbf865_v2_3_7_9", json_data
        )

    def creates_an_i_cap_configuration_intent_for_preview_approve(
        self,
        preview_description=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This creates an ICAP configuration intent for preview approval. The intent is not deployed to the device until
        further preview-approve APIs are applied. This API is the first step in the preview-approve workflow,
        which consists of several APIs. Skipping any API in the process is not recommended for a complete
        preview-approve use case. For detailed information about the usage of the API, please refer to the Open
        API specification document https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-ICAP_APIs-1.0.0-resolved.yaml .

        Args:
            preview_description(str): previewDescription query parameter. The ICAP intent's preview-deploy
                description string .
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!creates-an-i-c-a-p-configuration-intent-for-preview-approve
        """
        check_type(headers, dict)
        check_type(payload, list)
        check_type(preview_description, str)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "previewDescription": preview_description,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = payload or []
        if active_validation:
            self._request_validator(
                "jsd_cb38886d0236502783d431455e3fb880_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/icapSettings/configurationModels"
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
            "bpm_cb38886d0236502783d431455e3fb880_v2_3_7_9", json_data
        )

    def creates_ai_cap_configuration_workflow_for_i_capintent_to_remove_the_i_cap_configuration_on_the_device(
        self,
        id,
        object=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Creates a ICAP configuration intent to remove the ICAP RFSTATS or ANOMALY configuration from the device. The
        task has not been applied to the device yet. Subsequent preview-approve workflow APIs must be used to
        complete the preview-approve process.  The path parameter 'id' can be retrieved from **GET
        /dna/intent/api/v1/icapSettings** API. For detailed information about the usage of the API, please refer
        to the Open API specification document https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-ICAP_APIs-1.0.0-resolved.yaml .

        Args:
            object(string): Sensors's object.
            id(str): id path parameter. A unique ID of the deployed ICAP object, which can be obtained from **GET
                /dna/intent/api/v1/icapSettings** .
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
            https://developer.cisco.com/docs/dna-center/#!creates-a-i-c-a-p-configuration-workflow-for-i-c-a-p-intent-to-remove-the-i-c-a-p-configuration-on-the-device
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }
        _payload = {
            "object": object,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_f924b4c27d18500b9b23df516b55c182_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/icapSettings/configurationModels/{id}" + "/deleteDeploy"
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
            "bpm_f924b4c27d18500b9b23df516b55c182_v2_3_7_9", json_data
        )

    def discards_the_i_cap_configuration_intent_by_activity_id(
        self, preview_activity_id, headers=None, **request_parameters
    ):
        """Discard the ICAP configuration intent by activity ID, which was returned in TaskResponse's property "taskId" at
        the beginning of the preview-approve workflow.  Discarding the intent can only be applied to intent
        activities that have not been deployed. Note that ICAP type FULL, ONBOARDING, OTA, and SPECTRUM for the
        scheduled-disabled task cannot be discarded or cancelled because they have already deployed.  The
        feature can only be disabled by sending in a direct-deploy DELETE with API
        /dna/intent/api/v1/icapSettings/deploy/deployedId/{icapDeployedId} For detailed information about the
        usage of the API, please refer to the Open API specification document https://github.com/cisco-en-
        programmability/catalyst-center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-
        ICAP_APIs-1.0.0-resolved.yaml .

        Args:
            preview_activity_id(str): previewActivityId path parameter. activity from the POST
                /deviceConfigugrationModels task response .
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
            https://developer.cisco.com/docs/dna-center/#!discards-the-i-c-a-p-configuration-intent-by-activity-i-d
        """
        check_type(headers, dict)
        check_type(preview_activity_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "previewActivityId": preview_activity_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/icapSettings/configurationModels/{pre"
            + "viewActivityId}"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_cd924ed4c4ed5fd3a463d5251896d31c_v2_3_7_9", json_data
        )

    def deploys_the_i_cap_configuration_intent_by_activity_id(
        self,
        preview_activity_id,
        object=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Deploys the ICAP configuration intent by activity ID, which was returned in property "taskId" of the
        TaskResponse of the POST.  POST'ing the intent prior to generating the intent CLI for preview-approve
        has the same effect as direct-deploy'ing the intent to the device. Generating of device's CLIs for
        preview-approve is not available for this activity ID after using this POST API. For detailed
        information about the usage of the API, please refer to the Open API specification document
        https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-ICAP_APIs-1.0.0-resolved.yaml .

        Args:
            object(string): Sensors's object.
            preview_activity_id(str): previewActivityId path parameter. activity from the POST
                /deviceConfigugrationModels task response .
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
            https://developer.cisco.com/docs/dna-center/#!deploys-the-i-c-a-p-configuration-intent-by-activity-i-d
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(preview_activity_id, str, may_be_none=False)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "previewActivityId": preview_activity_id,
        }
        _payload = {
            "object": object,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_de1769e2886b5948b408100225b4a034_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/icapSettings/configurationModels/{pre"
            + "viewActivityId}/deploy"
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
            "bpm_de1769e2886b5948b408100225b4a034_v2_3_7_9", json_data
        )

    def get_i_cap_configuration_status_per_network_device(
        self, preview_activity_id, headers=None, **request_parameters
    ):
        """Get ICAP configuration status per network device using the activity ID, which was returned in property "taskId"
        of the TaskResponse of the POST. For detailed information about the usage of the API, please refer to
        the Open API specification document https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-ICAP_APIs-1.0.0-resolved.yaml .

        Args:
            preview_activity_id(str): previewActivityId path parameter. activity from the POST
                /deviceConfigugrationModels task response .
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
            https://developer.cisco.com/docs/dna-center/#!get-i-c-a-p-configuration-status-per-network-device
        """
        check_type(headers, dict)
        check_type(preview_activity_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "previewActivityId": preview_activity_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/icapSettings/configurationModels/{pre"
            + "viewActivityId}/networkDeviceStatusDetails"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c6f94fda3501dbb0055d06e71e025_v2_3_7_9", json_data
        )

    def retrieves_the_devices_clis_of_the_i_capintent(
        self, network_device_id, preview_activity_id, headers=None, **request_parameters
    ):
        """Returns the device's CLIs of the ICAP intent. For detailed information about the usage of the API, please refer
        to the Open API specification document https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-ICAP_APIs-1.0.0-resolved.yaml .

        Args:
            preview_activity_id(str): previewActivityId path parameter. activity from the POST
                /deviceConfigugrationModels task response .
            network_device_id(str): networkDeviceId path parameter. device id from intent/api/v1/network-device .
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-the-devices-c-l-is-of-the-i-c-a-p-intent
        """
        check_type(headers, dict)
        check_type(preview_activity_id, str, may_be_none=False)
        check_type(network_device_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "previewActivityId": preview_activity_id,
            "networkDeviceId": network_device_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/icapSettings/configurationModels/{pre"
            + "viewActivityId}/networkDevices/{networkDeviceId}/config"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_f657ae3d75ecd87e97be0a1571923_v2_3_7_9", json_data
        )

    def generates_the_devices_clis_of_the_i_cap_configuration_intent(
        self,
        network_device_id,
        preview_activity_id,
        object=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Generates the device's CLIs of the ICAP intent for preview and approve prior to deploying the ICAP configuration
        intent to the device.  After deploying the configuration intent, generating intent CLIs will not be
        available for preview. For detailed information about the usage of the API, please refer to the Open API
        specification document https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-ICAP_APIs-1.0.0-resolved.yaml .

        Args:
            object(string): Sensors's object.
            preview_activity_id(str): previewActivityId path parameter. activity from the POST
                /deviceConfigugrationModels task response .
            network_device_id(str): networkDeviceId path parameter. device id from intent/api/v1/network-device .
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
            https://developer.cisco.com/docs/dna-center/#!generates-the-devices-c-l-is-of-the-i-c-a-p-configuration-intent
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(preview_activity_id, str, may_be_none=False)
        check_type(network_device_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "previewActivityId": preview_activity_id,
            "networkDeviceId": network_device_id,
        }
        _payload = {
            "object": object,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_ac98aec39c95c2d97532514ee9b9f3e_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/icapSettings/configurationModels/{pre"
            + "viewActivityId}/networkDevices/{networkDeviceId}/config"
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
            "bpm_ac98aec39c95c2d97532514ee9b9f3e_v2_3_7_9", json_data
        )

    def retrieves_the_count_of_deployed_i_cap_configurations_while_supporting_basic_filtering(
        self,
        capture_status,
        apid=None,
        capture_type=None,
        client_mac=None,
        wlc_id=None,
        headers=None,
        **request_parameters
    ):
        """Retrieves the count of deployed ICAP configurations while supporting basic filtering. For detailed information
        about the usage of the API, please refer to the Open API specification document
        https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-ICAP_APIs-1.0.0-resolved.yaml .

        Args:
            capture_type(str): captureType query parameter. Catalyst Center ICAP type .
            capture_status(str): captureStatus query parameter. Catalyst Center ICAP status .
            client_mac(str): clientMac query parameter. The client device MAC address in ICAP configuration .
            apid(str): apId query parameter. The AP device's UUID. .
            wlc_id(str): wlcId query parameter. The wireless controller device's UUID .
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-the-count-of-deployed-i-c-a-p-configurations-while-supporting-basic-filtering
        """
        check_type(headers, dict)
        check_type(capture_type, str)
        check_type(capture_status, str, may_be_none=False)
        check_type(client_mac, str)
        check_type(apid, str)
        check_type(wlc_id, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "captureType": capture_type,
            "captureStatus": capture_status,
            "clientMac": client_mac,
            "apId": apid,
            "wlcId": wlc_id,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/icapSettings/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_d122ab38d3758cba132f5e883d607c3_v2_3_7_9", json_data
        )

    def deploys_the_given_i_cap_configuration_intent_without_preview_and_approve(
        self,
        preview_description=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Deploys the given ICAP intent without preview and approval. The response body contains a task object with a
        taskId and a URL for more information about the task. The deployment status of this ICAP intent can be
        found in the output of the URL.  For detailed information about the usage of the API, please refer to
        the Open API specification document https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-ICAP_APIs-1.0.0-resolved.yaml .

        Args:
            preview_description(str): previewDescription query parameter. The ICAP intent's preview-deploy
                description string .
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!deploys-the-given-i-c-a-p-configuration-intent-without-preview-and-approve
        """
        check_type(headers, dict)
        check_type(payload, list)
        check_type(preview_description, str)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "previewDescription": preview_description,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = payload or []
        if active_validation:
            self._request_validator(
                "jsd_eea45fca32f5f12adc30a9d03c43ac6_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/icapSettings/deploy"
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
            "bpm_eea45fca32f5f12adc30a9d03c43ac6_v2_3_7_9", json_data
        )

    def remove_the_i_cap_configuration_on_the_device_without_preview(
        self,
        id,
        object=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Remove the ICAP configuration from the device by *id* without preview-deploy. The path parameter *id* can be
        retrieved from the **GET /dna/intent/api/v1/icapSettings** API. The response body contains a task object
        with a taskId and a URL. Use the URL to check the task status. ICAP FULL, ONBOARDING, OTA, and SPECTRUM
        configurations have a durationInMins field. A disable task is scheduled to remove the configuration from
        the device. Removing the ICAP intent should be done after the pre-scheduled disable task has been
        deployed. For detailed information about the usage of the API, please refer to the Open API
        specification document https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-ICAP_APIs-1.0.0-resolved.yaml .

        Args:
            object(string): Sensors's object.
            id(str): id path parameter. A unique ID of the deployed ICAP object, which can be obtained from **GET
                /dna/intent/api/v1/icapSettings** .
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
            https://developer.cisco.com/docs/dna-center/#!remove-the-i-c-a-p-configuration-on-the-device-without-preview
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }
        _payload = {
            "object": object,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_e2ec291c2e775df3895aadc639713eea_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/icapSettings/deploy/{id}/deleteDeploy"
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
            "bpm_e2ec291c2e775df3895aadc639713eea_v2_3_7_9", json_data
        )

    def get_device_deployment_status(
        self,
        deploy_activity_id=None,
        limit=None,
        network_device_ids=None,
        offset=None,
        order=None,
        sort_by=None,
        headers=None,
        **request_parameters
    ):
        """Retrieves ICAP configuration deployment status(s) per device based on filter criteria. For detailed information
        about the usage of the API, please refer to the Open API specification document
        https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-ICAP_APIs-1.0.0-resolved.yaml .

        Args:
            deploy_activity_id(str): deployActivityId query parameter. activity from the /deploy task response .
            network_device_ids(str): networkDeviceIds query parameter. device ids, retrievable from the id attribute
                in intent/api/v1/network-device .
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
            https://developer.cisco.com/docs/dna-center/#!get-device-deployment-status
        """
        check_type(headers, dict)
        check_type(deploy_activity_id, str)
        check_type(network_device_ids, str)
        check_type(offset, int)
        check_type(limit, int)
        check_type(sort_by, str)
        check_type(order, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "deployActivityId": deploy_activity_id,
            "networkDeviceIds": network_device_ids,
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

        e_url = "/dna/intent/api/v1/icapSettings/deviceDeployments"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_bebb4e5aaf8ba6e5284cdbeafb_v2_3_7_9", json_data
        )

    def get_device_deployment_status_count(
        self,
        deploy_activity_id=None,
        network_device_ids=None,
        headers=None,
        **request_parameters
    ):
        """Returns the count of device deployment status(s) based on filter criteria. For detailed information about the
        usage of the API, please refer to the Open API specification document https://github.com/cisco-en-
        programmability/catalyst-center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-
        ICAP_APIs-1.0.0-resolved.yaml .

        Args:
            deploy_activity_id(str): deployActivityId query parameter. activity from the /deploy task response .
            network_device_ids(str): networkDeviceIds query parameter. device ids, retrievable from the id attribute
                in intent/api/v1/network-device .
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
            https://developer.cisco.com/docs/dna-center/#!get-device-deployment-status-count
        """
        check_type(headers, dict)
        check_type(deploy_activity_id, str)
        check_type(network_device_ids, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "deployActivityId": deploy_activity_id,
            "networkDeviceIds": network_device_ids,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/icapSettings/deviceDeployments/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_d04eba6a847958ae9c883f6957081ead_v2_3_7_9", json_data
        )

    def create_sensor_test_template(
        self,
        apCoverage=None,
        connection=None,
        encryptionMode=None,
        locationInfoList=None,
        modelVersion=None,
        name=None,
        profiles=None,
        runNow=None,
        sensors=None,
        ssids=None,
        version=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Intent API to create a SENSOR test template with a new SSID, existing SSID, or both new and existing SSID .

        Args:
            apCoverage(list): Sensors's apCoverage (list of objects).
            connection(string): Sensors's connection type of test: WIRED, WIRELESS, BOTH .
            encryptionMode(string): Sensors's Encryption mode .
            locationInfoList(list): Sensors's locationInfoList (list of objects).
            modelVersion(integer): Sensors's Test template object model version (must be 2) .
            name(string): Sensors's The sensor test template name .
            profiles(list): Sensors's profiles (list of objects).
            runNow(string): Sensors's Run now (YES, NO) .
            sensors(list): Sensors's sensors (list of objects).
            ssids(list): Sensors's ssids (list of objects).
            version(integer): Sensors's The sensor test template version (must be 2) .
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
            https://developer.cisco.com/docs/dna-center/#!create-sensor-test-template
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
            "version": version,
            "modelVersion": modelVersion,
            "connection": connection,
            "ssids": ssids,
            "profiles": profiles,
            "encryptionMode": encryptionMode,
            "runNow": runNow,
            "locationInfoList": locationInfoList,
            "sensors": sensors,
            "apCoverage": apCoverage,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_f7dd6a6cf8d57499168aae05847ad34_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/sensor"
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
            "bpm_f7dd6a6cf8d57499168aae05847ad34_v2_3_7_9", json_data
        )

    def delete_sensor_test(self, template_name, headers=None, **request_parameters):
        """Intent API to delete an existing SENSOR test template .

        Args:
            template_name(str): templateName query parameter.
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
            https://developer.cisco.com/docs/dna-center/#!delete-sensor-test
        """
        check_type(headers, dict)
        check_type(template_name, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "templateName": template_name,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/sensor"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a1c0ac4386555300b7f4a541d8dba625_v2_3_7_9", json_data
        )

    def sensors(self, site_id=None, headers=None, **request_parameters):
        """Intent API to get a list of SENSOR devices .

        Args:
            site_id(str): siteId query parameter.
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
            https://developer.cisco.com/docs/dna-center/#!sensors
        """
        check_type(headers, dict)
        check_type(site_id, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "siteId": site_id,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/sensor"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_cda740c5bdc92fd150c334d0e4e_v2_3_7_9", json_data
        )

    def run_now_sensor_test(
        self,
        templateName=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Intent API to run a deployed SENSOR test .

        Args:
            templateName(string): Sensors's Template Name.
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
            https://developer.cisco.com/docs/dna-center/#!run-now-sensor-test
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
            "templateName": templateName,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_cfadc5e4c912588389f4f63d2fb6e4ed_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/sensor-run-now"
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
            "bpm_cfadc5e4c912588389f4f63d2fb6e4ed_v2_3_7_9", json_data
        )

    def duplicate_sensor_test_template(
        self,
        newTemplateName=None,
        templateName=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Intent API to duplicate an existing SENSOR test template .

        Args:
            newTemplateName(string): Sensors's Destination test template name .
            templateName(string): Sensors's Source test template name .
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
            https://developer.cisco.com/docs/dna-center/#!duplicate-sensor-test-template
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
            "templateName": templateName,
            "newTemplateName": newTemplateName,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_a352f6280e445075b3ea7cbf868c2d94_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/sensorTestTemplate"
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
            "bpm_a352f6280e445075b3ea7cbf868c2d94_v2_3_7_9", json_data
        )


# Alias Functions

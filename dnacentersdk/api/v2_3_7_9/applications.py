# -*- coding: utf-8 -*-
"""Cisco Catalyst Center Applications API wrapper.

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


class Applications(object):
    """Cisco Catalyst Center Applications API (version: 2.3.7.9).

    Wraps the Catalyst Center Applications
    API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new Applications
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Catalyst Center service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(Applications, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def retrieves_the_list_of_network_applications_along_with_experience_and_health_metrics_v1(self,
                                                                                               site_id,
                                                                                               application_name=None,
                                                                                               attribute=None,
                                                                                               business_relevance=None,
                                                                                               end_time=None,
                                                                                               limit=None,
                                                                                               offset=None,
                                                                                               order=None,
                                                                                               sort_by=None,
                                                                                               ssid=None,
                                                                                               start_time=None,
                                                                                               headers=None,
                                                                                               **request_parameters):
        """Retrieves the list of network applications along with experience and health metrics. If startTime and endTime
        are not provided, the API defaults to the last 24 hours. `siteId` is mandatory. `siteId` must be a site
        UUID of a building. For detailed information about the usage of the API, please refer to the Open API
        specification document https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-NetworkApplications-1.0.0-resolved.yaml .

        Args:
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
            site_id(str): siteId query parameter. The site UUID without the top level hierarchy. `siteId` is
                mandatory. `siteId` must be a site UUID of a building. (Ex."buildingUuid") Examples:
                `siteId=buildingUuid` (single siteId requested)
                `siteId=buildingUuid1&siteId=buildingUuid2` (multiple siteId requested) .
            ssid(str): ssid query parameter. In the context of a network application, SSID refers to the name
                of the wireless network to which the client connects. Examples: `ssid=Alpha` (single
                ssid requested) `ssid=Alpha&ssid=Guest` (multiple ssid requested) .
            application_name(str): applicationName query parameter. Name of the application for which the
                experience data is intended. Examples: `applicationName=webex` (single applicationName
                requested) `applicationName=webex&applicationName=teams` (multiple applicationName
                requested) .
            business_relevance(str): businessRelevance query parameter. The application can be chosen to be
                categorized as business-relevant, irrelevant, or default (neutral). By doing so, the
                assurance application prioritizes the monitoring and analysis of business-relevant data,
                ensuring critical insights are captured. Applications marked as irrelevant or default
                are selectively excluded from certain data sets, streamlining focus on what's most
                important for business outcomes. .
            attribute(str): attribute query parameter. List of attributes related to resource that can be
                requested to only be part of the response along with the required attributes. Supported
                attributes are applicationName, siteId, exporterIpAddress, exporterNetworkDeviceId,
                healthScore, businessRelevance, usage, throughput, packetLossPercent, networkLatency,
                applicationServerLatency, clientNetworkLatency, serverNetworkLatency, trafficClass,
                jitter, ssid Examples: `attribute=healthScore` (single attribute requested)
                `attribute=healthScore&attribute=ssid&attribute=jitter` (multiple attribute requested) .
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-the-list-of-network-applications-along-with-experience-and-health-metrics
        """
        check_type(headers, dict)
        check_type(start_time, int)
        check_type(end_time, int)
        check_type(limit, int)
        check_type(offset, int)
        check_type(sort_by, str)
        check_type(order, str)
        check_type(site_id, str,
                   may_be_none=False)
        check_type(ssid, str)
        check_type(application_name, str)
        check_type(business_relevance, str)
        check_type(attribute, str)
        if headers is not None:
            if 'X-CALLER-ID' in headers:
                check_type(headers.get('X-CALLER-ID'),
                           str)
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'startTime':
                start_time,
            'endTime':
                end_time,
            'limit':
                limit,
            'offset':
                offset,
            'sortBy':
                sort_by,
            'order':
                order,
            'siteId':
                site_id,
            'ssid':
                ssid,
            'applicationName':
                application_name,
            'businessRelevance':
                business_relevance,
            'attribute':
                attribute,
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

        e_url = ('/dna/data/api/v1/networkApplications')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_fb02436a6c935d5d8a536b86de8b2846_v2_3_7_9', json_data)

    def retrieves_the_total_count_of_network_applications_by_applying_basic_filtering_v1(self,
                                                                                         site_id,
                                                                                         application_name=None,
                                                                                         business_relevance=None,
                                                                                         end_time=None,
                                                                                         ssid=None,
                                                                                         start_time=None,
                                                                                         headers=None,
                                                                                         **request_parameters):
        """Retrieves the number of network applications by applying basic filtering. If startTime and endTime are not
        provided, the API defaults to the last 24 hours. `siteId` is mandatory. `siteId` must be a site UUID of
        a building. For detailed information about the usage of the API, please refer to the Open API
        specification document https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-NetworkApplications-1.0.0-resolved.yaml .

        Args:
            start_time(int): startTime query parameter. Start time from which API queries the data set related to
                the resource. It must be specified in UNIX epochtime in milliseconds. Value is
                inclusive. .
            end_time(int): endTime query parameter. End time to which API queries the data set related to the
                resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive. .
            site_id(str): siteId query parameter. The site UUID without the top level hierarchy. `siteId` is
                mandatory. `siteId` must be a site UUID of a building. (Ex."buildingUuid") Examples:
                `siteId=buildingUuid` (single siteId requested)
                `siteId=buildingUuid1&siteId=buildingUuid2` (multiple siteId requested) .
            ssid(str): ssid query parameter. In the context of a network application, SSID refers to the name
                of the wireless network to which the client connects. Examples: `ssid=Alpha` (single
                ssid requested) `ssid=Alpha&ssid=Guest` (multiple ssid requested) .
            application_name(str): applicationName query parameter. Name of the application for which the
                experience data is intended. Examples: `applicationName=webex` (single applicationName
                requested) `applicationName=webex&applicationName=teams` (multiple applicationName
                requested) .
            business_relevance(str): businessRelevance query parameter. The application can be chosen to be
                categorized as business-relevant, irrelevant, or default (neutral). By doing so, the
                assurance application prioritizes the monitoring and analysis of business-relevant data,
                ensuring critical insights are captured. Applications marked as irrelevant or default
                are selectively excluded from certain data sets, streamlining focus on what's most
                important for business outcomes. .
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-the-total-count-of-network-applications-by-applying-basic-filtering
        """
        check_type(headers, dict)
        check_type(start_time, int)
        check_type(end_time, int)
        check_type(site_id, str,
                   may_be_none=False)
        check_type(ssid, str)
        check_type(application_name, str)
        check_type(business_relevance, str)
        if headers is not None:
            if 'X-CALLER-ID' in headers:
                check_type(headers.get('X-CALLER-ID'),
                           str)
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
            'ssid':
                ssid,
            'applicationName':
                application_name,
            'businessRelevance':
                business_relevance,
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

        e_url = ('/dna/data/api/v1/networkApplications/count')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_c50def6b3a58e5acab3ae592a57da8_v2_3_7_9', json_data)

    def retrieves_the_trend_analytics_data_related_to_network_applications_v1(self,
                                                                              aggregateAttributes=None,
                                                                              attributes=None,
                                                                              endTime=None,
                                                                              filters=None,
                                                                              groupBy=None,
                                                                              page=None,
                                                                              siteIds=None,
                                                                              startTime=None,
                                                                              trendInterval=None,
                                                                              headers=None,
                                                                              payload=None,
                                                                              active_validation=True,
                                                                              **request_parameters):
        """Retrieves the trend analytics of applications experience data for the specified time range. The data will be
        grouped based on the given trend time interval. This API facilitates obtaining consolidated insights
        into the performance and status of the network applications over the specified start and end time. If
        startTime and endTime are not provided, the API defaults to the last 24 hours. `siteId` and
        `trendInterval` are mandatory. `siteId` must be a site UUID of a building. For detailed information
        about the usage of the API, please refer to the Open API specification document
        https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-NetworkApplications-1.0.0-resolved.yaml .

        Args:
            aggregateAttributes(list): Applications's aggregateAttributes (list of objects).
            attributes(list): Applications's Attributes (list of strings).
            endTime(integer): Applications's End Time.
            filters(list): Applications's filters (list of objects).
            groupBy(list): Applications's Group By (list of strings).
            page(object): Applications's page.
            siteIds(list): Applications's Site Ids (list of strings).
            startTime(integer): Applications's Start Time.
            trendInterval(string): Applications's Trend Interval.
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-the-trend-analytics-data-related-to-network-applications
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if 'Content-Type' in headers:
                check_type(headers.get('Content-Type'),
                           str, may_be_none=False)
            if 'X-CALLER-ID' in headers:
                check_type(headers.get('X-CALLER-ID'),
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
            'startTime':
                startTime,
            'endTime':
                endTime,
            'siteIds':
                siteIds,
            'trendInterval':
                trendInterval,
            'groupBy':
                groupBy,
            'attributes':
                attributes,
            'filters':
                filters,
            'aggregateAttributes':
                aggregateAttributes,
            'page':
                page,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_6ce35f19bc4c1d058aa01536_v2_3_7_9')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/data/api/v1/networkApplications/trendAnalytics')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_6ce35f19bc4c1d058aa01536_v2_3_7_9', json_data)

    def applications_v1(self,
                        application_health=None,
                        application_name=None,
                        device_id=None,
                        end_time=None,
                        limit=None,
                        mac_address=None,
                        offset=None,
                        site_id=None,
                        start_time=None,
                        headers=None,
                        **request_parameters):
        """Intent API to get a list of applications for a specific site, a device, or a client device's MAC address. For a
        combination of a specific application with site and/or device the API gets list of
        issues/devices/endpoints. .

        Args:
            site_id(str): siteId query parameter. Assurance site UUID value (Cannot be submitted together
                with deviceId and clientMac) .
            device_id(str): deviceId query parameter. Assurance device UUID value (Cannot be submitted
                together with siteId and clientMac) .
            mac_address(str): macAddress query parameter. Client device's MAC address (Cannot be submitted
                together with siteId and deviceId) .
            start_time(int): startTime query parameter. Starting epoch time in milliseconds of time window .
            end_time(int): endTime query parameter. Ending epoch time in milliseconds of time window .
            application_health(str): applicationHealth query parameter. Application health category (POOR,
                FAIR, or GOOD.  Optionally use with siteId only) .
            offset(int): offset query parameter. The offset of the first application in the returned data
                (optionally used with siteId only) .
            limit(int): limit query parameter. The max number of application entries in returned data [1, 1000]
                (optionally used with siteId only) .
            application_name(str): applicationName query parameter. The name of the application to get
                information on .
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
            https://developer.cisco.com/docs/dna-center/#!applications
        """
        check_type(headers, dict)
        check_type(site_id, str)
        check_type(device_id, str)
        check_type(mac_address, str)
        check_type(start_time, int)
        check_type(end_time, int)
        check_type(application_health, str)
        check_type(offset, int)
        check_type(limit, int)
        check_type(application_name, str)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'siteId':
                site_id,
            'deviceId':
                device_id,
            'macAddress':
                mac_address,
            'startTime':
                start_time,
            'endTime':
                end_time,
            'applicationHealth':
                application_health,
            'offset':
                offset,
            'limit':
                limit,
            'applicationName':
                application_name,
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

        e_url = ('/dna/intent/api/v1/application-health')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_b85e4ce533d5ff49ddd3b2f9657cfa5_v2_3_7_9', json_data)



    # Alias Function
    def retrieves_the_trend_analytics_data_related_to_network_applications(self,
                                                                              aggregateAttributes=None,
                                                                              attributes=None,
                                                                              endTime=None,
                                                                              filters=None,
                                                                              groupBy=None,
                                                                              page=None,
                                                                              siteIds=None,
                                                                              startTime=None,
                                                                              trendInterval=None,
                                                                              headers=None,
                                                                              payload=None,
                                                                              active_validation=True,
                                                                              **request_parameters):
        """ This function is an alias of retrieves_the_trend_analytics_data_related_to_network_applications_v1 .
        Args:
            aggregateAttributes(list): Applications's aggregateAttributes (list of objects).
            attributes(list): Applications's Attributes (list of strings).
            endTime(integer): Applications's End Time.
            filters(list): Applications's filters (list of objects).
            groupBy(list): Applications's Group By (list of strings).
            page(object): Applications's page.
            siteIds(list): Applications's Site Ids (list of strings).
            startTime(integer): Applications's Start Time.
            trendInterval(string): Applications's Trend Interval.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of retrieves_the_trend_analytics_data_related_to_network_applications_v1 .
        """
        return self.retrieves_the_trend_analytics_data_related_to_network_applications_v1(
                    aggregateAttributes=aggregateAttributes,
                    attributes=attributes,
                    endTime=endTime,
                    filters=filters,
                    groupBy=groupBy,
                    page=page,
                    siteIds=siteIds,
                    startTime=startTime,
                    trendInterval=trendInterval,
                    headers=headers,
                    payload=payload,
                    active_validation=active_validation,
                    **request_parameters
        )


    # Alias Function
    def retrieves_the_list_of_network_applications_along_with_experience_and_health_metrics(self,
                                                                                               site_id,
                                                                                               application_name=None,
                                                                                               attribute=None,
                                                                                               business_relevance=None,
                                                                                               end_time=None,
                                                                                               limit=None,
                                                                                               offset=None,
                                                                                               order=None,
                                                                                               sort_by=None,
                                                                                               ssid=None,
                                                                                               start_time=None,
                                                                                               headers=None,
                                                                                               **request_parameters):
        """ This function is an alias of retrieves_the_list_of_network_applications_along_with_experience_and_health_metrics_v1 .
        Args:
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
            site_id(str): siteId query parameter. The site UUID without the top level hierarchy. `siteId` is
                mandatory. `siteId` must be a site UUID of a building. (Ex."buildingUuid") Examples:
                `siteId=buildingUuid` (single siteId requested)
                `siteId=buildingUuid1&siteId=buildingUuid2` (multiple siteId requested) .
            ssid(str): ssid query parameter. In the context of a network application, SSID refers to the name
                of the wireless network to which the client connects. Examples: `ssid=Alpha` (single
                ssid requested) `ssid=Alpha&ssid=Guest` (multiple ssid requested) .
            application_name(str): applicationName query parameter. Name of the application for which the
                experience data is intended. Examples: `applicationName=webex` (single applicationName
                requested) `applicationName=webex&applicationName=teams` (multiple applicationName
                requested) .
            business_relevance(str): businessRelevance query parameter. The application can be chosen to be
                categorized as business-relevant, irrelevant, or default (neutral). By doing so, the
                assurance application prioritizes the monitoring and analysis of business-relevant data,
                ensuring critical insights are captured. Applications marked as irrelevant or default
                are selectively excluded from certain data sets, streamlining focus on what's most
                important for business outcomes. .
            attribute(str): attribute query parameter. List of attributes related to resource that can be
                requested to only be part of the response along with the required attributes. Supported
                attributes are applicationName, siteId, exporterIpAddress, exporterNetworkDeviceId,
                healthScore, businessRelevance, usage, throughput, packetLossPercent, networkLatency,
                applicationServerLatency, clientNetworkLatency, serverNetworkLatency, trafficClass,
                jitter, ssid Examples: `attribute=healthScore` (single attribute requested)
                `attribute=healthScore&attribute=ssid&attribute=jitter` (multiple attribute requested) .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of retrieves_the_list_of_network_applications_along_with_experience_and_health_metrics_v1 .
        """
        return self.retrieves_the_list_of_network_applications_along_with_experience_and_health_metrics_v1(
                    site_id=site_id,
                    application_name=application_name,
                    attribute=attribute,
                    business_relevance=business_relevance,
                    end_time=end_time,
                    limit=limit,
                    offset=offset,
                    order=order,
                    sort_by=sort_by,
                    ssid=ssid,
                    start_time=start_time,
                    headers=headers,
                    **request_parameters
        )


    # Alias Function
    def retrieves_the_total_count_of_network_applications_by_applying_basic_filtering(self,
                                                                                         site_id,
                                                                                         application_name=None,
                                                                                         business_relevance=None,
                                                                                         end_time=None,
                                                                                         ssid=None,
                                                                                         start_time=None,
                                                                                         headers=None,
                                                                                         **request_parameters):
        """ This function is an alias of retrieves_the_total_count_of_network_applications_by_applying_basic_filtering_v1 .
        Args:
            start_time(int): startTime query parameter. Start time from which API queries the data set related to
                the resource. It must be specified in UNIX epochtime in milliseconds. Value is
                inclusive. .
            end_time(int): endTime query parameter. End time to which API queries the data set related to the
                resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive. .
            site_id(str): siteId query parameter. The site UUID without the top level hierarchy. `siteId` is
                mandatory. `siteId` must be a site UUID of a building. (Ex."buildingUuid") Examples:
                `siteId=buildingUuid` (single siteId requested)
                `siteId=buildingUuid1&siteId=buildingUuid2` (multiple siteId requested) .
            ssid(str): ssid query parameter. In the context of a network application, SSID refers to the name
                of the wireless network to which the client connects. Examples: `ssid=Alpha` (single
                ssid requested) `ssid=Alpha&ssid=Guest` (multiple ssid requested) .
            application_name(str): applicationName query parameter. Name of the application for which the
                experience data is intended. Examples: `applicationName=webex` (single applicationName
                requested) `applicationName=webex&applicationName=teams` (multiple applicationName
                requested) .
            business_relevance(str): businessRelevance query parameter. The application can be chosen to be
                categorized as business-relevant, irrelevant, or default (neutral). By doing so, the
                assurance application prioritizes the monitoring and analysis of business-relevant data,
                ensuring critical insights are captured. Applications marked as irrelevant or default
                are selectively excluded from certain data sets, streamlining focus on what's most
                important for business outcomes. .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of retrieves_the_total_count_of_network_applications_by_applying_basic_filtering_v1 .
        """
        return self.retrieves_the_total_count_of_network_applications_by_applying_basic_filtering_v1(
                    site_id=site_id,
                    application_name=application_name,
                    business_relevance=business_relevance,
                    end_time=end_time,
                    ssid=ssid,
                    start_time=start_time,
                    headers=headers,
                    **request_parameters
        )


    # Alias Function
    def applications(self,
                        application_health=None,
                        application_name=None,
                        device_id=None,
                        end_time=None,
                        limit=None,
                        mac_address=None,
                        offset=None,
                        site_id=None,
                        start_time=None,
                        headers=None,
                        **request_parameters):
        """ This function is an alias of applications_v1 .
        Args:
            site_id(str): siteId query parameter. Assurance site UUID value (Cannot be submitted together
                with deviceId and clientMac) .
            device_id(str): deviceId query parameter. Assurance device UUID value (Cannot be submitted
                together with siteId and clientMac) .
            mac_address(str): macAddress query parameter. Client device's MAC address (Cannot be submitted
                together with siteId and deviceId) .
            start_time(int): startTime query parameter. Starting epoch time in milliseconds of time window .
            end_time(int): endTime query parameter. Ending epoch time in milliseconds of time window .
            application_health(str): applicationHealth query parameter. Application health category (POOR,
                FAIR, or GOOD.  Optionally use with siteId only) .
            offset(int): offset query parameter. The offset of the first application in the returned data
                (optionally used with siteId only) .
            limit(int): limit query parameter. The max number of application entries in returned data [1, 1000]
                (optionally used with siteId only) .
            application_name(str): applicationName query parameter. The name of the application to get
                information on .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of applications_v1 .
        """
        return self.applications_v1(
                    application_health=application_health,
                    application_name=application_name,
                    device_id=device_id,
                    end_time=end_time,
                    limit=limit,
                    mac_address=mac_address,
                    offset=offset,
                    site_id=site_id,
                    start_time=start_time,
                    headers=headers,
                    **request_parameters
        )



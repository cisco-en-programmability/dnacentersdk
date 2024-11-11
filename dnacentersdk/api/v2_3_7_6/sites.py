# -*- coding: utf-8 -*-
"""Cisco DNA Center Sites API wrapper.

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


class Sites(object):
    """Cisco DNA Center Sites API (version: 2.3.7.6).

    Wraps the DNA Center Sites
    API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new Sites
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the DNA Center service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(Sites, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def read_list_of_site_health_summaries_v1(self,
                                              attribute=None,
                                              end_time=None,
                                              id=None,
                                              limit=None,
                                              offset=None,
                                              order=None,
                                              site_hierarchy=None,
                                              site_hierarchy_id=None,
                                              site_type=None,
                                              sort_by=None,
                                              start_time=None,
                                              view=None,
                                              headers=None,
                                              **request_parameters):
        """Get a paginated list of site health summaries. Use the available query parameters to identify a subset of sites
        you want health summaries for. This API provides the latest health data from a given `endTime` If data
        is not ready for the provided endTime, the request will fail, and the error message will indicate the
        recommended endTime to use to retrieve a complete data set. This behavior may occur if the provided
        endTime=currentTime, since we are not a real time system. When `endTime` is not provided, the API
        returns the latest data. This API also provides issue data. The `startTime` query param can be used to
        specify the beginning point of time range to retrieve the active issue counts in. When this param is not
        provided, the default `startTime` will be 24 hours before endTime. Valid values for `sortBy` param in
        this API are limited to the attributes provided in the `site` view. Default sortBy is 'siteHierarchy' in
        order 'asc' (ascending). For detailed information about the usage of the API, please refer to the Open
        API specification document https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-siteHealthSummaries-1.0.3-resolved.yaml .

        Args:
            start_time(int): startTime query parameter. Start time from which API queries the data set related to
                the resource. It must be specified in UNIX epochtime in milliseconds. Value is
                inclusive. If `startTime` is not provided, API will default to current time. .
            end_time(int): endTime query parameter. End time to which API queries the data set related to the
                resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive. .
            limit(int): limit query parameter. Maximum number of records to return .
            offset(int): offset query parameter. Specifies the starting point within all records returned by the
                API. It's one based offset. The starting value is 1. .
            sort_by(str): sortBy query parameter. A field within the response to sort by. .
            order(str): order query parameter. The sort order of the field ascending or descending. .
            site_hierarchy(str): siteHierarchy query parameter. The full hierarchical breakdown of the site
                tree starting from Global site name and ending with the specific site name. The Root
                site is named "Global" (Ex. `Global/AreaName/BuildingName/FloorName`) This field
                supports wildcard asterisk (`*`) character search support. E.g. `*/San*, */San, /San*`
                Examples: `?siteHierarchy=Global/AreaName/BuildingName/FloorName` (single siteHierarchy
                requested) `?siteHierarchy=Global/AreaName/BuildingName/FloorName&siteHierarchy=Global/A
                reaName2/BuildingName2/FloorName2` (multiple siteHierarchies requested) .
            site_hierarchy_id(str): siteHierarchyId query parameter. The full hierarchy breakdown of the site
                tree in id form starting from Global site UUID and ending with the specific site UUID.
                (Ex. `globalUuid/areaUuid/buildingUuid/floorUuid`) This field supports wildcard asterisk
                (`*`) character search support. E.g. `*uuid*, *uuid, uuid*` Examples:
                `?siteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid `(single siteHierarchyId
                requested) `?siteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid&siteHierarchyId=
                globalUuid/areaUuid2/buildingUuid2/floorUuid2` (multiple siteHierarchyIds requested) .
            site_type(str): siteType query parameter. The type of the site. A site can be an area, building,
                or floor. Default when not provided will be `[floor,building,area]` Examples:
                `?siteType=area` (single siteType requested)
                `?siteType=area&siteType=building&siteType=floor` (multiple siteTypes requested) .
            id(str): id query parameter. The list of entity Uuids.
                (Ex."6bef213c-19ca-4170-8375-b694e251101c") Examples:
                id=6bef213c-19ca-4170-8375-b694e251101c (single entity uuid requested) id=6bef213c-19ca-
                4170-8375-b694e251101c&id=32219612-819e-4b5e-a96b-cf22aca13dd9&id=2541e9a7-b80d-4955-
                8aa2-79b233318ba0 (multiple entity uuid with '&' separator) .
            view(str): view query parameter. The specific summary view being requested. This is an optional
                parameter which can be passed to get one or more of the specific health data summaries
                associated with sites. ### Response data proviced by each view:   1. **site** [id,
                siteHierarchy, siteHierarchyId, siteType, latitude, longitude]   2. **network** [id,
                networkDeviceCount, networkDeviceGoodHealthCount,wirelessDeviceCount,
                wirelessDeviceGoodHealthCount, accessDeviceCount, accessDeviceGoodHealthCount,
                coreDeviceCount, coreDeviceGoodHealthCount, distributionDeviceCount,
                distributionDeviceGoodHealthCount, routerDeviceCount, routerDeviceGoodHealthCount,
                apDeviceCount, apDeviceGoodHealthCount, wlcDeviceCount, wlcDeviceGoodHealthCount,
                switchDeviceCount, switchDeviceGoodHealthCount, networkDeviceGoodHealthPercentage,
                accessDeviceGoodHealthPercentage, coreDeviceGoodHealthPercentage,
                distributionDeviceGoodHealthPercentage, routerDeviceGoodHealthPercentage,
                apDeviceGoodHealthPercentage, wlcDeviceGoodHealthPercentage,
                switchDeviceGoodHealthPercentage, wirelessDeviceGoodHealthPercentage]   3. **client**
                [id, clientCount, clientGoodHealthCount, wiredClientCount, wirelessClientCount,
                wiredClientGoodHealthCount, wirelessClientGoodHealthCount, clientGoodHealthPercentage,
                wiredClientGoodHealthPercentage, wirelessClientGoodHealthPercentage, clientDataUsage]
                4. **issue** [id, p1IssueCount, p2IssueCount, p3IssueCount, p4IssueCount, issueCount]
                When this query parameter is not added the default summaries are:
                **[site,client,network,issue]** Examples: view=client (single view requested)
                view=client&view=network&view=issue (multiple views requested) .
            attribute(str): attribute query parameter. Supported Attributes: [id, siteHierarchy,
                siteHierarchyId, siteType, latitude, longitude, networkDeviceCount,
                networkDeviceGoodHealthCount,wirelessDeviceCount, wirelessDeviceGoodHealthCount,
                accessDeviceCount, accessDeviceGoodHealthCount, coreDeviceCount,
                coreDeviceGoodHealthCount, distributionDeviceCount, distributionDeviceGoodHealthCount,
                routerDeviceCount, routerDeviceGoodHealthCount, apDeviceCount, apDeviceGoodHealthCount,
                wlcDeviceCount, wlcDeviceGoodHealthCount, switchDeviceCount,
                switchDeviceGoodHealthCount, networkDeviceGoodHealthPercentage,
                accessDeviceGoodHealthPercentage, coreDeviceGoodHealthPercentage,
                distributionDeviceGoodHealthPercentage, routerDeviceGoodHealthPercentage,
                apDeviceGoodHealthPercentage, wlcDeviceGoodHealthPercentage,
                switchDeviceGoodHealthPercentage, wirelessDeviceGoodHealthPercentage, clientCount,
                clientGoodHealthCount, wiredClientCount, wirelessClientCount,
                wiredClientGoodHealthCount, wirelessClientGoodHealthCount, clientGoodHealthPercentage,
                wiredClientGoodHealthPercentage, wirelessClientGoodHealthPercentage, clientDataUsage,
                p1IssueCount, p2IssueCount, p3IssueCount, p4IssueCount, issueCount] If length of
                attribute list is too long, please use 'view' param instead. Examples:
                attribute=siteHierarchy (single attribute requested)
                attribute=siteHierarchy&attribute=clientCount (multiple attributes requested) .
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
            https://developer.cisco.com/docs/dna-center/#!read-list-of-site-health-summaries
        """
        check_type(headers, dict)
        check_type(start_time, int)
        check_type(end_time, int)
        check_type(limit, int)
        check_type(offset, int)
        check_type(sort_by, str)
        check_type(order, str)
        check_type(site_hierarchy, str)
        check_type(site_hierarchy_id, str)
        check_type(site_type, str)
        check_type(id, str)
        check_type(view, str)
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
            'siteHierarchy':
                site_hierarchy,
            'siteHierarchyId':
                site_hierarchy_id,
            'siteType':
                site_type,
            'id':
                id,
            'view':
                view,
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

        e_url = ('/dna/data/api/v1/siteHealthSummaries')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_b40b4f6d558bfbebcf8fcbc4df56b_v2_3_7_6', json_data)

    def read_site_count_v1(self,
                           end_time=None,
                           id=None,
                           site_hierarchy=None,
                           site_hierarchy_id=None,
                           site_type=None,
                           headers=None,
                           **request_parameters):
        """Get a count of sites. Use the available query parameters to get the count of a subset of sites. This API
        provides the latest data from a given `endTime` If data is not ready for the provided endTime, the
        request will fail, and the error message will indicate the recommended endTime to use to retrieve a
        complete data set. This behavior may occur if the provided endTime=currentTime, since we are not a real
        time system. When `endTime` is not provided, the API returns the latest data. For detailed information
        about the usage of the API, please refer to the Open API specification document
        https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-siteHealthSummaries-1.0.3-resolved.yaml .

        Args:
            end_time(int): endTime query parameter. End time to which API queries the data set related to the
                resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive. .
            site_hierarchy(str): siteHierarchy query parameter. The full hierarchical breakdown of the site
                tree starting from Global site name and ending with the specific site name. The Root
                site is named "Global" (Ex. `Global/AreaName/BuildingName/FloorName`) This field
                supports wildcard asterisk (`*`) character search support. E.g. `*/San*, */San, /San*`
                Examples: `?siteHierarchy=Global/AreaName/BuildingName/FloorName` (single siteHierarchy
                requested) `?siteHierarchy=Global/AreaName/BuildingName/FloorName&siteHierarchy=Global/A
                reaName2/BuildingName2/FloorName2` (multiple siteHierarchies requested) .
            site_hierarchy_id(str): siteHierarchyId query parameter. The full hierarchy breakdown of the site
                tree in id form starting from Global site UUID and ending with the specific site UUID.
                (Ex. `globalUuid/areaUuid/buildingUuid/floorUuid`) This field supports wildcard asterisk
                (`*`) character search support. E.g. `*uuid*, *uuid, uuid*` Examples:
                `?siteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid `(single siteHierarchyId
                requested) `?siteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid&siteHierarchyId=
                globalUuid/areaUuid2/buildingUuid2/floorUuid2` (multiple siteHierarchyIds requested) .
            site_type(str): siteType query parameter. The type of the site. A site can be an area, building,
                or floor. Default when not provided will be `[floor,building,area]` Examples:
                `?siteType=area` (single siteType requested)
                `?siteType=area&siteType=building&siteType=floor` (multiple siteTypes requested) .
            id(str): id query parameter. The list of entity Uuids.
                (Ex."6bef213c-19ca-4170-8375-b694e251101c") Examples:
                id=6bef213c-19ca-4170-8375-b694e251101c (single entity uuid requested) id=6bef213c-19ca-
                4170-8375-b694e251101c&id=32219612-819e-4b5e-a96b-cf22aca13dd9&id=2541e9a7-b80d-4955-
                8aa2-79b233318ba0 (multiple entity uuid with '&' separator) .
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
            https://developer.cisco.com/docs/dna-center/#!read-site-count
        """
        check_type(headers, dict)
        check_type(end_time, int)
        check_type(site_hierarchy, str)
        check_type(site_hierarchy_id, str)
        check_type(site_type, str)
        check_type(id, str)
        if headers is not None:
            if 'X-CALLER-ID' in headers:
                check_type(headers.get('X-CALLER-ID'),
                           str)
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'endTime':
                end_time,
            'siteHierarchy':
                site_hierarchy,
            'siteHierarchyId':
                site_hierarchy_id,
            'siteType':
                site_type,
            'id':
                id,
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

        e_url = ('/dna/data/api/v1/siteHealthSummaries/count')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_e67558dd99925a0385f5f870bbb8f634_v2_3_7_6', json_data)

    def read_an_aggregated_summary_of_site_health_data_v1(self,
                                                          attribute=None,
                                                          end_time=None,
                                                          id=None,
                                                          site_hierarchy=None,
                                                          site_hierarchy_id=None,
                                                          site_type=None,
                                                          start_time=None,
                                                          view=None,
                                                          headers=None,
                                                          **request_parameters):
        """Get an aggregated summary of all site health or use the query params to get an aggregated summary of health for
        a subset of sites. This API provides the latest health data from a given `endTime` If data is not ready
        for the provided endTime, the request will fail, and the error message will indicate the recommended
        endTime to use to retrieve a complete data set. This behavior may occur if the provided
        endTime=currentTime, since we are not a real time system. When `endTime` is not provided, the API
        returns the latest data. This API also provides issue data. The `startTime` query param can be used to
        specify the beginning point of time range to retrieve the active issue counts in. When this param is not
        provided, the default `startTime` will be 24 hours before endTime. Aggregated response data will NOT
        have unique identifier data populated. List of unique identifier data: [`id`, `siteHierarchy`,
        `siteHierarchyId`, `siteType`, `latitude`, `longitude`]. For detailed information about the usage of the
        API, please refer to the Open API specification document https://github.com/cisco-en-
        programmability/catalyst-center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-
        siteHealthSummaries-1.0.3-resolved.yaml .

        Args:
            start_time(int): startTime query parameter. Start time from which API queries the data set related to
                the resource. It must be specified in UNIX epochtime in milliseconds. Value is
                inclusive. If `startTime` is not provided, API will default to current time. .
            end_time(int): endTime query parameter. End time to which API queries the data set related to the
                resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive. .
            site_hierarchy(str): siteHierarchy query parameter. The full hierarchical breakdown of the site
                tree starting from Global site name and ending with the specific site name. The Root
                site is named "Global" (Ex. `Global/AreaName/BuildingName/FloorName`) This field
                supports wildcard asterisk (`*`) character search support. E.g. `*/San*, */San, /San*`
                Examples: `?siteHierarchy=Global/AreaName/BuildingName/FloorName` (single siteHierarchy
                requested) `?siteHierarchy=Global/AreaName/BuildingName/FloorName&siteHierarchy=Global/A
                reaName2/BuildingName2/FloorName2` (multiple siteHierarchies requested) .
            site_hierarchy_id(str): siteHierarchyId query parameter. The full hierarchy breakdown of the site
                tree in id form starting from Global site UUID and ending with the specific site UUID.
                (Ex. `globalUuid/areaUuid/buildingUuid/floorUuid`) This field supports wildcard asterisk
                (`*`) character search support. E.g. `*uuid*, *uuid, uuid*` Examples:
                `?siteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid `(single siteHierarchyId
                requested) `?siteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid&siteHierarchyId=
                globalUuid/areaUuid2/buildingUuid2/floorUuid2` (multiple siteHierarchyIds requested) .
            site_type(str): siteType query parameter. The type of the site. A site can be an area, building,
                or floor. Default when not provided will be `[floor,building,area]` Examples:
                `?siteType=area` (single siteType requested)
                `?siteType=area&siteType=building&siteType=floor` (multiple siteTypes requested) .
            id(str): id query parameter. The list of entity Uuids.
                (Ex."6bef213c-19ca-4170-8375-b694e251101c") Examples:
                id=6bef213c-19ca-4170-8375-b694e251101c (single entity uuid requested) id=6bef213c-19ca-
                4170-8375-b694e251101c&id=32219612-819e-4b5e-a96b-cf22aca13dd9&id=2541e9a7-b80d-4955-
                8aa2-79b233318ba0 (multiple entity uuid with '&' separator) .
            view(str): view query parameter. The specific summary view being requested. This is an optional
                parameter which can be passed to get one or more of the specific health data summaries
                associated with sites. ### Response data proviced by each view:   1. **site** [id,
                siteHierarchy, siteHierarchyId, siteType, latitude, longitude]   2. **network** [id,
                networkDeviceCount, networkDeviceGoodHealthCount,wirelessDeviceCount,
                wirelessDeviceGoodHealthCount, accessDeviceCount, accessDeviceGoodHealthCount,
                coreDeviceCount, coreDeviceGoodHealthCount, distributionDeviceCount,
                distributionDeviceGoodHealthCount, routerDeviceCount, routerDeviceGoodHealthCount,
                apDeviceCount, apDeviceGoodHealthCount, wlcDeviceCount, wlcDeviceGoodHealthCount,
                switchDeviceCount, switchDeviceGoodHealthCount, networkDeviceGoodHealthPercentage,
                accessDeviceGoodHealthPercentage, coreDeviceGoodHealthPercentage,
                distributionDeviceGoodHealthPercentage, routerDeviceGoodHealthPercentage,
                apDeviceGoodHealthPercentage, wlcDeviceGoodHealthPercentage,
                switchDeviceGoodHealthPercentage, wirelessDeviceGoodHealthPercentage]   3. **client**
                [id, clientCount, clientGoodHealthCount, wiredClientCount, wirelessClientCount,
                wiredClientGoodHealthCount, wirelessClientGoodHealthCount, clientGoodHealthPercentage,
                wiredClientGoodHealthPercentage, wirelessClientGoodHealthPercentage, clientDataUsage]
                4. **issue** [id, p1IssueCount, p2IssueCount, p3IssueCount, p4IssueCount, issueCount]
                When this query parameter is not added the default summaries are:
                **[site,client,network,issue]** Examples: view=client (single view requested)
                view=client&view=network&view=issue (multiple views requested) .
            attribute(str): attribute query parameter. Supported Attributes: [id, siteHierarchy,
                siteHierarchyId, siteType, latitude, longitude, networkDeviceCount,
                networkDeviceGoodHealthCount,wirelessDeviceCount, wirelessDeviceGoodHealthCount,
                accessDeviceCount, accessDeviceGoodHealthCount, coreDeviceCount,
                coreDeviceGoodHealthCount, distributionDeviceCount, distributionDeviceGoodHealthCount,
                routerDeviceCount, routerDeviceGoodHealthCount, apDeviceCount, apDeviceGoodHealthCount,
                wlcDeviceCount, wlcDeviceGoodHealthCount, switchDeviceCount,
                switchDeviceGoodHealthCount, networkDeviceGoodHealthPercentage,
                accessDeviceGoodHealthPercentage, coreDeviceGoodHealthPercentage,
                distributionDeviceGoodHealthPercentage, routerDeviceGoodHealthPercentage,
                apDeviceGoodHealthPercentage, wlcDeviceGoodHealthPercentage,
                switchDeviceGoodHealthPercentage, wirelessDeviceGoodHealthPercentage, clientCount,
                clientGoodHealthCount, wiredClientCount, wirelessClientCount,
                wiredClientGoodHealthCount, wirelessClientGoodHealthCount, clientGoodHealthPercentage,
                wiredClientGoodHealthPercentage, wirelessClientGoodHealthPercentage, clientDataUsage,
                p1IssueCount, p2IssueCount, p3IssueCount, p4IssueCount, issueCount] If length of
                attribute list is too long, please use 'view' param instead. Examples:
                attribute=siteHierarchy (single attribute requested)
                attribute=siteHierarchy&attribute=clientCount (multiple attributes requested) .
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
            https://developer.cisco.com/docs/dna-center/#!read-an-aggregated-summary-of-site-health-data
        """
        check_type(headers, dict)
        check_type(start_time, int)
        check_type(end_time, int)
        check_type(site_hierarchy, str)
        check_type(site_hierarchy_id, str)
        check_type(site_type, str)
        check_type(id, str)
        check_type(view, str)
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
            'siteHierarchy':
                site_hierarchy,
            'siteHierarchyId':
                site_hierarchy_id,
            'siteType':
                site_type,
            'id':
                id,
            'view':
                view,
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

        e_url = ('/dna/data/api/v1/siteHealthSummaries/summaryAnalytics')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_fc80b3e12ee9577a8e7fa5d4cd84e8fc_v2_3_7_6', json_data)

    def query_an_aggregated_summary_of_site_health_data_v1(self,
                                                           attributes=None,
                                                           endTime=None,
                                                           id=None,
                                                           site_hierarchy=None,
                                                           site_hierarchy_id=None,
                                                           site_type=None,
                                                           startTime=None,
                                                           views=None,
                                                           headers=None,
                                                           payload=None,
                                                           active_validation=True,
                                                           **request_parameters):
        """Query an aggregated summary of all site health This API provides the latest health data from a given `endTime`
        If data is not ready for the provided endTime, the request will fail, and the error message will
        indicate the recommended endTime to use to retrieve a complete data set. This behavior may occur if the
        provided endTime=currentTime, since we are not a real time system. When `endTime` is not provided, the
        API returns the latest data. This API also provides issue data. The `startTime` query param can be used
        to specify the beginning point of time range to retrieve the active issue counts in. When this param is
        not provided, the default `startTime` will be 24 hours before endTime.   Aggregated response data will
        NOT have unique identifier data populated.   List of unique identifier data: [`id`, `siteHierarchy`,
        `siteHierarchyId`, `siteType`, `latitude`, `longitude`] Please refer to the 'API Support Documentation'
        section to understand which fields are supported. For detailed information about the usage of the API,
        please refer to the Open API specification document https://github.com/cisco-en-
        programmability/catalyst-center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-
        siteHealthSummaries-1.0.3-resolved.yaml .

        Args:
            attributes(list): Sites's Attributes (list of strings).
            endTime(integer): Sites's End Time.
            startTime(integer): Sites's Start Time.
            views(list): Sites's Views (list of strings).
            site_hierarchy(str): siteHierarchy query parameter. The full hierarchical breakdown of the site
                tree starting from Global site name and ending with the specific site name. The Root
                site is named "Global" (Ex. `Global/AreaName/BuildingName/FloorName`) This field
                supports wildcard asterisk (`*`) character search support. E.g. `*/San*, */San, /San*`
                Examples: `?siteHierarchy=Global/AreaName/BuildingName/FloorName` (single siteHierarchy
                requested) `?siteHierarchy=Global/AreaName/BuildingName/FloorName&siteHierarchy=Global/A
                reaName2/BuildingName2/FloorName2` (multiple siteHierarchies requested) .
            site_hierarchy_id(str): siteHierarchyId query parameter. The full hierarchy breakdown of the site
                tree in id form starting from Global site UUID and ending with the specific site UUID.
                (Ex. `globalUuid/areaUuid/buildingUuid/floorUuid`) This field supports wildcard asterisk
                (`*`) character search support. E.g. `*uuid*, *uuid, uuid*` Examples:
                `?siteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid `(single siteHierarchyId
                requested) `?siteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid&siteHierarchyId=
                globalUuid/areaUuid2/buildingUuid2/floorUuid2` (multiple siteHierarchyIds requested) .
            site_type(str): siteType query parameter. The type of the site. A site can be an area, building,
                or floor. Default when not provided will be `[floor,building,area]` Examples:
                `?siteType=area` (single siteType requested)
                `?siteType=area&siteType=building&siteType=floor` (multiple siteTypes requested) .
            id(str): id query parameter. The list of entity Uuids.
                (Ex."6bef213c-19ca-4170-8375-b694e251101c") Examples:
                id=6bef213c-19ca-4170-8375-b694e251101c (single entity uuid requested) id=6bef213c-19ca-
                4170-8375-b694e251101c&id=32219612-819e-4b5e-a96b-cf22aca13dd9&id=2541e9a7-b80d-4955-
                8aa2-79b233318ba0 (multiple entity uuid with '&' separator) .
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
            https://developer.cisco.com/docs/dna-center/#!query-an-aggregated-summary-of-site-health-data
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(site_hierarchy, str)
        check_type(site_hierarchy_id, str)
        check_type(site_type, str)
        check_type(id, str)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'siteHierarchy':
                site_hierarchy,
            'siteHierarchyId':
                site_hierarchy_id,
            'siteType':
                site_type,
            'id':
                id,
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
            'views':
                views,
            'attributes':
                attributes,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_bec2dde673c5b2f940d0474fed32af6_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/data/api/v1/siteHealthSummaries/summaryAnalytics')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_bec2dde673c5b2f940d0474fed32af6_v2_3_7_6', json_data)

    def read_site_health_summary_data_by_site_id_v1(self,
                                                    id,
                                                    attribute=None,
                                                    end_time=None,
                                                    start_time=None,
                                                    view=None,
                                                    headers=None,
                                                    **request_parameters):
        """Get a health summary for a specific site by providing the unique site id in the url path. This API provides the
        latest health data from a given `endTime` If data is not ready for the provided endTime, the request
        will fail, and the error message will indicate the recommended endTime to use to retrieve a complete
        data set. This behavior may occur if the provided endTime=currentTime, since we are not a real time
        system. When `endTime` is not provided, the API returns the latest data. This API also provides issue
        data. The `startTime` query param can be used to specify the beginning point of time range to retrieve
        the active issue counts in. When this param is not provided, the default `startTime` will be 24 hours
        before endTime. For detailed information about the usage of the API, please refer to the Open API
        specification document https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-siteHealthSummaries-1.0.3-resolved.yaml .

        Args:
            id(str): id path parameter. unique site uuid .
            start_time(int): startTime query parameter. Start time from which API queries the data set related to
                the resource. It must be specified in UNIX epochtime in milliseconds. Value is
                inclusive. If `startTime` is not provided, API will default to current time. .
            end_time(int): endTime query parameter. End time to which API queries the data set related to the
                resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive. .
            view(str): view query parameter. The specific summary view being requested. This is an optional
                parameter which can be passed to get one or more of the specific health data summaries
                associated with sites. ### Response data proviced by each view:   1. **site** [id,
                siteHierarchy, siteHierarchyId, siteType, latitude, longitude]   2. **network** [id,
                networkDeviceCount, networkDeviceGoodHealthCount,wirelessDeviceCount,
                wirelessDeviceGoodHealthCount, accessDeviceCount, accessDeviceGoodHealthCount,
                coreDeviceCount, coreDeviceGoodHealthCount, distributionDeviceCount,
                distributionDeviceGoodHealthCount, routerDeviceCount, routerDeviceGoodHealthCount,
                apDeviceCount, apDeviceGoodHealthCount, wlcDeviceCount, wlcDeviceGoodHealthCount,
                switchDeviceCount, switchDeviceGoodHealthCount, networkDeviceGoodHealthPercentage,
                accessDeviceGoodHealthPercentage, coreDeviceGoodHealthPercentage,
                distributionDeviceGoodHealthPercentage, routerDeviceGoodHealthPercentage,
                apDeviceGoodHealthPercentage, wlcDeviceGoodHealthPercentage,
                switchDeviceGoodHealthPercentage, wirelessDeviceGoodHealthPercentage]   3. **client**
                [id, clientCount, clientGoodHealthCount, wiredClientCount, wirelessClientCount,
                wiredClientGoodHealthCount, wirelessClientGoodHealthCount, clientGoodHealthPercentage,
                wiredClientGoodHealthPercentage, wirelessClientGoodHealthPercentage, clientDataUsage]
                4. **issue** [id, p1IssueCount, p2IssueCount, p3IssueCount, p4IssueCount, issueCount]
                When this query parameter is not added the default summaries are:
                **[site,client,network,issue]** Examples: view=client (single view requested)
                view=client&view=network&view=issue (multiple views requested) .
            attribute(str): attribute query parameter. Supported Attributes: [id, siteHierarchy,
                siteHierarchyId, siteType, latitude, longitude, networkDeviceCount,
                networkDeviceGoodHealthCount,wirelessDeviceCount, wirelessDeviceGoodHealthCount,
                accessDeviceCount, accessDeviceGoodHealthCount, coreDeviceCount,
                coreDeviceGoodHealthCount, distributionDeviceCount, distributionDeviceGoodHealthCount,
                routerDeviceCount, routerDeviceGoodHealthCount, apDeviceCount, apDeviceGoodHealthCount,
                wlcDeviceCount, wlcDeviceGoodHealthCount, switchDeviceCount,
                switchDeviceGoodHealthCount, networkDeviceGoodHealthPercentage,
                accessDeviceGoodHealthPercentage, coreDeviceGoodHealthPercentage,
                distributionDeviceGoodHealthPercentage, routerDeviceGoodHealthPercentage,
                apDeviceGoodHealthPercentage, wlcDeviceGoodHealthPercentage,
                switchDeviceGoodHealthPercentage, wirelessDeviceGoodHealthPercentage, clientCount,
                clientGoodHealthCount, wiredClientCount, wirelessClientCount,
                wiredClientGoodHealthCount, wirelessClientGoodHealthCount, clientGoodHealthPercentage,
                wiredClientGoodHealthPercentage, wirelessClientGoodHealthPercentage, clientDataUsage,
                p1IssueCount, p2IssueCount, p3IssueCount, p4IssueCount, issueCount] If length of
                attribute list is too long, please use 'view' param instead. Examples:
                attribute=siteHierarchy (single attribute requested)
                attribute=siteHierarchy&attribute=clientCount (multiple attributes requested) .
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
            https://developer.cisco.com/docs/dna-center/#!read-site-health-summary-data-by-site-id
        """
        check_type(headers, dict)
        check_type(start_time, int)
        check_type(end_time, int)
        check_type(view, str)
        check_type(attribute, str)
        check_type(id, str,
                   may_be_none=False)
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
            'view':
                view,
            'attribute':
                attribute,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'id': id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/data/api/v1/siteHealthSummaries/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_f214555abaa6a30cdbcc32e713_v2_3_7_6', json_data)

    def assign_devices_to_site_v1(self,
                                  site_id,
                                  device=None,
                                  headers=None,
                                  payload=None,
                                  active_validation=True,
                                  **request_parameters):
        """Assigns unassigned devices to a site. This API does not move assigned devices to other sites. .

        Args:
            device(list): Sites's device (list of objects).
            site_id(str): siteId path parameter. Site Id where device(s) needs to be assigned .
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
            https://developer.cisco.com/docs/dna-center/#!assign-devices-to-site
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(site_id, str,
                   may_be_none=False)
        if headers is not None:
            if '__runsync' in headers:
                check_type(headers.get('__runsync'),
                           bool, may_be_none=False)
            if '__timeout' in headers:
                check_type(headers.get('__timeout'),
                           int)
            if '__persistbapioutput' in headers:
                check_type(headers.get('__persistbapioutput'),
                           bool, may_be_none=False)
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'siteId': site_id,
        }
        _payload = {
            'device':
                device,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_a544e27e18e5412af3b68d915c8ca50_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/assign-device-to-site/{siteId}/device')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_a544e27e18e5412af3b68d915c8ca50_v2_3_7_6', json_data)

    def export_map_archive_v1(self,
                              site_hierarchy_uuid,
                              headers=None,
                              payload=None,
                              active_validation=True,
                              **request_parameters):
        """Allows exporting a Map archive in an XML interchange format along with the associated images.  .

        Args:
            site_hierarchy_uuid(str): siteHierarchyUuid path parameter. The site hierarchy element UUID to
                export, all child elements starting at this hierarchy element will be included. Limited
                to a hierarchy that contains 500 or fewer maps. .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload((list, dict)): A JSON serializable Python object to send in the
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
            https://developer.cisco.com/docs/dna-center/#!export-map-archive
        """
        check_type(headers, dict)
        check_type(payload, (list, dict))
        check_type(site_hierarchy_uuid, str,
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
            'siteHierarchyUuid': site_hierarchy_uuid,
        }
        _payload = payload or {}
        if active_validation:
            self._request_validator('jsd_c937494318f952ba92eaeb82b144c338_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/maps/export/{siteHierarchyUuid}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_c937494318f952ba92eaeb82b144c338_v2_3_7_6', json_data)

    def import_map_archive_start_import_v1(self,
                                           headers=None,
                                           **request_parameters):
        """Initiates a map archive import of a tar.gz file.  The archive must consist of one xmlDir/MapsImportExport.xml
        map descriptor file, and 1 or more images for the map areas nested under /images folder. .

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
            ApiError: If the DNA Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!import-map-archive-start-import
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

        e_url = ('/dna/intent/api/v1/maps/import/start')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params)

        return self._object_factory('bpm_ea81890f92553aaed79952ab7ab363_v2_3_7_6', json_data)

    def import_map_archive_cancel_an_import_v1(self,
                                               import_context_uuid,
                                               headers=None,
                                               **request_parameters):
        """Cancels a previously initatied import, allowing the system to cleanup cached resources about that import data,
        and ensures the import cannot accidentally be performed / approved at a later time. .

        Args:
            import_context_uuid(str): importContextUuid path parameter. The unique import context UUID given
                by a previous call to Start Import API .
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
            https://developer.cisco.com/docs/dna-center/#!import-map-archive-cancel-an-import
        """
        check_type(headers, dict)
        check_type(import_context_uuid, str,
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
            'importContextUuid': import_context_uuid,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/maps/import/{importContextUuid}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(endpoint_full_url, params=_params,
                                             headers=_headers)
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_a59853e8a3462db736556ab4_v2_3_7_6', json_data)

    def import_map_archive_perform_import_v1(self,
                                             import_context_uuid,
                                             headers=None,
                                             **request_parameters):
        """For a previously initatied import, approves the import to be performed, accepting that data loss may occur.  A
        Map import will fully replace existing Maps data for the site(s) defined in the archive. The Map Archive
        Import Status API /maps/import/${contextUuid}/status should always be checked to validate the pre-import
        validation output prior to performing the import. .

        Args:
            import_context_uuid(str): importContextUuid path parameter. The unique import context UUID given
                by a previous call of Start Import API .
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
            https://developer.cisco.com/docs/dna-center/#!import-map-archive-perform-import
        """
        check_type(headers, dict)
        check_type(import_context_uuid, str,
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
            'importContextUuid': import_context_uuid,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/maps/import/{importContextUuid}/perfo'
                 + 'rm')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params)

        return self._object_factory('bpm_df05fb7a09595d0b9f6bc46b24275927_v2_3_7_6', json_data)

    def import_map_archive_import_status_v1(self,
                                            import_context_uuid,
                                            headers=None,
                                            **request_parameters):
        """Gets the status of a map archive import operation. For a map archive import that has just been initiated, will
        provide the result of validation of the archive and a pre-import preview of what will be performed if
        the import is performed.  Once an import is requested to be performed, this API will give the status of
        the import and upon completion a post-import summary of what was performed by the operation. .

        Args:
            import_context_uuid(str): importContextUuid path parameter. The unique import context UUID given
                by a previous and recent call to maps/import/start API .
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
            https://developer.cisco.com/docs/dna-center/#!import-map-archive-import-status
        """
        check_type(headers, dict)
        check_type(import_context_uuid, str,
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
            'importContextUuid': import_context_uuid,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/maps/import/{importContextUuid}/statu'
                 + 's')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_c04c790688e4566c9f5eaa52b8fe39c8_v2_3_7_6', json_data)

    def maps_supported_access_points_v1(self,
                                        headers=None,
                                        **request_parameters):
        """Gets the list of supported access point types as well as valid antenna pattern names that can be used for each.
        .

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
            ApiError: If the DNA Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!maps-supported-access-points
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

        e_url = ('/dna/intent/api/v1/maps/supported-access-points')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_a5e16b065e3534c8894e52d52540f99_v2_3_7_6', json_data)

    def get_membership_v1(self,
                          site_id,
                          device_family=None,
                          limit=None,
                          offset=None,
                          serial_number=None,
                          headers=None,
                          **request_parameters):
        """Getting the site children details and device details. .

        Args:
            site_id(str): siteId path parameter. Site id to retrieve device associated with the site. .
            offset(int): offset query parameter. offset/starting row .
            limit(int): limit query parameter. Number of sites to be retrieved .
            device_family(str): deviceFamily query parameter. Device family name  .
            serial_number(str): serialNumber query parameter. Device serial number .
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
            https://developer.cisco.com/docs/dna-center/#!get-membership
        """
        check_type(headers, dict)
        check_type(offset, int)
        check_type(limit, int)
        check_type(device_family, str)
        check_type(serial_number, str)
        check_type(site_id, str,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'offset':
                offset,
            'limit':
                limit,
            'deviceFamily':
                device_family,
            'serialNumber':
                serial_number,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'siteId': site_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/membership/{siteId}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_ca11e0b5f8d91395e2462a9cfdc_v2_3_7_6', json_data)

    def create_site_v1(self,
                       site=None,
                       type=None,
                       headers=None,
                       payload=None,
                       active_validation=True,
                       **request_parameters):
        """Creates site with area/building/floor with specified hierarchy. .

        Args:
            site(object): Sites's site.
            type(string): Sites's Type of site to create (eg: area, building, floor) . Available values are 'area',
                'building' and 'floor'.
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
            https://developer.cisco.com/docs/dna-center/#!create-site
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if '__runsync' in headers:
                check_type(headers.get('__runsync'),
                           bool, may_be_none=False)
            if '__timeout' in headers:
                check_type(headers.get('__timeout'),
                           int)
            if '__persistbapioutput' in headers:
                check_type(headers.get('__persistbapioutput'),
                           bool, may_be_none=False)
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
            'type':
                type,
            'site':
                site,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_bce8e6b307ce52dd8f5546fbd78e05ee_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/site')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_bce8e6b307ce52dd8f5546fbd78e05ee_v2_3_7_6', json_data)

    def get_site_v1(self,
                    limit=None,
                    name=None,
                    offset=None,
                    site_id=None,
                    type=None,
                    headers=None,
                    **request_parameters):
        """Get site(s) by site-name-hierarchy or siteId or type. List all sites if these parameters are not given as an
        input. .

        Args:
            name(str): name query parameter. Site name hierarchy (E.g Global/USA/CA) .
            site_id(str): siteId query parameter. Site Id .
            type(str): type query parameter. Site type (Ex: area, building, floor) .
            offset(int): offset query parameter. Offset/starting index for pagination. Indexed from 1. .
            limit(int): limit query parameter. Number of sites to be listed .
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
            https://developer.cisco.com/docs/dna-center/#!get-site
        """
        check_type(headers, dict)
        check_type(name, str)
        check_type(site_id, str)
        check_type(type, str)
        check_type(offset, int)
        check_type(limit, int)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'name':
                name,
            'siteId':
                site_id,
            'type':
                type,
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

        e_url = ('/dna/intent/api/v1/site')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_dbdd6074bedc59b9a3edd6477897d659_v2_3_7_6', json_data)

    def get_site_health_v1(self,
                           limit=None,
                           offset=None,
                           site_type=None,
                           timestamp=None,
                           headers=None,
                           **request_parameters):
        """Returns Overall Health information for all sites .

        Args:
            site_type(str): siteType query parameter. site type: AREA or BUILDING (case insensitive) .
            offset(int): offset query parameter. Offset of the first returned data set entry (Multiple of 'limit' +
                1) .
            limit(int): limit query parameter. Max number of data entries in the returned data set [1,50].  Default
                is 25 .
            timestamp(int): timestamp query parameter. Epoch time(in milliseconds) when the Site Hierarchy data is
                required .
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
            https://developer.cisco.com/docs/dna-center/#!get-site-health
        """
        check_type(headers, dict)
        check_type(site_type, str)
        check_type(offset, int)
        check_type(limit, int)
        check_type(timestamp, int)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'siteType':
                site_type,
            'offset':
                offset,
            'limit':
                limit,
            'timestamp':
                timestamp,
        }

        if _params['timestamp'] is None:
            _params['timestamp'] = ''
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/site-health')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_ae4b592f66035f24b55028f79c1b7290_v2_3_7_6', json_data)

    def get_devices_that_are_assigned_to_a_site_v1(self,
                                                   id,
                                                   member_type,
                                                   level=None,
                                                   limit=None,
                                                   offset=None,
                                                   headers=None,
                                                   **request_parameters):
        """API to get devices that are assigned to a site. .

        Args:
            id(str): id path parameter. Site Id .
            offset(str): offset query parameter. Offset/starting index for pagination .
            limit(str): limit query parameter. Number of devices to be listed. Default and max supported
                value is 500 .
            member_type(str): memberType query parameter. Member type (This API only supports the
                'networkdevice' type) .
            level(str): level query parameter. Depth of site hierarchy to be considered to list the devices.
                If the provided value is -1, devices for all child sites will be listed. .
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
            https://developer.cisco.com/docs/dna-center/#!get-devices-that-are-assigned-to-a-site
        """
        check_type(headers, dict)
        check_type(offset, str)
        check_type(limit, str)
        check_type(member_type, str,
                   may_be_none=False)
        check_type(level, str)
        check_type(id, str,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'offset':
                offset,
            'limit':
                limit,
            'memberType':
                member_type,
            'level':
                level,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'id': id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/site-member/{id}/member')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_cfabe762b2af55f282076fe2a14b6792_v2_3_7_6', json_data)

    def get_site_count_v1(self,
                          site_id=None,
                          headers=None,
                          **request_parameters):
        """Get the site count of the specified site's sub-hierarchy (inclusive of the provided site) .

        Args:
            site_id(str): siteId query parameter. Site instance UUID .
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
            https://developer.cisco.com/docs/dna-center/#!get-site-count
        """
        check_type(headers, dict)
        check_type(site_id, str)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'siteId':
                site_id,
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

        e_url = ('/dna/intent/api/v1/site/count')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_e7a025fbe2c452fc82eedd5c50104aba_v2_3_7_6', json_data)

    def update_site_v1(self,
                       site_id,
                       site=None,
                       type=None,
                       headers=None,
                       payload=None,
                       active_validation=True,
                       **request_parameters):
        """Update site area/building/floor with specified hierarchy and new values .

        Args:
            site(object): Sites's site.
            type(string): Sites's Site type . Available values are 'area', 'building' and 'floor'.
            site_id(str): siteId path parameter. Site id to which site details to be updated. .
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
            https://developer.cisco.com/docs/dna-center/#!update-site
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(site_id, str,
                   may_be_none=False)
        if headers is not None:
            if '__runsync' in headers:
                check_type(headers.get('__runsync'),
                           bool)
            if '__timeout' in headers:
                check_type(headers.get('__timeout'),
                           int)
            if '__persistbapioutput' in headers:
                check_type(headers.get('__persistbapioutput'),
                           bool, may_be_none=False)
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'siteId': site_id,
        }
        _payload = {
            'type':
                type,
            'site':
                site,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_df9908ad265e83ab77d73803925678_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/site/{siteId}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload,
                                          headers=_headers)
        else:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload)

        return self._object_factory('bpm_df9908ad265e83ab77d73803925678_v2_3_7_6', json_data)

    def delete_site_v1(self,
                       site_id,
                       headers=None,
                       **request_parameters):
        """Delete site with area/building/floor by siteId. .

        Args:
            site_id(str): siteId path parameter. Site id to which site details to be deleted. .
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
            https://developer.cisco.com/docs/dna-center/#!delete-site
        """
        check_type(headers, dict)
        check_type(site_id, str,
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
            'siteId': site_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/site/{siteId}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(endpoint_full_url, params=_params,
                                             headers=_headers)
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_ba5567f03dea5b6891957dd410319e3f_v2_3_7_6', json_data)

    def get_site_v2(self,
                    group_name_hierarchy=None,
                    id=None,
                    limit=None,
                    offset=None,
                    type=None,
                    headers=None,
                    **request_parameters):
        """API to get site(s) by site-name-hierarchy or siteId or type. List all sites if these parameters  are not given
        as an input. .

        Args:
            group_name_hierarchy(str): groupNameHierarchy query parameter. Site name hierarchy (E.g.
                Global/USA/CA) .
            id(str): id query parameter. Site Id .
            type(str): type query parameter. Site type (Acceptable values: area, building, floor) .
            offset(str): offset query parameter. Offset/starting index for pagination .
            limit(str): limit query parameter. Number of sites to be listed. Default and max supported value
                is 500 .
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
            https://developer.cisco.com/docs/dna-center/#!get-site-v2
        """
        check_type(headers, dict)
        check_type(group_name_hierarchy, str)
        check_type(id, str)
        check_type(type, str)
        check_type(offset, str)
        check_type(limit, str)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'groupNameHierarchy':
                group_name_hierarchy,
            'id':
                id,
            'type':
                type,
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

        e_url = ('/dna/intent/api/v2/site')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_c5e65cce2954fdb7177ac0a8e0b76f_v2_3_7_6', json_data)

    def get_site_count_v2(self,
                          id=None,
                          headers=None,
                          **request_parameters):
        """Get the site count of the specified site's sub-hierarchy (inclusive of the provided site) .

        Args:
            id(str): id query parameter. Site instance UUID .
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
            https://developer.cisco.com/docs/dna-center/#!get-site-count-v2
        """
        check_type(headers, dict)
        check_type(id, str)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'id':
                id,
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

        e_url = ('/dna/intent/api/v2/site/count')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_b10ff66e5568ebe6d41faeeabda22_v2_3_7_6', json_data)

                
    
    # Alias Function
    def get_site_health(self,
                           limit=None,
                           offset=None,
                           site_type=None,
                           timestamp=None,
                           headers=None,
                           **request_parameters):
        """ This function is an alias of get_site_health_v1 .
        Args:
            site_type(basestring): siteType query parameter. site type: AREA or BUILDING (case insensitive) .
            offset(int): offset query parameter. Offset of the first returned data set entry (Multiple of 'limit' +
                1) .
            limit(int): limit query parameter. Max number of data entries in the returned data set [1,50].  Default
                is 25 .
            timestamp(int): timestamp query parameter. Epoch time(in milliseconds) when the Site Hierarchy data is
                required .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_site_health_v1 .
        """ 
        return self.get_site_health_v1(
                    limit=limit,
                    offset=offset,
                    site_type=site_type,
                    timestamp=timestamp,
                    headers=headers,
                    **request_parameters
        )
                
    
    # Alias Function
    def create_site(self,
                       site=None,
                       type=None,
                       headers=None,
                       payload=None,
                       active_validation=True,
                       **request_parameters):
        """ This function is an alias of create_site_v1 .
        Args:
            site(object): Sites's site.
            type(string): Sites's Type of site to create (eg: area, building, floor) . Available values are 'area',
                'building' and 'floor'.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of create_site_v1 .
        """ 
        return self.create_site_v1(
                    site=site,
                    type=type,
                    headers=headers,
                    payload=payload,
                    active_validation=active_validation,
                    **request_parameters
        )
                
    
    # Alias Function
    def import_map_archive_perform_import(self,
                                             import_context_uuid,
                                             headers=None,
                                             **request_parameters):
        """ This function is an alias of import_map_archive_perform_import_v1 .
        Args:
            import_context_uuid(basestring): importContextUuid path parameter. The unique import context UUID given
                by a previous call of Start Import API .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of import_map_archive_perform_import_v1 .
        """ 
        return self.import_map_archive_perform_import_v1(
                    import_context_uuid=import_context_uuid,
                    headers=headers,
                    **request_parameters
        )
                
    
    # Alias Function
    def import_map_archive_import_status(self,
                                            import_context_uuid,
                                            headers=None,
                                            **request_parameters):
        """ This function is an alias of import_map_archive_import_status_v1 .
        Args:
            import_context_uuid(basestring): importContextUuid path parameter. The unique import context UUID given
                by a previous and recent call to maps/import/start API .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of import_map_archive_import_status_v1 .
        """ 
        return self.import_map_archive_import_status_v1(
                    import_context_uuid=import_context_uuid,
                    headers=headers,
                    **request_parameters
        )
                
    
    # Alias Function
    def import_map_archive_cancel_an_import(self,
                                               import_context_uuid,
                                               headers=None,
                                               **request_parameters):
        """ This function is an alias of import_map_archive_cancel_an_import_v1 .
        Args:
            import_context_uuid(basestring): importContextUuid path parameter. The unique import context UUID given
                by a previous call to Start Import API .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of import_map_archive_cancel_an_import_v1 .
        """ 
        return self.import_map_archive_cancel_an_import_v1(
                    import_context_uuid=import_context_uuid,
                    headers=headers,
                    **request_parameters
        )
                
    
    # Alias Function
    def get_site_count(self,
                          site_id=None,
                          headers=None,
                          **request_parameters):
        """ This function is an alias of get_site_count_v1 .
        Args:
            site_id(basestring): siteId query parameter. Site instance UUID .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_site_count_v1 .
        """ 
        return self.get_site_count_v1(
                    site_id=site_id,
                    headers=headers,
                    **request_parameters
        )
                
    
    # Alias Function
    def read_site_count(self,
                           end_time=None,
                           id=None,
                           site_hierarchy=None,
                           site_hierarchy_id=None,
                           site_type=None,
                           headers=None,
                           **request_parameters):
        """ This function is an alias of read_site_count_v1 .
        Args:
            end_time(int): endTime query parameter. End time to which API queries the data set related to the
                resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive. .
            site_hierarchy(basestring): siteHierarchy query parameter. The full hierarchical breakdown of the site
                tree starting from Global site name and ending with the specific site name. The Root
                site is named "Global" (Ex. `Global/AreaName/BuildingName/FloorName`) This field
                supports wildcard asterisk (`*`) character search support. E.g. `*/San*, */San, /San*`
                Examples: `?siteHierarchy=Global/AreaName/BuildingName/FloorName` (single siteHierarchy
                requested) `?siteHierarchy=Global/AreaName/BuildingName/FloorName&siteHierarchy=Global/A
                reaName2/BuildingName2/FloorName2` (multiple siteHierarchies requested) .
            site_hierarchy_id(basestring): siteHierarchyId query parameter. The full hierarchy breakdown of the site
                tree in id form starting from Global site UUID and ending with the specific site UUID.
                (Ex. `globalUuid/areaUuid/buildingUuid/floorUuid`) This field supports wildcard asterisk
                (`*`) character search support. E.g. `*uuid*, *uuid, uuid*` Examples:
                `?siteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid `(single siteHierarchyId
                requested) `?siteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid&siteHierarchyId=
                globalUuid/areaUuid2/buildingUuid2/floorUuid2` (multiple siteHierarchyIds requested) .
            site_type(basestring): siteType query parameter. The type of the site. A site can be an area, building,
                or floor. Default when not provided will be `[floor,building,area]` Examples:
                `?siteType=area` (single siteType requested)
                `?siteType=area&siteType=building&siteType=floor` (multiple siteTypes requested) .
            id(basestring): id query parameter. The list of entity Uuids.
                (Ex."6bef213c-19ca-4170-8375-b694e251101c") Examples:
                id=6bef213c-19ca-4170-8375-b694e251101c (single entity uuid requested) id=6bef213c-19ca-
                4170-8375-b694e251101c&id=32219612-819e-4b5e-a96b-cf22aca13dd9&id=2541e9a7-b80d-4955-
                8aa2-79b233318ba0 (multiple entity uuid with '&' separator) .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of read_site_count_v1 .
        """ 
        return self.read_site_count_v1(
                    end_time=end_time,
                    id=id,
                    site_hierarchy=site_hierarchy,
                    site_hierarchy_id=site_hierarchy_id,
                    site_type=site_type,
                    headers=headers,
                    **request_parameters
        )
                
    
    # Alias Function
    def get_membership(self,
                          site_id,
                          device_family=None,
                          limit=None,
                          offset=None,
                          serial_number=None,
                          headers=None,
                          **request_parameters):
        """ This function is an alias of get_membership_v1 .
        Args:
            site_id(basestring): siteId path parameter. Site id to retrieve device associated with the site. .
            offset(int): offset query parameter. offset/starting row .
            limit(int): limit query parameter. Number of sites to be retrieved .
            device_family(basestring): deviceFamily query parameter. Device family name  .
            serial_number(basestring): serialNumber query parameter. Device serial number .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_membership_v1 .
        """ 
        return self.get_membership_v1(
                    site_id=site_id,
                    device_family=device_family,
                    limit=limit,
                    offset=offset,
                    serial_number=serial_number,
                    headers=headers,
                    **request_parameters
        )
                
    
    # Alias Function
    def read_list_of_site_health_summaries(self,
                                              attribute=None,
                                              end_time=None,
                                              id=None,
                                              limit=None,
                                              offset=None,
                                              order=None,
                                              site_hierarchy=None,
                                              site_hierarchy_id=None,
                                              site_type=None,
                                              sort_by=None,
                                              start_time=None,
                                              view=None,
                                              headers=None,
                                              **request_parameters):
        """ This function is an alias of read_list_of_site_health_summaries_v1 .
        Args:
            start_time(int): startTime query parameter. Start time from which API queries the data set related to
                the resource. It must be specified in UNIX epochtime in milliseconds. Value is
                inclusive. If `startTime` is not provided, API will default to current time. .
            end_time(int): endTime query parameter. End time to which API queries the data set related to the
                resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive. .
            limit(int): limit query parameter. Maximum number of records to return .
            offset(int): offset query parameter. Specifies the starting point within all records returned by the
                API. It's one based offset. The starting value is 1. .
            sort_by(basestring): sortBy query parameter. A field within the response to sort by. .
            order(basestring): order query parameter. The sort order of the field ascending or descending. .
            site_hierarchy(basestring): siteHierarchy query parameter. The full hierarchical breakdown of the site
                tree starting from Global site name and ending with the specific site name. The Root
                site is named "Global" (Ex. `Global/AreaName/BuildingName/FloorName`) This field
                supports wildcard asterisk (`*`) character search support. E.g. `*/San*, */San, /San*`
                Examples: `?siteHierarchy=Global/AreaName/BuildingName/FloorName` (single siteHierarchy
                requested) `?siteHierarchy=Global/AreaName/BuildingName/FloorName&siteHierarchy=Global/A
                reaName2/BuildingName2/FloorName2` (multiple siteHierarchies requested) .
            site_hierarchy_id(basestring): siteHierarchyId query parameter. The full hierarchy breakdown of the site
                tree in id form starting from Global site UUID and ending with the specific site UUID.
                (Ex. `globalUuid/areaUuid/buildingUuid/floorUuid`) This field supports wildcard asterisk
                (`*`) character search support. E.g. `*uuid*, *uuid, uuid*` Examples:
                `?siteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid `(single siteHierarchyId
                requested) `?siteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid&siteHierarchyId=
                globalUuid/areaUuid2/buildingUuid2/floorUuid2` (multiple siteHierarchyIds requested) .
            site_type(basestring): siteType query parameter. The type of the site. A site can be an area, building,
                or floor. Default when not provided will be `[floor,building,area]` Examples:
                `?siteType=area` (single siteType requested)
                `?siteType=area&siteType=building&siteType=floor` (multiple siteTypes requested) .
            id(basestring): id query parameter. The list of entity Uuids.
                (Ex."6bef213c-19ca-4170-8375-b694e251101c") Examples:
                id=6bef213c-19ca-4170-8375-b694e251101c (single entity uuid requested) id=6bef213c-19ca-
                4170-8375-b694e251101c&id=32219612-819e-4b5e-a96b-cf22aca13dd9&id=2541e9a7-b80d-4955-
                8aa2-79b233318ba0 (multiple entity uuid with '&' separator) .
            view(basestring): view query parameter. The specific summary view being requested. This is an optional
                parameter which can be passed to get one or more of the specific health data summaries
                associated with sites. ### Response data proviced by each view:   1. **site** [id,
                siteHierarchy, siteHierarchyId, siteType, latitude, longitude]   2. **network** [id,
                networkDeviceCount, networkDeviceGoodHealthCount,wirelessDeviceCount,
                wirelessDeviceGoodHealthCount, accessDeviceCount, accessDeviceGoodHealthCount,
                coreDeviceCount, coreDeviceGoodHealthCount, distributionDeviceCount,
                distributionDeviceGoodHealthCount, routerDeviceCount, routerDeviceGoodHealthCount,
                apDeviceCount, apDeviceGoodHealthCount, wlcDeviceCount, wlcDeviceGoodHealthCount,
                switchDeviceCount, switchDeviceGoodHealthCount, networkDeviceGoodHealthPercentage,
                accessDeviceGoodHealthPercentage, coreDeviceGoodHealthPercentage,
                distributionDeviceGoodHealthPercentage, routerDeviceGoodHealthPercentage,
                apDeviceGoodHealthPercentage, wlcDeviceGoodHealthPercentage,
                switchDeviceGoodHealthPercentage, wirelessDeviceGoodHealthPercentage]   3. **client**
                [id, clientCount, clientGoodHealthCount, wiredClientCount, wirelessClientCount,
                wiredClientGoodHealthCount, wirelessClientGoodHealthCount, clientGoodHealthPercentage,
                wiredClientGoodHealthPercentage, wirelessClientGoodHealthPercentage, clientDataUsage]
                4. **issue** [id, p1IssueCount, p2IssueCount, p3IssueCount, p4IssueCount, issueCount]
                When this query parameter is not added the default summaries are:
                **[site,client,network,issue]** Examples: view=client (single view requested)
                view=client&view=network&view=issue (multiple views requested) .
            attribute(basestring): attribute query parameter. Supported Attributes: [id, siteHierarchy,
                siteHierarchyId, siteType, latitude, longitude, networkDeviceCount,
                networkDeviceGoodHealthCount,wirelessDeviceCount, wirelessDeviceGoodHealthCount,
                accessDeviceCount, accessDeviceGoodHealthCount, coreDeviceCount,
                coreDeviceGoodHealthCount, distributionDeviceCount, distributionDeviceGoodHealthCount,
                routerDeviceCount, routerDeviceGoodHealthCount, apDeviceCount, apDeviceGoodHealthCount,
                wlcDeviceCount, wlcDeviceGoodHealthCount, switchDeviceCount,
                switchDeviceGoodHealthCount, networkDeviceGoodHealthPercentage,
                accessDeviceGoodHealthPercentage, coreDeviceGoodHealthPercentage,
                distributionDeviceGoodHealthPercentage, routerDeviceGoodHealthPercentage,
                apDeviceGoodHealthPercentage, wlcDeviceGoodHealthPercentage,
                switchDeviceGoodHealthPercentage, wirelessDeviceGoodHealthPercentage, clientCount,
                clientGoodHealthCount, wiredClientCount, wirelessClientCount,
                wiredClientGoodHealthCount, wirelessClientGoodHealthCount, clientGoodHealthPercentage,
                wiredClientGoodHealthPercentage, wirelessClientGoodHealthPercentage, clientDataUsage,
                p1IssueCount, p2IssueCount, p3IssueCount, p4IssueCount, issueCount] If length of
                attribute list is too long, please use 'view' param instead. Examples:
                attribute=siteHierarchy (single attribute requested)
                attribute=siteHierarchy&attribute=clientCount (multiple attributes requested) .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of read_list_of_site_health_summaries_v1 .
        """ 
        return self.read_list_of_site_health_summaries_v1(
                    attribute=attribute,
                    end_time=end_time,
                    id=id,
                    limit=limit,
                    offset=offset,
                    order=order,
                    site_hierarchy=site_hierarchy,
                    site_hierarchy_id=site_hierarchy_id,
                    site_type=site_type,
                    sort_by=sort_by,
                    start_time=start_time,
                    view=view,
                    headers=headers,
                    **request_parameters
        )
                
    
    # Alias Function
    def get_site(self,
                    limit=None,
                    name=None,
                    offset=None,
                    site_id=None,
                    type=None,
                    headers=None,
                    **request_parameters):
        """ This function is an alias of get_site_v1 .
        Args:
            name(basestring): name query parameter. Site name hierarchy (E.g Global/USA/CA) .
            site_id(basestring): siteId query parameter. Site Id .
            type(basestring): type query parameter. Site type (Ex: area, building, floor) .
            offset(int): offset query parameter. Offset/starting index for pagination. Indexed from 1. .
            limit(int): limit query parameter. Number of sites to be listed .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_site_v1 .
        """ 
        return self.get_site_v1(
                    limit=limit,
                    name=name,
                    offset=offset,
                    site_id=site_id,
                    type=type,
                    headers=headers,
                    **request_parameters
        )
                
    
    # Alias Function
    def read_an_aggregated_summary_of_site_health_data(self,
                                                          attribute=None,
                                                          end_time=None,
                                                          id=None,
                                                          site_hierarchy=None,
                                                          site_hierarchy_id=None,
                                                          site_type=None,
                                                          start_time=None,
                                                          view=None,
                                                          headers=None,
                                                          **request_parameters):
        """ This function is an alias of read_an_aggregated_summary_of_site_health_data_v1 .
        Args:
            start_time(int): startTime query parameter. Start time from which API queries the data set related to
                the resource. It must be specified in UNIX epochtime in milliseconds. Value is
                inclusive. If `startTime` is not provided, API will default to current time. .
            end_time(int): endTime query parameter. End time to which API queries the data set related to the
                resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive. .
            site_hierarchy(basestring): siteHierarchy query parameter. The full hierarchical breakdown of the site
                tree starting from Global site name and ending with the specific site name. The Root
                site is named "Global" (Ex. `Global/AreaName/BuildingName/FloorName`) This field
                supports wildcard asterisk (`*`) character search support. E.g. `*/San*, */San, /San*`
                Examples: `?siteHierarchy=Global/AreaName/BuildingName/FloorName` (single siteHierarchy
                requested) `?siteHierarchy=Global/AreaName/BuildingName/FloorName&siteHierarchy=Global/A
                reaName2/BuildingName2/FloorName2` (multiple siteHierarchies requested) .
            site_hierarchy_id(basestring): siteHierarchyId query parameter. The full hierarchy breakdown of the site
                tree in id form starting from Global site UUID and ending with the specific site UUID.
                (Ex. `globalUuid/areaUuid/buildingUuid/floorUuid`) This field supports wildcard asterisk
                (`*`) character search support. E.g. `*uuid*, *uuid, uuid*` Examples:
                `?siteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid `(single siteHierarchyId
                requested) `?siteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid&siteHierarchyId=
                globalUuid/areaUuid2/buildingUuid2/floorUuid2` (multiple siteHierarchyIds requested) .
            site_type(basestring): siteType query parameter. The type of the site. A site can be an area, building,
                or floor. Default when not provided will be `[floor,building,area]` Examples:
                `?siteType=area` (single siteType requested)
                `?siteType=area&siteType=building&siteType=floor` (multiple siteTypes requested) .
            id(basestring): id query parameter. The list of entity Uuids.
                (Ex."6bef213c-19ca-4170-8375-b694e251101c") Examples:
                id=6bef213c-19ca-4170-8375-b694e251101c (single entity uuid requested) id=6bef213c-19ca-
                4170-8375-b694e251101c&id=32219612-819e-4b5e-a96b-cf22aca13dd9&id=2541e9a7-b80d-4955-
                8aa2-79b233318ba0 (multiple entity uuid with '&' separator) .
            view(basestring): view query parameter. The specific summary view being requested. This is an optional
                parameter which can be passed to get one or more of the specific health data summaries
                associated with sites. ### Response data proviced by each view:   1. **site** [id,
                siteHierarchy, siteHierarchyId, siteType, latitude, longitude]   2. **network** [id,
                networkDeviceCount, networkDeviceGoodHealthCount,wirelessDeviceCount,
                wirelessDeviceGoodHealthCount, accessDeviceCount, accessDeviceGoodHealthCount,
                coreDeviceCount, coreDeviceGoodHealthCount, distributionDeviceCount,
                distributionDeviceGoodHealthCount, routerDeviceCount, routerDeviceGoodHealthCount,
                apDeviceCount, apDeviceGoodHealthCount, wlcDeviceCount, wlcDeviceGoodHealthCount,
                switchDeviceCount, switchDeviceGoodHealthCount, networkDeviceGoodHealthPercentage,
                accessDeviceGoodHealthPercentage, coreDeviceGoodHealthPercentage,
                distributionDeviceGoodHealthPercentage, routerDeviceGoodHealthPercentage,
                apDeviceGoodHealthPercentage, wlcDeviceGoodHealthPercentage,
                switchDeviceGoodHealthPercentage, wirelessDeviceGoodHealthPercentage]   3. **client**
                [id, clientCount, clientGoodHealthCount, wiredClientCount, wirelessClientCount,
                wiredClientGoodHealthCount, wirelessClientGoodHealthCount, clientGoodHealthPercentage,
                wiredClientGoodHealthPercentage, wirelessClientGoodHealthPercentage, clientDataUsage]
                4. **issue** [id, p1IssueCount, p2IssueCount, p3IssueCount, p4IssueCount, issueCount]
                When this query parameter is not added the default summaries are:
                **[site,client,network,issue]** Examples: view=client (single view requested)
                view=client&view=network&view=issue (multiple views requested) .
            attribute(basestring): attribute query parameter. Supported Attributes: [id, siteHierarchy,
                siteHierarchyId, siteType, latitude, longitude, networkDeviceCount,
                networkDeviceGoodHealthCount,wirelessDeviceCount, wirelessDeviceGoodHealthCount,
                accessDeviceCount, accessDeviceGoodHealthCount, coreDeviceCount,
                coreDeviceGoodHealthCount, distributionDeviceCount, distributionDeviceGoodHealthCount,
                routerDeviceCount, routerDeviceGoodHealthCount, apDeviceCount, apDeviceGoodHealthCount,
                wlcDeviceCount, wlcDeviceGoodHealthCount, switchDeviceCount,
                switchDeviceGoodHealthCount, networkDeviceGoodHealthPercentage,
                accessDeviceGoodHealthPercentage, coreDeviceGoodHealthPercentage,
                distributionDeviceGoodHealthPercentage, routerDeviceGoodHealthPercentage,
                apDeviceGoodHealthPercentage, wlcDeviceGoodHealthPercentage,
                switchDeviceGoodHealthPercentage, wirelessDeviceGoodHealthPercentage, clientCount,
                clientGoodHealthCount, wiredClientCount, wirelessClientCount,
                wiredClientGoodHealthCount, wirelessClientGoodHealthCount, clientGoodHealthPercentage,
                wiredClientGoodHealthPercentage, wirelessClientGoodHealthPercentage, clientDataUsage,
                p1IssueCount, p2IssueCount, p3IssueCount, p4IssueCount, issueCount] If length of
                attribute list is too long, please use 'view' param instead. Examples:
                attribute=siteHierarchy (single attribute requested)
                attribute=siteHierarchy&attribute=clientCount (multiple attributes requested) .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of read_an_aggregated_summary_of_site_health_data_v1 .
        """ 
        return self.read_an_aggregated_summary_of_site_health_data_v1(
                    attribute=attribute,
                    end_time=end_time,
                    id=id,
                    site_hierarchy=site_hierarchy,
                    site_hierarchy_id=site_hierarchy_id,
                    site_type=site_type,
                    start_time=start_time,
                    view=view,
                    headers=headers,
                    **request_parameters
        )
                
    
    # Alias Function
    def assign_devices_to_site(self,
                                  site_id,
                                  device=None,
                                  headers=None,
                                  payload=None,
                                  active_validation=True,
                                  **request_parameters):
        """ This function is an alias of assign_devices_to_site_v1 .
        Args:
            device(list): Sites's device (list of objects).
            site_id(basestring): siteId path parameter. Site Id where device(s) needs to be assigned .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of assign_devices_to_site_v1 .
        """ 
        return self.assign_devices_to_site_v1(
                    site_id=site_id,
                    device=device,
                    headers=headers,
                    payload=payload,
                    active_validation=active_validation,
                    **request_parameters
        )
                
    
    # Alias Function
    def export_map_archive(self,
                              site_hierarchy_uuid,
                              headers=None,
                              payload=None,
                              active_validation=True,
                              **request_parameters):
        """ This function is an alias of export_map_archive_v1 .
        Args:
            site_hierarchy_uuid(basestring): siteHierarchyUuid path parameter. The site hierarchy element UUID to
                export, all child elements starting at this hierarchy element will be included. Limited
                to a hierarchy that contains 500 or fewer maps. .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of export_map_archive_v1 .
        """ 
        return self.export_map_archive_v1(
                    site_hierarchy_uuid=site_hierarchy_uuid,
                    headers=headers,
                    payload=payload,
                    active_validation=active_validation,
                    **request_parameters
        )
                
    
    # Alias Function
    def update_site(self,
                       site_id,
                       site=None,
                       type=None,
                       headers=None,
                       payload=None,
                       active_validation=True,
                       **request_parameters):
        """ This function is an alias of update_site_v1 .
        Args:
            site(object): Sites's site.
            type(string): Sites's Site type . Available values are 'area', 'building' and 'floor'.
            site_id(basestring): siteId path parameter. Site id to which site details to be updated. .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of update_site_v1 .
        """ 
        return self.update_site_v1(
                    site_id=site_id,
                    site=site,
                    type=type,
                    headers=headers,
                    payload=payload,
                    active_validation=active_validation,
                    **request_parameters
        )
                
    
    # Alias Function
    def get_devices_that_are_assigned_to_a_site(self,
                                                   id,
                                                   member_type,
                                                   level=None,
                                                   limit=None,
                                                   offset=None,
                                                   headers=None,
                                                   **request_parameters):
        """ This function is an alias of get_devices_that_are_assigned_to_a_site_v1 .
        Args:
            id(basestring): id path parameter. Site Id .
            offset(basestring): offset query parameter. Offset/starting index for pagination .
            limit(basestring): limit query parameter. Number of devices to be listed. Default and max supported
                value is 500 .
            member_type(basestring): memberType query parameter. Member type (This API only supports the
                'networkdevice' type) .
            level(basestring): level query parameter. Depth of site hierarchy to be considered to list the devices.
                If the provided value is -1, devices for all child sites will be listed. .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_devices_that_are_assigned_to_a_site_v1 .
        """ 
        return self.get_devices_that_are_assigned_to_a_site_v1(
                    id=id,
                    member_type=member_type,
                    level=level,
                    limit=limit,
                    offset=offset,
                    headers=headers,
                    **request_parameters
        )
                
    
    # Alias Function
    def query_an_aggregated_summary_of_site_health_data(self,
                                                           attributes=None,
                                                           endTime=None,
                                                           id=None,
                                                           site_hierarchy=None,
                                                           site_hierarchy_id=None,
                                                           site_type=None,
                                                           startTime=None,
                                                           views=None,
                                                           headers=None,
                                                           payload=None,
                                                           active_validation=True,
                                                           **request_parameters):
        """ This function is an alias of query_an_aggregated_summary_of_site_health_data_v1 .
        Args:
            attributes(list): Sites's Attributes (list of strings).
            endTime(integer): Sites's End Time.
            startTime(integer): Sites's Start Time.
            views(list): Sites's Views (list of strings).
            site_hierarchy(basestring): siteHierarchy query parameter. The full hierarchical breakdown of the site
                tree starting from Global site name and ending with the specific site name. The Root
                site is named "Global" (Ex. `Global/AreaName/BuildingName/FloorName`) This field
                supports wildcard asterisk (`*`) character search support. E.g. `*/San*, */San, /San*`
                Examples: `?siteHierarchy=Global/AreaName/BuildingName/FloorName` (single siteHierarchy
                requested) `?siteHierarchy=Global/AreaName/BuildingName/FloorName&siteHierarchy=Global/A
                reaName2/BuildingName2/FloorName2` (multiple siteHierarchies requested) .
            site_hierarchy_id(basestring): siteHierarchyId query parameter. The full hierarchy breakdown of the site
                tree in id form starting from Global site UUID and ending with the specific site UUID.
                (Ex. `globalUuid/areaUuid/buildingUuid/floorUuid`) This field supports wildcard asterisk
                (`*`) character search support. E.g. `*uuid*, *uuid, uuid*` Examples:
                `?siteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid `(single siteHierarchyId
                requested) `?siteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid&siteHierarchyId=
                globalUuid/areaUuid2/buildingUuid2/floorUuid2` (multiple siteHierarchyIds requested) .
            site_type(basestring): siteType query parameter. The type of the site. A site can be an area, building,
                or floor. Default when not provided will be `[floor,building,area]` Examples:
                `?siteType=area` (single siteType requested)
                `?siteType=area&siteType=building&siteType=floor` (multiple siteTypes requested) .
            id(basestring): id query parameter. The list of entity Uuids.
                (Ex."6bef213c-19ca-4170-8375-b694e251101c") Examples:
                id=6bef213c-19ca-4170-8375-b694e251101c (single entity uuid requested) id=6bef213c-19ca-
                4170-8375-b694e251101c&id=32219612-819e-4b5e-a96b-cf22aca13dd9&id=2541e9a7-b80d-4955-
                8aa2-79b233318ba0 (multiple entity uuid with '&' separator) .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of query_an_aggregated_summary_of_site_health_data_v1 .
        """ 
        return self.query_an_aggregated_summary_of_site_health_data_v1(
                    attributes=attributes,
                    endTime=endTime,
                    id=id,
                    site_hierarchy=site_hierarchy,
                    site_hierarchy_id=site_hierarchy_id,
                    site_type=site_type,
                    startTime=startTime,
                    views=views,
                    headers=headers,
                    payload=payload,
                    active_validation=active_validation,
                    **request_parameters
        )
                
    
    # Alias Function
    def import_map_archive_start_import(self,
                                           headers=None,
                                           **request_parameters):
        """ This function is an alias of import_map_archive_start_import_v1 .
        Args:
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of import_map_archive_start_import_v1 .
        """ 
        return self.import_map_archive_start_import_v1(
                    headers=headers,
                    **request_parameters
        )
                
    
    # Alias Function
    def delete_site(self,
                       site_id,
                       headers=None,
                       **request_parameters):
        """ This function is an alias of delete_site_v1 .
        Args:
            site_id(basestring): siteId path parameter. Site id to which site details to be deleted. .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of delete_site_v1 .
        """ 
        return self.delete_site_v1(
                    site_id=site_id,
                    headers=headers,
                    **request_parameters
        )
                
    
    # Alias Function
    def maps_supported_access_points(self,
                                        headers=None,
                                        **request_parameters):
        """ This function is an alias of maps_supported_access_points_v1 .
        Args:
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of maps_supported_access_points_v1 .
        """
        return self.maps_supported_access_points_v1(
                    headers=headers,
                    **request_parameters
        )
                
    
    # Alias Function
    def read_site_health_summary_data_by_site_id(self,
                                                    id,
                                                    attribute=None,
                                                    end_time=None,
                                                    start_time=None,
                                                    view=None,
                                                    headers=None,
                                                    **request_parameters):
        """ This function is an alias of read_site_health_summary_data_by_site_id_v1 .
        Args:
            id(basestring): id path parameter. unique site uuid .
            start_time(int): startTime query parameter. Start time from which API queries the data set related to
                the resource. It must be specified in UNIX epochtime in milliseconds. Value is
                inclusive. If `startTime` is not provided, API will default to current time. .
            end_time(int): endTime query parameter. End time to which API queries the data set related to the
                resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive. .
            view(basestring): view query parameter. The specific summary view being requested. This is an optional
                parameter which can be passed to get one or more of the specific health data summaries
                associated with sites. ### Response data proviced by each view:   1. **site** [id,
                siteHierarchy, siteHierarchyId, siteType, latitude, longitude]   2. **network** [id,
                networkDeviceCount, networkDeviceGoodHealthCount,wirelessDeviceCount,
                wirelessDeviceGoodHealthCount, accessDeviceCount, accessDeviceGoodHealthCount,
                coreDeviceCount, coreDeviceGoodHealthCount, distributionDeviceCount,
                distributionDeviceGoodHealthCount, routerDeviceCount, routerDeviceGoodHealthCount,
                apDeviceCount, apDeviceGoodHealthCount, wlcDeviceCount, wlcDeviceGoodHealthCount,
                switchDeviceCount, switchDeviceGoodHealthCount, networkDeviceGoodHealthPercentage,
                accessDeviceGoodHealthPercentage, coreDeviceGoodHealthPercentage,
                distributionDeviceGoodHealthPercentage, routerDeviceGoodHealthPercentage,
                apDeviceGoodHealthPercentage, wlcDeviceGoodHealthPercentage,
                switchDeviceGoodHealthPercentage, wirelessDeviceGoodHealthPercentage]   3. **client**
                [id, clientCount, clientGoodHealthCount, wiredClientCount, wirelessClientCount,
                wiredClientGoodHealthCount, wirelessClientGoodHealthCount, clientGoodHealthPercentage,
                wiredClientGoodHealthPercentage, wirelessClientGoodHealthPercentage, clientDataUsage]
                4. **issue** [id, p1IssueCount, p2IssueCount, p3IssueCount, p4IssueCount, issueCount]
                When this query parameter is not added the default summaries are:
                **[site,client,network,issue]** Examples: view=client (single view requested)
                view=client&view=network&view=issue (multiple views requested) .
            attribute(basestring): attribute query parameter. Supported Attributes: [id, siteHierarchy,
                siteHierarchyId, siteType, latitude, longitude, networkDeviceCount,
                networkDeviceGoodHealthCount,wirelessDeviceCount, wirelessDeviceGoodHealthCount,
                accessDeviceCount, accessDeviceGoodHealthCount, coreDeviceCount,
                coreDeviceGoodHealthCount, distributionDeviceCount, distributionDeviceGoodHealthCount,
                routerDeviceCount, routerDeviceGoodHealthCount, apDeviceCount, apDeviceGoodHealthCount,
                wlcDeviceCount, wlcDeviceGoodHealthCount, switchDeviceCount,
                switchDeviceGoodHealthCount, networkDeviceGoodHealthPercentage,
                accessDeviceGoodHealthPercentage, coreDeviceGoodHealthPercentage,
                distributionDeviceGoodHealthPercentage, routerDeviceGoodHealthPercentage,
                apDeviceGoodHealthPercentage, wlcDeviceGoodHealthPercentage,
                switchDeviceGoodHealthPercentage, wirelessDeviceGoodHealthPercentage, clientCount,
                clientGoodHealthCount, wiredClientCount, wirelessClientCount,
                wiredClientGoodHealthCount, wirelessClientGoodHealthCount, clientGoodHealthPercentage,
                wiredClientGoodHealthPercentage, wirelessClientGoodHealthPercentage, clientDataUsage,
                p1IssueCount, p2IssueCount, p3IssueCount, p4IssueCount, issueCount] If length of
                attribute list is too long, please use 'view' param instead. Examples:
                attribute=siteHierarchy (single attribute requested)
                attribute=siteHierarchy&attribute=clientCount (multiple attributes requested) .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of read_site_health_summary_data_by_site_id_v1 .
        """ 
        return self.read_site_health_summary_data_by_site_id_v1(
                    id=id,
                    attribute=attribute,
                    end_time=end_time,
                    start_time=start_time,
                    view=view,
                    headers=headers,
                    **request_parameters
        )



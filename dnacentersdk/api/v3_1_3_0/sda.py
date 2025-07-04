# -*- coding: utf-8 -*-
"""Cisco Catalyst Center SDA API wrapper.

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


class Sda(object):
    """Cisco Catalyst Center SDA API (version: 3.1.3.0).

    Wraps the Catalyst Center SDA
    API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new Sda
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Catalyst Center service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(Sda, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def read_list_of_fabric_sites_with_their_health_summary(
        self,
        attribute=None,
        end_time=None,
        id=None,
        limit=None,
        offset=None,
        order=None,
        site_hierarchy=None,
        site_hierarchy_id=None,
        sort_by=None,
        start_time=None,
        view=None,
        headers=None,
        **request_parameters
    ):
        """Get a paginated list of Fabric sites Networks with health summary. This API provides the latest health data
        until the given `endTime`. If data is not ready for the provided endTime, the request will fail with
        error code `400 Bad Request`, and the error message will indicate the recommended endTime to use to
        retrieve a complete data set. This behavior may occur if the provided endTime=currentTime, since we are
        not a real time system. When `endTime` is not provided, the API returns the latest data. For detailed
        information about the usage of the API, please refer to the Open API specification document
        https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-fabricSiteHealthSummaries-1.0.1-resolved.yaml .

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
            id(str): id query parameter. The list of entity Uuids. (Ex."6bef213c-19ca-4170-8375-b694e251101c")
                Examples: id=6bef213c-19ca-4170-8375-b694e251101c (single entity uuid requested) id=6bef
                213c-19ca-4170-8375-b694e251101c&id=32219612-819e-4b5e-a96b-cf22aca13dd9&id=2541e9a7-
                b80d-4955-8aa2-79b233318ba0 (multiple entity uuid with '&' separator) .
            attribute(str): attribute query parameter. The list of FabricSite health attributes. Please refer to
                ```fabricSiteAttributes``` section in the Open API specification document mentioned in
                the description. .
            view(str): view query parameter. The specific summary view being requested. A maximum of 3 views can be
                queried at a time per request.  Please refer to ```fabricSiteViews``` section in the
                Open API specification document mentioned in the description. .
            site_hierarchy(str): siteHierarchy query parameter. The full hierarchical breakdown of the site tree
                starting from Global site name and ending with the specific site name. The Root site is
                named "Global" (Ex. `Global/AreaName/BuildingName/FloorName`)          This field
                supports wildcard asterisk (`*`) character search support. E.g. `*/San*, */San, /San*`
                Examples:          `?siteHierarchy=Global/AreaName/BuildingName/FloorName` (single
                siteHierarchy requested)          `?siteHierarchy=Global/AreaName/BuildingName/FloorName
                &siteHierarchy=Global/AreaName2/BuildingName2/FloorName2` (multiple siteHierarchies
                requested) .
            site_hierarchy_id(str): siteHierarchyId query parameter. The full hierarchy breakdown of the site tree
                in id form starting from Global site UUID and ending with the specific site UUID. (Ex.
                `globalUuid/areaUuid/buildingUuid/floorUuid`)          This field supports wildcard
                asterisk (`*`) character search support. E.g. `*uuid*, *uuid, uuid*`          Examples:
                `?siteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid `(single siteHierarchyId
                requested)          `?siteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid&siteHie
                rarchyId=globalUuid/areaUuid2/buildingUuid2/floorUuid2` (multiple siteHierarchyIds
                requested) .
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
            https://developer.cisco.com/docs/dna-center/#!read-list-of-fabric-sites-with-their-health-summary
        """
        check_type(headers, dict)
        check_type(start_time, int)
        check_type(end_time, int)
        check_type(limit, int)
        check_type(offset, int)
        check_type(sort_by, str)
        check_type(order, str)
        check_type(id, str)
        check_type(attribute, str)
        check_type(view, str)
        check_type(site_hierarchy, str)
        check_type(site_hierarchy_id, str)
        if headers is not None:
            if "X-CALLER-ID" in headers:
                check_type(headers.get("X-CALLER-ID"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "startTime": start_time,
            "endTime": end_time,
            "limit": limit,
            "offset": offset,
            "sortBy": sort_by,
            "order": order,
            "id": id,
            "attribute": attribute,
            "view": view,
            "siteHierarchy": site_hierarchy,
            "siteHierarchyId": site_hierarchy_id,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/fabricSiteHealthSummaries"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a4f14955aea82772d0299ffb0d_v3_1_3_0", json_data
        )

    def read_fabric_site_count(
        self,
        end_time=None,
        id=None,
        site_hierarchy=None,
        site_hierarchy_id=None,
        start_time=None,
        headers=None,
        **request_parameters
    ):
        """Get a count of Fabric sites. Use available query parameters to get the count of a subset of fabric sites. This
        API provides the latest health data until the given `endTime`. If data is not ready for the provided
        endTime, the request will fail with error code `400 Bad Request`, and the error message will indicate
        the recommended endTime to use to retrieve a complete data set. This behavior may occur if the provided
        endTime=currentTime, since we are not a real time system. When `endTime` is not provided, the API
        returns the latest data. For detailed information about the usage of the API, please refer to the Open
        API specification document https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-fabricSiteHealthSummaries-1.0.1-resolved.yaml .

        Args:
            start_time(int): startTime query parameter. Start time from which API queries the data set related to
                the resource. It must be specified in UNIX epochtime in milliseconds. Value is
                inclusive. .
            end_time(int): endTime query parameter. End time to which API queries the data set related to the
                resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive. .
            id(str): id query parameter. The list of entity Uuids. (Ex."6bef213c-19ca-4170-8375-b694e251101c")
                Examples: id=6bef213c-19ca-4170-8375-b694e251101c (single entity uuid requested) id=6bef
                213c-19ca-4170-8375-b694e251101c&id=32219612-819e-4b5e-a96b-cf22aca13dd9&id=2541e9a7-
                b80d-4955-8aa2-79b233318ba0 (multiple entity uuid with '&' separator) .
            site_hierarchy(str): siteHierarchy query parameter. The full hierarchical breakdown of the site tree
                starting from Global site name and ending with the specific site name. The Root site is
                named "Global" (Ex. `Global/AreaName/BuildingName/FloorName`)          This field
                supports wildcard asterisk (`*`) character search support. E.g. `*/San*, */San, /San*`
                Examples:          `?siteHierarchy=Global/AreaName/BuildingName/FloorName` (single
                siteHierarchy requested)          `?siteHierarchy=Global/AreaName/BuildingName/FloorName
                &siteHierarchy=Global/AreaName2/BuildingName2/FloorName2` (multiple siteHierarchies
                requested) .
            site_hierarchy_id(str): siteHierarchyId query parameter. The full hierarchy breakdown of the site tree
                in id form starting from Global site UUID and ending with the specific site UUID. (Ex.
                `globalUuid/areaUuid/buildingUuid/floorUuid`)          This field supports wildcard
                asterisk (`*`) character search support. E.g. `*uuid*, *uuid, uuid*`          Examples:
                `?siteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid `(single siteHierarchyId
                requested)          `?siteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid&siteHie
                rarchyId=globalUuid/areaUuid2/buildingUuid2/floorUuid2` (multiple siteHierarchyIds
                requested) .
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
            https://developer.cisco.com/docs/dna-center/#!read-fabric-site-count
        """
        check_type(headers, dict)
        check_type(start_time, int)
        check_type(end_time, int)
        check_type(id, str)
        check_type(site_hierarchy, str)
        check_type(site_hierarchy_id, str)
        if headers is not None:
            if "X-CALLER-ID" in headers:
                check_type(headers.get("X-CALLER-ID"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "startTime": start_time,
            "endTime": end_time,
            "id": id,
            "siteHierarchy": site_hierarchy,
            "siteHierarchyId": site_hierarchy_id,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/fabricSiteHealthSummaries/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_d7eeb4af6215c3599693c8f36711ddd_v3_1_3_0", json_data
        )

    def read_fabric_sites_with_health_summary_from_id(
        self,
        id,
        attribute=None,
        end_time=None,
        start_time=None,
        view=None,
        headers=None,
        **request_parameters
    ):
        """Get Fabric site health summary for a specific fabric site by providing the unique fabric site id in the url
        path. This API provides the latest health data until the given `endTime`. If data is not ready for the
        provided endTime, the request will fail with error code `400 Bad Request`, and the error message will
        indicate the recommended endTime to use to retrieve a complete data set. This behavior may occur if the
        provided endTime=currentTime, since we are not a real time system. When `endTime` is not provided, the
        API returns the latest data. For detailed information about the usage of the API, please refer to the
        Open API specification document https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-fabricSiteHealthSummaries-1.0.1-resolved.yaml .

        Args:
            id(str): id path parameter. unique fabric site id .
            start_time(int): startTime query parameter. Start time from which API queries the data set related to
                the resource. It must be specified in UNIX epochtime in milliseconds. Value is
                inclusive. .
            end_time(int): endTime query parameter. End time to which API queries the data set related to the
                resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive. .
            attribute(str): attribute query parameter. The list of FabricSite health attributes. Please refer to
                ```fabricSiteAttributes``` section in the Open API specification document mentioned in
                the description. .
            view(str): view query parameter. The specific summary view being requested. A maximum of 3 views can be
                queried at a time per request.  Please refer to ```fabricSiteViews``` section in the
                Open API specification document mentioned in the description. .
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
            https://developer.cisco.com/docs/dna-center/#!read-fabric-sites-with-health-summary-from-id
        """
        check_type(headers, dict)
        check_type(start_time, int)
        check_type(end_time, int)
        check_type(attribute, str)
        check_type(view, str)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-CALLER-ID" in headers:
                check_type(headers.get("X-CALLER-ID"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "startTime": start_time,
            "endTime": end_time,
            "attribute": attribute,
            "view": view,
        }
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

        e_url = "/dna/data/api/v1/fabricSiteHealthSummaries/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_daad662049da50a985dbd37a3a7fd28c_v3_1_3_0", json_data
        )

    def the_trend_analytics_data_for_a_fabric_site_in_the_specified_time_range(
        self,
        id,
        trend_interval,
        attribute=None,
        end_time=None,
        limit=None,
        offset=None,
        order=None,
        start_time=None,
        headers=None,
        **request_parameters
    ):
        """Get health time series for a specific Fabric Site by providing the unique Fabric site id in the url path. The
        data will be grouped based on the specified trend time interval. If startTime and endTime are not
        provided, the API defaults to the last 24 hours. By default: the number of records returned will be 500.
        the records will be sorted in time ascending (`asc`) order ex: id:93a25378-7740-4e20-8d90-0060ad9a1be0
        This API provides the latest health data until the given `endTime`. If data is not ready for the
        provided endTime, the request will fail with error code `400 Bad Request`, and the error message will
        indicate the recommended endTime to use to retrieve a complete data set. This behavior may occur if the
        provided endTime=currentTime, since we are not a real time system. When `endTime` is not provided, the
        API returns the latest data. For detailed information about the usage of the API, please refer to the
        Open API specification document https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-fabricSiteHealthSummaries-1.0.1-resolved.yaml .

        Args:
            id(str): id path parameter. unique fabric site id .
            start_time(int): startTime query parameter. Start time from which API queries the data set related to
                the resource. It must be specified in UNIX epochtime in milliseconds. Value is
                inclusive. .
            end_time(int): endTime query parameter. End time to which API queries the data set related to the
                resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive. .
            trend_interval(str): trendInterval query parameter. The time window to aggregate the metrics. Interval
                can be 5 minutes or 10 minutes or 1 hour or 1 day or 7 days .
            limit(int): limit query parameter. Maximum number of records to return .
            offset(int): offset query parameter. Specifies the starting point within all records returned by the
                API. It's one based offset. The starting value is 1. .
            order(str): order query parameter. The sort order of the field ascending or descending. .
            attribute(str): attribute query parameter. The interested fields in the request. For valid attributes,
                verify the documentation. .
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
            https://developer.cisco.com/docs/dna-center/#!the-trend-analytics-data-for-a-fabric-site-in-the-specified-time-range
        """
        check_type(headers, dict)
        check_type(start_time, int)
        check_type(end_time, int)
        check_type(trend_interval, str, may_be_none=False)
        check_type(limit, int)
        check_type(offset, int)
        check_type(order, str)
        check_type(attribute, str)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-CALLER-ID" in headers:
                check_type(headers.get("X-CALLER-ID"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "startTime": start_time,
            "endTime": end_time,
            "trendInterval": trend_interval,
            "limit": limit,
            "offset": offset,
            "order": order,
            "attribute": attribute,
        }
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

        e_url = "/dna/data/api/v1/fabricSiteHealthSummaries/{id}/trendAna" + "lytics"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_f333e0d9b155d36a7dab8b54f9ef9b9_v3_1_3_0", json_data
        )

    def read_fabric_entity_summary(
        self,
        end_time=None,
        site_hierarchy=None,
        site_hierarchy_id=None,
        start_time=None,
        headers=None,
        **request_parameters
    ):
        """Read Fabric summary for overall deployment. Get an aggregated summary of all fabric entities in a deployment
        including the entity health. This API provides the latest health data until the given `endTime`. If data
        is not ready for the provided endTime, the request will fail with error code `400 Bad Request`, and the
        error message will indicate the recommended endTime to use to retrieve a complete data set. This
        behavior may occur if the provided endTime=currentTime, since we are not a real time system. When
        `endTime` is not provided, the API returns the latest data. For detailed information about the usage of
        the API, please refer to the Open API specification document https://github.com/cisco-en-
        programmability/catalyst-center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-
        fabricSummary-1.1.0-resolved.yaml .

        Args:
            start_time(int): startTime query parameter. Start time from which API queries the data set related to
                the resource. It must be specified in UNIX epochtime in milliseconds. Value is
                inclusive. .
            end_time(int): endTime query parameter. End time to which API queries the data set related to the
                resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive. .
            site_hierarchy(str): siteHierarchy query parameter. The full hierarchical breakdown of the site tree
                starting from Global site name and ending with the specific site name. The Root site is
                named "Global" (Ex. `Global/AreaName/BuildingName/FloorName`)          This field
                supports wildcard asterisk (`*`) character search support. E.g. `*/San*, */San, /San*`
                Examples:          `?siteHierarchy=Global/AreaName/BuildingName/FloorName` (single
                siteHierarchy requested)          `?siteHierarchy=Global/AreaName/BuildingName/FloorName
                &siteHierarchy=Global/AreaName2/BuildingName2/FloorName2` (multiple siteHierarchies
                requested) .
            site_hierarchy_id(str): siteHierarchyId query parameter. The full hierarchy breakdown of the site tree
                in id form starting from Global site UUID and ending with the specific site UUID. (Ex.
                `globalUuid/areaUuid/buildingUuid/floorUuid`)          This field supports wildcard
                asterisk (`*`) character search support. E.g. `*uuid*, *uuid, uuid*`          Examples:
                `?siteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid `(single siteHierarchyId
                requested)          `?siteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid&siteHie
                rarchyId=globalUuid/areaUuid2/buildingUuid2/floorUuid2` (multiple siteHierarchyIds
                requested) .
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
            https://developer.cisco.com/docs/dna-center/#!read-fabric-entity-summary
        """
        check_type(headers, dict)
        check_type(start_time, int)
        check_type(end_time, int)
        check_type(site_hierarchy, str)
        check_type(site_hierarchy_id, str)
        if headers is not None:
            if "X-CALLER-ID" in headers:
                check_type(headers.get("X-CALLER-ID"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "startTime": start_time,
            "endTime": end_time,
            "siteHierarchy": site_hierarchy,
            "siteHierarchyId": site_hierarchy_id,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/fabricSummary"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ee22675da09af2616f46776746_v3_1_3_0", json_data
        )

    def read_list_of_transit_networks_with_their_health_summary(
        self,
        attribute=None,
        end_time=None,
        id=None,
        limit=None,
        offset=None,
        order=None,
        sort_by=None,
        start_time=None,
        view=None,
        headers=None,
        **request_parameters
    ):
        """Get a paginated list of Transit Networks with health summary. This API provides the latest health data until the
        given `endTime`. If data is not ready for the provided endTime, the request will fail with error code
        `400 Bad Request`, and the error message will indicate the recommended endTime to use to retrieve a
        complete data set. This behavior may occur if the provided endTime=currentTime, since we are not a real
        time system. When `endTime` is not provided, the API returns the latest data. For detailed information
        about the usage of the API, please refer to the Open API specification document
        https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-transitNetworkHealthSummaries-1.0.1-resolved.yaml .

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
            id(str): id query parameter. The list of transit entity ids. (Ex "1551156a-bc97-3c63-aeda-8a6d3765b5b9")
                Examples: id=1551156a-bc97-3c63-aeda-8a6d3765b5b9 (single entity uuid requested)
                id=1551156a-bc97-3c63-aeda-8a6d3765b5b9&id=4aa20652-237c-4625-b2b4-fd7e82b6a81e
                (multiple entity uuids with '&' separator) .
            attribute(str): attribute query parameter. The interested fields in the request. For valid attributes,
                verify the documentation. .
            view(str): view query parameter. The specific summary view being requested. This is an optional
                parameter which can be passed to get one or more of the specific health data summaries
                associated with sites. .
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
            https://developer.cisco.com/docs/dna-center/#!read-list-of-transit-networks-with-their-health-summary
        """
        check_type(headers, dict)
        check_type(start_time, int)
        check_type(end_time, int)
        check_type(limit, int)
        check_type(offset, int)
        check_type(sort_by, str)
        check_type(order, str)
        check_type(id, str)
        check_type(attribute, str)
        check_type(view, str)
        if headers is not None:
            if "X-CALLER-ID" in headers:
                check_type(headers.get("X-CALLER-ID"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "startTime": start_time,
            "endTime": end_time,
            "limit": limit,
            "offset": offset,
            "sortBy": sort_by,
            "order": order,
            "id": id,
            "attribute": attribute,
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

        e_url = "/dna/data/api/v1/transitNetworkHealthSummaries"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_f6abbbea801355559c36dd413a32abe3_v3_1_3_0", json_data
        )

    def read_transit_networks_count(
        self,
        end_time=None,
        id=None,
        start_time=None,
        headers=None,
        **request_parameters
    ):
        """Get a count of transit networks. Use available query parameters to get the count of a subset of transit
        networks. This API provides the latest health data until the given `endTime`. If data is not ready for
        the provided endTime, the request will fail with error code `400 Bad Request`, and the error message
        will indicate the recommended endTime to use to retrieve a complete data set. This behavior may occur if
        the provided endTime=currentTime, since we are not a real time system. When `endTime` is not provided,
        the API returns the latest data. For detailed information about the usage of the API, please refer to
        the Open API specification document https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-transitNetworkHealthSummaries-1.0.1-resolved.yaml .

        Args:
            start_time(int): startTime query parameter. Start time from which API queries the data set related to
                the resource. It must be specified in UNIX epochtime in milliseconds. Value is
                inclusive. .
            end_time(int): endTime query parameter. End time to which API queries the data set related to the
                resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive. .
            id(str): id query parameter. The list of transit entity ids. (Ex "1551156a-bc97-3c63-aeda-8a6d3765b5b9")
                Examples: id=1551156a-bc97-3c63-aeda-8a6d3765b5b9 (single entity uuid requested)
                id=1551156a-bc97-3c63-aeda-8a6d3765b5b9&id=4aa20652-237c-4625-b2b4-fd7e82b6a81e
                (multiple entity uuids with '&' separator) .
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
            https://developer.cisco.com/docs/dna-center/#!read-transit-networks-count
        """
        check_type(headers, dict)
        check_type(start_time, int)
        check_type(end_time, int)
        check_type(id, str)
        if headers is not None:
            if "X-CALLER-ID" in headers:
                check_type(headers.get("X-CALLER-ID"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "startTime": start_time,
            "endTime": end_time,
            "id": id,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/transitNetworkHealthSummaries/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_d8b91fbaa8f5872979edf536c094b30_v3_1_3_0", json_data
        )

    def read_transit_network_with_its_health_summary_from_id(
        self,
        id,
        attribute=None,
        end_time=None,
        start_time=None,
        view=None,
        headers=None,
        **request_parameters
    ):
        """Get health summary for a specific transit Network by providing the unique transit networks id in the url path.
        This API provides the latest health data until the given `endTime`. If data is not ready for the
        provided endTime, the request will fail with error code `400 Bad Request`, and the error message will
        indicate the recommended endTime to use to retrieve a complete data set. This behavior may occur if the
        provided endTime=currentTime, since we are not a real time system. When `endTime` is not provided, the
        API returns the latest data. For detailed information about the usage of the API, please refer to the
        Open API specification document https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-transitNetworkHealthSummaries-1.0.1-resolved.yaml .

        Args:
            id(str): id path parameter. The unique transit network id, Ex “1551156a-bc97-3c63-aeda-8a6d3765b5b9" .
            end_time(int): endTime query parameter. End time to which API queries the data set related to the
                resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive. .
            start_time(int): startTime query parameter. Start time from which API queries the data set related to
                the resource. It must be specified in UNIX epochtime in milliseconds. Value is
                inclusive. .
            attribute(str): attribute query parameter. The interested fields in the request. For valid attributes,
                verify the documentation. .
            view(str): view query parameter. The specific summary view being requested. This is an optional
                parameter which can be passed to get one or more of the specific health data summaries
                associated with sites. .
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
            https://developer.cisco.com/docs/dna-center/#!read-transit-network-with-its-health-summary-from-id
        """
        check_type(headers, dict)
        check_type(end_time, int)
        check_type(start_time, int)
        check_type(attribute, str)
        check_type(view, str)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-CALLER-ID" in headers:
                check_type(headers.get("X-CALLER-ID"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "endTime": end_time,
            "startTime": start_time,
            "attribute": attribute,
            "view": view,
        }
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

        e_url = "/dna/data/api/v1/transitNetworkHealthSummaries/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_b95b73d75c7956acab07b3d5ba39d191_v3_1_3_0", json_data
        )

    def the_trend_analytics_data_for_a_transit_network_in_the_specified_time_range(
        self,
        id,
        trend_interval,
        attribute=None,
        end_time=None,
        limit=None,
        offset=None,
        order=None,
        start_time=None,
        headers=None,
        **request_parameters
    ):
        """Get health time series for a specific Transit Network by providing the unique Transit Network id in the url
        path. The data will be grouped based on the specified trend time interval. If startTime and endTime are
        not provided, the API defaults to the last 24 hours. By default: the number of records returned will be
        500. the records will be sorted in time ascending (`asc`) order This API provides the latest health data
        until the given `endTime`. If data is not ready for the provided endTime, the request will fail with
        error code `400 Bad Request`, and the error message will indicate the recommended endTime to use to
        retrieve a complete data set. This behavior may occur if the provided endTime=currentTime, since we are
        not a real time system. When `endTime` is not provided, the API returns the latest data. For detailed
        information about the usage of the API, please refer to the Open API specification document
        https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-transitNetworkHealthSummaries-1.0.1-resolved.yaml .

        Args:
            id(str): id path parameter. The unique transit network id, Ex “1551156a-bc97-3c63-aeda-8a6d3765b5b9" .
            start_time(int): startTime query parameter. Start time from which API queries the data set related to
                the resource. It must be specified in UNIX epochtime in milliseconds. Value is
                inclusive. .
            end_time(int): endTime query parameter. End time to which API queries the data set related to the
                resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive. .
            trend_interval(str): trendInterval query parameter. The time window to aggregate the metrics. Interval
                can be 5 minutes or 10 minutes or 1 hour or 1 day or 7 days .
            limit(int): limit query parameter. Maximum number of records to return .
            offset(int): offset query parameter. Specifies the starting point within all records returned by the
                API. It's one based offset. The starting value is 1. .
            order(str): order query parameter. The sort order of the field ascending or descending. .
            attribute(str): attribute query parameter. The interested fields in the request. For valid attributes,
                verify the documentation. .
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
            https://developer.cisco.com/docs/dna-center/#!the-trend-analytics-data-for-a-transit-network-in-the-specified-time-range
        """
        check_type(headers, dict)
        check_type(start_time, int)
        check_type(end_time, int)
        check_type(trend_interval, str, may_be_none=False)
        check_type(limit, int)
        check_type(offset, int)
        check_type(order, str)
        check_type(attribute, str)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-CALLER-ID" in headers:
                check_type(headers.get("X-CALLER-ID"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "startTime": start_time,
            "endTime": end_time,
            "trendInterval": trend_interval,
            "limit": limit,
            "offset": offset,
            "order": order,
            "attribute": attribute,
        }
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

        e_url = (
            "/dna/data/api/v1/transitNetworkHealthSummaries/{id}/tren" + "dAnalytics"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_b57676da2385a4bb7c6e5dc9b8a89dc_v3_1_3_0", json_data
        )

    def read_list_of_virtual_networks_with_their_health_summary(
        self,
        attribute=None,
        end_time=None,
        id=None,
        limit=None,
        offset=None,
        order=None,
        site_hierarchy=None,
        site_hierarchy_id=None,
        sort_by=None,
        start_time=None,
        view=None,
        vn_layer=None,
        headers=None,
        **request_parameters
    ):
        """Get a paginated list of Virtual Networks with health summary. Layer 2 Virtual Networks are only included in
        health reporting for EVPN protocol deployments. The special Layer 3 VN called ‘INFRA_VN’ is also not
        included for user access through Assurance virtualNetworkHealthSummaries APIS. Please find INFRA_VN
        related health metrics under /data/api/v1/fabricSiteHealthSummaries (Ex: attributes
        ‘pubsubInfraVnGoodHealthPercentage’ and ‘bgpPeerInfraVnScoreGoodHealthPercentage’). This API provides
        the latest health data until the given `endTime`. If data is not ready for the provided endTime, the
        request will fail with error code `400 Bad Request`, and the error message will indicate the recommended
        endTime to use to retrieve a complete data set. This behavior may occur if the provided
        endTime=currentTime, since we are not a real time system. When `endTime` is not provided, the API
        returns the latest data. For detailed information about the usage of the API, please refer to the Open
        API specification document https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-virtualNetworkHealthSummaries-1.0.1-resolved.yaml .

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
            id(str): id query parameter. The list of entity Uuids. (Ex."6bef213c-19ca-4170-8375-b694e251101c")
                Examples: id=6bef213c-19ca-4170-8375-b694e251101c (single entity uuid requested) id=6bef
                213c-19ca-4170-8375-b694e251101c&id=32219612-819e-4b5e-a96b-cf22aca13dd9&id=2541e9a7-
                b80d-4955-8aa2-79b233318ba0 (multiple entity uuid with '&' separator) .
            vn_layer(str): vnLayer query parameter. VN Layer information covering Layer 3 or Layer 2 VNs. .
            attribute(str): attribute query parameter. The interested fields in the request. For valid attributes,
                verify the documentation. .
            view(str): view query parameter. The specific summary view being requested. This is an optional
                parameter which can be passed to get one or more of the specific health data summaries
                associated with virtual networks. .
            site_hierarchy(str): siteHierarchy query parameter. The full hierarchical breakdown of the site tree
                starting from Global site name and ending with the specific site name. The Root site is
                named "Global" (Ex. `Global/AreaName/BuildingName/FloorName`)          This field
                supports wildcard asterisk (`*`) character search support. E.g. `*/San*, */San, /San*`
                Examples:          `?siteHierarchy=Global/AreaName/BuildingName/FloorName` (single
                siteHierarchy requested)          `?siteHierarchy=Global/AreaName/BuildingName/FloorName
                &siteHierarchy=Global/AreaName2/BuildingName2/FloorName2` (multiple siteHierarchies
                requested) .
            site_hierarchy_id(str): SiteHierarchyId query parameter. The full hierarchy breakdown of the site tree
                in id form starting from Global site UUID and ending with the specific site UUID. (Ex.
                `globalUuid/areaUuid/buildingUuid/floorUuid`)          This field supports wildcard
                asterisk (`*`) character search support. E.g. `*uuid*, *uuid, uuid*`          Examples:
                `?siteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid `(single siteHierarchyId
                requested)          `?siteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid&siteHie
                rarchyId=globalUuid/areaUuid2/buildingUuid2/floorUuid2` (multiple siteHierarchyIds
                requested) .
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
            https://developer.cisco.com/docs/dna-center/#!read-list-of-virtual-networks-with-their-health-summary
        """
        check_type(headers, dict)
        check_type(start_time, int)
        check_type(end_time, int)
        check_type(limit, int)
        check_type(offset, int)
        check_type(sort_by, str)
        check_type(order, str)
        check_type(id, str)
        check_type(vn_layer, str)
        check_type(attribute, str)
        check_type(view, str)
        check_type(site_hierarchy, str)
        check_type(site_hierarchy_id, str)
        if headers is not None:
            if "X-CALLER-ID" in headers:
                check_type(headers.get("X-CALLER-ID"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "startTime": start_time,
            "endTime": end_time,
            "limit": limit,
            "offset": offset,
            "sortBy": sort_by,
            "order": order,
            "id": id,
            "vnLayer": vn_layer,
            "attribute": attribute,
            "view": view,
            "siteHierarchy": site_hierarchy,
            "SiteHierarchyId": site_hierarchy_id,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/virtualNetworkHealthSummaries"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a89a96bc132d58d5abc0bdf4d3868b42_v3_1_3_0", json_data
        )

    def read_virtual_networks_count(
        self,
        end_time=None,
        id=None,
        site_hierarchy=None,
        site_hierarchy_id=None,
        start_time=None,
        vn_layer=None,
        headers=None,
        **request_parameters
    ):
        """Get a count of virtual networks. Use available query parameters to get the count of a subset of virtual
        networks. Layer 2 Virtual Networks are only included for EVPN protocol deployments. The special Layer 3
        VN called ‘INFRA_VN’ is also not included. This API provides the latest health data until the given
        `endTime`. If data is not ready for the provided endTime, the request will fail with error code `400 Bad
        Request`, and the error message will indicate the recommended endTime to use to retrieve a complete data
        set. This behavior may occur if the provided endTime=currentTime, since we are not a real time system.
        When `endTime` is not provided, the API returns the latest data. For detailed information about the
        usage of the API, please refer to the Open API specification document https://github.com/cisco-en-
        programmability/catalyst-center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-
        virtualNetworkHealthSummaries-1.0.1-resolved.yaml .

        Args:
            start_time(int): startTime query parameter. Start time from which API queries the data set related to
                the resource. It must be specified in UNIX epochtime in milliseconds. Value is
                inclusive. .
            end_time(int): endTime query parameter. End time to which API queries the data set related to the
                resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive. .
            id(str): id query parameter. The list of entity Uuids. (Ex."6bef213c-19ca-4170-8375-b694e251101c")
                Examples: id=6bef213c-19ca-4170-8375-b694e251101c (single entity uuid requested) id=6bef
                213c-19ca-4170-8375-b694e251101c&id=32219612-819e-4b5e-a96b-cf22aca13dd9&id=2541e9a7-
                b80d-4955-8aa2-79b233318ba0 (multiple entity uuid with '&' separator) .
            vn_layer(str): vnLayer query parameter. VN Layer information covering Layer 3 or Layer 2 VNs. .
            site_hierarchy(str): siteHierarchy query parameter. The full hierarchical breakdown of the site tree
                starting from Global site name and ending with the specific site name. The Root site is
                named "Global" (Ex. `Global/AreaName/BuildingName/FloorName`)          This field
                supports wildcard asterisk (`*`) character search support. E.g. `*/San*, */San, /San*`
                Examples:          `?siteHierarchy=Global/AreaName/BuildingName/FloorName` (single
                siteHierarchy requested)          `?siteHierarchy=Global/AreaName/BuildingName/FloorName
                &siteHierarchy=Global/AreaName2/BuildingName2/FloorName2` (multiple siteHierarchies
                requested) .
            site_hierarchy_id(str): siteHierarchyId query parameter. The full hierarchy breakdown of the site tree
                in id form starting from Global site UUID and ending with the specific site UUID. (Ex.
                `globalUuid/areaUuid/buildingUuid/floorUuid`)          This field supports wildcard
                asterisk (`*`) character search support. E.g. `*uuid*, *uuid, uuid*`          Examples:
                `?siteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid `(single siteHierarchyId
                requested)          `?siteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid&siteHie
                rarchyId=globalUuid/areaUuid2/buildingUuid2/floorUuid2` (multiple siteHierarchyIds
                requested) .
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
            https://developer.cisco.com/docs/dna-center/#!read-virtual-networks-count
        """
        check_type(headers, dict)
        check_type(start_time, int)
        check_type(end_time, int)
        check_type(id, str)
        check_type(vn_layer, str)
        check_type(site_hierarchy, str)
        check_type(site_hierarchy_id, str)
        if headers is not None:
            if "X-CALLER-ID" in headers:
                check_type(headers.get("X-CALLER-ID"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "startTime": start_time,
            "endTime": end_time,
            "id": id,
            "vnLayer": vn_layer,
            "siteHierarchy": site_hierarchy,
            "siteHierarchyId": site_hierarchy_id,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/virtualNetworkHealthSummaries/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_eb1c33328c25d25b062bc85609b23df_v3_1_3_0", json_data
        )

    def read_virtual_network_with_its_health_summary_from_id(
        self,
        id,
        attribute=None,
        end_time=None,
        start_time=None,
        view=None,
        headers=None,
        **request_parameters
    ):
        """Get health summary for a specific Virtual Network by providing the unique virtual networks id in the url path.
        L2 Virtual Networks are only included in health reporting for EVPN protocol deployments. The special
        Layer 3 VN called ‘INFRA_VN’ is also not included for user access through Assurance
        virtualNetworkHealthSummaries APIS. Please find INFRA_VN related health metrics under
        /data/api/v1/fabricSiteHealthSummaries (Ex: attributes ‘pubsubInfraVnGoodHealthPercentage’ and
        ‘bgpPeerInfraVnScoreGoodHealthPercentage’). This API provides the latest health data until the given
        `endTime`. If data is not ready for the provided endTime, the request will fail with error code `400 Bad
        Request`, and the error message will indicate the recommended endTime to use to retrieve a complete data
        set. This behavior may occur if the provided endTime=currentTime, since we are not a real time system.
        When `endTime` is not provided, the API returns the latest data. For detailed information about the
        usage of the API, please refer to the Open API specification document https://github.com/cisco-en-
        programmability/catalyst-center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-
        virtualNetworkHealthSummaries-1.0.1-resolved.yaml .

        Args:
            id(str): id path parameter. unique virtual networks id .
            end_time(int): endTime query parameter. End time to which API queries the data set related to the
                resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive. .
            start_time(int): startTime query parameter. Start time from which API queries the data set related to
                the resource. It must be specified in UNIX epochtime in milliseconds. Value is
                inclusive. .
            attribute(str): attribute query parameter. The interested fields in the request. For valid attributes,
                verify the documentation. .
            view(str): view query parameter. The specific summary view being requested. This is an optional
                parameter which can be passed to get one or more of the specific health data summaries
                associated with virtual networks. .
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
            https://developer.cisco.com/docs/dna-center/#!read-virtual-network-with-its-health-summary-from-id
        """
        check_type(headers, dict)
        check_type(end_time, int)
        check_type(start_time, int)
        check_type(attribute, str)
        check_type(view, str)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-CALLER-ID" in headers:
                check_type(headers.get("X-CALLER-ID"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "endTime": end_time,
            "startTime": start_time,
            "attribute": attribute,
            "view": view,
        }
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

        e_url = "/dna/data/api/v1/virtualNetworkHealthSummaries/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_bbb30e8498ac5c8f8bcb5c5fd33cff43_v3_1_3_0", json_data
        )

    def the_trend_analytics_data_for_a_virtual_network_in_the_specified_time_range(
        self,
        id,
        trend_interval,
        attribute=None,
        end_time=None,
        limit=None,
        offset=None,
        order=None,
        start_time=None,
        headers=None,
        **request_parameters
    ):
        """Get health time series for a specific Virtual Network by providing the unique Virtual Network id in the url
        path. Layer 2 Virtual Networks are only included in health reporting for EVPN protocol deployments. The
        special Layer 3 VN called ‘INFRA_VN’ is also not included for user access through Assurance
        virtualNetworkHealthSummaries APIS. The data will be grouped based on the specified trend time interval.
        If startTime and endTime are not provided, the API defaults to the last 24 hours. By default: the number
        of records returned will be 500. the records will be sorted in time ascending (`asc`) order For EVPN ,
        {id} is a combination of VN:FabrisiteId. ex: L2VN1:93a25378-7740-4e20-8d90-0060ad9a1be0 This API
        provides the latest health data until the given `endTime`. If data is not ready for the provided
        endTime, the request will fail with error code `400 Bad Request`, and the error message will indicate
        the recommended endTime to use to retrieve a complete data set. This behavior may occur if the provided
        endTime=currentTime, since we are not a real time system. When `endTime` is not provided, the API
        returns the latest data. For detailed information about the usage of the API, please refer to the Open
        API specification document https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-virtualNetworkHealthSummaries-1.0.1-resolved.yaml .

        Args:
            id(str): id path parameter. unique virtual network id .
            start_time(int): startTime query parameter. Start time from which API queries the data set related to
                the resource. It must be specified in UNIX epochtime in milliseconds. Value is
                inclusive. .
            end_time(int): endTime query parameter. End time to which API queries the data set related to the
                resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive. .
            trend_interval(str): trendInterval query parameter. The time window to aggregate the metrics. Interval
                can be 5 minutes or 10 minutes or 1 hour or 1 day or 7 days .
            limit(int): limit query parameter. Maximum number of records to return .
            offset(int): offset query parameter. Specifies the starting point within all records returned by the
                API. It's one based offset. The starting value is 1. .
            order(str): order query parameter. The sort order of the field ascending or descending. .
            attribute(str): attribute query parameter. The interested fields in the request. For valid attributes,
                verify the documentation. .
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
            https://developer.cisco.com/docs/dna-center/#!the-trend-analytics-data-for-a-virtual-network-in-the-specified-time-range
        """
        check_type(headers, dict)
        check_type(start_time, int)
        check_type(end_time, int)
        check_type(trend_interval, str, may_be_none=False)
        check_type(limit, int)
        check_type(offset, int)
        check_type(order, str)
        check_type(attribute, str)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-CALLER-ID" in headers:
                check_type(headers.get("X-CALLER-ID"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "startTime": start_time,
            "endTime": end_time,
            "trendInterval": trend_interval,
            "limit": limit,
            "offset": offset,
            "order": order,
            "attribute": attribute,
        }
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

        e_url = (
            "/dna/data/api/v1/virtualNetworkHealthSummaries/{id}/tren" + "dAnalytics"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_f73065603c85196a35142243bc48509_v3_1_3_0", json_data
        )

    def get_default_authentication_profile(
        self,
        site_name_hierarchy,
        authenticate_template_name=None,
        headers=None,
        **request_parameters
    ):
        """Get default authentication profile from SDA Fabric .

        Args:
            site_name_hierarchy(str): siteNameHierarchy query parameter.
            authenticate_template_name(str): authenticateTemplateName query parameter.
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
            https://developer.cisco.com/docs/dna-center/#!get-default-authentication-profile-from-s-d-a-fabric
        """
        check_type(headers, dict)
        check_type(site_name_hierarchy, str, may_be_none=False)
        check_type(authenticate_template_name, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "siteNameHierarchy": site_name_hierarchy,
            "authenticateTemplateName": authenticate_template_name,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/business/sda/authentication-profile"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_e414dcbeeabd5a359352a0e2ad5ec3f5_v3_1_3_0", json_data
        )

    def add_default_authentication_profile(
        self, headers=None, payload=None, active_validation=True, **request_parameters
    ):
        """Add default authentication template in SDA Fabric .

        Args:
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
            https://developer.cisco.com/docs/dna-center/#!add-default-authentication-template-in-s-d-a-fabric
        """
        check_type(headers, dict)
        check_type(payload, list)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = payload or []
        if active_validation:
            self._request_validator(
                "jsd_d1d42ef2f1895a82a2830bf1353e6baa_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/business/sda/authentication-profile"
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
            "bpm_d1d42ef2f1895a82a2830bf1353e6baa_v3_1_3_0", json_data
        )

    def update_default_authentication_profile(
        self, headers=None, payload=None, active_validation=True, **request_parameters
    ):
        """Update default authentication profile in SDA Fabric .

        Args:
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
            https://developer.cisco.com/docs/dna-center/#!update-default-authentication-profile-in-s-d-a-fabric
        """
        check_type(headers, dict)
        check_type(payload, list)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = payload or []
        if active_validation:
            self._request_validator(
                "jsd_d999a1d36ee52babb6b619877dad734_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/business/sda/authentication-profile"
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
            "bpm_d999a1d36ee52babb6b619877dad734_v3_1_3_0", json_data
        )

    def delete_default_authentication_profile(
        self, site_name_hierarchy, headers=None, **request_parameters
    ):
        """Delete default authentication profile in SDA Fabric .

        Args:
            site_name_hierarchy(str): siteNameHierarchy query parameter.
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
            https://developer.cisco.com/docs/dna-center/#!delete-default-authentication-profile-from-s-d-a-fabric
        """
        check_type(headers, dict)
        check_type(site_name_hierarchy, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "siteNameHierarchy": site_name_hierarchy,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/business/sda/authentication-profile"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_b2be8b5dda8b81620b903afe9f_v3_1_3_0", json_data
        )

    def adds_border_device(
        self, headers=None, payload=None, active_validation=True, **request_parameters
    ):
        """Add border device in SDA Fabric .

        Args:
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
            https://developer.cisco.com/docs/dna-center/#!add-border-device-in-s-d-a-fabric
        """
        check_type(headers, dict)
        check_type(payload, list)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = payload or []
        if active_validation:
            self._request_validator(
                "jsd_b6f2d8e46cdd5f05bb06f52cd1b26fb2_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/business/sda/border-device"
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
            "bpm_b6f2d8e46cdd5f05bb06f52cd1b26fb2_v3_1_3_0", json_data
        )

    def gets_border_device_detail(
        self, device_management_ip_address, headers=None, **request_parameters
    ):
        """Get border device detail from SDA Fabric .

        Args:
            device_management_ip_address(str): deviceManagementIpAddress query parameter.
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
            https://developer.cisco.com/docs/dna-center/#!get-border-device-detail-from-s-d-a-fabric
        """
        check_type(headers, dict)
        check_type(device_management_ip_address, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "deviceManagementIpAddress": device_management_ip_address,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/business/sda/border-device"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_aae881ff75d5488a5325ea949be4c5b_v3_1_3_0", json_data
        )

    def deletes_border_device(
        self, device_management_ip_address, headers=None, **request_parameters
    ):
        """Delete border device from SDA Fabric .

        Args:
            device_management_ip_address(str): deviceManagementIpAddress query parameter.
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
            https://developer.cisco.com/docs/dna-center/#!delete-border-device-from-s-d-a-fabric
        """
        check_type(headers, dict)
        check_type(device_management_ip_address, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "deviceManagementIpAddress": device_management_ip_address,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/business/sda/border-device"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a102ba155e35f84b7af3396aa407d02_v3_1_3_0", json_data
        )

    def delete_control_plane_device(
        self, device_management_ip_address, headers=None, **request_parameters
    ):
        """Delete control plane device in SDA Fabric .

        Args:
            device_management_ip_address(str): deviceManagementIpAddress query parameter.
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
            https://developer.cisco.com/docs/dna-center/#!delete-control-plane-device-in-s-d-a-fabric
        """
        check_type(headers, dict)
        check_type(device_management_ip_address, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "deviceManagementIpAddress": device_management_ip_address,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/business/sda/control-plane-device"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c05702ed7075a2f9ab14c051f1ac883_v3_1_3_0", json_data
        )

    def get_control_plane_device(
        self, device_management_ip_address, headers=None, **request_parameters
    ):
        """Get control plane device from SDA Fabric .

        Args:
            device_management_ip_address(str): deviceManagementIpAddress query parameter.
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
            https://developer.cisco.com/docs/dna-center/#!get-control-plane-device-from-s-d-a-fabric
        """
        check_type(headers, dict)
        check_type(device_management_ip_address, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "deviceManagementIpAddress": device_management_ip_address,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/business/sda/control-plane-device"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c1a89e4a8ff15608bc6c10d7ef7389d7_v3_1_3_0", json_data
        )

    def add_control_plane_device(
        self,
        deviceManagementIpAddress=None,
        routeDistributionProtocol=None,
        siteNameHierarchy=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Add control plane device in SDA Fabric .

        Args:
            deviceManagementIpAddress(string): SDA's Management Ip Address of the Device which is provisioned
                successfully .
            routeDistributionProtocol(string): SDA's Route Distribution Protocol for Control Plane Device. Allowed
                values are "LISP_BGP" or "LISP_PUB_SUB". Default value is "LISP_BGP" .
            siteNameHierarchy(string): SDA's siteNameHierarchy of the Provisioned Device(site should be part of
                Fabric Site) .
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
            https://developer.cisco.com/docs/dna-center/#!add-control-plane-device-in-s-d-a-fabric
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
            "deviceManagementIpAddress": deviceManagementIpAddress,
            "siteNameHierarchy": siteNameHierarchy,
            "routeDistributionProtocol": routeDistributionProtocol,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_ae7f02a3d051f2baf7cc087990d658_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/business/sda/control-plane-device"
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
            "bpm_ae7f02a3d051f2baf7cc087990d658_v3_1_3_0", json_data
        )

    def get_device_info(
        self, device_management_ip_address, headers=None, **request_parameters
    ):
        """Get device info from SDA Fabric .

        Args:
            device_management_ip_address(str): deviceManagementIpAddress query parameter.
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
            https://developer.cisco.com/docs/dna-center/#!get-device-info-from-s-d-a-fabric
        """
        check_type(headers, dict)
        check_type(device_management_ip_address, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "deviceManagementIpAddress": device_management_ip_address,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/business/sda/device"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_d12790f461c553a08142ec740db5efbf_v3_1_3_0", json_data
        )

    def get_device_role_in_sda_fabric(
        self, device_management_ip_address, headers=None, **request_parameters
    ):
        """Get device role in SDA Fabric .

        Args:
            device_management_ip_address(str): deviceManagementIpAddress query parameter. Device Management IP
                Address .
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
            https://developer.cisco.com/docs/dna-center/#!get-device-role-in-s-d-a-fabric
        """
        check_type(headers, dict)
        check_type(device_management_ip_address, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "deviceManagementIpAddress": device_management_ip_address,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/business/sda/device/role"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ea24b22ce355a229b7fd067401ddf3a_v3_1_3_0", json_data
        )

    def add_edge_device(
        self,
        deviceManagementIpAddress=None,
        siteNameHierarchy=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Add edge device in SDA Fabric .

        Args:
            deviceManagementIpAddress(string): SDA's Management Ip Address of the Device which is provisioned
                successfully .
            siteNameHierarchy(string): SDA's siteNameHierarchy of the Provisioned Device(site should be part of
                Fabric Site) .
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
            https://developer.cisco.com/docs/dna-center/#!add-edge-device-in-s-d-a-fabric
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
            "deviceManagementIpAddress": deviceManagementIpAddress,
            "siteNameHierarchy": siteNameHierarchy,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_e0c7b28d55c85d49a84c1403ca14bd5f_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/business/sda/edge-device"
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
            "bpm_e0c7b28d55c85d49a84c1403ca14bd5f_v3_1_3_0", json_data
        )

    def delete_edge_device(
        self, device_management_ip_address, headers=None, **request_parameters
    ):
        """Delete edge device from SDA Fabric. .

        Args:
            device_management_ip_address(str): deviceManagementIpAddress query parameter.
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
            https://developer.cisco.com/docs/dna-center/#!delete-edge-device-from-s-d-a-fabric
        """
        check_type(headers, dict)
        check_type(device_management_ip_address, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "deviceManagementIpAddress": device_management_ip_address,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/business/sda/edge-device"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_b70d8c6f85254a053ab281fd9e8fc_v3_1_3_0", json_data
        )

    def get_edge_device(
        self, device_management_ip_address, headers=None, **request_parameters
    ):
        """Get edge device from SDA Fabric .

        Args:
            device_management_ip_address(str): deviceManagementIpAddress query parameter.
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
            https://developer.cisco.com/docs/dna-center/#!get-edge-device-from-s-d-a-fabric
        """
        check_type(headers, dict)
        check_type(device_management_ip_address, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "deviceManagementIpAddress": device_management_ip_address,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/business/sda/edge-device"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a2ee396d6595001acfbbcdfa25093ff_v3_1_3_0", json_data
        )

    def get_site(self, site_name_hierarchy, headers=None, **request_parameters):
        """Get Site info from SDA Fabric .

        Args:
            site_name_hierarchy(str): siteNameHierarchy query parameter. Site Name Hierarchy .
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
            https://developer.cisco.com/docs/dna-center/#!get-site-from-s-d-a-fabric
        """
        check_type(headers, dict)
        check_type(site_name_hierarchy, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "siteNameHierarchy": site_name_hierarchy,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/business/sda/fabric-site"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_d23f3e54f8c59caac3ca905f7bf543a_v3_1_3_0", json_data
        )

    def delete_site(self, site_name_hierarchy, headers=None, **request_parameters):
        """Delete Site from SDA Fabric .

        Args:
            site_name_hierarchy(str): siteNameHierarchy query parameter. Site Name Hierarchy .
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
            https://developer.cisco.com/docs/dna-center/#!delete-site-from-s-d-a-fabric
        """
        check_type(headers, dict)
        check_type(site_name_hierarchy, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "siteNameHierarchy": site_name_hierarchy,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/business/sda/fabric-site"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_f9db3b115f0b8c8b3ce14bc5f975_v3_1_3_0", json_data
        )

    def add_site(
        self,
        fabricName=None,
        fabricType=None,
        siteNameHierarchy=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Add Site in SDA Fabric .

        Args:
            fabricName(string): SDA's Warning Starting Catalyst Center 2.2.3.5 release, this field has been deprecated.
                SD-Access Fabric does not need it anymore.  It will be removed in future Catalyst Center
                releases. .
            fabricType(string): SDA's Type of SD-Access Fabric. Allowed values are "FABRIC_SITE" or "FABRIC_ZONE".
                Default value is "FABRIC_SITE". .
            siteNameHierarchy(string): SDA's Existing site name hierarchy available at global level. For Example
                "Global/Chicago/Building21/Floor1" .
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
            https://developer.cisco.com/docs/dna-center/#!add-site-in-s-d-a-fabric
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
            "fabricName": fabricName,
            "siteNameHierarchy": siteNameHierarchy,
            "fabricType": fabricType,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_a764c85d8df5c30b9143619d4f9cde9_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/business/sda/fabric-site"
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
            "bpm_a764c85d8df5c30b9143619d4f9cde9_v3_1_3_0", json_data
        )

    def add_port_assignment_for_access_point(
        self,
        authenticateTemplateName=None,
        dataIpAddressPoolName=None,
        deviceManagementIpAddress=None,
        interfaceDescription=None,
        interfaceName=None,
        siteNameHierarchy=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Add Port assignment for access point in SDA Fabric .

        Args:
            authenticateTemplateName(string): SDA's Authenticate TemplateName associated to Fabric Site . Available
                values are 'No Authentication', 'Open Authentication', 'Closed Authentication ' and 'Low
                Impact '.
            dataIpAddressPoolName(string): SDA's Ip Pool Name, that is assigned to INFRA_VN .
            deviceManagementIpAddress(string): SDA's Management Ip Address of the edge device .
            interfaceDescription(string): SDA's Details or note of interface port assignment .
            interfaceName(string): SDA's Interface Name of the edge device .
            siteNameHierarchy(string): SDA's Path of sda Fabric Site .
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
            https://developer.cisco.com/docs/dna-center/#!add-port-assignment-for-access-point-in-s-d-a-fabric
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
            "siteNameHierarchy": siteNameHierarchy,
            "deviceManagementIpAddress": deviceManagementIpAddress,
            "interfaceName": interfaceName,
            "dataIpAddressPoolName": dataIpAddressPoolName,
            "authenticateTemplateName": authenticateTemplateName,
            "interfaceDescription": interfaceDescription,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_e4a09bf566f35babad9e27f5eb61a86d_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/business/sda/hostonboarding/access-" + "point"
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
            "bpm_e4a09bf566f35babad9e27f5eb61a86d_v3_1_3_0", json_data
        )

    def delete_port_assignment_for_access_point(
        self,
        device_management_ip_address,
        interface_name,
        headers=None,
        **request_parameters
    ):
        """Delete Port assignment for access point in SDA Fabric .

        Args:
            device_management_ip_address(str): deviceManagementIpAddress query parameter.
            interface_name(str): interfaceName query parameter.
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
            https://developer.cisco.com/docs/dna-center/#!delete-port-assignment-for-access-point-in-s-d-a-fabric
        """
        check_type(headers, dict)
        check_type(device_management_ip_address, str, may_be_none=False)
        check_type(interface_name, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "deviceManagementIpAddress": device_management_ip_address,
            "interfaceName": interface_name,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/business/sda/hostonboarding/access-" + "point"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_bd26b08b64545bae20f60c56891576_v3_1_3_0", json_data
        )

    def get_port_assignment_for_access_point(
        self,
        device_management_ip_address,
        interface_name,
        headers=None,
        **request_parameters
    ):
        """Get Port assignment for access point in SDA Fabric .

        Args:
            device_management_ip_address(str): deviceManagementIpAddress query parameter.
            interface_name(str): interfaceName query parameter.
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
            https://developer.cisco.com/docs/dna-center/#!get-port-assignment-for-access-point-in-s-d-a-fabric
        """
        check_type(headers, dict)
        check_type(device_management_ip_address, str, may_be_none=False)
        check_type(interface_name, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "deviceManagementIpAddress": device_management_ip_address,
            "interfaceName": interface_name,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/business/sda/hostonboarding/access-" + "point"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_b035b0b3b60b5f2bb7c8c82e7f94b63b_v3_1_3_0", json_data
        )

    def delete_port_assignment_for_user_device(
        self,
        device_management_ip_address,
        interface_name,
        headers=None,
        **request_parameters
    ):
        """Delete Port assignment for user device in SDA Fabric. .

        Args:
            device_management_ip_address(str): deviceManagementIpAddress query parameter.
            interface_name(str): interfaceName query parameter.
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
            https://developer.cisco.com/docs/dna-center/#!delete-port-assignment-for-user-device-in-s-d-a-fabric
        """
        check_type(headers, dict)
        check_type(device_management_ip_address, str, may_be_none=False)
        check_type(interface_name, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "deviceManagementIpAddress": device_management_ip_address,
            "interfaceName": interface_name,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/business/sda/hostonboarding/user-" + "device"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_cb88b50dd5ead96ecfb4ab0390f47_v3_1_3_0", json_data
        )

    def add_port_assignment_for_user_device(
        self,
        authenticateTemplateName=None,
        dataIpAddressPoolName=None,
        deviceManagementIpAddress=None,
        interfaceDescription=None,
        interfaceName=None,
        interfaceNames=None,
        scalableGroupName=None,
        siteNameHierarchy=None,
        voiceIpAddressPoolName=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Add Port assignment for user device in SDA Fabric. .

        Args:
            authenticateTemplateName(string): SDA's Authenticate TemplateName associated with siteNameHierarchy .
                Available values are 'Open Authentication', 'Closed Authentication', 'Low Impact' and
                'No Authentication'.
            dataIpAddressPoolName(string): SDA's Ip Pool Name, that is assigned to virtual network with traffic type
                as DATA(can't be empty if voiceIpAddressPoolName is empty) .
            deviceManagementIpAddress(string): SDA's Management Ip Address of the Edge Node Device. .
            interfaceDescription(string): SDA's User defined text message for port assignment .
            interfaceName(string): SDA's Interface Name on the Edge Node Device. .
            interfaceNames(list): SDA's List of Interface Names on the Edge Node Device.
                E.g.["GigabitEthernet1/0/3","GigabitEthernet1/0/4"]  (list of strings).
            scalableGroupName(string): SDA's Scalable Group name associated with VN .
            siteNameHierarchy(string): SDA's Complete Path of SD-Access Fabric Site. .
            voiceIpAddressPoolName(string): SDA's Ip Pool Name, that is assigned to virtual network with traffic
                type as VOICE(can't be empty if dataIpAddressPoolName is empty) .
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
            https://developer.cisco.com/docs/dna-center/#!add-port-assignment-for-user-device-in-s-d-a-fabric
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
            "siteNameHierarchy": siteNameHierarchy,
            "deviceManagementIpAddress": deviceManagementIpAddress,
            "interfaceName": interfaceName,
            "interfaceNames": interfaceNames,
            "dataIpAddressPoolName": dataIpAddressPoolName,
            "voiceIpAddressPoolName": voiceIpAddressPoolName,
            "authenticateTemplateName": authenticateTemplateName,
            "scalableGroupName": scalableGroupName,
            "interfaceDescription": interfaceDescription,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_af29516f0c8591da2a92523b5ab3386_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/business/sda/hostonboarding/user-" + "device"
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
            "bpm_af29516f0c8591da2a92523b5ab3386_v3_1_3_0", json_data
        )

    def get_port_assignment_for_user_device(
        self,
        device_management_ip_address,
        interface_name,
        headers=None,
        **request_parameters
    ):
        """Get Port assignment for user device in SDA Fabric. .

        Args:
            device_management_ip_address(str): deviceManagementIpAddress query parameter.
            interface_name(str): interfaceName query parameter.
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
            https://developer.cisco.com/docs/dna-center/#!get-port-assignment-for-user-device-in-s-d-a-fabric
        """
        check_type(headers, dict)
        check_type(device_management_ip_address, str, may_be_none=False)
        check_type(interface_name, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "deviceManagementIpAddress": device_management_ip_address,
            "interfaceName": interface_name,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/business/sda/hostonboarding/user-" + "device"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a446d7327733580e9a6b661715eb4c09_v3_1_3_0", json_data
        )

    def add_multicast_in_sda_fabric(
        self,
        multicastMethod=None,
        multicastType=None,
        multicastVnInfo=None,
        siteNameHierarchy=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Add multicast in SDA fabric .

        Args:
            multicastMethod(string): SDA's Multicast Method . Available values are 'native_multicast'.
            multicastType(string): SDA's Multicast Type . Available values are 'ssm', 'asm_with_internal_rp' and
                'asm_with_external_rp'.
            multicastVnInfo(list): SDA's multicastVnInfo (list of objects).
            siteNameHierarchy(string): SDA's Full path of sda Fabric Site .
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
            https://developer.cisco.com/docs/dna-center/#!add-multicast-in-s-d-a-fabric
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
            "siteNameHierarchy": siteNameHierarchy,
            "multicastMethod": multicastMethod,
            "multicastType": multicastType,
            "multicastVnInfo": multicastVnInfo,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_b7079a38844e56dd8f1b6b876880a02e_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/business/sda/multicast"
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
            "bpm_b7079a38844e56dd8f1b6b876880a02e_v3_1_3_0", json_data
        )

    def get_multicast_details_from_sda_fabric(
        self, site_name_hierarchy, headers=None, **request_parameters
    ):
        """Get multicast details from SDA fabric .

        Args:
            site_name_hierarchy(str): siteNameHierarchy query parameter. fabric site name hierarchy .
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
            https://developer.cisco.com/docs/dna-center/#!get-multicast-details-from-s-d-a-fabric
        """
        check_type(headers, dict)
        check_type(site_name_hierarchy, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "siteNameHierarchy": site_name_hierarchy,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/business/sda/multicast"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c27bbb42365955bc210924e1362c34_v3_1_3_0", json_data
        )

    def delete_multicast_from_sda_fabric(
        self, site_name_hierarchy, headers=None, **request_parameters
    ):
        """Delete multicast from SDA fabric .

        Args:
            site_name_hierarchy(str): siteNameHierarchy query parameter.
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
            https://developer.cisco.com/docs/dna-center/#!delete-multicast-from-s-d-a-fabric
        """
        check_type(headers, dict)
        check_type(site_name_hierarchy, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "siteNameHierarchy": site_name_hierarchy,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/business/sda/multicast"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_e8e007d3e25f7fb83a6579016aea72_v3_1_3_0", json_data
        )

    def delete_provisioned_wired_device(
        self, device_management_ip_address, headers=None, **request_parameters
    ):
        """Delete provisioned Wired Device .

        Args:
            device_management_ip_address(str): deviceManagementIpAddress query parameter. Valid IP address of the
                device currently provisioned in a fabric site .
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
            https://developer.cisco.com/docs/dna-center/#!delete-provisioned-wired-device
        """
        check_type(headers, dict)
        check_type(device_management_ip_address, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "deviceManagementIpAddress": device_management_ip_address,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/business/sda/provision-device"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_e5bd8dbbf65253f0aadd77a62b1b8b58_v3_1_3_0", json_data
        )

    def re_provision_wired_device(
        self,
        deviceManagementIpAddress=None,
        siteNameHierarchy=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Re-Provision Wired Device .

        Args:
            deviceManagementIpAddress(string): SDA's Management Ip Address of the device to be re-provisioned .
            siteNameHierarchy(string): SDA's siteNameHierarchy of the provisioned device .
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
            https://developer.cisco.com/docs/dna-center/#!re-provision-wired-device
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
            "deviceManagementIpAddress": deviceManagementIpAddress,
            "siteNameHierarchy": siteNameHierarchy,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_fd488ff002115f3b8f0ee165e5347609_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/business/sda/provision-device"
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
            "bpm_fd488ff002115f3b8f0ee165e5347609_v3_1_3_0", json_data
        )

    def provision_wired_device(
        self,
        deviceManagementIpAddress=None,
        siteNameHierarchy=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Provision Wired Device .

        Args:
            deviceManagementIpAddress(string): SDA's Management Ip Address of the device to be provisioned .
            siteNameHierarchy(string): SDA's Site Name Hierarchy for device location(only building / floor level) .
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
            https://developer.cisco.com/docs/dna-center/#!provision-wired-device
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
            "deviceManagementIpAddress": deviceManagementIpAddress,
            "siteNameHierarchy": siteNameHierarchy,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_d1608b2751c883a072ee3fb80228_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/business/sda/provision-device"
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
            "bpm_d1608b2751c883a072ee3fb80228_v3_1_3_0", json_data
        )

    def get_provisioned_wired_device(
        self, device_management_ip_address, headers=None, **request_parameters
    ):
        """Get Provisioned Wired Device .

        Args:
            device_management_ip_address(str): deviceManagementIpAddress query parameter.
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
            https://developer.cisco.com/docs/dna-center/#!get-provisioned-wired-device
        """
        check_type(headers, dict)
        check_type(device_management_ip_address, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "deviceManagementIpAddress": device_management_ip_address,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/business/sda/provision-device"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_d8f10868c21856eab31776f109aba2bb_v3_1_3_0", json_data
        )

    def delete_transit_peer_network(
        self, transit_peer_network_name, headers=None, **request_parameters
    ):
        """Delete Transit Peer Network from SD-Access .

        Args:
            transit_peer_network_name(str): transitPeerNetworkName query parameter. Transit Peer Network Name .
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
            https://developer.cisco.com/docs/dna-center/#!delete-transit-peer-network
        """
        check_type(headers, dict)
        check_type(transit_peer_network_name, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "transitPeerNetworkName": transit_peer_network_name,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/business/sda/transit-peer-network"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a34aab91750028f4d584d36811844_v3_1_3_0", json_data
        )

    def get_transit_peer_network_info(
        self, transit_peer_network_name, headers=None, **request_parameters
    ):
        """Get Transit Peer Network Info from SD-Access .

        Args:
            transit_peer_network_name(str): transitPeerNetworkName query parameter. Transit or Peer Network Name .
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
            https://developer.cisco.com/docs/dna-center/#!get-transit-peer-network-info
        """
        check_type(headers, dict)
        check_type(transit_peer_network_name, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "transitPeerNetworkName": transit_peer_network_name,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/business/sda/transit-peer-network"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_d39e10793a45d3db229d6d3820c665a_v3_1_3_0", json_data
        )

    def add_transit_peer_network(
        self,
        ipTransitSettings=None,
        sdaTransitSettings=None,
        transitPeerNetworkName=None,
        transitPeerNetworkType=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Add Transit Peer Network in SD-Access .

        Args:
            ipTransitSettings(object): SDA's ipTransitSettings.
            sdaTransitSettings(object): SDA's sdaTransitSettings.
            transitPeerNetworkName(string): SDA's Transit Peer Network Name .
            transitPeerNetworkType(string): SDA's Transit Peer Network Type . Available values are 'ip_transit',
                'sda_transit_with_lisp_bgp' and 'sda_transit_with_pub_sub'.
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
            https://developer.cisco.com/docs/dna-center/#!add-transit-peer-network
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
            "transitPeerNetworkName": transitPeerNetworkName,
            "transitPeerNetworkType": transitPeerNetworkType,
            "ipTransitSettings": ipTransitSettings,
            "sdaTransitSettings": sdaTransitSettings,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_d7073129453698264e7519d82991c_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/business/sda/transit-peer-network"
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
            "bpm_d7073129453698264e7519d82991c_v3_1_3_0", json_data
        )

    def delete_vn(
        self,
        site_name_hierarchy,
        virtual_network_name,
        headers=None,
        **request_parameters
    ):
        """Delete virtual network (VN) from SDA Fabric .

        Args:
            virtual_network_name(str): virtualNetworkName query parameter.
            site_name_hierarchy(str): siteNameHierarchy query parameter.
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
            https://developer.cisco.com/docs/dna-center/#!delete-v-n-from-s-d-a-fabric
        """
        check_type(headers, dict)
        check_type(virtual_network_name, str, may_be_none=False)
        check_type(site_name_hierarchy, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "virtualNetworkName": virtual_network_name,
            "siteNameHierarchy": site_name_hierarchy,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/business/sda/virtual-network"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_cb9f8ad5359b2b2cbc151ac3a842a_v3_1_3_0", json_data
        )

    def get_vn(
        self,
        site_name_hierarchy,
        virtual_network_name,
        headers=None,
        **request_parameters
    ):
        """Get virtual network (VN) from SDA Fabric .

        Args:
            virtual_network_name(str): virtualNetworkName query parameter.
            site_name_hierarchy(str): siteNameHierarchy query parameter.
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
            https://developer.cisco.com/docs/dna-center/#!get-v-n-from-s-d-a-fabric
        """
        check_type(headers, dict)
        check_type(virtual_network_name, str, may_be_none=False)
        check_type(site_name_hierarchy, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "virtualNetworkName": virtual_network_name,
            "siteNameHierarchy": site_name_hierarchy,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/business/sda/virtual-network"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_cb1fe08692b85767a42b84340c4c7d53_v3_1_3_0", json_data
        )

    def add_vn(
        self,
        siteNameHierarchy=None,
        virtualNetworkName=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Add virtual network (VN) in SDA Fabric .

        Args:
            siteNameHierarchy(string): SDA's Path of sda Fabric Site .
            virtualNetworkName(string): SDA's Virtual Network Name, that is created at Global level .
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
            https://developer.cisco.com/docs/dna-center/#!add-v-n-in-fabric
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
            "virtualNetworkName": virtualNetworkName,
            "siteNameHierarchy": siteNameHierarchy,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_e3a724a35854758d65a83823c88435_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/business/sda/virtual-network"
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
            "bpm_e3a724a35854758d65a83823c88435_v3_1_3_0", json_data
        )

    def get_virtual_network_summary(
        self, site_name_hierarchy, headers=None, **request_parameters
    ):
        """Get Virtual Network Summary .

        Args:
            site_name_hierarchy(str): siteNameHierarchy query parameter. Complete fabric siteNameHierarchy Path .
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
            https://developer.cisco.com/docs/dna-center/#!get-virtual-network-summary
        """
        check_type(headers, dict)
        check_type(site_name_hierarchy, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "siteNameHierarchy": site_name_hierarchy,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/business/sda/virtual-network/summary"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ccf5ce99e049525f8184fcaa5991d919_v3_1_3_0", json_data
        )

    def get_ip_pool_from_sda_virtual_network(
        self,
        ip_pool_name,
        site_name_hierarchy,
        virtual_network_name,
        headers=None,
        **request_parameters
    ):
        """Get IP Pool from SDA Virtual Network .

        Args:
            site_name_hierarchy(str): siteNameHierarchy query parameter.
            virtual_network_name(str): virtualNetworkName query parameter.
            ip_pool_name(str): ipPoolName query parameter. ipPoolName. Note: Use vlanName as a value for this
                parameter if same ip pool is assigned to multiple virtual networks (e.g..
                ipPoolName=vlan1021) .
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
            https://developer.cisco.com/docs/dna-center/#!get-i-p-pool-from-s-d-a-virtual-network
        """
        check_type(headers, dict)
        check_type(site_name_hierarchy, str, may_be_none=False)
        check_type(virtual_network_name, str, may_be_none=False)
        check_type(ip_pool_name, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "siteNameHierarchy": site_name_hierarchy,
            "virtualNetworkName": virtual_network_name,
            "ipPoolName": ip_pool_name,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/business/sda/virtualnetwork/ippool"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_b88723912610599ba42292db52d1dae4_v3_1_3_0", json_data
        )

    def delete_ip_pool_from_sda_virtual_network(
        self,
        ip_pool_name,
        site_name_hierarchy,
        virtual_network_name,
        headers=None,
        **request_parameters
    ):
        """Delete IP Pool from SDA Virtual Network .

        Args:
            site_name_hierarchy(str): siteNameHierarchy query parameter.
            virtual_network_name(str): virtualNetworkName query parameter.
            ip_pool_name(str): ipPoolName query parameter.
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
            https://developer.cisco.com/docs/dna-center/#!delete-i-p-pool-from-s-d-a-virtual-network
        """
        check_type(headers, dict)
        check_type(site_name_hierarchy, str, may_be_none=False)
        check_type(virtual_network_name, str, may_be_none=False)
        check_type(ip_pool_name, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "siteNameHierarchy": site_name_hierarchy,
            "virtualNetworkName": virtual_network_name,
            "ipPoolName": ip_pool_name,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/business/sda/virtualnetwork/ippool"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c923d016d5401b7a9943724df3844_v3_1_3_0", json_data
        )

    def add_ip_pool_in_sda_virtual_network(
        self,
        autoGenerateVlanName=None,
        ipPoolName=None,
        isBridgeModeVm=None,
        isCommonPool=None,
        isIpDirectedBroadcast=None,
        isL2FloodingEnabled=None,
        isLayer2Only=None,
        isThisCriticalPool=None,
        isWirelessPool=None,
        poolType=None,
        scalableGroupName=None,
        siteNameHierarchy=None,
        trafficType=None,
        virtualNetworkName=None,
        vlanId=None,
        vlanName=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Add IP Pool in SDA Virtual Network .

        Args:
            autoGenerateVlanName(boolean): SDA's It will auto generate vlanName, if vlanName is empty(applicable for
                L3  and INFRA_VN) .
            ipPoolName(string): SDA's Ip Pool Name, that is reserved to Fabric Site (Required for L3 and INFRA_VN) .
            isBridgeModeVm(boolean): SDA's Bridge Mode Vm enablement flag (applicable for L3 and L2 and default
                value is False ) .
            isCommonPool(boolean): SDA's Common Pool enablement flag(applicable for L3 and L2 and default value is
                False ) .
            isIpDirectedBroadcast(boolean): SDA's Ip Directed Broadcast enablement flag(applicable for L3 and
                default value is False ) .
            isL2FloodingEnabled(boolean): SDA's Layer2 flooding enablement flag(applicable for L3 , L2 and always
                true for L2 and default value is False ) .
            isLayer2Only(boolean): SDA's Layer2 Only enablement flag and default value is False .
            isThisCriticalPool(boolean): SDA's Critical pool enablement flag(applicable for L3 and default value is
                False ) .
            isWirelessPool(boolean): SDA's Wireless Pool enablement flag(applicable for L3  and L2 and default value
                is False ) .
            poolType(string): SDA's Pool Type (applicable for INFRA_VN) . Available values are 'AP' and 'Extended'.
            scalableGroupName(string): SDA's Scalable Group Name(applicable for L3) .
            siteNameHierarchy(string): SDA's Path of sda Fabric Site .
            trafficType(string): SDA's Traffic type(applicable for L3  and L2) . Available values are 'Data' and
                'Voice'.
            virtualNetworkName(string): SDA's Virtual Network Name, that is associated to Fabric Site .
            vlanId(string): SDA's vlan Id(applicable for L3 , L2 and  INFRA_VN) .
            vlanName(string): SDA's Vlan name represent the segment name, if empty, vlanName would be auto generated
                by API .
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
            https://developer.cisco.com/docs/dna-center/#!add-i-p-pool-in-s-d-a-virtual-network
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
            "siteNameHierarchy": siteNameHierarchy,
            "virtualNetworkName": virtualNetworkName,
            "isLayer2Only": isLayer2Only,
            "ipPoolName": ipPoolName,
            "vlanId": vlanId,
            "vlanName": vlanName,
            "autoGenerateVlanName": autoGenerateVlanName,
            "trafficType": trafficType,
            "scalableGroupName": scalableGroupName,
            "isL2FloodingEnabled": isL2FloodingEnabled,
            "isThisCriticalPool": isThisCriticalPool,
            "isWirelessPool": isWirelessPool,
            "isIpDirectedBroadcast": isIpDirectedBroadcast,
            "isCommonPool": isCommonPool,
            "isBridgeModeVm": isBridgeModeVm,
            "poolType": poolType,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_b07f187b7456c8bbb6088a2f24dcee_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/business/sda/virtualnetwork/ippool"
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
            "bpm_b07f187b7456c8bbb6088a2f24dcee_v3_1_3_0", json_data
        )

    def update_anycast_gateways(
        self, headers=None, payload=None, active_validation=True, **request_parameters
    ):
        """Updates anycast gateways based on user input. .

        Args:
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
            https://developer.cisco.com/docs/dna-center/#!update-anycast-gateways
        """
        check_type(headers, dict)
        check_type(payload, list)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = payload or []
        if active_validation:
            self._request_validator(
                "jsd_f486694f3da57b4921b7f2036a1b754_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/sda/anycastGateways"
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
            "bpm_f486694f3da57b4921b7f2036a1b754_v3_1_3_0", json_data
        )

    def add_anycast_gateways(
        self, headers=None, payload=None, active_validation=True, **request_parameters
    ):
        """Adds anycast gateways based on user input. .

        Args:
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
            https://developer.cisco.com/docs/dna-center/#!add-anycast-gateways
        """
        check_type(headers, dict)
        check_type(payload, list)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = payload or []
        if active_validation:
            self._request_validator(
                "jsd_ee8590b6b45048b84e814161272bee_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/sda/anycastGateways"
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
            "bpm_ee8590b6b45048b84e814161272bee_v3_1_3_0", json_data
        )

    def get_anycast_gateways(
        self,
        fabric_id=None,
        id=None,
        ip_pool_name=None,
        limit=None,
        offset=None,
        virtual_network_name=None,
        vlan_id=None,
        vlan_name=None,
        headers=None,
        **request_parameters
    ):
        """Returns a list of anycast gateways that match the provided query parameters. .

        Args:
            id(str): id query parameter. ID of the anycast gateway. .
            fabric_id(str): fabricId query parameter. ID of the fabric the anycast gateway is assigned to. .
            virtual_network_name(str): virtualNetworkName query parameter. Name of the virtual network associated
                with the anycast gateways. .
            ip_pool_name(str): ipPoolName query parameter. Name of the IP pool associated with the anycast gateways.
                .
            vlan_name(str): vlanName query parameter. VLAN name of the anycast gateways. .
            vlan_id(int): vlanId query parameter. VLAN ID of the anycast gateways. The allowed range for vlanId is
                [2-4093] except for reserved VLANs [1002-1005], 2046, and 4094. .
            offset(int): offset query parameter. Starting record for pagination. .
            limit(int): limit query parameter. Maximum number of records to return. The maximum number of objects
                supported in a single request is 500. .
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
            https://developer.cisco.com/docs/dna-center/#!get-anycast-gateways
        """
        check_type(headers, dict)
        check_type(id, str)
        check_type(fabric_id, str)
        check_type(virtual_network_name, str)
        check_type(ip_pool_name, str)
        check_type(vlan_name, str)
        check_type(vlan_id, int)
        check_type(offset, int)
        check_type(limit, int)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "id": id,
            "fabricId": fabric_id,
            "virtualNetworkName": virtual_network_name,
            "ipPoolName": ip_pool_name,
            "vlanName": vlan_name,
            "vlanId": vlan_id,
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

        e_url = "/dna/intent/api/v1/sda/anycastGateways"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c634a503551e885c053fd1ed9d3fd_v3_1_3_0", json_data
        )

    def get_anycast_gateway_count(
        self,
        fabric_id=None,
        ip_pool_name=None,
        virtual_network_name=None,
        vlan_id=None,
        vlan_name=None,
        headers=None,
        **request_parameters
    ):
        """Returns the count of anycast gateways that match the provided query parameters. .

        Args:
            fabric_id(str): fabricId query parameter. ID of the fabric the anycast gateway is assigned to. .
            virtual_network_name(str): virtualNetworkName query parameter. Name of the virtual network associated
                with the anycast gateways. .
            ip_pool_name(str): ipPoolName query parameter. Name of the IP pool associated with the anycast gateways.
                .
            vlan_name(str): vlanName query parameter. VLAN name of the anycast gateways. .
            vlan_id(int): vlanId query parameter. VLAN ID of the anycast gateways. The allowed range for vlanId is
                [2-4093] except for reserved VLANs [1002-1005], 2046, and 4094. .
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
            https://developer.cisco.com/docs/dna-center/#!get-anycast-gateway-count
        """
        check_type(headers, dict)
        check_type(fabric_id, str)
        check_type(virtual_network_name, str)
        check_type(ip_pool_name, str)
        check_type(vlan_name, str)
        check_type(vlan_id, int)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "fabricId": fabric_id,
            "virtualNetworkName": virtual_network_name,
            "ipPoolName": ip_pool_name,
            "vlanName": vlan_name,
            "vlanId": vlan_id,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/sda/anycastGateways/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a280b785a3ca53c349c68ca9070_v3_1_3_0", json_data
        )

    def delete_anycast_gateway_by_id(self, id, headers=None, **request_parameters):
        """Deletes an anycast gateway based on id. .

        Args:
            id(str): id path parameter. ID of the anycast gateway. .
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
            https://developer.cisco.com/docs/dna-center/#!delete-anycast-gateway-by-id
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

        e_url = "/dna/intent/api/v1/sda/anycastGateways/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_e66d9fbfe55cf5882bf219b0fffa13_v3_1_3_0", json_data
        )

    def get_authentication_profiles(
        self,
        authentication_profile_name=None,
        fabric_id=None,
        is_global_authentication_profile=None,
        limit=None,
        offset=None,
        headers=None,
        **request_parameters
    ):
        """Returns a list of authentication profiles that match the provided query parameters. .

        Args:
            fabric_id(str): fabricId query parameter. ID of the fabric the authentication profile is assigned to. .
            authentication_profile_name(str): authenticationProfileName query parameter. Return only the
                authentication profiles with this specified name. Note that 'No Authentication' is not a
                valid option for this parameter. .
            is_global_authentication_profile(bool): isGlobalAuthenticationProfile query parameter. Set to true to
                return only global authentication profiles, or set to false to hide them.
                isGlobalAuthenticationProfile must not be true when fabricId is provided. .
            offset(int): offset query parameter. Starting record for pagination. .
            limit(int): limit query parameter. Maximum number of records to return. The maximum number of objects
                supported in a single request is 500. .
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
            https://developer.cisco.com/docs/dna-center/#!get-authentication-profiles
        """
        check_type(headers, dict)
        check_type(fabric_id, str)
        check_type(authentication_profile_name, str)
        check_type(is_global_authentication_profile, bool)
        check_type(offset, int)
        check_type(limit, int)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "fabricId": fabric_id,
            "authenticationProfileName": authentication_profile_name,
            "isGlobalAuthenticationProfile": is_global_authentication_profile,
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

        e_url = "/dna/intent/api/v1/sda/authenticationProfiles"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_e6713a34508993b3e9f6837dd690_v3_1_3_0", json_data
        )

    def update_authentication_profile(
        self, headers=None, payload=None, active_validation=True, **request_parameters
    ):
        """Updates an authentication profile based on user input. .

        Args:
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
            https://developer.cisco.com/docs/dna-center/#!update-authentication-profile
        """
        check_type(headers, dict)
        check_type(payload, list)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = payload or []
        if active_validation:
            self._request_validator("jsd_ea8d75a9d8d9e6882da4a4a91_v3_1_3_0").validate(
                _payload
            )

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/sda/authenticationProfiles"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(
                endpoint_full_url, params=_params, json=_payload, headers=_headers
            )
        else:
            json_data = self._session.put(
                endpoint_full_url, params=_params, json=_payload
            )

        return self._object_factory("bpm_ea8d75a9d8d9e6882da4a4a91_v3_1_3_0", json_data)

    def delete_extranet_policies(
        self, extranet_policy_name=None, headers=None, **request_parameters
    ):
        """Deletes extranet policies based on user input. .

        Args:
            extranet_policy_name(str): extranetPolicyName query parameter. Name of the extranet policy. .
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
            https://developer.cisco.com/docs/dna-center/#!delete-extranet-policies
        """
        check_type(headers, dict)
        check_type(extranet_policy_name, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "extranetPolicyName": extranet_policy_name,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/sda/extranetPolicies"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_e5f7c332c255f34b7b6e2bd6ac13800_v3_1_3_0", json_data
        )

    def update_extranet_policy(
        self, headers=None, payload=None, active_validation=True, **request_parameters
    ):
        """Updates an extranet policy based on user input. .

        Args:
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
            https://developer.cisco.com/docs/dna-center/#!update-extranet-policy
        """
        check_type(headers, dict)
        check_type(payload, list)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = payload or []
        if active_validation:
            self._request_validator(
                "jsd_ccd75f80ece59f08cadda085402cef5_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/sda/extranetPolicies"
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
            "bpm_ccd75f80ece59f08cadda085402cef5_v3_1_3_0", json_data
        )

    def add_extranet_policy(
        self, headers=None, payload=None, active_validation=True, **request_parameters
    ):
        """Adds an extranet policy based on user input. .

        Args:
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
            https://developer.cisco.com/docs/dna-center/#!add-extranet-policy
        """
        check_type(headers, dict)
        check_type(payload, list)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = payload or []
        if active_validation:
            self._request_validator(
                "jsd_a0c237c8fc115b6f98b87cc7a1360dd0_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/sda/extranetPolicies"
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
            "bpm_a0c237c8fc115b6f98b87cc7a1360dd0_v3_1_3_0", json_data
        )

    def get_extranet_policies(
        self,
        extranet_policy_name=None,
        limit=None,
        offset=None,
        headers=None,
        **request_parameters
    ):
        """Returns a list of extranet policies that match the provided query parameters. .

        Args:
            extranet_policy_name(str): extranetPolicyName query parameter. Name of the extranet policy. .
            offset(int): offset query parameter. Starting record for pagination. .
            limit(int): limit query parameter. Maximum number of records to return. The maximum number of objects
                supported in a single request is 500. .
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
            https://developer.cisco.com/docs/dna-center/#!get-extranet-policies
        """
        check_type(headers, dict)
        check_type(extranet_policy_name, str)
        check_type(offset, int)
        check_type(limit, int)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "extranetPolicyName": extranet_policy_name,
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

        e_url = "/dna/intent/api/v1/sda/extranetPolicies"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c88d4f7170b9553abf9af4d011a25f0f_v3_1_3_0", json_data
        )

    def get_extranet_policy_count(self, headers=None, **request_parameters):
        """Returns the count of extranet policies that match the provided query parameters. .

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
            https://developer.cisco.com/docs/dna-center/#!get-extranet-policy-count
        """
        check_type(headers, dict)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/sda/extranetPolicies/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_dd8262eb13145dc292e7aee84e56e065_v3_1_3_0", json_data
        )

    def delete_extranet_policy_by_id(self, id, headers=None, **request_parameters):
        """Deletes an extranet policy based on id. .

        Args:
            id(str): id path parameter. ID of the extranet policy. .
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
            https://developer.cisco.com/docs/dna-center/#!delete-extranet-policy-by-id
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

        e_url = "/dna/intent/api/v1/sda/extranetPolicies/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_aeee667e2d567cbbff106e1888bbbe_v3_1_3_0", json_data
        )

    def get_fabric_devices(
        self,
        fabric_id,
        device_roles=None,
        limit=None,
        network_device_id=None,
        offset=None,
        headers=None,
        **request_parameters
    ):
        """Returns a list of fabric devices that match the provided query parameters. .

        Args:
            fabric_id(str): fabricId query parameter. ID of the fabric this device belongs to. .
            network_device_id(str): networkDeviceId query parameter. Network device ID of the fabric device. .
            device_roles(str): deviceRoles query parameter. Device roles of the fabric device. Allowed values are
                [CONTROL_PLANE_NODE, EDGE_NODE, BORDER_NODE, WIRELESS_CONTROLLER_NODE, EXTENDED_NODE]. .
            offset(int): offset query parameter. Starting record for pagination. .
            limit(int): limit query parameter. Maximum number of records to return. The maximum number of objects
                supported in a single request is 500. .
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
            https://developer.cisco.com/docs/dna-center/#!get-fabric-devices
        """
        check_type(headers, dict)
        check_type(fabric_id, str, may_be_none=False)
        check_type(network_device_id, str)
        check_type(device_roles, str)
        check_type(offset, int)
        check_type(limit, int)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "fabricId": fabric_id,
            "networkDeviceId": network_device_id,
            "deviceRoles": device_roles,
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

        e_url = "/dna/intent/api/v1/sda/fabricDevices"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_d5486968c9ff5b23ae1fdd15ad6da1ef_v3_1_3_0", json_data
        )

    def update_fabric_devices(
        self, headers=None, payload=None, active_validation=True, **request_parameters
    ):
        """Updates fabric devices based on user input. .

        Args:
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
            https://developer.cisco.com/docs/dna-center/#!update-fabric-devices
        """
        check_type(headers, dict)
        check_type(payload, list)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = payload or []
        if active_validation:
            self._request_validator(
                "jsd_a924f763a15125a8d5beaa6dd6fa2c_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/sda/fabricDevices"
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
            "bpm_a924f763a15125a8d5beaa6dd6fa2c_v3_1_3_0", json_data
        )

    def delete_fabric_devices(
        self,
        fabric_id,
        device_roles=None,
        network_device_id=None,
        headers=None,
        **request_parameters
    ):
        """Deletes fabric devices based on user input. .

        Args:
            fabric_id(str): fabricId query parameter. ID of the fabric this device belongs to. .
            network_device_id(str): networkDeviceId query parameter. Network device ID of the fabric device. .
            device_roles(str): deviceRoles query parameter. Device roles of the fabric device. Allowed values are
                [CONTROL_PLANE_NODE, EDGE_NODE, BORDER_NODE, WIRELESS_CONTROLLER_NODE]. .
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
            https://developer.cisco.com/docs/dna-center/#!delete-fabric-devices
        """
        check_type(headers, dict)
        check_type(fabric_id, str, may_be_none=False)
        check_type(network_device_id, str)
        check_type(device_roles, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "fabricId": fabric_id,
            "networkDeviceId": network_device_id,
            "deviceRoles": device_roles,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/sda/fabricDevices"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c5d22b295a4c8e4a1dfdb4645f92_v3_1_3_0", json_data
        )

    def add_fabric_devices(
        self, headers=None, payload=None, active_validation=True, **request_parameters
    ):
        """Adds fabric devices based on user input. .

        Args:
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
            https://developer.cisco.com/docs/dna-center/#!add-fabric-devices
        """
        check_type(headers, dict)
        check_type(payload, list)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = payload or []
        if active_validation:
            self._request_validator(
                "jsd_d77719c37558f694e5545a21406275_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/sda/fabricDevices"
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
            "bpm_d77719c37558f694e5545a21406275_v3_1_3_0", json_data
        )

    def get_fabric_devices_count(
        self,
        fabric_id,
        device_roles=None,
        network_device_id=None,
        headers=None,
        **request_parameters
    ):
        """Returns the count of fabric devices that match the provided query parameters. .

        Args:
            fabric_id(str): fabricId query parameter. ID of the fabric this device belongs to. .
            network_device_id(str): networkDeviceId query parameter. Network device ID of the fabric device. .
            device_roles(str): deviceRoles query parameter. Device roles of the fabric device. Allowed values are
                [CONTROL_PLANE_NODE, EDGE_NODE, BORDER_NODE, WIRELESS_CONTROLLER_NODE, EXTENDED_NODE]. .
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
            https://developer.cisco.com/docs/dna-center/#!get-fabric-devices-count
        """
        check_type(headers, dict)
        check_type(fabric_id, str, may_be_none=False)
        check_type(network_device_id, str)
        check_type(device_roles, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "fabricId": fabric_id,
            "networkDeviceId": network_device_id,
            "deviceRoles": device_roles,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/sda/fabricDevices/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_f081250cdc75361afea8d1624123bb4_v3_1_3_0", json_data
        )

    def delete_fabric_device_layer2_handoffs(
        self, fabric_id, network_device_id, headers=None, **request_parameters
    ):
        """Deletes layer 2 handoffs of a fabric device based on user input. .

        Args:
            fabric_id(str): fabricId query parameter. ID of the fabric this device belongs to. .
            network_device_id(str): networkDeviceId query parameter. Network device ID of the fabric device. .
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
            https://developer.cisco.com/docs/dna-center/#!delete-fabric-device-layer2-handoffs
        """
        check_type(headers, dict)
        check_type(fabric_id, str, may_be_none=False)
        check_type(network_device_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "fabricId": fabric_id,
            "networkDeviceId": network_device_id,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/sda/fabricDevices/layer2Handoffs"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_b6484275a25c54488d300c11c5ddd481_v3_1_3_0", json_data
        )

    def get_fabric_devices_layer2_handoffs(
        self,
        fabric_id,
        limit=None,
        network_device_id=None,
        offset=None,
        headers=None,
        **request_parameters
    ):
        """Returns a list of layer 2 handoffs of fabric devices that match the provided query parameters. .

        Args:
            fabric_id(str): fabricId query parameter. ID of the fabric this device belongs to. .
            network_device_id(str): networkDeviceId query parameter. Network device ID of the fabric device. .
            offset(int): offset query parameter. Starting record for pagination. .
            limit(int): limit query parameter. Maximum number of records to return. The maximum number of objects
                supported in a single request is 500. .
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
            https://developer.cisco.com/docs/dna-center/#!get-fabric-devices-layer2-handoffs
        """
        check_type(headers, dict)
        check_type(fabric_id, str, may_be_none=False)
        check_type(network_device_id, str)
        check_type(offset, int)
        check_type(limit, int)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "fabricId": fabric_id,
            "networkDeviceId": network_device_id,
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

        e_url = "/dna/intent/api/v1/sda/fabricDevices/layer2Handoffs"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ec047337e36b59db977e1dae8dd724ef_v3_1_3_0", json_data
        )

    def add_fabric_devices_layer2_handoffs(
        self, headers=None, payload=None, active_validation=True, **request_parameters
    ):
        """Adds layer 2 handoffs in fabric devices based on user input. .

        Args:
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
            https://developer.cisco.com/docs/dna-center/#!add-fabric-devices-layer2-handoffs
        """
        check_type(headers, dict)
        check_type(payload, list)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = payload or []
        if active_validation:
            self._request_validator(
                "jsd_e86b65311b05d29ba5eea0d5f1fd88f_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/sda/fabricDevices/layer2Handoffs"
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
            "bpm_e86b65311b05d29ba5eea0d5f1fd88f_v3_1_3_0", json_data
        )

    def get_fabric_devices_layer2_handoffs_count(
        self, fabric_id, network_device_id=None, headers=None, **request_parameters
    ):
        """Returns the count of layer 2 handoffs of fabric devices that match the provided query parameters. .

        Args:
            fabric_id(str): fabricId query parameter. ID of the fabric this device belongs to. .
            network_device_id(str): networkDeviceId query parameter. Network device ID of the fabric device. .
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
            https://developer.cisco.com/docs/dna-center/#!get-fabric-devices-layer2-handoffs-count
        """
        check_type(headers, dict)
        check_type(fabric_id, str, may_be_none=False)
        check_type(network_device_id, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "fabricId": fabric_id,
            "networkDeviceId": network_device_id,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/sda/fabricDevices/layer2Handoffs/coun" + "t"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c6da6b1da95bb691d2e39cee84dbb2_v3_1_3_0", json_data
        )

    def delete_fabric_device_layer2_handoff_by_id(
        self, id, headers=None, **request_parameters
    ):
        """Deletes a layer 2 handoff of a fabric device based on id. .

        Args:
            id(str): id path parameter. ID of the layer 2 handoff of a fabric device. .
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
            https://developer.cisco.com/docs/dna-center/#!delete-fabric-device-layer2-handoff-by-id
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

        e_url = "/dna/intent/api/v1/sda/fabricDevices/layer2Handoffs/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_b6406a55509e5aeaa71d960f98_v3_1_3_0", json_data
        )

    def add_fabric_devices_layer3_handoffs_with_ip_transit(
        self, headers=None, payload=None, active_validation=True, **request_parameters
    ):
        """Adds layer 3 handoffs with ip transit in fabric devices based on user input. .

        Args:
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
            https://developer.cisco.com/docs/dna-center/#!add-fabric-devices-layer3-handoffs-with-ip-transit
        """
        check_type(headers, dict)
        check_type(payload, list)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = payload or []
        if active_validation:
            self._request_validator(
                "jsd_c45c1c55d498d03a72933690098_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/sda/fabricDevices/layer3Handoffs/ipTr" + "ansits"
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
            "bpm_c45c1c55d498d03a72933690098_v3_1_3_0", json_data
        )

    def update_fabric_devices_layer3_handoffs_with_ip_transit(
        self, headers=None, payload=None, active_validation=True, **request_parameters
    ):
        """Updates layer 3 handoffs with ip transit of fabric devices based on user input. .

        Args:
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
            https://developer.cisco.com/docs/dna-center/#!update-fabric-devices-layer3-handoffs-with-ip-transit
        """
        check_type(headers, dict)
        check_type(payload, list)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = payload or []
        if active_validation:
            self._request_validator(
                "jsd_f0942fbb79f855e889d60777f41ea944_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/sda/fabricDevices/layer3Handoffs/ipTr" + "ansits"
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
            "bpm_f0942fbb79f855e889d60777f41ea944_v3_1_3_0", json_data
        )

    def delete_fabric_device_layer3_handoffs_with_ip_transit(
        self, fabric_id, network_device_id, headers=None, **request_parameters
    ):
        """Deletes layer 3 handoffs with ip transit of a fabric device based on user input. .

        Args:
            fabric_id(str): fabricId query parameter. ID of the fabric this device belongs to. .
            network_device_id(str): networkDeviceId query parameter. Network device ID of the fabric device. .
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
            https://developer.cisco.com/docs/dna-center/#!delete-fabric-device-layer3-handoffs-with-ip-transit
        """
        check_type(headers, dict)
        check_type(fabric_id, str, may_be_none=False)
        check_type(network_device_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "fabricId": fabric_id,
            "networkDeviceId": network_device_id,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/sda/fabricDevices/layer3Handoffs/ipTr" + "ansits"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_fdab9b7917a1567980b0071e058921fe_v3_1_3_0", json_data
        )

    def get_fabric_devices_layer3_handoffs_with_ip_transit(
        self,
        fabric_id,
        limit=None,
        network_device_id=None,
        offset=None,
        headers=None,
        **request_parameters
    ):
        """Returns a list of layer 3 handoffs with ip transit of fabric devices that match the provided query parameters. .

        Args:
            fabric_id(str): fabricId query parameter. ID of the fabric this device belongs to. .
            network_device_id(str): networkDeviceId query parameter. Network device ID of the fabric device. .
            offset(int): offset query parameter. Starting record for pagination. .
            limit(int): limit query parameter. Maximum number of records to return. The maximum number of objects
                supported in a single request is 500. .
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
            https://developer.cisco.com/docs/dna-center/#!get-fabric-devices-layer3-handoffs-with-ip-transit
        """
        check_type(headers, dict)
        check_type(fabric_id, str, may_be_none=False)
        check_type(network_device_id, str)
        check_type(offset, int)
        check_type(limit, int)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "fabricId": fabric_id,
            "networkDeviceId": network_device_id,
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

        e_url = "/dna/intent/api/v1/sda/fabricDevices/layer3Handoffs/ipTr" + "ansits"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ee0d11a1e0dd573da2d6fb96d92c4bb8_v3_1_3_0", json_data
        )

    def get_fabric_devices_layer3_handoffs_with_ip_transit_count(
        self, fabric_id, network_device_id=None, headers=None, **request_parameters
    ):
        """Returns the count of layer 3 handoffs with ip transit of fabric devices that match the provided query
        parameters. .

        Args:
            fabric_id(str): fabricId query parameter. ID of the fabric this device belongs to. .
            network_device_id(str): networkDeviceId query parameter. Network device ID of the fabric device. .
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
            https://developer.cisco.com/docs/dna-center/#!get-fabric-devices-layer3-handoffs-with-ip-transit-count
        """
        check_type(headers, dict)
        check_type(fabric_id, str, may_be_none=False)
        check_type(network_device_id, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "fabricId": fabric_id,
            "networkDeviceId": network_device_id,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/sda/fabricDevices/layer3Handoffs/ipTr" + "ansits/count"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a4fa61561aa0fe56939c3f24d4_v3_1_3_0", json_data
        )

    def delete_fabric_device_layer3_handoff_with_ip_transit_by_id(
        self, id, headers=None, **request_parameters
    ):
        """Deletes a layer 3 handoff with ip transit of a fabric device by id. .

        Args:
            id(str): id path parameter. ID of the layer 3 handoff with ip transit of a fabric device. .
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
            https://developer.cisco.com/docs/dna-center/#!delete-fabric-device-layer3-handoff-with-ip-transit-by-id
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

        e_url = (
            "/dna/intent/api/v1/sda/fabricDevices/layer3Handoffs/ipTr" + "ansits/{id}"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_fafe4d2d2fe510db8f0906e5f583559_v3_1_3_0", json_data
        )

    def update_fabric_devices_layer3_handoffs_with_sda_transit(
        self, headers=None, payload=None, active_validation=True, **request_parameters
    ):
        """Updates layer 3 handoffs with sda transit of fabric devices based on user input. .

        Args:
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
            https://developer.cisco.com/docs/dna-center/#!update-fabric-devices-layer3-handoffs-with-sda-transit
        """
        check_type(headers, dict)
        check_type(payload, list)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = payload or []
        if active_validation:
            self._request_validator(
                "jsd_c90c04b8356cf9974957e0f9516d0_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/sda/fabricDevices/layer3Handoffs/sdaT" + "ransits"
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
            "bpm_c90c04b8356cf9974957e0f9516d0_v3_1_3_0", json_data
        )

    def get_fabric_devices_layer3_handoffs_with_sda_transit(
        self,
        fabric_id,
        limit=None,
        network_device_id=None,
        offset=None,
        headers=None,
        **request_parameters
    ):
        """Returns a list of layer 3 handoffs with sda transit of fabric devices that match the provided query parameters.
        .

        Args:
            fabric_id(str): fabricId query parameter. ID of the fabric this device belongs to. .
            network_device_id(str): networkDeviceId query parameter. Network device ID of the fabric device. .
            offset(int): offset query parameter. Starting record for pagination. .
            limit(int): limit query parameter. Maximum number of records to return. The maximum number of objects
                supported in a single request is 500. .
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
            https://developer.cisco.com/docs/dna-center/#!get-fabric-devices-layer3-handoffs-with-sda-transit
        """
        check_type(headers, dict)
        check_type(fabric_id, str, may_be_none=False)
        check_type(network_device_id, str)
        check_type(offset, int)
        check_type(limit, int)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "fabricId": fabric_id,
            "networkDeviceId": network_device_id,
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

        e_url = "/dna/intent/api/v1/sda/fabricDevices/layer3Handoffs/sdaT" + "ransits"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_d8e5a783df185c88bae2bd8ba6b6bb2d_v3_1_3_0", json_data
        )

    def delete_fabric_device_layer3_handoffs_with_sda_transit(
        self, fabric_id, network_device_id, headers=None, **request_parameters
    ):
        """Deletes layer 3 handoffs with sda transit of a fabric device based on user input. .

        Args:
            fabric_id(str): fabricId query parameter. ID of the fabric this device belongs to. .
            network_device_id(str): networkDeviceId query parameter. Network device ID of the fabric device. .
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
            https://developer.cisco.com/docs/dna-center/#!delete-fabric-device-layer3-handoffs-with-sda-transit
        """
        check_type(headers, dict)
        check_type(fabric_id, str, may_be_none=False)
        check_type(network_device_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "fabricId": fabric_id,
            "networkDeviceId": network_device_id,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/sda/fabricDevices/layer3Handoffs/sdaT" + "ransits"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_aae870923852f3ac5904f65812c559_v3_1_3_0", json_data
        )

    def add_fabric_devices_layer3_handoffs_with_sda_transit(
        self, headers=None, payload=None, active_validation=True, **request_parameters
    ):
        """Adds layer 3 handoffs with sda transit in fabric devices based on user input. .

        Args:
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
            https://developer.cisco.com/docs/dna-center/#!add-fabric-devices-layer3-handoffs-with-sda-transit
        """
        check_type(headers, dict)
        check_type(payload, list)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = payload or []
        if active_validation:
            self._request_validator(
                "jsd_f95014e3b3385f21afa39325f3508427_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/sda/fabricDevices/layer3Handoffs/sdaT" + "ransits"
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
            "bpm_f95014e3b3385f21afa39325f3508427_v3_1_3_0", json_data
        )

    def get_fabric_devices_layer3_handoffs_with_sda_transit_count(
        self, fabric_id, network_device_id=None, headers=None, **request_parameters
    ):
        """Returns the count of layer 3 handoffs with sda transit of fabric devices that match the provided query
        parameters. .

        Args:
            fabric_id(str): fabricId query parameter. ID of the fabric this device belongs to. .
            network_device_id(str): networkDeviceId query parameter. Network device ID of the fabric device. .
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
            https://developer.cisco.com/docs/dna-center/#!get-fabric-devices-layer3-handoffs-with-sda-transit-count
        """
        check_type(headers, dict)
        check_type(fabric_id, str, may_be_none=False)
        check_type(network_device_id, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "fabricId": fabric_id,
            "networkDeviceId": network_device_id,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/sda/fabricDevices/layer3Handoffs/sdaT" + "ransits/count"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_b183d0cc487506ab776e0d470b0db91_v3_1_3_0", json_data
        )

    def delete_fabric_device_by_id(self, id, headers=None, **request_parameters):
        """Deletes a fabric device based on id. .

        Args:
            id(str): id path parameter. ID of the fabric device. .
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
            https://developer.cisco.com/docs/dna-center/#!delete-fabric-device-by-id
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

        e_url = "/dna/intent/api/v1/sda/fabricDevices/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_d9e0c5eb356eda1fa6f45928cb6f2_v3_1_3_0", json_data
        )

    def get_fabric_sites(
        self,
        id=None,
        limit=None,
        offset=None,
        site_id=None,
        headers=None,
        **request_parameters
    ):
        """Returns a list of fabric sites that match the provided query parameters. .

        Args:
            id(str): id query parameter. ID of the fabric site. .
            site_id(str): siteId query parameter. ID of the network hierarchy associated with the fabric site. .
            offset(int): offset query parameter. Starting record for pagination. .
            limit(int): limit query parameter. Maximum number of records to return. The maximum number of objects
                supported in a single request is 500. .
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
            https://developer.cisco.com/docs/dna-center/#!get-fabric-sites
        """
        check_type(headers, dict)
        check_type(id, str)
        check_type(site_id, str)
        check_type(offset, int)
        check_type(limit, int)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "id": id,
            "siteId": site_id,
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

        e_url = "/dna/intent/api/v1/sda/fabricSites"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a7079f75dd5973b2bf50461bdcf2de_v3_1_3_0", json_data
        )

    def add_fabric_site(
        self, headers=None, payload=None, active_validation=True, **request_parameters
    ):
        """Adds a fabric site based on user input. .

        Args:
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
            https://developer.cisco.com/docs/dna-center/#!add-fabric-site
        """
        check_type(headers, dict)
        check_type(payload, list)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = payload or []
        if active_validation:
            self._request_validator(
                "jsd_bfca373c5d7c863eef14abc654fd_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/sda/fabricSites"
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
            "bpm_bfca373c5d7c863eef14abc654fd_v3_1_3_0", json_data
        )

    def update_fabric_site(
        self, headers=None, payload=None, active_validation=True, **request_parameters
    ):
        """Updates a fabric site based on user input. .

        Args:
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
            https://developer.cisco.com/docs/dna-center/#!update-fabric-site
        """
        check_type(headers, dict)
        check_type(payload, list)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = payload or []
        if active_validation:
            self._request_validator(
                "jsd_effb55c158f28469762804e84633_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/sda/fabricSites"
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
            "bpm_effb55c158f28469762804e84633_v3_1_3_0", json_data
        )

    def get_fabric_site_count(self, headers=None, **request_parameters):
        """Returns the count of fabric sites that match the provided query parameters. .

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
            https://developer.cisco.com/docs/dna-center/#!get-fabric-site-count
        """
        check_type(headers, dict)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/sda/fabricSites/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_b871b97883085717bfbb14e860ab6654_v3_1_3_0", json_data
        )

    def delete_fabric_site_by_id(self, id, headers=None, **request_parameters):
        """Deletes a fabric site based on id. .

        Args:
            id(str): id path parameter. ID of the fabric site. .
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
            https://developer.cisco.com/docs/dna-center/#!delete-fabric-site-by-id
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

        e_url = "/dna/intent/api/v1/sda/fabricSites/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c94ba483b75e03a2c23aae02c510ac_v3_1_3_0", json_data
        )

    def get_fabric_zones(
        self,
        id=None,
        limit=None,
        offset=None,
        site_id=None,
        headers=None,
        **request_parameters
    ):
        """Returns a list of fabric zones that match the provided query parameters. .

        Args:
            id(str): id query parameter. ID of the fabric zone. .
            site_id(str): siteId query parameter. ID of the network hierarchy associated with the fabric zone. .
            offset(int): offset query parameter. Starting record for pagination. .
            limit(int): limit query parameter. Maximum number of records to return. The maximum number of objects
                supported in a single request is 500. .
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
            https://developer.cisco.com/docs/dna-center/#!get-fabric-zones
        """
        check_type(headers, dict)
        check_type(id, str)
        check_type(site_id, str)
        check_type(offset, int)
        check_type(limit, int)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "id": id,
            "siteId": site_id,
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

        e_url = "/dna/intent/api/v1/sda/fabricZones"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_e722d98d14d5e119ca03fa114edb38f_v3_1_3_0", json_data
        )

    def update_fabric_zone(
        self, headers=None, payload=None, active_validation=True, **request_parameters
    ):
        """Updates a fabric zone based on user input. .

        Args:
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
            https://developer.cisco.com/docs/dna-center/#!update-fabric-zone
        """
        check_type(headers, dict)
        check_type(payload, list)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = payload or []
        if active_validation:
            self._request_validator(
                "jsd_ada3522de8ef54729e9fc242df292547_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/sda/fabricZones"
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
            "bpm_ada3522de8ef54729e9fc242df292547_v3_1_3_0", json_data
        )

    def add_fabric_zone(
        self, headers=None, payload=None, active_validation=True, **request_parameters
    ):
        """Adds a fabric zone based on user input. .

        Args:
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
            https://developer.cisco.com/docs/dna-center/#!add-fabric-zone
        """
        check_type(headers, dict)
        check_type(payload, list)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = payload or []
        if active_validation:
            self._request_validator(
                "jsd_ae4d33eacca95f109bebc6fd0528ca48_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/sda/fabricZones"
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
            "bpm_ae4d33eacca95f109bebc6fd0528ca48_v3_1_3_0", json_data
        )

    def get_fabric_zone_count(self, headers=None, **request_parameters):
        """Returns the count of fabric zones that match the provided query parameters. .

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
            https://developer.cisco.com/docs/dna-center/#!get-fabric-zone-count
        """
        check_type(headers, dict)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/sda/fabricZones/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_b7004918aecc58c7880ae97d344bb885_v3_1_3_0", json_data
        )

    def delete_fabric_zone_by_id(self, id, headers=None, **request_parameters):
        """Deletes a fabric zone based on id. .

        Args:
            id(str): id path parameter. ID of the fabric zone. .
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
            https://developer.cisco.com/docs/dna-center/#!delete-fabric-zone-by-id
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

        e_url = "/dna/intent/api/v1/sda/fabricZones/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_cdb33e11852af80e1ed8f26e4336d_v3_1_3_0", json_data
        )

    def add_layer2_virtual_networks(
        self, headers=None, payload=None, active_validation=True, **request_parameters
    ):
        """Adds layer 2 virtual networks based on user input. .

        Args:
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
            https://developer.cisco.com/docs/dna-center/#!add-layer2-virtual-networks
        """
        check_type(headers, dict)
        check_type(payload, list)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = payload or []
        if active_validation:
            self._request_validator(
                "jsd_f09c94c65c858e4b7be0b7cb3d25b7a_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/sda/layer2VirtualNetworks"
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
            "bpm_f09c94c65c858e4b7be0b7cb3d25b7a_v3_1_3_0", json_data
        )

    def delete_layer2_virtual_networks(
        self,
        fabric_id,
        associated_layer3_virtual_network_name=None,
        traffic_type=None,
        vlan_id=None,
        vlan_name=None,
        headers=None,
        **request_parameters
    ):
        """Deletes layer 2 virtual networks based on user input. .

        Args:
            fabric_id(str): fabricId query parameter. ID of the fabric the layer 2 virtual network is assigned to. .
            vlan_name(str): vlanName query parameter. The vlan name of the layer 2 virtual network. .
            vlan_id(int): vlanId query parameter. The vlan ID of the layer 2 virtual network. .
            traffic_type(str): trafficType query parameter. The traffic type of the layer 2 virtual network. .
            associated_layer3_virtual_network_name(str): associatedLayer3VirtualNetworkName query parameter. Name of
                the associated layer 3 virtual network. .
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
            https://developer.cisco.com/docs/dna-center/#!delete-layer2-virtual-networks
        """
        check_type(headers, dict)
        check_type(fabric_id, str, may_be_none=False)
        check_type(vlan_name, str)
        check_type(vlan_id, int)
        check_type(traffic_type, str)
        check_type(associated_layer3_virtual_network_name, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "fabricId": fabric_id,
            "vlanName": vlan_name,
            "vlanId": vlan_id,
            "trafficType": traffic_type,
            "associatedLayer3VirtualNetworkName": associated_layer3_virtual_network_name,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/sda/layer2VirtualNetworks"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_fa8caf01309507e9be1544b9d1faa39_v3_1_3_0", json_data
        )

    def get_layer2_virtual_networks(
        self,
        associated_layer3_virtual_network_name=None,
        fabric_id=None,
        id=None,
        limit=None,
        offset=None,
        traffic_type=None,
        vlan_id=None,
        vlan_name=None,
        headers=None,
        **request_parameters
    ):
        """Returns a list of layer 2 virtual networks that match the provided query parameters. .

        Args:
            id(str): id query parameter. ID of the layer 2 virtual network. .
            fabric_id(str): fabricId query parameter. ID of the fabric the layer 2 virtual network is assigned to. .
            vlan_name(str): vlanName query parameter. The vlan name of the layer 2 virtual network. .
            vlan_id(int): vlanId query parameter. The vlan ID of the layer 2 virtual network. .
            traffic_type(str): trafficType query parameter. The traffic type of the layer 2 virtual network. .
            associated_layer3_virtual_network_name(str): associatedLayer3VirtualNetworkName query parameter. Name of
                the associated layer 3 virtual network. .
            offset(int): offset query parameter. Starting record for pagination. .
            limit(int): limit query parameter. Maximum number of records to return. The maximum number of objects
                supported in a single request is 500. .
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
            https://developer.cisco.com/docs/dna-center/#!get-layer2-virtual-networks
        """
        check_type(headers, dict)
        check_type(id, str)
        check_type(fabric_id, str)
        check_type(vlan_name, str)
        check_type(vlan_id, int)
        check_type(traffic_type, str)
        check_type(associated_layer3_virtual_network_name, str)
        check_type(offset, int)
        check_type(limit, int)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "id": id,
            "fabricId": fabric_id,
            "vlanName": vlan_name,
            "vlanId": vlan_id,
            "trafficType": traffic_type,
            "associatedLayer3VirtualNetworkName": associated_layer3_virtual_network_name,
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

        e_url = "/dna/intent/api/v1/sda/layer2VirtualNetworks"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c794771a235f0da82cf11d968c9ec3_v3_1_3_0", json_data
        )

    def update_layer2_virtual_networks(
        self, headers=None, payload=None, active_validation=True, **request_parameters
    ):
        """Updates layer 2 virtual networks based on user input. .

        Args:
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
            https://developer.cisco.com/docs/dna-center/#!update-layer2-virtual-networks
        """
        check_type(headers, dict)
        check_type(payload, list)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = payload or []
        if active_validation:
            self._request_validator(
                "jsd_bcb7a52e3c5763b246bcf438fe57c9_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/sda/layer2VirtualNetworks"
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
            "bpm_bcb7a52e3c5763b246bcf438fe57c9_v3_1_3_0", json_data
        )

    def get_layer2_virtual_network_count(
        self,
        associated_layer3_virtual_network_name=None,
        fabric_id=None,
        traffic_type=None,
        vlan_id=None,
        vlan_name=None,
        headers=None,
        **request_parameters
    ):
        """Returns the count of layer 2 virtual networks that match the provided query parameters. .

        Args:
            fabric_id(str): fabricId query parameter. ID of the fabric the layer 2 virtual network is assigned to. .
            vlan_name(str): vlanName query parameter. The vlan name of the layer 2 virtual network. .
            vlan_id(int): vlanId query parameter. The vlan ID of the layer 2 virtual network. .
            traffic_type(str): trafficType query parameter. The traffic type of the layer 2 virtual network. .
            associated_layer3_virtual_network_name(str): associatedLayer3VirtualNetworkName query parameter. Name of
                the associated layer 3 virtual network. .
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
            https://developer.cisco.com/docs/dna-center/#!get-layer2-virtual-network-count
        """
        check_type(headers, dict)
        check_type(fabric_id, str)
        check_type(vlan_name, str)
        check_type(vlan_id, int)
        check_type(traffic_type, str)
        check_type(associated_layer3_virtual_network_name, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "fabricId": fabric_id,
            "vlanName": vlan_name,
            "vlanId": vlan_id,
            "trafficType": traffic_type,
            "associatedLayer3VirtualNetworkName": associated_layer3_virtual_network_name,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/sda/layer2VirtualNetworks/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a69aee0c555fb5baaa9db43327f955_v3_1_3_0", json_data
        )

    def delete_layer2_virtual_network_by_id(
        self, id, headers=None, **request_parameters
    ):
        """Deletes a layer 2 virtual network based on id. .

        Args:
            id(str): id path parameter. ID of the layer 2 virtual network. .
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
            https://developer.cisco.com/docs/dna-center/#!delete-layer2-virtual-network-by-id
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

        e_url = "/dna/intent/api/v1/sda/layer2VirtualNetworks/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_bfbdb9daba59fc9587824918c61cd6_v3_1_3_0", json_data
        )

    def add_layer3_virtual_networks(
        self, headers=None, payload=None, active_validation=True, **request_parameters
    ):
        """Adds layer 3 virtual networks based on user input. .

        Args:
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
            https://developer.cisco.com/docs/dna-center/#!add-layer3-virtual-networks
        """
        check_type(headers, dict)
        check_type(payload, list)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = payload or []
        if active_validation:
            self._request_validator(
                "jsd_dabd13cd5e9c928daf80d6758d62_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/sda/layer3VirtualNetworks"
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
            "bpm_dabd13cd5e9c928daf80d6758d62_v3_1_3_0", json_data
        )

    def get_layer3_virtual_networks(
        self,
        anchored_site_id=None,
        fabric_id=None,
        limit=None,
        offset=None,
        virtual_network_name=None,
        headers=None,
        **request_parameters
    ):
        """Returns a list of layer 3 virtual networks that match the provided query parameters. .

        Args:
            virtual_network_name(str): virtualNetworkName query parameter. Name of the layer 3 virtual network. .
            fabric_id(str): fabricId query parameter. ID of the fabric the layer 3 virtual network is assigned to. .
            anchored_site_id(str): anchoredSiteId query parameter. Fabric ID of the fabric site the layer 3 virtual
                network is anchored at. .
            offset(int): offset query parameter. Starting record for pagination. .
            limit(int): limit query parameter. Maximum number of records to return. The maximum number of objects
                supported in a single request is 500. .
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
            https://developer.cisco.com/docs/dna-center/#!get-layer3-virtual-networks
        """
        check_type(headers, dict)
        check_type(virtual_network_name, str)
        check_type(fabric_id, str)
        check_type(anchored_site_id, str)
        check_type(offset, int)
        check_type(limit, int)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "virtualNetworkName": virtual_network_name,
            "fabricId": fabric_id,
            "anchoredSiteId": anchored_site_id,
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

        e_url = "/dna/intent/api/v1/sda/layer3VirtualNetworks"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_fa3e62148dd542a8452b68ea888833a_v3_1_3_0", json_data
        )

    def delete_layer3_virtual_networks(
        self, virtual_network_name=None, headers=None, **request_parameters
    ):
        """Deletes layer 3 virtual networks based on user input. .

        Args:
            virtual_network_name(str): virtualNetworkName query parameter. Name of the layer 3 virtual network. .
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
            https://developer.cisco.com/docs/dna-center/#!delete-layer3-virtual-networks
        """
        check_type(headers, dict)
        check_type(virtual_network_name, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "virtualNetworkName": virtual_network_name,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/sda/layer3VirtualNetworks"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_e14a6db07f5c41903df6039be72e9c_v3_1_3_0", json_data
        )

    def update_layer3_virtual_networks(
        self, headers=None, payload=None, active_validation=True, **request_parameters
    ):
        """Updates layer 3 virtual networks based on user input. .

        Args:
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
            https://developer.cisco.com/docs/dna-center/#!update-layer3-virtual-networks
        """
        check_type(headers, dict)
        check_type(payload, list)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = payload or []
        if active_validation:
            self._request_validator(
                "jsd_ed9125b257ea54b79ef2db2d8ebd9d00_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/sda/layer3VirtualNetworks"
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
            "bpm_ed9125b257ea54b79ef2db2d8ebd9d00_v3_1_3_0", json_data
        )

    def get_layer3_virtual_networks_count(
        self, anchored_site_id=None, fabric_id=None, headers=None, **request_parameters
    ):
        """Returns the count of layer 3 virtual networks that match the provided query parameters. .

        Args:
            fabric_id(str): fabricId query parameter. ID of the fabric the layer 3 virtual network is assigned to. .
            anchored_site_id(str): anchoredSiteId query parameter. Fabric ID of the fabric site the layer 3 virtual
                network is anchored at. .
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
            https://developer.cisco.com/docs/dna-center/#!get-layer3-virtual-networks-count
        """
        check_type(headers, dict)
        check_type(fabric_id, str)
        check_type(anchored_site_id, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "fabricId": fabric_id,
            "anchoredSiteId": anchored_site_id,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/sda/layer3VirtualNetworks/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ced302dd267557c79c2f5aee72da9e4c_v3_1_3_0", json_data
        )

    def delete_layer3_virtual_network_by_id(
        self, id, headers=None, **request_parameters
    ):
        """Deletes a layer 3 virtual network based on id. .

        Args:
            id(str): id path parameter. ID of the layer 3 virtual network. .
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
            https://developer.cisco.com/docs/dna-center/#!delete-layer3-virtual-network-by-id
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

        e_url = "/dna/intent/api/v1/sda/layer3VirtualNetworks/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a4e95fb6765d48bac0c654a393a0a8_v3_1_3_0", json_data
        )

    def update_multicast(
        self, headers=None, payload=None, active_validation=True, **request_parameters
    ):
        """Updates a multicast configuration at a fabric level based on user input. .

        Args:
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
            https://developer.cisco.com/docs/dna-center/#!update-multicast
        """
        check_type(headers, dict)
        check_type(payload, list)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = payload or []
        if active_validation:
            self._request_validator(
                "jsd_cfb964a2958909f7ca12d23ab2bdb_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/sda/multicast"
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
            "bpm_cfb964a2958909f7ca12d23ab2bdb_v3_1_3_0", json_data
        )

    def get_multicast(
        self,
        fabric_id=None,
        limit=None,
        offset=None,
        headers=None,
        **request_parameters
    ):
        """Returns a list of multicast configurations at a fabric site level that match the provided query parameters. .

        Args:
            fabric_id(str): fabricId query parameter. ID of the fabric site where multicast is configured. .
            offset(int): offset query parameter. Starting record for pagination. .
            limit(int): limit query parameter. Maximum number of records to return. The maximum number of objects
                supported in a single request is 500. .
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
            https://developer.cisco.com/docs/dna-center/#!get-multicast
        """
        check_type(headers, dict)
        check_type(fabric_id, str)
        check_type(offset, int)
        check_type(limit, int)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "fabricId": fabric_id,
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

        e_url = "/dna/intent/api/v1/sda/multicast"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_eb648d275875745950bc33d3f12a28f_v3_1_3_0", json_data
        )

    def add_multicast_virtual_networks(
        self, headers=None, payload=None, active_validation=True, **request_parameters
    ):
        """Adds multicast for virtual networks based on user input. .

        Args:
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
            https://developer.cisco.com/docs/dna-center/#!add-multicast-virtual-networks
        """
        check_type(headers, dict)
        check_type(payload, list)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = payload or []
        if active_validation:
            self._request_validator(
                "jsd_cdc0bafd4257e78d211a1f4120bfa9_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/sda/multicast/virtualNetworks"
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
            "bpm_cdc0bafd4257e78d211a1f4120bfa9_v3_1_3_0", json_data
        )

    def get_multicast_virtual_networks(
        self,
        fabric_id=None,
        limit=None,
        offset=None,
        virtual_network_name=None,
        headers=None,
        **request_parameters
    ):
        """Returns a list of multicast configurations for virtual networks that match the provided query parameters. .

        Args:
            fabric_id(str): fabricId query parameter. ID of the fabric site where multicast is configured. .
            virtual_network_name(str): virtualNetworkName query parameter. Name of the virtual network associated to
                the multicast configuration. .
            offset(int): offset query parameter. Starting record for pagination. .
            limit(int): limit query parameter. Maximum number of records to return. The maximum number of objects
                supported in a single request is 500. .
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
            https://developer.cisco.com/docs/dna-center/#!get-multicast-virtual-networks
        """
        check_type(headers, dict)
        check_type(fabric_id, str)
        check_type(virtual_network_name, str)
        check_type(offset, int)
        check_type(limit, int)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "fabricId": fabric_id,
            "virtualNetworkName": virtual_network_name,
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

        e_url = "/dna/intent/api/v1/sda/multicast/virtualNetworks"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_bc8fbaa14c0b5064ba44a9aaf997a593_v3_1_3_0", json_data
        )

    def update_multicast_virtual_networks(
        self, headers=None, payload=None, active_validation=True, **request_parameters
    ):
        """Updates multicast configurations for virtual networks based on user input. .

        Args:
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
            https://developer.cisco.com/docs/dna-center/#!update-multicast-virtual-networks
        """
        check_type(headers, dict)
        check_type(payload, list)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = payload or []
        if active_validation:
            self._request_validator(
                "jsd_bc3ed6556f9b9c959e53e271d70_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/sda/multicast/virtualNetworks"
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
            "bpm_bc3ed6556f9b9c959e53e271d70_v3_1_3_0", json_data
        )

    def get_multicast_virtual_network_count(
        self, fabric_id=None, headers=None, **request_parameters
    ):
        """Returns the count of multicast configurations associated to virtual networks that match the provided query
        parameters. .

        Args:
            fabric_id(str): fabricId query parameter. ID of the fabric site the multicast configuration is
                associated with. .
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
            https://developer.cisco.com/docs/dna-center/#!get-multicast-virtual-network-count
        """
        check_type(headers, dict)
        check_type(fabric_id, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "fabricId": fabric_id,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/sda/multicast/virtualNetworks/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ecb8526b5333b7d7223dc4a68794_v3_1_3_0", json_data
        )

    def delete_multicast_virtual_network_by_id(
        self, id, headers=None, **request_parameters
    ):
        """Deletes a multicast configuration for a virtual network based on id. .

        Args:
            id(str): id path parameter. ID of the multicast configuration. .
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
            https://developer.cisco.com/docs/dna-center/#!delete-multicast-virtual-network-by-id
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

        e_url = "/dna/intent/api/v1/sda/multicast/virtualNetworks/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_e1e7b254440156e0a9ed4e72c5a9685a_v3_1_3_0", json_data
        )

    def get_pending_fabric_events(
        self,
        fabric_id=None,
        limit=None,
        offset=None,
        headers=None,
        **request_parameters
    ):
        """Returns a list of pending fabric events that match the provided query parameters. .

        Args:
            fabric_id(str): fabricId query parameter. ID of the fabric. .
            offset(int): offset query parameter. Starting record for pagination. .
            limit(int): limit query parameter. Maximum number of records to return. The maximum number of objects
                supported in a single request is 500. .
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
            https://developer.cisco.com/docs/dna-center/#!get-pending-fabric-events
        """
        check_type(headers, dict)
        check_type(fabric_id, str)
        check_type(offset, int)
        check_type(limit, int)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "fabricId": fabric_id,
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

        e_url = "/dna/intent/api/v1/sda/pendingFabricEvents"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_e044ddd8c5804989c999cf6f87e3a_v3_1_3_0", json_data
        )

    def apply_pending_fabric_events(
        self, headers=None, payload=None, active_validation=True, **request_parameters
    ):
        """Applies pending fabric events based on user input. .

        Args:
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
            https://developer.cisco.com/docs/dna-center/#!apply-pending-fabric-events
        """
        check_type(headers, dict)
        check_type(payload, list)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = payload or []
        if active_validation:
            self._request_validator(
                "jsd_f20eecc6e2d95a03a9e8961cd4337467_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/sda/pendingFabricEvents/apply"
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
            "bpm_f20eecc6e2d95a03a9e8961cd4337467_v3_1_3_0", json_data
        )

    def add_port_assignments(
        self, headers=None, payload=None, active_validation=True, **request_parameters
    ):
        """Adds port assignments based on user input. .

        Args:
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
            https://developer.cisco.com/docs/dna-center/#!add-port-assignments
        """
        check_type(headers, dict)
        check_type(payload, list)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = payload or []
        if active_validation:
            self._request_validator(
                "jsd_d6b58f378895114839682dceed1a9b5_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/sda/portAssignments"
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
            "bpm_d6b58f378895114839682dceed1a9b5_v3_1_3_0", json_data
        )

    def get_port_assignments(
        self,
        data_vlan_name=None,
        fabric_id=None,
        interface_name=None,
        limit=None,
        native_vlan_id=None,
        network_device_id=None,
        offset=None,
        voice_vlan_name=None,
        headers=None,
        **request_parameters
    ):
        """Returns a list of port assignments that match the provided query parameters. .

        Args:
            fabric_id(str): fabricId query parameter. ID of the fabric the device is assigned to. .
            network_device_id(str): networkDeviceId query parameter. Network device ID of the port assignment. .
            interface_name(str): interfaceName query parameter. Interface name of the port assignment. .
            data_vlan_name(str): dataVlanName query parameter. Data VLAN name of the port assignment. .
            voice_vlan_name(str): voiceVlanName query parameter. Voice VLAN name of the port assignment. .
            native_vlan_id(int): nativeVlanId query parameter. Native VLAN of the port assignment, this option is
                only applicable to TRUNKING_DEVICE connectedDeviceType.(VLAN must be between 1 and 4094.
                In cases value not set when connectedDeviceType is TRUNKING_DEVICE, default value will
                be '1'). .
            offset(int): offset query parameter. Starting record for pagination. .
            limit(int): limit query parameter. Maximum number of records to return. The maximum number of objects
                supported in a single request is 500. .
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
            https://developer.cisco.com/docs/dna-center/#!get-port-assignments
        """
        check_type(headers, dict)
        check_type(fabric_id, str)
        check_type(network_device_id, str)
        check_type(interface_name, str)
        check_type(data_vlan_name, str)
        check_type(voice_vlan_name, str)
        check_type(native_vlan_id, int)
        check_type(offset, int)
        check_type(limit, int)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "fabricId": fabric_id,
            "networkDeviceId": network_device_id,
            "interfaceName": interface_name,
            "dataVlanName": data_vlan_name,
            "voiceVlanName": voice_vlan_name,
            "nativeVlanId": native_vlan_id,
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

        e_url = "/dna/intent/api/v1/sda/portAssignments"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a9bc4645925814ac76d95268fe3f05_v3_1_3_0", json_data
        )

    def update_port_assignments(
        self, headers=None, payload=None, active_validation=True, **request_parameters
    ):
        """Updates port assignments based on user input. .

        Args:
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
            https://developer.cisco.com/docs/dna-center/#!update-port-assignments
        """
        check_type(headers, dict)
        check_type(payload, list)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = payload or []
        if active_validation:
            self._request_validator(
                "jsd_cad522e57a7b96b7238935689ed_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/sda/portAssignments"
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
            "bpm_cad522e57a7b96b7238935689ed_v3_1_3_0", json_data
        )

    def delete_port_assignments(
        self,
        fabric_id,
        network_device_id,
        data_vlan_name=None,
        interface_name=None,
        voice_vlan_name=None,
        headers=None,
        **request_parameters
    ):
        """Deletes port assignments based on user input. .

        Args:
            fabric_id(str): fabricId query parameter. ID of the fabric the device is assigned to. .
            network_device_id(str): networkDeviceId query parameter. Network device ID of the port assignment. .
            interface_name(str): interfaceName query parameter. Interface name of the port assignment. .
            data_vlan_name(str): dataVlanName query parameter. Data VLAN name of the port assignment. .
            voice_vlan_name(str): voiceVlanName query parameter. Voice VLAN name of the port assignment. .
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
            https://developer.cisco.com/docs/dna-center/#!delete-port-assignments
        """
        check_type(headers, dict)
        check_type(fabric_id, str, may_be_none=False)
        check_type(network_device_id, str, may_be_none=False)
        check_type(interface_name, str)
        check_type(data_vlan_name, str)
        check_type(voice_vlan_name, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "fabricId": fabric_id,
            "networkDeviceId": network_device_id,
            "interfaceName": interface_name,
            "dataVlanName": data_vlan_name,
            "voiceVlanName": voice_vlan_name,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/sda/portAssignments"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ee38ba825f79a76d9e7e6074c450_v3_1_3_0", json_data
        )

    def get_port_assignment_count(
        self,
        data_vlan_name=None,
        fabric_id=None,
        interface_name=None,
        network_device_id=None,
        voice_vlan_name=None,
        headers=None,
        **request_parameters
    ):
        """Returns the count of port assignments that match the provided query parameters. .

        Args:
            fabric_id(str): fabricId query parameter. ID of the fabric the device is assigned to. .
            network_device_id(str): networkDeviceId query parameter. Network device ID of the port assignment. .
            interface_name(str): interfaceName query parameter. Interface name of the port assignment. .
            data_vlan_name(str): dataVlanName query parameter. Data VLAN name of the port assignment. .
            voice_vlan_name(str): voiceVlanName query parameter. Voice VLAN name of the port assignment. .
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
            https://developer.cisco.com/docs/dna-center/#!get-port-assignment-count
        """
        check_type(headers, dict)
        check_type(fabric_id, str)
        check_type(network_device_id, str)
        check_type(interface_name, str)
        check_type(data_vlan_name, str)
        check_type(voice_vlan_name, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "fabricId": fabric_id,
            "networkDeviceId": network_device_id,
            "interfaceName": interface_name,
            "dataVlanName": data_vlan_name,
            "voiceVlanName": voice_vlan_name,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/sda/portAssignments/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_e11301d6336f512fbc6db01768e3ad5a_v3_1_3_0", json_data
        )

    def delete_port_assignment_by_id(self, id, headers=None, **request_parameters):
        """Deletes a port assignment based on id. .

        Args:
            id(str): id path parameter. ID of the port assignment. .
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
            https://developer.cisco.com/docs/dna-center/#!delete-port-assignment-by-id
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

        e_url = "/dna/intent/api/v1/sda/portAssignments/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_aa18582de8753438e0908cf9d92c2de_v3_1_3_0", json_data
        )

    def get_port_channels_connectivity(
        self,
        connected_device_type=None,
        fabric_id=None,
        limit=None,
        native_vlan_id=None,
        network_device_id=None,
        offset=None,
        port_channel_name=None,
        headers=None,
        **request_parameters
    ):
        """Returns a list of port channels that match the provided query parameters. .

        Args:
            fabric_id(str): fabricId query parameter. ID of the fabric the device is assigned to. .
            network_device_id(str): networkDeviceId query parameter. ID of the network device. .
            port_channel_name(str): portChannelName query parameter. Name of the port channel. .
            connected_device_type(str): connectedDeviceType query parameter. Connected device type of the port
                channel. The allowed values are [TRUNK, EXTENDED_NODE]. .
            native_vlan_id(int): nativeVlanId query parameter. Native VLAN of the port channel, this option is only
                applicable to TRUNK connectedDeviceType.(VLAN must be between 1 and 4094. In cases value
                not set when connectedDeviceType is TRUNK, default value will be '1'). .
            offset(int): offset query parameter. Starting record for pagination. .
            limit(int): limit query parameter. Maximum number of records to return. The maximum number of objects
                supported in a single request is 500. .
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
            https://developer.cisco.com/docs/dna-center/#!get-port-channels-connectivity
        """
        check_type(headers, dict)
        check_type(fabric_id, str)
        check_type(network_device_id, str)
        check_type(port_channel_name, str)
        check_type(connected_device_type, str)
        check_type(native_vlan_id, int)
        check_type(offset, int)
        check_type(limit, int)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "fabricId": fabric_id,
            "networkDeviceId": network_device_id,
            "portChannelName": port_channel_name,
            "connectedDeviceType": connected_device_type,
            "nativeVlanId": native_vlan_id,
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

        e_url = "/dna/intent/api/v1/sda/portChannels"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c747d79eb18e52f5a161006aa28df129_v3_1_3_0", json_data
        )

    def add_port_channels(
        self, headers=None, payload=None, active_validation=True, **request_parameters
    ):
        """Adds port channels based on user input. .

        Args:
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
            https://developer.cisco.com/docs/dna-center/#!add-port-channels
        """
        check_type(headers, dict)
        check_type(payload, list)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = payload or []
        if active_validation:
            self._request_validator(
                "jsd_f2b137487385de6925b7b6136d4b027_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/sda/portChannels"
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
            "bpm_f2b137487385de6925b7b6136d4b027_v3_1_3_0", json_data
        )

    def update_port_channels(
        self, headers=None, payload=None, active_validation=True, **request_parameters
    ):
        """Updates port channels based on user input. .

        Args:
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
            https://developer.cisco.com/docs/dna-center/#!update-port-channels
        """
        check_type(headers, dict)
        check_type(payload, list)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = payload or []
        if active_validation:
            self._request_validator(
                "jsd_bd421c1db8c5deaa3301b8cc73dd541_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/sda/portChannels"
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
            "bpm_bd421c1db8c5deaa3301b8cc73dd541_v3_1_3_0", json_data
        )

    def delete_port_channels(
        self,
        fabric_id,
        connected_device_type=None,
        network_device_id=None,
        port_channel_ids=None,
        port_channel_name=None,
        headers=None,
        **request_parameters
    ):
        """Deletes port channels based on user input. .

        Args:
            fabric_id(str): fabricId query parameter. ID of the fabric the device is assigned to. .
            network_device_id(str): networkDeviceId query parameter. ID of the network device. .
            port_channel_name(str): portChannelName query parameter. Name of the port channel. .
            port_channel_ids(str): portChannelIds query parameter. IDs of the port channels to be selectively
                deleted(Maximum number of IDs this parameter could consume is 10). .
            connected_device_type(str): connectedDeviceType query parameter. Connected device type of the port
                channel. The allowed values are [TRUNK, EXTENDED_NODE]. .
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
            https://developer.cisco.com/docs/dna-center/#!delete-port-channels
        """
        check_type(headers, dict)
        check_type(fabric_id, str, may_be_none=False)
        check_type(network_device_id, str)
        check_type(port_channel_name, str)
        check_type(port_channel_ids, str)
        check_type(connected_device_type, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "fabricId": fabric_id,
            "networkDeviceId": network_device_id,
            "portChannelName": port_channel_name,
            "portChannelIds": port_channel_ids,
            "connectedDeviceType": connected_device_type,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/sda/portChannels"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_fd48c49a3f65cecb1f84f10b69b04f5_v3_1_3_0", json_data
        )

    def get_port_channel_count(
        self,
        connected_device_type=None,
        fabric_id=None,
        network_device_id=None,
        port_channel_name=None,
        headers=None,
        **request_parameters
    ):
        """Returns the count of port channels that match the provided query parameters. .

        Args:
            fabric_id(str): fabricId query parameter. ID of the fabric the device is assigned to. .
            network_device_id(str): networkDeviceId query parameter. ID of the network device. .
            port_channel_name(str): portChannelName query parameter. Name of the port channel. .
            connected_device_type(str): connectedDeviceType query parameter. Connected device type of the port
                channel. The allowed values are [TRUNK, EXTENDED_NODE]. .
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
            https://developer.cisco.com/docs/dna-center/#!get-port-channel-count
        """
        check_type(headers, dict)
        check_type(fabric_id, str)
        check_type(network_device_id, str)
        check_type(port_channel_name, str)
        check_type(connected_device_type, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "fabricId": fabric_id,
            "networkDeviceId": network_device_id,
            "portChannelName": port_channel_name,
            "connectedDeviceType": connected_device_type,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/sda/portChannels/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_b6ba7d5504bb3493964063611a_v3_1_3_0", json_data
        )

    def delete_port_channel_by_id(self, id, headers=None, **request_parameters):
        """Deletes a port channel based on id. .

        Args:
            id(str): id path parameter. ID of the port channel. .
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
            https://developer.cisco.com/docs/dna-center/#!delete-port-channel-by-id
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

        e_url = "/dna/intent/api/v1/sda/portChannels/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_bcad6a4ea0850bf9b099b938bc55932_v3_1_3_0", json_data
        )

    def delete_provisioned_devices(
        self,
        clean_up_config=None,
        network_device_id=None,
        site_id=None,
        headers=None,
        **request_parameters
    ):
        """Delete provisioned devices based on query parameters. .

        Args:
            network_device_id(str): networkDeviceId query parameter. ID of the network device. .
            site_id(str): siteId query parameter. ID of the site hierarchy. .
            clean_up_config(bool): cleanUpConfig query parameter. Enable/disable configuration cleanup for the
                device(s). Defaults to true. .
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
            https://developer.cisco.com/docs/dna-center/#!delete-provisioned-devices
        """
        check_type(headers, dict)
        check_type(network_device_id, str)
        check_type(site_id, str)
        check_type(clean_up_config, bool)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "networkDeviceId": network_device_id,
            "siteId": site_id,
            "cleanUpConfig": clean_up_config,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/sda/provisionDevices"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_b049914e384051afbf87971d3066152b_v3_1_3_0", json_data
        )

    def provision_devices(
        self, headers=None, payload=None, active_validation=True, **request_parameters
    ):
        """Provisions network devices to respective Sites based on user input. .

        Args:
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
            https://developer.cisco.com/docs/dna-center/#!provision-devices
        """
        check_type(headers, dict)
        check_type(payload, list)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = payload or []
        if active_validation:
            self._request_validator(
                "jsd_bdcb514ae33b571795e4a42147d11f87_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/sda/provisionDevices"
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
            "bpm_bdcb514ae33b571795e4a42147d11f87_v3_1_3_0", json_data
        )

    def get_provisioned_devices(
        self,
        id=None,
        limit=None,
        network_device_id=None,
        offset=None,
        site_id=None,
        headers=None,
        **request_parameters
    ):
        """Returns the list of provisioned devices based on query parameters. .

        Args:
            id(str): id query parameter. ID of the provisioned device. .
            network_device_id(str): networkDeviceId query parameter. ID of the network device. .
            site_id(str): siteId query parameter. ID of the site hierarchy. .
            offset(int): offset query parameter. Starting record for pagination. .
            limit(int): limit query parameter. Maximum number of devices to return. The maximum number of objects
                supported in a single request is 500. .
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
            https://developer.cisco.com/docs/dna-center/#!get-provisioned-devices
        """
        check_type(headers, dict)
        check_type(id, str)
        check_type(network_device_id, str)
        check_type(site_id, str)
        check_type(offset, int)
        check_type(limit, int)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "id": id,
            "networkDeviceId": network_device_id,
            "siteId": site_id,
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

        e_url = "/dna/intent/api/v1/sda/provisionDevices"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_f974cbea9645bfda97affac9ea41ffe_v3_1_3_0", json_data
        )

    def re_provision_devices(
        self, headers=None, payload=None, active_validation=True, **request_parameters
    ):
        """Re-provisions network devices to the site based on the user input. .

        Args:
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
            https://developer.cisco.com/docs/dna-center/#!re-provision-devices
        """
        check_type(headers, dict)
        check_type(payload, list)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = payload or []
        if active_validation:
            self._request_validator(
                "jsd_f4b2825561e808787a16f7e0a1f_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/sda/provisionDevices"
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
            "bpm_f4b2825561e808787a16f7e0a1f_v3_1_3_0", json_data
        )

    def get_provisioned_devices_count(
        self, site_id=None, headers=None, **request_parameters
    ):
        """Returns the count of provisioned devices based on query parameters. .

        Args:
            site_id(str): siteId query parameter. ID of the site hierarchy. .
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
            https://developer.cisco.com/docs/dna-center/#!get-provisioned-devices-count
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

        e_url = "/dna/intent/api/v1/sda/provisionDevices/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_acb7d048a5455b75965c3706f8977_v3_1_3_0", json_data
        )

    def delete_provisioned_device_by_id(
        self, id, clean_up_config=None, headers=None, **request_parameters
    ):
        """Deletes provisioned device based on Id. .

        Args:
            id(str): id path parameter. ID of the provisioned device. .
            clean_up_config(bool): cleanUpConfig query parameter. Enable/disable configuration cleanup for the
                particular device. Defaults to true. .
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
            https://developer.cisco.com/docs/dna-center/#!delete-provisioned-device-by-id
        """
        check_type(headers, dict)
        check_type(clean_up_config, bool)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "cleanUpConfig": clean_up_config,
        }
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

        e_url = "/dna/intent/api/v1/sda/provisionDevices/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ab7cbac7eaa45f259c9035fb828f6c08_v3_1_3_0", json_data
        )

    def update_transit_networks(
        self, headers=None, payload=None, active_validation=True, **request_parameters
    ):
        """Updates transit networks based on user input. .

        Args:
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
            https://developer.cisco.com/docs/dna-center/#!update-transit-networks
        """
        check_type(headers, dict)
        check_type(payload, list)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = payload or []
        if active_validation:
            self._request_validator(
                "jsd_cc1599012a5a59c8abdda5376b5cc583_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/sda/transitNetworks"
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
            "bpm_cc1599012a5a59c8abdda5376b5cc583_v3_1_3_0", json_data
        )

    def get_transit_networks(
        self,
        id=None,
        limit=None,
        name=None,
        offset=None,
        type=None,
        headers=None,
        **request_parameters
    ):
        """Returns a list of transit networks that match the provided query parameters. .

        Args:
            id(str): id query parameter. ID of the transit network. .
            name(str): name query parameter. Name of the transit network. .
            type(str): type query parameter. Type of the transit network. Allowed values are [IP_BASED_TRANSIT,
                SDA_LISP_PUB_SUB_TRANSIT, SDA_LISP_BGP_TRANSIT]. .
            offset(int): offset query parameter. Starting record for pagination. .
            limit(int): limit query parameter. Maximum number of records to return. The maximum number of objects
                supported in a single request is 500. .
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
            https://developer.cisco.com/docs/dna-center/#!get-transit-networks
        """
        check_type(headers, dict)
        check_type(id, str)
        check_type(name, str)
        check_type(type, str)
        check_type(offset, int)
        check_type(limit, int)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "id": id,
            "name": name,
            "type": type,
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

        e_url = "/dna/intent/api/v1/sda/transitNetworks"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_eb415f4615ac09e61c6582ecca2fa_v3_1_3_0", json_data
        )

    def add_transit_networks(
        self, headers=None, payload=None, active_validation=True, **request_parameters
    ):
        """Adds transit networks based on user input. .

        Args:
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
            https://developer.cisco.com/docs/dna-center/#!add-transit-networks
        """
        check_type(headers, dict)
        check_type(payload, list)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = payload or []
        if active_validation:
            self._request_validator(
                "jsd_ae57085565e551594fc05b4db6a64af_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/sda/transitNetworks"
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
            "bpm_ae57085565e551594fc05b4db6a64af_v3_1_3_0", json_data
        )

    def get_transit_networks_count(self, type=None, headers=None, **request_parameters):
        """Returns the count of transit networks that match the provided query parameters. .

        Args:
            type(str): type query parameter. Type of the transit network. Allowed values are [IP_BASED_TRANSIT,
                SDA_LISP_PUB_SUB_TRANSIT, SDA_LISP_BGP_TRANSIT]. .
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
            https://developer.cisco.com/docs/dna-center/#!get-transit-networks-count
        """
        check_type(headers, dict)
        check_type(type, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "type": type,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/sda/transitNetworks/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_fe6a7f95437d57bd997d2c8f0482310d_v3_1_3_0", json_data
        )

    def delete_transit_network_by_id(self, id, headers=None, **request_parameters):
        """Deletes a transit network based on id. .

        Args:
            id(str): id path parameter. ID of the transit network. .
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
            https://developer.cisco.com/docs/dna-center/#!delete-transit-network-by-id
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

        e_url = "/dna/intent/api/v1/sda/transitNetworks/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_bc1bbf0065150ebabbe5e5bee3d80d7_v3_1_3_0", json_data
        )

    def sda_fabric_sites_readiness(
        self, order=None, sort_by=None, headers=None, **request_parameters
    ):
        """Retrieves a list of all SDA fabric sites along with their readiness status for Security Service Insertion (SSI)
        deployment. .

        Args:
            order(str): order query parameter. Whether ascending or descending order should be used to sort the
                response. .
            sort_by(str): sortBy query parameter. Sort results by the fabric site name. .
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
            https://developer.cisco.com/docs/dna-center/#!sda-fabric-sites-readiness
        """
        check_type(headers, dict)
        check_type(order, str)
        check_type(sort_by, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "order": order,
            "sortBy": sort_by,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/securityServiceInsertion/fabricSitesR" + "eadiness"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_d7e3a78757b95ad9985ff0acc067a238_v3_1_3_0", json_data
        )

    def readiness_status_for_a_fabric_site(
        self, id, order=None, headers=None, **request_parameters
    ):
        """Gets a list of SDA virtual networks for the specified fabric site, including their individual readiness status
        for Security Service Insertion (SSI) deployment. .

        Args:
            id(str): id path parameter. Sda fabric site id. .
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
            https://developer.cisco.com/docs/dna-center/#!readiness-status-for-a-fabric-site
        """
        check_type(headers, dict)
        check_type(order, str)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "order": order,
        }
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

        e_url = (
            "/dna/intent/api/v1/securityServiceInsertion/fabricSitesR" + "eadiness/{id}"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_aecbd1e1776e5bc3b28e7dc5b6d8be9f_v3_1_3_0", json_data
        )

    def readiness_status_of_switches_in_a_specified_virtual_network_within_a_fabric_site(
        self, id, site_id, headers=None, **request_parameters
    ):
        """Retrieves a list of switches list of switches for the specified virtual network within a fabric site, including
        their individual readiness status for Security Service Insertion (SSI) deployment. .

        Args:
            site_id(str): siteId path parameter. Sda fabric site id. .
            id(str): id path parameter. Virtual network id .
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
            https://developer.cisco.com/docs/dna-center/#!readiness-status-of-switches-in-a-specified-virtual-network-within-a-fabric-site
        """
        check_type(headers, dict)
        check_type(site_id, str, may_be_none=False)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "siteId": site_id,
            "id": id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/securityServiceInsertion/fabricSitesR"
            + "eadiness/{siteId}/virtualNetworks/{id}"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_bcf22d44f7252d49f614e0a1b42e235_v3_1_3_0", json_data
        )

    def security_service_insertion_readiness(self, headers=None, **request_parameters):
        """Retrieves readiness information for Security Service Insertion, including integration status, security group
        details, and access control information. .

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
            https://developer.cisco.com/docs/dna-center/#!security-service-insertion-readiness
        """
        check_type(headers, dict)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/securityServiceInsertion/systemReadin" + "ess"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c763eb5c55e9a9f3460f27ba14821_v3_1_3_0", json_data
        )

    def security_service_insertion_summary(
        self,
        fabric_site_name=None,
        limit=None,
        offset=None,
        order=None,
        headers=None,
        **request_parameters
    ):
        """Retrieves a summary of all Security Service Insertions (SSIs). .

        Args:
            order(str): order query parameter. The sorting order for the response can be specified as either
                ascending (asc) or descending (desc). If no value is specified, the default order is
                ascending (asc). .
            limit(int): limit query parameter. Maximum number of records to return. Default value is 500, minimum
                value is 1 and  maximum value is 500. .
            offset(int): offset query parameter. Starting record for pagination. The first record is numbered 1. .
            fabric_site_name(str): fabricSiteName query parameter. Filter by fabric site name (supports partial
                search). For example, searching for "London" will match "London fabric site", etc. .
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
            https://developer.cisco.com/docs/dna-center/#!security-service-insertion-summary
        """
        check_type(headers, dict)
        check_type(order, str)
        check_type(limit, int)
        check_type(offset, int)
        check_type(fabric_site_name, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "order": order,
            "limit": limit,
            "offset": offset,
            "fabricSiteName": fabric_site_name,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/securityServiceInsertionSummaries"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ff7589b0248580db8450a5434a91cab_v3_1_3_0", json_data
        )

    def count_of_security_service_insertion_summaries(
        self, headers=None, **request_parameters
    ):
        """Retrieves the total count of Security Service Insertion (SSI) summaries. .

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
            https://developer.cisco.com/docs/dna-center/#!count-of-security-service-insertion-summaries
        """
        check_type(headers, dict)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/securityServiceInsertionSummaries/cou" + "nt"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a6610acbace5872b265628f1bb24d21_v3_1_3_0", json_data
        )

    def security_service_insertions(
        self,
        fabric_site_name=None,
        limit=None,
        offset=None,
        order=None,
        headers=None,
        **request_parameters
    ):
        """Retrieves a list of all Security Service Insertions (SSIs) configured across fabric sites. .

        Args:
            limit(str): limit query parameter. Maximum number of records to return. Default value is 100, minimum
                value is 1 and maximum value is 100. .
            offset(int): offset query parameter. Starting record for pagination. The first record is numbered 1. .
            order(str): order query parameter. The sorting order for the response can be specified as either
                ascending (asc) or descending (desc). The default order is ascending (asc). .
            fabric_site_name(str): fabricSiteName query parameter. Filter by fabric site name (supports partial
                search). For example, searching for "London" will match "London fabric site", etc. .
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
            https://developer.cisco.com/docs/dna-center/#!security-service-insertions
        """
        check_type(headers, dict)
        check_type(limit, str)
        check_type(offset, int)
        check_type(order, str)
        check_type(fabric_site_name, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "limit": limit,
            "offset": offset,
            "order": order,
            "fabricSiteName": fabric_site_name,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/securityServiceInsertions"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory("bpm_835f549d94c86248a73cc472_v3_1_3_0", json_data)

    def create_security_service_insertion_on_a_specific_fabric_site(
        self,
        siteId=None,
        virtualNetworks=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Enables Security Service Insertion (SSI) on a fabric site within a network. Security Service Insertion allows
        the integration of security services, such as firewalls, into the fabric network, ensuring that traffic
        within Virtual Networks (VNs) is routed through these security devices. .

        Args:
            siteId(string): SDA's The ID of the fabric site where the service insertion is configured. .
            virtualNetworks(list): SDA's virtualNetworks (list of objects).
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
            https://developer.cisco.com/docs/dna-center/#!create-security-service-insertion-on-a-specific-fabric-site
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
            "siteId": siteId,
            "virtualNetworks": virtualNetworks,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator("jsd_b67ad5d41a330c4bdc9f7159f_v3_1_3_0").validate(
                _payload
            )

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/securityServiceInsertions"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(
                endpoint_full_url, params=_params, json=_payload, headers=_headers
            )
        else:
            json_data = self._session.post(
                endpoint_full_url, params=_params, json=_payload
            )

        return self._object_factory("bpm_b67ad5d41a330c4bdc9f7159f_v3_1_3_0", json_data)

    def count_of_security_service_insertions(self, headers=None, **request_parameters):
        """Retrieves the count of Security Service Insertions. .

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
            https://developer.cisco.com/docs/dna-center/#!count-of-security-service-insertions
        """
        check_type(headers, dict)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/securityServiceInsertions/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_bcad82ec2bd650b79161871e31119e8b_v3_1_3_0", json_data
        )

    def delete_security_service_insertion(self, id, headers=None, **request_parameters):
        """Removes the Security Service Insertion (SSI) configuration from the fabric site where it was created. .

        Args:
            id(str): id path parameter. The unique identifier of the Security Service Insertion (SSI). .
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
            https://developer.cisco.com/docs/dna-center/#!delete-security-service-insertion
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

        e_url = "/dna/intent/api/v1/securityServiceInsertions/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a0436f277d255a13aa82c427efc25f36_v3_1_3_0", json_data
        )

    def security_service_insertion_by_id(self, id, headers=None, **request_parameters):
        """Retrieves the details of a specific Security Service Insertion (SSI) by its ID. .

        Args:
            id(str): id path parameter. The unique identifier of the Security Service Insertion (SSI). .
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
            https://developer.cisco.com/docs/dna-center/#!security-service-insertion-by-id
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

        e_url = "/dna/intent/api/v1/securityServiceInsertions/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a9b856dc5a85d55a378e1f83c54f3b7_v3_1_3_0", json_data
        )

    def update_the_security_service_insertion(
        self,
        id,
        siteId=None,
        virtualNetworks=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Updates the Security Service Insertion (SSI). It allows modifications to the associated Virtual Networks (VNs),
        border devices, and firewall ips. .

        Args:
            siteId(string): SDA's The ID of the fabric site where the service insertion is configured. .
            virtualNetworks(list): SDA's virtualNetworks (list of objects).
            id(str): id path parameter. The unique identifier of the Security Service Insertion (SSI). .
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
            https://developer.cisco.com/docs/dna-center/#!update-the-security-service-insertion
        """
        check_type(headers, dict)
        check_type(payload, dict)
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
        _payload = {
            "siteId": siteId,
            "virtualNetworks": virtualNetworks,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator("jsd_493a5d8cab239b9d2d0b49ce_v3_1_3_0").validate(
                _payload
            )

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/securityServiceInsertions/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(
                endpoint_full_url, params=_params, json=_payload, headers=_headers
            )
        else:
            json_data = self._session.put(
                endpoint_full_url, params=_params, json=_payload
            )

        return self._object_factory("bpm_493a5d8cab239b9d2d0b49ce_v3_1_3_0", json_data)

    def add_virtual_network_with_scalable_groups(
        self,
        isGuestVirtualNetwork=None,
        scalableGroupNames=None,
        vManageVpnId=None,
        virtualNetworkName=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Add virtual network with scalable groups at global level .

        Args:
            isGuestVirtualNetwork(boolean): SDA's Guest Virtual Network enablement flag, default value is False. .
            scalableGroupNames(list): SDA's Scalable Group to be associated to virtual network  (list of strings).
            vManageVpnId(string): SDA's vManage vpn id for SD-WAN .
            virtualNetworkName(string): SDA's Virtual Network Name to be assigned at global level .
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
            https://developer.cisco.com/docs/dna-center/#!add-virtual-network-with-scalable-groups
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
            "virtualNetworkName": virtualNetworkName,
            "isGuestVirtualNetwork": isGuestVirtualNetwork,
            "scalableGroupNames": scalableGroupNames,
            "vManageVpnId": vManageVpnId,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_f5ebb9d50aab287f320d32181c0_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/virtual-network"
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
            "bpm_f5ebb9d50aab287f320d32181c0_v3_1_3_0", json_data
        )

    def delete_virtual_network_with_scalable_groups(
        self, virtual_network_name, headers=None, **request_parameters
    ):
        """Delete virtual network with scalable groups .

        Args:
            virtual_network_name(str): virtualNetworkName query parameter.
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
            https://developer.cisco.com/docs/dna-center/#!delete-virtual-network-with-scalable-groups
        """
        check_type(headers, dict)
        check_type(virtual_network_name, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "virtualNetworkName": virtual_network_name,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/virtual-network"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_f2e8552eabc5e5f97e1f40bcc4b4c75_v3_1_3_0", json_data
        )

    def get_virtual_network_with_scalable_groups(
        self, virtual_network_name, headers=None, **request_parameters
    ):
        """Get virtual network with scalable groups .

        Args:
            virtual_network_name(str): virtualNetworkName query parameter.
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
            https://developer.cisco.com/docs/dna-center/#!get-virtual-network-with-scalable-groups
        """
        check_type(headers, dict)
        check_type(virtual_network_name, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "virtualNetworkName": virtual_network_name,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/virtual-network"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ea4b1c052b855bd9a0e99f803e6185a5_v3_1_3_0", json_data
        )

    def update_virtual_network_with_scalable_groups(
        self,
        isGuestVirtualNetwork=None,
        scalableGroupNames=None,
        vManageVpnId=None,
        virtualNetworkName=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Update virtual network with scalable groups .

        Args:
            isGuestVirtualNetwork(boolean): SDA's Indicates whether to set this as guest virtual network or not,
                default value is False. .
            scalableGroupNames(list): SDA's Scalable Group Name to be associated to virtual network  (list of
                strings).
            vManageVpnId(string): SDA's vManage vpn id for SD-WAN .
            virtualNetworkName(string): SDA's Virtual Network Name to be assigned global level .
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
            https://developer.cisco.com/docs/dna-center/#!update-virtual-network-with-scalable-groups
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
            "virtualNetworkName": virtualNetworkName,
            "isGuestVirtualNetwork": isGuestVirtualNetwork,
            "scalableGroupNames": scalableGroupNames,
            "vManageVpnId": vManageVpnId,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_f9492367570c5f009cf8b5955790e87c_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/virtual-network"
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
            "bpm_f9492367570c5f009cf8b5955790e87c_v3_1_3_0", json_data
        )

    # Alias Functions
    @deprecated
    def get_port_channels(
        self,
        connected_device_type=None,
        fabric_id=None,
        limit=None,
        native_vlan_id=None,
        network_device_id=None,
        offset=None,
        port_channel_name=None,
        headers=None,
        **request_parameters
    ):
        """alias for get_port_channels_connectivity"""
        return self.get_port_channels_connectivity(
            connected_device_type=connected_device_type,
            fabric_id=fabric_id,
            limit=limit,
            native_vlan_id=native_vlan_id,
            network_device_id=network_device_id,
            offset=offset,
            port_channel_name=port_channel_name,
            headers=headers,
            **request_parameters
        )

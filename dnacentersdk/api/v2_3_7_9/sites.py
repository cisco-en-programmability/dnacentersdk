# -*- coding: utf-8 -*-
"""Cisco Catalyst Center Sites API wrapper.

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


class Sites(object):
    """Cisco Catalyst Center Sites API (version: 2.3.7.9).

    Wraps the Catalyst Center Sites
    API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new Sites
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Catalyst Center service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(Sites, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def get_sites_energy(
        self,
        attribute=None,
        device_category=None,
        end_time=None,
        limit=None,
        offset=None,
        order=None,
        site_hierarchy=None,
        site_hierarchy_id=None,
        site_id=None,
        site_name=None,
        site_type=None,
        sort_by=None,
        start_time=None,
        task_id=None,
        views=None,
        headers=None,
        **request_parameters
    ):
        """Retrieves a list of sites with energy data based on the specified query parameters. For detailed information
        about the usage of the API, please refer to the Open API specification document
        - https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-sitesEnergy-1.0.1-resolved.yaml .

        Args:
            start_time(int): startTime query parameter. Start time from which API queries the data set related to
                the resource. It must be specified in UNIX epochtime in milliseconds. Value is
                inclusive. If `startTime` is not provided, API will default to one day before `endTime`.
                .
            end_time(int): endTime query parameter. End time to which API queries the data set related to the
                resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive. If
                `endTime` is not provided, API will default to one day after `startTime`. If `startTime`
                is not provided either, API will default to current time. .
            limit(int): limit query parameter. Maximum number of records to return .
            offset(int): offset query parameter. Specifies the starting point within all records returned by the
                API. It's one based offset. The starting value is 1. .
            sort_by(str): sortBy query parameter. A field within the response to sort by. .
            order(str): order query parameter. The sort order of the field ascending or descending. .
            site_hierarchy(str): siteHierarchy query parameter. The full hierarchical breakdown of the site tree
                starting from Global site name and ending with the specific site name. The Root site is
                named "Global" (Ex. `Global/AreaName/BuildingName/FloorName`) This field supports
                wildcard asterisk (`*`) character search support. E.g. `*/San*, */San, /San*` Examples:
                `?siteHierarchy=Global/AreaName/BuildingName/FloorName` (single siteHierarchy requested)
                `?siteHierarchy=Global/AreaName/BuildingName/FloorName&siteHierarchy=Global/AreaName2/Bu
                ildingName2/FloorName2` (multiple siteHierarchies requested) .
            site_hierarchy_id(str): siteHierarchyId query parameter. The full hierarchy breakdown of the site tree
                in id form starting from Global site UUID and ending with the specific site UUID. (Ex.
                `globalUuid/areaUuid/buildingUuid/floorUuid`) This field supports wildcard asterisk
                (`*`) character search support. E.g. `*uuid*, *uuid, uuid*` Examples:
                `?siteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid `(single siteHierarchyId
                requested) `?siteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid&siteHierarchyId=
                globalUuid/areaUuid2/buildingUuid2/floorUuid2` (multiple siteHierarchyIds requested) .
            site_name(str): siteName query parameter. The name of the site. (Ex. `FloorName`) This field supports
                wildcard asterisk (`*`) character search support. E.g. `*San*, *San, San*` Examples:
                `?siteName=building1` (single siteName requested)
                `?siteName=building1&siteName=building2&siteName=building3` (multiple siteNames
                requested) .
            site_type(str): siteType query parameter. The type of the site. A site can be an area, building, or
                floor. Default when not provided will be `[floor,building,area]` Examples:
                `?siteType=area` (single siteType requested)
                `?siteType=area&siteType=building&siteType=floor` (multiple siteTypes requested) .
            device_category(str): deviceCategory query parameter. The list of device categories. Note that this
                filter specifies which devices will be included when calculating energy consumption
                values, rather than specifying the list of returned sites. Examples:
                `deviceCategory=Switch` (single device category requested)
                `deviceCategory=Switch&deviceCategory=Router` (multiple device categories with comma
                separator) .
            site_id(str): siteId query parameter. The UUID of the site. (Ex. `flooruuid`) Examples: `?siteId=id1`
                (single id requested) `?siteId=id1&siteId=id2&siteId=id3` (multiple ids requested) .
            views(str): views query parameter. The specific summary view being requested. This is an optional
                parameter which can be passed to get one or more of the specific health data summaries
                associated with sites. ### Response data proviced by each view: 1. **Site** [id,
                siteHierarchy, siteHierarchyId, siteType, latitude, longitude] 2. **Energy**
                [energyConsumed, estimatedCost, estimatedEmission, carbonIntensity, numberOfDevices]
                When this query parameter is not added the default summaries are: **[site,energy]**
                Examples: views=site (single view requested) views=site,energy (multiple views
                requested) .
            attribute(str): attribute query parameter. Supported Attributes: [id, siteHierarchy, siteHierarchyId,
                siteType, latitude, longitude, energyConsumed, estimatedCost, estimatedEmission,
                carbonIntensity, numberOfDevices] If length of attribute list is too long, please use
                'view' param instead. Examples: attribute=siteHierarchy (single attribute requested)
                attribute=siteHierarchy&attribute=energyConsumed (multiple attributes requested) .
            task_id(str): taskId query parameter. used to retrieve asynchronously processed & stored data. When this
                parameter is used, the rest of the request params will be ignored. .
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
            https://developer.cisco.com/docs/dna-center/#!get-sites-energy
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
        check_type(site_name, str)
        check_type(site_type, str)
        check_type(device_category, str)
        check_type(site_id, str)
        check_type(views, str)
        check_type(attribute, str)
        check_type(task_id, str)
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
            "siteHierarchy": site_hierarchy,
            "siteHierarchyId": site_hierarchy_id,
            "siteName": site_name,
            "siteType": site_type,
            "deviceCategory": device_category,
            "siteId": site_id,
            "views": views,
            "attribute": attribute,
            "taskId": task_id,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/energy/sites"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory("bpm_e9d85a8da71b95b17b58263c_v2_3_7_9", json_data)

    def count_sites_energy(
        self,
        device_category=None,
        end_time=None,
        site_hierarchy=None,
        site_hierarchy_id=None,
        site_id=None,
        site_name=None,
        site_type=None,
        start_time=None,
        task_id=None,
        headers=None,
        **request_parameters
    ):
        """Retrieves the total count of sites that provide energy data, filtered according to the specified query
        parameters. For detailed information about the usage of the API, please refer to the Open API
        specification document https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-sitesEnergy-1.0.1-resolved.yaml .

        Args:
            start_time(int): startTime query parameter. Start time from which API queries the data set related to
                the resource. It must be specified in UNIX epochtime in milliseconds. Value is
                inclusive. If `startTime` is not provided, API will default to one day before `endTime`.
                .
            end_time(int): endTime query parameter. End time to which API queries the data set related to the
                resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive. If
                `endTime` is not provided, API will default to one day after `startTime`. If `startTime`
                is not provided either, API will default to current time. .
            site_hierarchy(str): siteHierarchy query parameter. The full hierarchical breakdown of the site tree
                starting from Global site name and ending with the specific site name. The Root site is
                named "Global" (Ex. `Global/AreaName/BuildingName/FloorName`) This field supports
                wildcard asterisk (`*`) character search support. E.g. `*/San*, */San, /San*` Examples:
                `?siteHierarchy=Global/AreaName/BuildingName/FloorName` (single siteHierarchy requested)
                `?siteHierarchy=Global/AreaName/BuildingName/FloorName&siteHierarchy=Global/AreaName2/Bu
                ildingName2/FloorName2` (multiple siteHierarchies requested) .
            site_hierarchy_id(str): siteHierarchyId query parameter. The full hierarchy breakdown of the site tree
                in id form starting from Global site UUID and ending with the specific site UUID. (Ex.
                `globalUuid/areaUuid/buildingUuid/floorUuid`) This field supports wildcard asterisk
                (`*`) character search support. E.g. `*uuid*, *uuid, uuid*` Examples:
                `?siteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid `(single siteHierarchyId
                requested) `?siteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid&siteHierarchyId=
                globalUuid/areaUuid2/buildingUuid2/floorUuid2` (multiple siteHierarchyIds requested) .
            site_name(str): siteName query parameter. The name of the site. (Ex. `FloorName`) This field supports
                wildcard asterisk (`*`) character search support. E.g. `*San*, *San, San*` Examples:
                `?siteName=building1` (single siteName requested)
                `?siteName=building1&siteName=building2&siteName=building3` (multiple siteNames
                requested) .
            site_type(str): siteType query parameter. The type of the site. A site can be an area, building, or
                floor. Default when not provided will be `[floor,building,area]` Examples:
                `?siteType=area` (single siteType requested)
                `?siteType=area&siteType=building&siteType=floor` (multiple siteTypes requested) .
            device_category(str): deviceCategory query parameter. The list of device categories. Note that this
                filter specifies which devices will be included when calculating energy consumption
                values, rather than specifying the list of returned sites. Examples:
                `deviceCategory=Switch` (single device category requested)
                `deviceCategory=Switch&deviceCategory=Router` (multiple device categories with comma
                separator) .
            site_id(str): siteId query parameter. The UUID of the site. (Ex. `flooruuid`) Examples: `?siteId=id1`
                (single id requested) `?siteId=id1&siteId=id2&siteId=id3` (multiple ids requested) .
            task_id(str): taskId query parameter. used to retrieve asynchronously processed & stored data. When this
                parameter is used, the rest of the request params will be ignored. .
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
            https://developer.cisco.com/docs/dna-center/#!count-sites-energy
        """
        check_type(headers, dict)
        check_type(start_time, int)
        check_type(end_time, int)
        check_type(site_hierarchy, str)
        check_type(site_hierarchy_id, str)
        check_type(site_name, str)
        check_type(site_type, str)
        check_type(device_category, str)
        check_type(site_id, str)
        check_type(task_id, str)
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
            "siteName": site_name,
            "siteType": site_type,
            "deviceCategory": device_category,
            "siteId": site_id,
            "taskId": task_id,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/energy/sites/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c449f48a0b517185b32bfd53f33a5b_v2_3_7_9", json_data
        )

    def submit_request_to_query_sites_energy(
        self,
        aggregateAttributes=None,
        attributes=None,
        endTime=None,
        filters=None,
        page=None,
        startTime=None,
        task_id=None,
        views=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Submits a request to retrieve a list of sites along with their energy data for a specified time range, based on
        the filters provided in the request body. For detailed information about the usage of the API, please
        refer to the Open API specification document - https://github.com/cisco-en-programmability/catalyst-
        center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-sitesEnergy-1.0.1-resolved.yaml .

        Args:
            aggregateAttributes(list): Sites's aggregateAttributes (list of objects).
            attributes(list): Sites's Attributes (list of strings).
            endTime(integer): Sites's End Time.
            filters(list): Sites's filters (list of objects).
            page(object): Sites's page.
            startTime(integer): Sites's Start Time.
            views(list): Sites's Views (list of strings).
            task_id(str): taskId query parameter. used to retrieve asynchronously processed & stored data. When this
                parameter is used, the rest of the request params will be ignored. .
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
            https://developer.cisco.com/docs/dna-center/#!submit-request-to-query-sites-energy
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(task_id, str)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-CALLER-ID" in headers:
                check_type(headers.get("X-CALLER-ID"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "taskId": task_id,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = {
            "startTime": startTime,
            "endTime": endTime,
            "filters": filters,
            "views": views,
            "attributes": attributes,
            "aggregateAttributes": aggregateAttributes,
            "page": page,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_ae8282c90a7059ceb31b4072429d00cd_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/energy/sites/query"
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
            "bpm_ae8282c90a7059ceb31b4072429d00cd_v2_3_7_9", json_data
        )

    def query_sites_energy_for_the_given_task_id(
        self, task_id=None, headers=None, **request_parameters
    ):
        """Gets query sites energy task result for the given task ID. For detailed information about the usage of the API,
        please refer to the Open API specification document - https://github.com/cisco-en-
        programmability/catalyst-center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-
        sitesEnergy-1.0.1-resolved.yaml .

        Args:
            task_id(str): taskId query parameter. used to retrieve asynchronously processed & stored data. When this
                parameter is used, the rest of the request params will be ignored. .
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
            https://developer.cisco.com/docs/dna-center/#!query-sites-energy-for-the-given-task-i-d
        """
        check_type(headers, dict)
        check_type(task_id, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "taskId": task_id,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/energy/sites/query"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_e06041b1f59638e377ae39ed162bd_v2_3_7_9", json_data
        )

    def count_sites_energy_for_the_given_task_id(
        self, task_id=None, headers=None, **request_parameters
    ):
        """Gets count sites energy task result for the given task ID. For detailed information about the usage of the API,
        please refer to the Open API specification document - https://github.com/cisco-en-
        programmability/catalyst-center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-
        sitesEnergy-1.0.1-resolved.yaml .

        Args:
            task_id(str): taskId query parameter. used to retrieve asynchronously processed & stored data. When this
                parameter is used, the rest of the request params will be ignored. .
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
            https://developer.cisco.com/docs/dna-center/#!count-sites-energy-for-the-given-task-i-d
        """
        check_type(headers, dict)
        check_type(task_id, str)
        if headers is not None:
            if "X-CALLER-ID" in headers:
                check_type(headers.get("X-CALLER-ID"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "taskId": task_id,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/energy/sites/query/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_cc0a299df36558d8646580f0a0d283c_v2_3_7_9", json_data
        )

    def submit_request_to_count_sites_energy_from_query(
        self,
        aggregateAttributes=None,
        attributes=None,
        endTime=None,
        filters=None,
        page=None,
        startTime=None,
        task_id=None,
        views=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Submits a request to retrieve the total count of sites that provide energy data, filtered according to the
        specified query parameters. For detailed information about the usage of the API, please refer to the
        Open API specification document - https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-sitesEnergy-1.0.1-resolved.yaml .

        Args:
            aggregateAttributes(list): Sites's aggregateAttributes (list of objects).
            attributes(list): Sites's Attributes (list of strings).
            endTime(integer): Sites's End Time.
            filters(list): Sites's filters (list of objects).
            page(object): Sites's page.
            startTime(integer): Sites's Start Time.
            views(list): Sites's Views (list of strings).
            task_id(str): taskId query parameter. used to retrieve asynchronously processed & stored data. When this
                parameter is used, the rest of the request params will be ignored. .
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
            https://developer.cisco.com/docs/dna-center/#!submit-request-to-count-sites-energy-from-query
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(task_id, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "taskId": task_id,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = {
            "startTime": startTime,
            "endTime": endTime,
            "filters": filters,
            "views": views,
            "attributes": attributes,
            "aggregateAttributes": aggregateAttributes,
            "page": page,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_d0e1021de57d5e95bbea5d5bd86b481a_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/energy/sites/query/count"
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
            "bpm_d0e1021de57d5e95bbea5d5bd86b481a_v2_3_7_9", json_data
        )

    def get_site_energy_by_id(
        self,
        id,
        attribute=None,
        device_category=None,
        end_time=None,
        start_time=None,
        task_id=None,
        views=None,
        headers=None,
        **request_parameters
    ):
        """Retrieve the energy summary data for a specific site based on the site ID. For detailed information about the
        usage of the API, please refer to the Open API specification document - https://github.com/cisco-en-
        programmability/catalyst-center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-
        sitesEnergy-1.0.1-resolved.yaml .

        Args:
            id(str): id path parameter. The UUID of the Site. (Ex. "6bef213c-19ca-4170-8375-b694e251101c") .
            start_time(int): startTime query parameter. Start time from which API queries the data set related to
                the resource. It must be specified in UNIX epochtime in milliseconds. Value is
                inclusive. If `startTime` is not provided, API will default to one day before `endTime`.
                .
            end_time(int): endTime query parameter. End time to which API queries the data set related to the
                resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive. If
                `endTime` is not provided, API will default to one day after `startTime`. If `startTime`
                is not provided either, API will default to current time. .
            views(str): views query parameter. The specific summary view being requested. This is an optional
                parameter which can be passed to get one or more of the specific health data summaries
                associated with sites. ### Response data proviced by each view: 1. **Site** [id,
                siteHierarchy, siteHierarchyId, siteType, latitude, longitude] 2. **Energy**
                [energyConsumed, estimatedCost, estimatedEmission, carbonIntensity, numberOfDevices]
                When this query parameter is not added the default summaries are: **[site,energy]**
                Examples: views=site (single view requested) views=site,energy (multiple views
                requested) .
            attribute(str): attribute query parameter. Supported Attributes: [id, siteHierarchy, siteHierarchyId,
                siteType, latitude, longitude, energyConsumed, estimatedCost, estimatedEmission,
                carbonIntensity, numberOfDevices] If length of attribute list is too long, please use
                'view' param instead. Examples: attribute=siteHierarchy (single attribute requested)
                attribute=siteHierarchy&attribute=energyConsumed (multiple attributes requested) .
            device_category(str): deviceCategory query parameter. The list of device categories. Note that this
                filter specifies which devices will be included when calculating energy consumption
                values, rather than specifying the list of returned sites. Examples:
                `deviceCategory=Switch` (single device category requested)
                `deviceCategory=Switch&deviceCategory=Router` (multiple device categories with comma
                separator) .
            task_id(str): taskId query parameter. used to retrieve asynchronously processed & stored data. When this
                parameter is used, the rest of the request params will be ignored. .
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
            https://developer.cisco.com/docs/dna-center/#!get-site-energy-by-i-d
        """
        check_type(headers, dict)
        check_type(start_time, int)
        check_type(end_time, int)
        check_type(views, str)
        check_type(attribute, str)
        check_type(device_category, str)
        check_type(task_id, str)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-CALLER-ID" in headers:
                check_type(headers.get("X-CALLER-ID"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "startTime": start_time,
            "endTime": end_time,
            "views": views,
            "attribute": attribute,
            "deviceCategory": device_category,
            "taskId": task_id,
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

        e_url = "/dna/data/api/v1/energy/sites/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_b688ff94649e552ca2d9535136b2c0a6_v2_3_7_9", json_data
        )

    def read_list_of_site_health_summaries(
        self,
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
        **request_parameters
    ):
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
            site_hierarchy(str): siteHierarchy query parameter. The full hierarchical breakdown of the site tree
                starting from Global site name and ending with the specific site name. The Root site is
                named "Global" (Ex. `Global/AreaName/BuildingName/FloorName`) This field supports
                wildcard asterisk (`*`) character search support. E.g. `*/San*, */San, /San*` Examples:
                `?siteHierarchy=Global/AreaName/BuildingName/FloorName` (single siteHierarchy requested)
                `?siteHierarchy=Global/AreaName/BuildingName/FloorName&siteHierarchy=Global/AreaName2/Bu
                ildingName2/FloorName2` (multiple siteHierarchies requested) .
            site_hierarchy_id(str): siteHierarchyId query parameter. The full hierarchy breakdown of the site tree
                in id form starting from Global site UUID and ending with the specific site UUID. (Ex.
                `globalUuid/areaUuid/buildingUuid/floorUuid`) This field supports wildcard asterisk
                (`*`) character search support. E.g. `*uuid*, *uuid, uuid*` Examples:
                `?siteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid `(single siteHierarchyId
                requested) `?siteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid&siteHierarchyId=
                globalUuid/areaUuid2/buildingUuid2/floorUuid2` (multiple siteHierarchyIds requested) .
            site_type(str): siteType query parameter. The type of the site. A site can be an area, building, or
                floor. Default when not provided will be `[floor,building,area]` Examples:
                `?siteType=area` (single siteType requested)
                `?siteType=area&siteType=building&siteType=floor` (multiple siteTypes requested) .
            id(str): id query parameter. The list of entity Uuids. (Ex."6bef213c-19ca-4170-8375-b694e251101c")
                Examples: id=6bef213c-19ca-4170-8375-b694e251101c (single entity uuid requested) id=6bef
                213c-19ca-4170-8375-b694e251101c&id=32219612-819e-4b5e-a96b-cf22aca13dd9&id=2541e9a7-
                b80d-4955-8aa2-79b233318ba0 (multiple entity uuid with '&' separator) .
            view(str): view query parameter. The specific summary view being requested. This is an optional
                parameter which can be passed to get one or more of the specific health data summaries
                associated with sites. ### Response data proviced by each view: 1. **site** [id,
                siteHierarchy, siteHierarchyId, siteType, latitude, longitude] 2. **network** [id,
                networkDeviceCount, networkDeviceGoodHealthCount,wirelessDeviceCount,
                wirelessDeviceGoodHealthCount, accessDeviceCount, accessDeviceGoodHealthCount,
                coreDeviceCount, coreDeviceGoodHealthCount, distributionDeviceCount,
                distributionDeviceGoodHealthCount, routerDeviceCount, routerDeviceGoodHealthCount,
                apDeviceCount, apDeviceGoodHealthCount, wlcDeviceCount, wlcDeviceGoodHealthCount,
                switchDeviceCount, switchDeviceGoodHealthCount, networkDeviceGoodHealthPercentage,
                accessDeviceGoodHealthPercentage, coreDeviceGoodHealthPercentage,
                distributionDeviceGoodHealthPercentage, routerDeviceGoodHealthPercentage,
                apDeviceGoodHealthPercentage, wlcDeviceGoodHealthPercentage,
                switchDeviceGoodHealthPercentage, wirelessDeviceGoodHealthPercentage] 3. **client** [id,
                clientCount, clientGoodHealthCount, wiredClientCount, wirelessClientCount,
                wiredClientGoodHealthCount, wirelessClientGoodHealthCount, clientGoodHealthPercentage,
                wiredClientGoodHealthPercentage, wirelessClientGoodHealthPercentage, clientDataUsage] 4.
                **issue** [id, p1IssueCount, p2IssueCount, p3IssueCount, p4IssueCount, issueCount] When
                this query parameter is not added the default summaries are:
                **[site,client,network,issue]** Examples: view=client (single view requested)
                view=client&view=network&view=issue (multiple views requested) .
            attribute(str): attribute query parameter. Supported Attributes: [id, siteHierarchy, siteHierarchyId,
                siteType, latitude, longitude, networkDeviceCount,
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
            ApiError: If the Catalyst Center cloud returns an error.
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
            "siteHierarchy": site_hierarchy,
            "siteHierarchyId": site_hierarchy_id,
            "siteType": site_type,
            "id": id,
            "view": view,
            "attribute": attribute,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/siteHealthSummaries"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_b40b4f6d558bfbebcf8fcbc4df56b_v2_3_7_9", json_data
        )

    def read_site_count(
        self,
        end_time=None,
        id=None,
        site_hierarchy=None,
        site_hierarchy_id=None,
        site_type=None,
        headers=None,
        **request_parameters
    ):
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
            site_hierarchy(str): siteHierarchy query parameter. The full hierarchical breakdown of the site tree
                starting from Global site name and ending with the specific site name. The Root site is
                named "Global" (Ex. `Global/AreaName/BuildingName/FloorName`) This field supports
                wildcard asterisk (`*`) character search support. E.g. `*/San*, */San, /San*` Examples:
                `?siteHierarchy=Global/AreaName/BuildingName/FloorName` (single siteHierarchy requested)
                `?siteHierarchy=Global/AreaName/BuildingName/FloorName&siteHierarchy=Global/AreaName2/Bu
                ildingName2/FloorName2` (multiple siteHierarchies requested) .
            site_hierarchy_id(str): siteHierarchyId query parameter. The full hierarchy breakdown of the site tree
                in id form starting from Global site UUID and ending with the specific site UUID. (Ex.
                `globalUuid/areaUuid/buildingUuid/floorUuid`) This field supports wildcard asterisk
                (`*`) character search support. E.g. `*uuid*, *uuid, uuid*` Examples:
                `?siteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid `(single siteHierarchyId
                requested) `?siteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid&siteHierarchyId=
                globalUuid/areaUuid2/buildingUuid2/floorUuid2` (multiple siteHierarchyIds requested) .
            site_type(str): siteType query parameter. The type of the site. A site can be an area, building, or
                floor. Default when not provided will be `[floor,building,area]` Examples:
                `?siteType=area` (single siteType requested)
                `?siteType=area&siteType=building&siteType=floor` (multiple siteTypes requested) .
            id(str): id query parameter. The list of entity Uuids. (Ex."6bef213c-19ca-4170-8375-b694e251101c")
                Examples: id=6bef213c-19ca-4170-8375-b694e251101c (single entity uuid requested) id=6bef
                213c-19ca-4170-8375-b694e251101c&id=32219612-819e-4b5e-a96b-cf22aca13dd9&id=2541e9a7-
                b80d-4955-8aa2-79b233318ba0 (multiple entity uuid with '&' separator) .
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
            https://developer.cisco.com/docs/dna-center/#!read-site-count
        """
        check_type(headers, dict)
        check_type(end_time, int)
        check_type(site_hierarchy, str)
        check_type(site_hierarchy_id, str)
        check_type(site_type, str)
        check_type(id, str)
        if headers is not None:
            if "X-CALLER-ID" in headers:
                check_type(headers.get("X-CALLER-ID"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "endTime": end_time,
            "siteHierarchy": site_hierarchy,
            "siteHierarchyId": site_hierarchy_id,
            "siteType": site_type,
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

        e_url = "/dna/data/api/v1/siteHealthSummaries/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_e67558dd99925a0385f5f870bbb8f634_v2_3_7_9", json_data
        )

    def read_an_aggregated_summary_of_site_health_data(
        self,
        attribute=None,
        end_time=None,
        id=None,
        site_hierarchy=None,
        site_hierarchy_id=None,
        site_type=None,
        start_time=None,
        view=None,
        headers=None,
        **request_parameters
    ):
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
            site_hierarchy(str): siteHierarchy query parameter. The full hierarchical breakdown of the site tree
                starting from Global site name and ending with the specific site name. The Root site is
                named "Global" (Ex. `Global/AreaName/BuildingName/FloorName`) This field supports
                wildcard asterisk (`*`) character search support. E.g. `*/San*, */San, /San*` Examples:
                `?siteHierarchy=Global/AreaName/BuildingName/FloorName` (single siteHierarchy requested)
                `?siteHierarchy=Global/AreaName/BuildingName/FloorName&siteHierarchy=Global/AreaName2/Bu
                ildingName2/FloorName2` (multiple siteHierarchies requested) .
            site_hierarchy_id(str): siteHierarchyId query parameter. The full hierarchy breakdown of the site tree
                in id form starting from Global site UUID and ending with the specific site UUID. (Ex.
                `globalUuid/areaUuid/buildingUuid/floorUuid`) This field supports wildcard asterisk
                (`*`) character search support. E.g. `*uuid*, *uuid, uuid*` Examples:
                `?siteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid `(single siteHierarchyId
                requested) `?siteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid&siteHierarchyId=
                globalUuid/areaUuid2/buildingUuid2/floorUuid2` (multiple siteHierarchyIds requested) .
            site_type(str): siteType query parameter. The type of the site. A site can be an area, building, or
                floor. Default when not provided will be `[floor,building,area]` Examples:
                `?siteType=area` (single siteType requested)
                `?siteType=area&siteType=building&siteType=floor` (multiple siteTypes requested) .
            id(str): id query parameter. The list of entity Uuids. (Ex."6bef213c-19ca-4170-8375-b694e251101c")
                Examples: id=6bef213c-19ca-4170-8375-b694e251101c (single entity uuid requested) id=6bef
                213c-19ca-4170-8375-b694e251101c&id=32219612-819e-4b5e-a96b-cf22aca13dd9&id=2541e9a7-
                b80d-4955-8aa2-79b233318ba0 (multiple entity uuid with '&' separator) .
            view(str): view query parameter. The specific summary view being requested. This is an optional
                parameter which can be passed to get one or more of the specific health data summaries
                associated with sites. ### Response data proviced by each view: 1. **site** [id,
                siteHierarchy, siteHierarchyId, siteType, latitude, longitude] 2. **network** [id,
                networkDeviceCount, networkDeviceGoodHealthCount,wirelessDeviceCount,
                wirelessDeviceGoodHealthCount, accessDeviceCount, accessDeviceGoodHealthCount,
                coreDeviceCount, coreDeviceGoodHealthCount, distributionDeviceCount,
                distributionDeviceGoodHealthCount, routerDeviceCount, routerDeviceGoodHealthCount,
                apDeviceCount, apDeviceGoodHealthCount, wlcDeviceCount, wlcDeviceGoodHealthCount,
                switchDeviceCount, switchDeviceGoodHealthCount, networkDeviceGoodHealthPercentage,
                accessDeviceGoodHealthPercentage, coreDeviceGoodHealthPercentage,
                distributionDeviceGoodHealthPercentage, routerDeviceGoodHealthPercentage,
                apDeviceGoodHealthPercentage, wlcDeviceGoodHealthPercentage,
                switchDeviceGoodHealthPercentage, wirelessDeviceGoodHealthPercentage] 3. **client** [id,
                clientCount, clientGoodHealthCount, wiredClientCount, wirelessClientCount,
                wiredClientGoodHealthCount, wirelessClientGoodHealthCount, clientGoodHealthPercentage,
                wiredClientGoodHealthPercentage, wirelessClientGoodHealthPercentage, clientDataUsage] 4.
                **issue** [id, p1IssueCount, p2IssueCount, p3IssueCount, p4IssueCount, issueCount] When
                this query parameter is not added the default summaries are:
                **[site,client,network,issue]** Examples: view=client (single view requested)
                view=client&view=network&view=issue (multiple views requested) .
            attribute(str): attribute query parameter. Supported Attributes: [id, siteHierarchy, siteHierarchyId,
                siteType, latitude, longitude, networkDeviceCount,
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
            ApiError: If the Catalyst Center cloud returns an error.
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
            if "X-CALLER-ID" in headers:
                check_type(headers.get("X-CALLER-ID"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "startTime": start_time,
            "endTime": end_time,
            "siteHierarchy": site_hierarchy,
            "siteHierarchyId": site_hierarchy_id,
            "siteType": site_type,
            "id": id,
            "view": view,
            "attribute": attribute,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/siteHealthSummaries/summaryAnalytics"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_fc80b3e12ee9577a8e7fa5d4cd84e8fc_v2_3_7_9", json_data
        )

    def query_an_aggregated_summary_of_site_health_data(
        self,
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
        **request_parameters
    ):
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
            site_hierarchy(str): siteHierarchy query parameter. The full hierarchical breakdown of the site tree
                starting from Global site name and ending with the specific site name. The Root site is
                named "Global" (Ex. `Global/AreaName/BuildingName/FloorName`) This field supports
                wildcard asterisk (`*`) character search support. E.g. `*/San*, */San, /San*` Examples:
                `?siteHierarchy=Global/AreaName/BuildingName/FloorName` (single siteHierarchy requested)
                `?siteHierarchy=Global/AreaName/BuildingName/FloorName&siteHierarchy=Global/AreaName2/Bu
                ildingName2/FloorName2` (multiple siteHierarchies requested) .
            site_hierarchy_id(str): siteHierarchyId query parameter. The full hierarchy breakdown of the site tree
                in id form starting from Global site UUID and ending with the specific site UUID. (Ex.
                `globalUuid/areaUuid/buildingUuid/floorUuid`) This field supports wildcard asterisk
                (`*`) character search support. E.g. `*uuid*, *uuid, uuid*` Examples:
                `?siteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid `(single siteHierarchyId
                requested) `?siteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid&siteHierarchyId=
                globalUuid/areaUuid2/buildingUuid2/floorUuid2` (multiple siteHierarchyIds requested) .
            site_type(str): siteType query parameter. The type of the site. A site can be an area, building, or
                floor. Default when not provided will be `[floor,building,area]` Examples:
                `?siteType=area` (single siteType requested)
                `?siteType=area&siteType=building&siteType=floor` (multiple siteTypes requested) .
            id(str): id query parameter. The list of entity Uuids. (Ex."6bef213c-19ca-4170-8375-b694e251101c")
                Examples: id=6bef213c-19ca-4170-8375-b694e251101c (single entity uuid requested) id=6bef
                213c-19ca-4170-8375-b694e251101c&id=32219612-819e-4b5e-a96b-cf22aca13dd9&id=2541e9a7-
                b80d-4955-8aa2-79b233318ba0 (multiple entity uuid with '&' separator) .
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
            https://developer.cisco.com/docs/dna-center/#!query-an-aggregated-summary-of-site-health-data
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(site_hierarchy, str)
        check_type(site_hierarchy_id, str)
        check_type(site_type, str)
        check_type(id, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "siteHierarchy": site_hierarchy,
            "siteHierarchyId": site_hierarchy_id,
            "siteType": site_type,
            "id": id,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = {
            "startTime": startTime,
            "endTime": endTime,
            "views": views,
            "attributes": attributes,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_bec2dde673c5b2f940d0474fed32af6_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/siteHealthSummaries/summaryAnalytics"
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
            "bpm_bec2dde673c5b2f940d0474fed32af6_v2_3_7_9", json_data
        )

    def read_trend_analytics_data_for_a_grouping_of_sites_in_your_network(
        self,
        attribute=None,
        end_time=None,
        id=None,
        limit=None,
        offset=None,
        site_hierarchy=None,
        site_hierarchy_id=None,
        site_type=None,
        start_time=None,
        task_id=None,
        time_sort_order=None,
        trend_interval=None,
        headers=None,
        **request_parameters
    ):
        """Retrieves the time series information of health and issue data for sites specified by query parameters, or all
        sites. The data will be grouped based on the specified trend time interval. For detailed information
        about the usage of the API, please refer to the Open API specification document
        https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-siteHealthSummaries-2.0.0-resolved.yaml .

        Args:
            start_time(int): startTime query parameter. Start time from which API queries the data set related to
                the resource. It must be specified in UNIX epochtime in milliseconds. Value is
                inclusive. .
            end_time(int): endTime query parameter. End time to which API queries the data set related to the
                resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive. .
            site_hierarchy(str): siteHierarchy query parameter. The full hierarchical breakdown of the site tree
                starting from Global site name and ending with the specific site name. The Root site is
                named "Global" (Ex. `Global/AreaName/BuildingName/FloorName`) This field supports
                wildcard asterisk (`*`) character search support. E.g. `*/San*, */San, /San*` Examples:
                `?siteHierarchy=Global/AreaName/BuildingName/FloorName` (single siteHierarchy requested)
                `?siteHierarchy=Global/AreaName/BuildingName/FloorName&siteHierarchy=Global/AreaName2/Bu
                ildingName2/FloorName2` (multiple siteHierarchies requested) .
            site_hierarchy_id(str): siteHierarchyId query parameter. The full hierarchy breakdown of the site tree
                in id form starting from Global site UUID and ending with the specific site UUID. (Ex.
                `globalUuid/areaUuid/buildingUuid/floorUuid`) This field supports wildcard asterisk
                (`*`) character search support. E.g. `*uuid*, *uuid, uuid*` Examples:
                `?siteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid `(single siteHierarchyId
                requested) `?siteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid&siteHierarchyId=
                globalUuid/areaUuid2/buildingUuid2/floorUuid2` (multiple siteHierarchyIds requested) .
            site_type(str): siteType query parameter. The type of the site. A site can be an area, building, or
                floor. Default when not provided will be `[floor,building,area]` Examples:
                `?siteType=area` (single siteType requested)
                `?siteType=area&siteType=building&siteType=floor` (multiple siteTypes requested) .
            id(str): id query parameter. The list of entity Uuids. (Ex."6bef213c-19ca-4170-8375-b694e251101c")
                Examples: id=6bef213c-19ca-4170-8375-b694e251101c (single entity uuid requested) id=6bef
                213c-19ca-4170-8375-b694e251101c&id=32219612-819e-4b5e-a96b-cf22aca13dd9&id=2541e9a7-
                b80d-4955-8aa2-79b233318ba0 (multiple entity uuid with '&' separator) .
            trend_interval(str): trendInterval query parameter. The time window to aggregate the metrics. Interval
                can be 5 minutes or 10 minutes or 1 hour or 1 day or 7 days .
            limit(int): limit query parameter. Maximum number of records to return .
            offset(int): offset query parameter. Specifies the starting point within all records returned by the
                API. It's one based offset. The starting value is 1. .
            time_sort_order(str): timeSortOrder query parameter. The sort order of a time sorted API response. .
            attribute(str): attribute query parameter. Supported Analytics Attributes: [networkDeviceCount,
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
                p1IssueCount, p2IssueCount, p3IssueCount, p4IssueCount, issueCount]
                attribute=networkDeviceCount (single attribute requested)
                attribute=networkDeviceCount&attribute=clientCount (multiple attributes requested) .
            task_id(str): taskId query parameter. used to retrieve asynchronously processed & stored data. When this
                parameter is used, the rest of the request params will be ignored. .
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
            https://developer.cisco.com/docs/dna-center/#!read-trend-analytics-data-for-a-grouping-of-sites-in-your-network
        """
        check_type(headers, dict)
        check_type(start_time, int)
        check_type(end_time, int)
        check_type(site_hierarchy, str)
        check_type(site_hierarchy_id, str)
        check_type(site_type, str)
        check_type(id, str)
        check_type(trend_interval, str)
        check_type(limit, int)
        check_type(offset, int)
        check_type(time_sort_order, str)
        check_type(attribute, str)
        check_type(task_id, str)
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
            "siteType": site_type,
            "id": id,
            "trendInterval": trend_interval,
            "limit": limit,
            "offset": offset,
            "timeSortOrder": time_sort_order,
            "attribute": attribute,
            "taskId": task_id,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/siteHealthSummaries/trendAnalytics"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a47540d95b8ba6d78bfe5db7dbe2_v2_3_7_9", json_data
        )

    def read_site_health_summary_data_by_site_id(
        self,
        id,
        attribute=None,
        end_time=None,
        start_time=None,
        view=None,
        headers=None,
        **request_parameters
    ):
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
                associated with sites. ### Response data proviced by each view: 1. **site** [id,
                siteHierarchy, siteHierarchyId, siteType, latitude, longitude] 2. **network** [id,
                networkDeviceCount, networkDeviceGoodHealthCount,wirelessDeviceCount,
                wirelessDeviceGoodHealthCount, accessDeviceCount, accessDeviceGoodHealthCount,
                coreDeviceCount, coreDeviceGoodHealthCount, distributionDeviceCount,
                distributionDeviceGoodHealthCount, routerDeviceCount, routerDeviceGoodHealthCount,
                apDeviceCount, apDeviceGoodHealthCount, wlcDeviceCount, wlcDeviceGoodHealthCount,
                switchDeviceCount, switchDeviceGoodHealthCount, networkDeviceGoodHealthPercentage,
                accessDeviceGoodHealthPercentage, coreDeviceGoodHealthPercentage,
                distributionDeviceGoodHealthPercentage, routerDeviceGoodHealthPercentage,
                apDeviceGoodHealthPercentage, wlcDeviceGoodHealthPercentage,
                switchDeviceGoodHealthPercentage, wirelessDeviceGoodHealthPercentage] 3. **client** [id,
                clientCount, clientGoodHealthCount, wiredClientCount, wirelessClientCount,
                wiredClientGoodHealthCount, wirelessClientGoodHealthCount, clientGoodHealthPercentage,
                wiredClientGoodHealthPercentage, wirelessClientGoodHealthPercentage, clientDataUsage] 4.
                **issue** [id, p1IssueCount, p2IssueCount, p3IssueCount, p4IssueCount, issueCount] When
                this query parameter is not added the default summaries are:
                **[site,client,network,issue]** Examples: view=client (single view requested)
                view=client&view=network&view=issue (multiple views requested) .
            attribute(str): attribute query parameter. Supported Attributes: [id, siteHierarchy, siteHierarchyId,
                siteType, latitude, longitude, networkDeviceCount,
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!read-site-health-summary-data-by-site-id
        """
        check_type(headers, dict)
        check_type(start_time, int)
        check_type(end_time, int)
        check_type(view, str)
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
            "view": view,
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

        e_url = "/dna/data/api/v1/siteHealthSummaries/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_f214555abaa6a30cdbcc32e713_v2_3_7_9", json_data
        )

    def read_trend_analytics_data_for_a_specific_site_in_your_network(
        self,
        id,
        attribute=None,
        end_time=None,
        limit=None,
        offset=None,
        start_time=None,
        task_id=None,
        time_sort_order=None,
        trend_interval=None,
        headers=None,
        **request_parameters
    ):
        """Retrieves the time series information of health and issue data for a site specified by the path parameter. The
        data will be grouped based on the specified trend time interval. For detailed information about the
        usage of the API, please refer to the Open API specification document https://github.com/cisco-en-
        programmability/catalyst-center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-
        siteHealthSummaries-2.0.0-resolved.yaml .

        Args:
            id(str): id path parameter. unique site uuid .
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
            time_sort_order(str): timeSortOrder query parameter. The sort order of a time sorted API response. .
            attribute(str): attribute query parameter. Supported Analytics Attributes: [networkDeviceCount,
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
                p1IssueCount, p2IssueCount, p3IssueCount, p4IssueCount, issueCount]
                attribute=networkDeviceCount (single attribute requested)
                attribute=networkDeviceCount&attribute=clientCount (multiple attributes requested) .
            task_id(str): taskId query parameter. used to retrieve asynchronously processed & stored data. When this
                parameter is used, the rest of the request params will be ignored. .
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
            https://developer.cisco.com/docs/dna-center/#!read-trend-analytics-data-for-a-specific-site-in-your-network
        """
        check_type(headers, dict)
        check_type(start_time, int)
        check_type(end_time, int)
        check_type(trend_interval, str)
        check_type(limit, int)
        check_type(offset, int)
        check_type(time_sort_order, str)
        check_type(attribute, str)
        check_type(task_id, str)
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
            "timeSortOrder": time_sort_order,
            "attribute": attribute,
            "taskId": task_id,
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

        e_url = "/dna/data/api/v1/siteHealthSummaries/{id}/trendAnalytics"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a75ee097a016562cbf861c4c52df3e30_v2_3_7_9", json_data
        )

    def get_site_analytics_for_the_child_sites_of_given_parent_site_and_other_query_parameters(
        self,
        attribute=None,
        band=None,
        end_time=None,
        failure_category=None,
        failure_reason=None,
        limit=None,
        offset=None,
        order=None,
        site_hierarchy=None,
        site_hierarchy_id=None,
        site_id=None,
        site_type=None,
        sort_by=None,
        ssid=None,
        start_time=None,
        task_id=None,
        view=None,
        headers=None,
        **request_parameters
    ):
        """Returns site analytics for all child sites of given parent site. For detailed information about the usage of the
        API, please refer to the Open API specification document https://github.com/cisco-en-
        programmability/catalyst-center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-
        SiteKpiSummaries-1.0.0-resolved.yaml .

        Args:
            task_id(str): taskId query parameter. used to retrieve asynchronously processed & stored data. When this
                parameter is used, the rest of the request params will be ignored. .
            start_time(int): startTime query parameter. Start time from which API queries the data set related to
                the resource. It must be specified in UNIX epochtime in milliseconds. Value is
                inclusive. .
            end_time(int): endTime query parameter. End time to which API queries the data set related to the
                resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive. .
            site_hierarchy(str): siteHierarchy query parameter. The full hierarchical breakdown of the site tree
                starting from Global site name and ending with the specific site name. The Root site is
                named "Global" (Ex. `Global/AreaName/BuildingName/FloorName`) This field supports
                wildcard asterisk (`*`) character search support. E.g. `*/San*, */San, /San*` Examples:
                `?siteHierarchy=Global/AreaName/BuildingName/FloorName` (single siteHierarchy requested)
                `?siteHierarchy=Global/AreaName/BuildingName/FloorName&siteHierarchy=Global/AreaName2/Bu
                ildingName2/FloorName2` (multiple siteHierarchies requested) .
            site_hierarchy_id(str): siteHierarchyId query parameter. The full hierarchy breakdown of the site tree
                in id form starting from Global site UUID and ending with the specific site UUID. (Ex.
                `globalUuid/areaUuid/buildingUuid/floorUuid`) This field supports wildcard asterisk
                (`*`) character search support. E.g. `*uuid*, *uuid, uuid*` Examples:
                `?siteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid `(single siteHierarchyId
                requested) `?siteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid&siteHierarchyId=
                globalUuid/areaUuid2/buildingUuid2/floorUuid2` (multiple siteHierarchyIds requested) .
            site_id(str): siteId query parameter. The UUID of the site. (Ex. `flooruuid`) Examples: `?siteId=id1`
                (single id requested) `?siteId=id1&siteId=id2&siteId=id3` (multiple ids requested) .
            site_type(str): siteType query parameter. The type of the site. A site can be an area, building, or
                floor. Default when not provided will be `[floor,building,area]` Examples:
                `?siteType=area` (single siteType requested)
                `?siteType=area&siteType=building&siteType=floor` (multiple siteTypes requested) .
            ssid(str): ssid query parameter. SSID is the name of wireless network to which client connects to. It is
                also referred to as WLAN ID Wireless Local Area Network Identifier. Examples:
                `ssid=Alpha` (single ssid requested) `ssid=Alpha&ssid=Guest` (multiple ssid requested) .
            band(str): band query parameter. WiFi frequency band that client or Access Point operates. Band value is
                represented in Giga Hertz GHz Examples: `band=5` (single band requested)
                `band=2.4&band=6` (multiple band requested) .
            failure_category(str): failureCategory query parameter. Category of failure when a client fails to meet
                the threshold. Examples: `failureCategory=AUTH` (single failure category requested)
                `failureCategory=AUTH&failureCategory=DHCP` (multiple failure categories requested) .
            failure_reason(str): failureReason query parameter. Reason for failure when a client fails to meet the
                threshold. Examples: `failureReason=MOBILITY_FAILURE` (single ssid requested)
                `failureReason=REASON_IPLEARN_CONNECT_TIMEOUT&failureReason=ST_EAP_TIMEOUT`   (multiple
                ssid requested) .
            view(str): view query parameter.  The name of the View. Each view represents a specific data set. Please
                refer to the  SiteAnalyticsView  Model for supported views. View is predefined set of
                attributes supported by the API. Only the attributes related to the given view will be
                part of the API response along with default attributes. If multiple views are provided,
                then response will contain attributes from all those views. If no views are specified,
                all attributes will be returned. View Name Included Attributes coverage coverageAverage,
                coverageSuccessPercentage, coverageSuccessCount, coverageTotalCount,
                coverageFailureCount, coverageClientCount, coverageImpactedEntities,
                coverageFailureImpactedEntities, coverageFailureMetrics onboardingAttempts
                onboardingAttemptsSuccessPercentage, onboardingAttemptsSuccessCount,
                onboardingAttemptsTotalCount, onboardingAttemptsFailureCount,
                onboardingAttemptsClientCount, onboardingAttemptsImpactedEntities,
                onboardingAttemptsFailureImpactedEntities, onboardingAttemptsFailureMetrics
                onboardingDuration onboardingDurationAverage, onboardingDurationSuccessPercentage,
                onboardingDurationSuccessCount, onboardingDurationTotalCount,
                onboardingDurationFailureCount, onboardingDurationClientCount,
                onboardingDurationImpactedEntities, onboardingDurationFailureImpactedEntities,
                onboardingDurationFailureMetrics roamingAttempts roamingAttemptsSuccessPercentage,
                roamingAttemptsSuccessCount, roamingAttemptsTotalCount, roamingAttemptsFailureCount,
                roamingAttemptsClientCount, roamingAttemptsImpactedEntities,
                roamingAttemptsFailureImpactedEntities, roamingAttemptsFailureMetrics roamingDuration
                roamingDurationAverage, roamingDurationSuccessPercentage, roamingDurationSuccessCount,
                roamingDurationTotalCount, roamingDurationFailureCount, roamingDurationClientCount,
                roamingDurationImpactedEntities, roamingDurationFailureImpactedEntities,
                roamingDurationFailureMetrics connectionSpeed connectionSpeedAverage,
                connectionSpeedSuccessPercentage, connectionSpeedSuccessCount,
                connectionSpeedTotalCount, connectionSpeedFailureCount, connectionSpeedClientCount,
                connectionSpeedImpactedEntities, connectionSpeedFailureImpactedEntities,
                connectionSpeedFailureMetrics Examples:  view=connectionSpeed  (single view requested)
                view=roamingDuration&view=roamingAttempts  (multiple views requested)        .
            attribute(str): attribute query parameter. List of attributes related to site analytics. If these are
                provided, then only those attributes will be part of response along with the default
                attributes. Examples: `attribute=coverageAverage` (single attribute requested)
                `attribute=coverageFailureMetrics&attribute=coverageTotalCount` (multiple attributes
                requested) .
            limit(int): limit query parameter. Maximum number of records to return .
            offset(int): offset query parameter. Specifies the starting point within all records returned by the
                API. It's one based offset. The starting value is 1. .
            sort_by(str): sortBy query parameter. Field name on which sorting needs to be done .
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
            https://developer.cisco.com/docs/dna-center/#!get-site-analytics-for-the-child-sites-of-given-parent-site-and-other-query-parameters
        """
        check_type(headers, dict)
        check_type(task_id, str)
        check_type(start_time, int)
        check_type(end_time, int)
        check_type(site_hierarchy, str)
        check_type(site_hierarchy_id, str)
        check_type(site_id, str)
        check_type(site_type, str)
        check_type(ssid, str)
        check_type(band, str)
        check_type(failure_category, str)
        check_type(failure_reason, str)
        check_type(view, str)
        check_type(attribute, str)
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
            "taskId": task_id,
            "startTime": start_time,
            "endTime": end_time,
            "siteHierarchy": site_hierarchy,
            "siteHierarchyId": site_hierarchy_id,
            "siteId": site_id,
            "siteType": site_type,
            "ssid": ssid,
            "band": band,
            "failureCategory": failure_category,
            "failureReason": failure_reason,
            "view": view,
            "attribute": attribute,
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

        e_url = "/dna/data/api/v1/siteKpiSummaries"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_fd376c6a5d9382d5bee853c43031_v2_3_7_9", json_data
        )

    def get_the_total_number_of_site_analytics_records_available_for_for_given_set_of_query_parameters(
        self,
        end_time=None,
        site_hierarchy=None,
        site_hierarchy_id=None,
        site_id=None,
        site_type=None,
        start_time=None,
        headers=None,
        **request_parameters
    ):
        """Returns the total number of site analytics records available for for given set of query parameters. For detailed
        information about the usage of the API, please refer to the Open API specification document
        https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-SiteKpiSummaries-1.0.0-resolved.yaml .

        Args:
            start_time(int): startTime query parameter. Start time from which API queries the data set related to
                the resource. It must be specified in UNIX epochtime in milliseconds. Value is
                inclusive. .
            end_time(int): endTime query parameter. End time to which API queries the data set related to the
                resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive. .
            site_hierarchy(str): siteHierarchy query parameter. The full hierarchical breakdown of the site tree
                starting from Global site name and ending with the specific site name. The Root site is
                named "Global" (Ex. `Global/AreaName/BuildingName/FloorName`) This field supports
                wildcard asterisk (`*`) character search support. E.g. `*/San*, */San, /San*` Examples:
                `?siteHierarchy=Global/AreaName/BuildingName/FloorName` (single siteHierarchy requested)
                `?siteHierarchy=Global/AreaName/BuildingName/FloorName&siteHierarchy=Global/AreaName2/Bu
                ildingName2/FloorName2` (multiple siteHierarchies requested) .
            site_hierarchy_id(str): siteHierarchyId query parameter. The full hierarchy breakdown of the site tree
                in id form starting from Global site UUID and ending with the specific site UUID. (Ex.
                `globalUuid/areaUuid/buildingUuid/floorUuid`) This field supports wildcard asterisk
                (`*`) character search support. E.g. `*uuid*, *uuid, uuid*` Examples:
                `?siteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid `(single siteHierarchyId
                requested) `?siteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid&siteHierarchyId=
                globalUuid/areaUuid2/buildingUuid2/floorUuid2` (multiple siteHierarchyIds requested) .
            site_id(str): siteId query parameter. The UUID of the site. (Ex. `flooruuid`) Examples: `?siteId=id1`
                (single id requested) `?siteId=id1&siteId=id2&siteId=id3` (multiple ids requested) .
            site_type(str): siteType query parameter. The type of the site. A site can be an area, building, or
                floor. Default when not provided will be `[floor,building,area]` Examples:
                `?siteType=area` (single siteType requested)
                `?siteType=area&siteType=building&siteType=floor` (multiple siteTypes requested) .
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
            https://developer.cisco.com/docs/dna-center/#!get-the-total-number-of-site-analytics-records-available-for-for-given-set-of-query-parameters
        """
        check_type(headers, dict)
        check_type(start_time, int)
        check_type(end_time, int)
        check_type(site_hierarchy, str)
        check_type(site_hierarchy_id, str)
        check_type(site_id, str)
        check_type(site_type, str)
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
            "siteId": site_id,
            "siteType": site_type,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/siteKpiSummaries/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_af22da7f49fd5d658d0ce2992ea7fef9_v2_3_7_9", json_data
        )

    def get_site_analytics_for_the_child_sites_of_given_parent_site_and_other_filters(
        self,
        attributes=None,
        endTime=None,
        filters=None,
        page=None,
        startTime=None,
        views=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Returns site analytics for all child sites of given parent site. For detailed information about the usage of the
        API, please refer to the Open API specification document https://github.com/cisco-en-
        programmability/catalyst-center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-
        SiteKpiSummaries-1.0.0-resolved.yaml .

        Args:
            attributes(list): Sites's Attributes (list of strings).
            endTime(integer): Sites's End Time.
            filters(list): Sites's filters (list of objects).
            page(object): Sites's page.
            startTime(integer): Sites's Start Time.
            views(list): Sites's Views (list of strings).
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
            https://developer.cisco.com/docs/dna-center/#!get-site-analytics-for-the-child-sites-of-given-parent-site-and-other-filters
        """
        check_type(headers, dict)
        check_type(payload, dict)
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

        path_params = {}
        _payload = {
            "startTime": startTime,
            "endTime": endTime,
            "filters": filters,
            "attributes": attributes,
            "views": views,
            "page": page,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_a4829a44597bbf9813664eb75de0_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/siteKpiSummaries/query"
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
            "bpm_a4829a44597bbf9813664eb75de0_v2_3_7_9", json_data
        )

    def get_the_total_number_of_site_analytics_records_available_for_for_given_set_of_filters(
        self,
        endTime=None,
        filters=None,
        startTime=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Returns the total number of site analytics records available for for given set of filters. For detailed
        information about the usage of the API, please refer to the Open API specification document
        https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-SiteKpiSummaries-1.0.0-resolved.yaml .

        Args:
            endTime(integer): Sites's End Time.
            filters(list): Sites's filters (list of objects).
            startTime(integer): Sites's Start Time.
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
            https://developer.cisco.com/docs/dna-center/#!get-the-total-number-of-site-analytics-records-available-for-for-given-set-of-filters
        """
        check_type(headers, dict)
        check_type(payload, dict)
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

        path_params = {}
        _payload = {
            "startTime": startTime,
            "endTime": endTime,
            "filters": filters,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_db690b800995e35bc4e8c43d8ea6c18_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/siteKpiSummaries/query/count"
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
            "bpm_db690b800995e35bc4e8c43d8ea6c18_v2_3_7_9", json_data
        )

    def get_site_analytics_summary_data_for_the_given_task_id(
        self, task_id, headers=None, **request_parameters
    ):
        """Get site analytics summary data for the given task id. For detailed information about the usage of the API,
        please refer to the Open API specification document https://github.com/cisco-en-
        programmability/catalyst-center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-
        SiteKpiSummaries-1.0.0-resolved.yaml .

        Args:
            task_id(str): taskId query parameter. used to retrieve asynchronously processed & stored data. When this
                parameter is used, the rest of the request params will be ignored. .
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
            https://developer.cisco.com/docs/dna-center/#!get-site-analytics-summary-data-for-the-given-task-id
        """
        check_type(headers, dict)
        check_type(task_id, str, may_be_none=False)
        if headers is not None:
            if "X-CALLER-ID" in headers:
                check_type(headers.get("X-CALLER-ID"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "taskId": task_id,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/siteKpiSummaries/summaryAnalytics"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c846dfbe75601831b5de7e8771829_v2_3_7_9", json_data
        )

    def submit_request_for_site_analytics_summary_data(
        self,
        attributes=None,
        endTime=None,
        filters=None,
        startTime=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Submits the task to get summary analytics data for a given site. For detailed information about the usage of the
        API, please refer to the Open API specification document https://github.com/cisco-en-
        programmability/catalyst-center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-
        SiteKpiSummaries-1.0.0-resolved.yaml .

        Args:
            attributes(list): Sites's Attributes (list of strings).
            endTime(integer): Sites's End Time.
            filters(list): Sites's filters (list of objects).
            startTime(integer): Sites's Start Time.
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
            https://developer.cisco.com/docs/dna-center/#!submit-request-for-site-analytics-summary-data
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
            "startTime": startTime,
            "endTime": endTime,
            "filters": filters,
            "attributes": attributes,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_b8a44ba454de8a7bb52d3efe97ca_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/siteKpiSummaries/summaryAnalytics"
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
            "bpm_b8a44ba454de8a7bb52d3efe97ca_v2_3_7_9", json_data
        )

    def get_top_n_entities_related_to_site_analytics_for_the_given_task_id(
        self, task_id, headers=None, **request_parameters
    ):
        """Gets the topN analytics data for a given taskId. For detailed information about the usage of the API, please
        refer to the Open API specification document https://github.com/cisco-en-programmability/catalyst-
        center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-SiteKpiSummaries-1.0.0-resolved.yaml .

        Args:
            task_id(str): taskId query parameter. used to retrieve asynchronously processed & stored data. When this
                parameter is used, the rest of the request params will be ignored. .
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
            https://developer.cisco.com/docs/dna-center/#!get-top-n-entities-related-to-site-analytics-for-the-given-task-id
        """
        check_type(headers, dict)
        check_type(task_id, str, may_be_none=False)
        if headers is not None:
            if "X-CALLER-ID" in headers:
                check_type(headers.get("X-CALLER-ID"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "taskId": task_id,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/siteKpiSummaries/topNAnalytics"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_e256f5fc9757c483f41ffef3677fef_v2_3_7_9", json_data
        )

    def submit_request_for_top_n_entities_related_to_site_analytics(
        self,
        endTime=None,
        filters=None,
        groupBy=None,
        startTime=None,
        topN=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Gets the Top N entites related based on site analytics for a given kpi type. For detailed information about the
        usage of the API, please refer to the Open API specification document https://github.com/cisco-en-
        programmability/catalyst-center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-
        SiteKpiSummaries-1.0.0-resolved.yaml .

        Args:
            endTime(integer): Sites's End Time.
            filters(list): Sites's filters (list of objects).
            groupBy(list): Sites's Group By (list of strings).
            startTime(integer): Sites's Start Time.
            topN(integer): Sites's Top N.
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
            https://developer.cisco.com/docs/dna-center/#!submit-request-for-top-n-entities-related-to-site-analytics
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
            "startTime": startTime,
            "endTime": endTime,
            "topN": topN,
            "groupBy": groupBy,
            "filters": filters,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_d9e3276d1ed3511b80b22ea8388959c8_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/siteKpiSummaries/topNAnalytics"
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
            "bpm_d9e3276d1ed3511b80b22ea8388959c8_v2_3_7_9", json_data
        )

    def get_site_analytics_trend_data_for_the_given_task_id(
        self, task_id, headers=None, **request_parameters
    ):
        """Gets site analytics trend data for the given task id. For detailed information about the usage of the API,
        please refer to the Open API specification document https://github.com/cisco-en-
        programmability/catalyst-center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-
        SiteKpiSummaries-1.0.0-resolved.yaml .

        Args:
            task_id(str): taskId query parameter. used to retrieve asynchronously processed & stored data. When this
                parameter is used, the rest of the request params will be ignored. .
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
            https://developer.cisco.com/docs/dna-center/#!get-site-analytics-trend-data-for-the-given-task-id
        """
        check_type(headers, dict)
        check_type(task_id, str, may_be_none=False)
        if headers is not None:
            if "X-CALLER-ID" in headers:
                check_type(headers.get("X-CALLER-ID"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "taskId": task_id,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/siteKpiSummaries/trendAnalytics"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_f396d5c149b510a8cd8e560f8baae4b_v2_3_7_9", json_data
        )

    def submit_request_for_site_analytics_trend_data(
        self,
        attributes=None,
        endTime=None,
        filters=None,
        page=None,
        startTime=None,
        trendInterval=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Submits the task to get site analytics trend data for a given site. For detailed information about the usage of
        the API, please refer to the Open API specification document https://github.com/cisco-en-
        programmability/catalyst-center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-
        SiteKpiSummaries-1.0.0-resolved.yaml .

        Args:
            attributes(list): Sites's Attributes (list of strings).
            endTime(integer): Sites's End Time.
            filters(list): Sites's filters (list of objects).
            page(object): Sites's page.
            startTime(integer): Sites's Start Time.
            trendInterval(string): Sites's Trend Interval.
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
            https://developer.cisco.com/docs/dna-center/#!submit-request-for-site-analytics-trend-data
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
            "startTime": startTime,
            "endTime": endTime,
            "trendInterval": trendInterval,
            "filters": filters,
            "attributes": attributes,
            "page": page,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_edc44e0e7a513191cc16dc2b4da88e_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/siteKpiSummaries/trendAnalytics"
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
            "bpm_edc44e0e7a513191cc16dc2b4da88e_v2_3_7_9", json_data
        )

    def get_site_analytics_for_one_site(
        self,
        id,
        attribute=None,
        band=None,
        end_time=None,
        failure_category=None,
        failure_reason=None,
        ssid=None,
        start_time=None,
        task_id=None,
        view=None,
        headers=None,
        **request_parameters
    ):
        """Returns site analytics for the given site. For detailed information about the usage of the API, please refer to
        the Open API specification document https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-SiteKpiSummaries-1.0.0-resolved.yaml .

        Args:
            id(str): id path parameter. The Site UUID .
            task_id(str): taskId query parameter. used to retrieve asynchronously processed & stored data. When this
                parameter is used, the rest of the request params will be ignored. .
            start_time(int): startTime query parameter. Start time from which API queries the data set related to
                the resource. It must be specified in UNIX epochtime in milliseconds. Value is
                inclusive. .
            end_time(int): endTime query parameter. End time to which API queries the data set related to the
                resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive. .
            ssid(str): ssid query parameter. SSID is the name of wireless network to which client connects to. It is
                also referred to as WLAN ID Wireless Local Area Network Identifier. Examples:
                `ssid=Alpha` (single ssid requested) `ssid=Alpha&ssid=Guest` (multiple ssid requested) .
            band(str): band query parameter. WiFi frequency band that client or Access Point operates. Band value is
                represented in Giga Hertz GHz Examples: `band=5` (single band requested)
                `band=2.4&band=6` (multiple band requested) .
            failure_category(str): failureCategory query parameter. Category of failure when a client fails to meet
                the threshold. Examples: `failureCategory=AUTH` (single failure category requested)
                `failureCategory=AUTH&failureCategory=DHCP` (multiple failure categories requested) .
            failure_reason(str): failureReason query parameter. Reason for failure when a client fails to meet the
                threshold. Examples: `failureReason=MOBILITY_FAILURE` (single ssid requested)
                `failureReason=REASON_IPLEARN_CONNECT_TIMEOUT&failureReason=ST_EAP_TIMEOUT`   (multiple
                ssid requested) .
            view(str): view query parameter.  The name of the View. Each view represents a specific data set. Please
                refer to the  SiteAnalyticsView  Model for supported views. View is predefined set of
                attributes supported by the API. Only the attributes related to the given view will be
                part of the API response along with default attributes. If multiple views are provided,
                then response will contain attributes from all those views. If no views are specified,
                all attributes will be returned. View Name Included Attributes coverage coverageAverage,
                coverageSuccessPercentage, coverageSuccessCount, coverageTotalCount,
                coverageFailureCount, coverageClientCount, coverageImpactedEntities,
                coverageFailureImpactedEntities, coverageFailureMetrics onboardingAttempts
                onboardingAttemptsSuccessPercentage, onboardingAttemptsSuccessCount,
                onboardingAttemptsTotalCount, onboardingAttemptsFailureCount,
                onboardingAttemptsClientCount, onboardingAttemptsImpactedEntities,
                onboardingAttemptsFailureImpactedEntities, onboardingAttemptsFailureMetrics
                onboardingDuration onboardingDurationAverage, onboardingDurationSuccessPercentage,
                onboardingDurationSuccessCount, onboardingDurationTotalCount,
                onboardingDurationFailureCount, onboardingDurationClientCount,
                onboardingDurationImpactedEntities, onboardingDurationFailureImpactedEntities,
                onboardingDurationFailureMetrics roamingAttempts roamingAttemptsSuccessPercentage,
                roamingAttemptsSuccessCount, roamingAttemptsTotalCount, roamingAttemptsFailureCount,
                roamingAttemptsClientCount, roamingAttemptsImpactedEntities,
                roamingAttemptsFailureImpactedEntities, roamingAttemptsFailureMetrics roamingDuration
                roamingDurationAverage, roamingDurationSuccessPercentage, roamingDurationSuccessCount,
                roamingDurationTotalCount, roamingDurationFailureCount, roamingDurationClientCount,
                roamingDurationImpactedEntities, roamingDurationFailureImpactedEntities,
                roamingDurationFailureMetrics connectionSpeed connectionSpeedAverage,
                connectionSpeedSuccessPercentage, connectionSpeedSuccessCount,
                connectionSpeedTotalCount, connectionSpeedFailureCount, connectionSpeedClientCount,
                connectionSpeedImpactedEntities, connectionSpeedFailureImpactedEntities,
                connectionSpeedFailureMetrics Examples:  view=connectionSpeed  (single view requested)
                view=roamingDuration&view=roamingAttempts  (multiple views requested)        .
            attribute(str): attribute query parameter. List of attributes related to site analytics. If these are
                provided, then only those attributes will be part of response along with the default
                attributes. Examples: `attribute=coverageAverage` (single attribute requested)
                `attribute=coverageFailureMetrics&attribute=coverageTotalCount` (multiple attributes
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
            https://developer.cisco.com/docs/dna-center/#!get-site-analytics-for-one-site
        """
        check_type(headers, dict)
        check_type(task_id, str)
        check_type(start_time, int)
        check_type(end_time, int)
        check_type(ssid, str)
        check_type(band, str)
        check_type(failure_category, str)
        check_type(failure_reason, str)
        check_type(view, str)
        check_type(attribute, str)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-CALLER-ID" in headers:
                check_type(headers.get("X-CALLER-ID"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "taskId": task_id,
            "startTime": start_time,
            "endTime": end_time,
            "ssid": ssid,
            "band": band,
            "failureCategory": failure_category,
            "failureReason": failure_reason,
            "view": view,
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

        e_url = "/dna/data/api/v1/siteKpiSummaries/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_aec803dd6056a0b2a3ebd66dc136d3_v2_3_7_9", json_data
        )

    def assign_devices_to_site(
        self,
        site_id,
        device=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!assign-devices-to-site
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(site_id, str, may_be_none=False)
        if headers is not None:
            if "__runsync" in headers:
                check_type(headers.get("__runsync"), bool, may_be_none=False)
            if "__timeout" in headers:
                check_type(headers.get("__timeout"), int)
            if "__persistbapioutput" in headers:
                check_type(headers.get("__persistbapioutput"), bool, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "siteId": site_id,
        }
        _payload = {
            "device": device,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_a544e27e18e5412af3b68d915c8ca50_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/assign-device-to-site/{siteId}/device"
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
            "bpm_a544e27e18e5412af3b68d915c8ca50_v2_3_7_9", json_data
        )

    def export_map_archive(
        self,
        site_hierarchy_uuid,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Allows exporting a Map archive in an XML interchange format along with the associated images. .

        Args:
            site_hierarchy_uuid(str): siteHierarchyUuid path parameter. The site hierarchy element UUID to export,
                all child elements starting at this hierarchy element will be included. Limited to a
                hierarchy that contains 500 or fewer maps. .
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!export-map-archive
        """
        check_type(headers, dict)
        check_type(payload, (list, dict))
        check_type(site_hierarchy_uuid, str, may_be_none=False)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "siteHierarchyUuid": site_hierarchy_uuid,
        }
        _payload = payload or {}
        if active_validation:
            self._request_validator(
                "jsd_c937494318f952ba92eaeb82b144c338_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/maps/export/{siteHierarchyUuid}"
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
            "bpm_c937494318f952ba92eaeb82b144c338_v2_3_7_9", json_data
        )

    def import_map_archive_start_import(self, headers=None, **request_parameters):
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!import-map-archive-start-import
        """
        check_type(headers, dict)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
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

        e_url = "/dna/intent/api/v1/maps/import/start"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.post(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ea81890f92553aaed79952ab7ab363_v2_3_7_9", json_data
        )

    def import_map_archive_cancel_an_import(
        self, import_context_uuid, headers=None, **request_parameters
    ):
        """Cancels a previously initatied import, allowing the system to cleanup cached resources about that import data,
        and ensures the import cannot accidentally be performed / approved at a later time. .

        Args:
            import_context_uuid(str): importContextUuid path parameter. The unique import context UUID given by a
                previous call to Start Import API .
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
            https://developer.cisco.com/docs/dna-center/#!import-map-archive-cancel-an-import
        """
        check_type(headers, dict)
        check_type(import_context_uuid, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "importContextUuid": import_context_uuid,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/maps/import/{importContextUuid}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory("bpm_a59853e8a3462db736556ab4_v2_3_7_9", json_data)

    def import_map_archive_perform_import(
        self, import_context_uuid, headers=None, **request_parameters
    ):
        """For a previously initatied import, approves the import to be performed, accepting that data loss may occur.  A
        Map import will fully replace existing Maps data for the site(s) defined in the archive. The Map Archive
        Import Status API /maps/import/${contextUuid}/status should always be checked to validate the pre-import
        validation output prior to performing the import. .

        Args:
            import_context_uuid(str): importContextUuid path parameter. The unique import context UUID given by a
                previous call of Start Import API .
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
            https://developer.cisco.com/docs/dna-center/#!import-map-archive-perform-import
        """
        check_type(headers, dict)
        check_type(import_context_uuid, str, may_be_none=False)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "importContextUuid": import_context_uuid,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/maps/import/{importContextUuid}/perfo" + "rm"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.post(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_df05fb7a09595d0b9f6bc46b24275927_v2_3_7_9", json_data
        )

    def import_map_archive_import_status(
        self, import_context_uuid, headers=None, **request_parameters
    ):
        """Gets the status of a map archive import operation. For a map archive import that has just been initiated, will
        provide the result of validation of the archive and a pre-import preview of what will be performed if
        the import is performed.  Once an import is requested to be performed, this API will give the status of
        the import and upon completion a post-import summary of what was performed by the operation. .

        Args:
            import_context_uuid(str): importContextUuid path parameter. The unique import context UUID given by a
                previous and recent call to maps/import/start API .
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
            https://developer.cisco.com/docs/dna-center/#!import-map-archive-import-status
        """
        check_type(headers, dict)
        check_type(import_context_uuid, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "importContextUuid": import_context_uuid,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/maps/import/{importContextUuid}/statu" + "s"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c04c790688e4566c9f5eaa52b8fe39c8_v2_3_7_9", json_data
        )

    def maps_supported_access_points(self, headers=None, **request_parameters):
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!maps-supported-access-points
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

        e_url = "/dna/intent/api/v1/maps/supported-access-points"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a5e16b065e3534c8894e52d52540f99_v2_3_7_9", json_data
        )

    def get_membership(
        self,
        site_id,
        device_family=None,
        limit=None,
        offset=None,
        serial_number=None,
        headers=None,
        **request_parameters
    ):
        """Getting the site children details and device details. .

        Args:
            site_id(str): siteId path parameter. Site id to retrieve device associated with the site. .
            offset(int): offset query parameter. offset/starting row .
            limit(int): limit query parameter. Number of sites to be retrieved .
            device_family(str): deviceFamily query parameter. Device family name .
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-membership
        """
        check_type(headers, dict)
        check_type(offset, int)
        check_type(limit, int)
        check_type(device_family, str)
        check_type(serial_number, str)
        check_type(site_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "offset": offset,
            "limit": limit,
            "deviceFamily": device_family,
            "serialNumber": serial_number,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "siteId": site_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/membership/{siteId}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ca11e0b5f8d91395e2462a9cfdc_v2_3_7_9", json_data
        )

    def create_site(
        self,
        site=None,
        type=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!create-site
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if "__runsync" in headers:
                check_type(headers.get("__runsync"), bool, may_be_none=False)
            if "__timeout" in headers:
                check_type(headers.get("__timeout"), int)
            if "__persistbapioutput" in headers:
                check_type(headers.get("__persistbapioutput"), bool, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = {
            "type": type,
            "site": site,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_bce8e6b307ce52dd8f5546fbd78e05ee_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/site"
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
            "bpm_bce8e6b307ce52dd8f5546fbd78e05ee_v2_3_7_9", json_data
        )

    def get_site(
        self,
        limit=None,
        name=None,
        offset=None,
        site_id=None,
        type=None,
        headers=None,
        **request_parameters
    ):
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
            ApiError: If the Catalyst Center cloud returns an error.
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
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "name": name,
            "siteId": site_id,
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

        e_url = "/dna/intent/api/v1/site"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_dbdd6074bedc59b9a3edd6477897d659_v2_3_7_9", json_data
        )

    def get_site_health(
        self,
        limit=None,
        offset=None,
        site_type=None,
        timestamp=None,
        headers=None,
        **request_parameters
    ):
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-site-health
        """
        check_type(headers, dict)
        check_type(site_type, str)
        check_type(offset, int)
        check_type(limit, int)
        check_type(timestamp, int)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "siteType": site_type,
            "offset": offset,
            "limit": limit,
            "timestamp": timestamp,
        }

        if _params["timestamp"] is None:
            _params["timestamp"] = ""
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/site-health"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ae4b592f66035f24b55028f79c1b7290_v2_3_7_9", json_data
        )

    def get_devices_that_are_assigned_to_a_site(
        self,
        id,
        member_type,
        level=None,
        limit=None,
        offset=None,
        headers=None,
        **request_parameters
    ):
        """API to get devices that are assigned to a site. .

        Args:
            id(str): id path parameter. Site Id .
            offset(str): offset query parameter. Offset/starting index for pagination .
            limit(str): limit query parameter. Number of devices to be listed. Default and max supported value is
                500 .
            member_type(str): memberType query parameter. Member type (This API only supports the 'networkdevice'
                type) .
            level(str): level query parameter. Depth of site hierarchy to be considered to list the devices. If the
                provided value is -1, devices for all child sites will be listed. .
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
            https://developer.cisco.com/docs/dna-center/#!get-devices-that-are-assigned-to-a-site
        """
        check_type(headers, dict)
        check_type(offset, str)
        check_type(limit, str)
        check_type(member_type, str, may_be_none=False)
        check_type(level, str)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "offset": offset,
            "limit": limit,
            "memberType": member_type,
            "level": level,
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

        e_url = "/dna/intent/api/v1/site-member/{id}/member"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_cfabe762b2af55f282076fe2a14b6792_v2_3_7_9", json_data
        )

    def get_site_count(self, site_id=None, headers=None, **request_parameters):
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-site-count
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

        e_url = "/dna/intent/api/v1/site/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_e7a025fbe2c452fc82eedd5c50104aba_v2_3_7_9", json_data
        )

    def update_site(
        self,
        site_id,
        site=None,
        type=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!update-site
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(site_id, str, may_be_none=False)
        if headers is not None:
            if "__runsync" in headers:
                check_type(headers.get("__runsync"), bool)
            if "__timeout" in headers:
                check_type(headers.get("__timeout"), int)
            if "__persistbapioutput" in headers:
                check_type(headers.get("__persistbapioutput"), bool, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "siteId": site_id,
        }
        _payload = {
            "type": type,
            "site": site,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_df9908ad265e83ab77d73803925678_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/site/{siteId}"
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
            "bpm_df9908ad265e83ab77d73803925678_v2_3_7_9", json_data
        )

    def delete_site(self, site_id, headers=None, **request_parameters):
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!delete-site
        """
        check_type(headers, dict)
        check_type(site_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "siteId": site_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/site/{siteId}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ba5567f03dea5b6891957dd410319e3f_v2_3_7_9", json_data
        )

    def get_site_v2(
        self,
        group_name_hierarchy=None,
        id=None,
        limit=None,
        offset=None,
        type=None,
        headers=None,
        **request_parameters
    ):
        """API to get site(s) by site-name-hierarchy or siteId or type. List all sites if these parameters  are not given
        as an input. .

        Args:
            group_name_hierarchy(str): groupNameHierarchy query parameter. Site name hierarchy (E.g. Global/USA/CA)
                .
            id(str): id query parameter. Site Id .
            type(str): type query parameter. Site type (Acceptable values: area, building, floor) .
            offset(str): offset query parameter. Offset/starting index for pagination .
            limit(str): limit query parameter. Number of sites to be listed. Default and max supported value is 500
                .
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
            https://developer.cisco.com/docs/dna-center/#!get-site-v2
        """
        check_type(headers, dict)
        check_type(group_name_hierarchy, str)
        check_type(id, str)
        check_type(type, str)
        check_type(offset, str)
        check_type(limit, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "groupNameHierarchy": group_name_hierarchy,
            "id": id,
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

        e_url = "/dna/intent/api/v2/site"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c5e65cce2954fdb7177ac0a8e0b76f_v2_3_7_9", json_data
        )

    def get_site_count_v2(self, id=None, headers=None, **request_parameters):
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-site-count-v2
        """
        check_type(headers, dict)
        check_type(id, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
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

        e_url = "/dna/intent/api/v2/site/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_b10ff66e5568ebe6d41faeeabda22_v2_3_7_9", json_data
        )


# Alias Functions

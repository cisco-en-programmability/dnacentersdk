# -*- coding: utf-8 -*-
"""Cisco Catalyst Center Clients API wrapper.

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


class Clients(object):
    """Cisco Catalyst Center Clients API (version: 2.3.7.9).

    Wraps the Catalyst Center Clients
    API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new Clients
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Catalyst Center service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(Clients, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def retrieves_the_list_of_clients_while_also_offering_basic_filtering_and_sorting_capabilities(
        self,
        attribute=None,
        band=None,
        connected_network_device_name=None,
        end_time=None,
        ipv4_address=None,
        ipv6_address=None,
        limit=None,
        mac_address=None,
        offset=None,
        order=None,
        os_type=None,
        os_version=None,
        site_hierarchy=None,
        site_hierarchy_id=None,
        site_id=None,
        sort_by=None,
        ssid=None,
        start_time=None,
        type=None,
        view=None,
        wlc_name=None,
        headers=None,
        **request_parameters
    ):
        """Retrieves the list of clients, while also offering basic filtering and sorting capabilities. For detailed
        information about the usage of the API, please refer to the Open API specification document
        https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-clients1-1.0.0-resolved.yaml .

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
            type(str): type query parameter. The client device type whether client is connected to network through
                Wired or Wireless medium. .
            os_type(str): osType query parameter. Client device operating system type. This field supports wildcard
                (`*`) character-based search. If the value contains the (`*`) character, please use the
                /query API for regex search. Ex: `*iOS*` or `iOS*` or `*iOS` Examples: `osType=iOS`
                (single osType requested) `osType=iOS&osType=Android` (multiple osType requested) .
            os_version(str): osVersion query parameter. Client device operating system version This field supports
                wildcard (`*`) character-based search. If the value contains the (`*`) character, please
                use the /query API for regex search. Ex: `*14.3*` or `14.3*` or `*14.3` Examples:
                `osVersion=14.3` (single osVersion requested) `osVersion=14.3&osVersion=10.1` (multiple
                osVersion requested) .
            site_hierarchy(str): siteHierarchy query parameter. The full hierarchical breakdown of the site tree
                starting from Global site name and ending with the specific site name. The Root site is
                named "Global" (Ex. "Global/AreaName/BuildingName/FloorName") This field supports
                wildcard (`*`) character-based search. If the value contains the (`*`) character, please
                use the /query API for regex search.  Ex: `*BuildingName*` or `BuildingName*` or
                `*BuildingName` Examples: `siteHierarchy=Global/AreaName/BuildingName/FloorName` (single
                siteHierarchy requested) `siteHierarchy=Global/AreaName/BuildingName1/FloorName1&siteHie
                rarchy=Global/AreaName/BuildingName1/FloorName2` (multiple siteHierarchy requested) .
            site_hierarchy_id(str): siteHierarchyId query parameter. The full hierarchy breakdown of the site tree
                in id form starting from Global site UUID and ending with the specific site UUID. (Ex.
                "globalUuid/areaUuid/buildingUuid/floorUuid") This field supports wildcard (`*`)
                character-based search.  Ex: `*buildingUuid*` or `buildingUuid*` or `*buildingUuid`
                Examples: `siteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid` (single
                siteHierarchyId requested) `siteHierarchyId=globalUuid/areaUuid/buildingUuid1/floorUuid1
                &siteHierarchyId=globalUuid/areaUuid/buildingUuid1/floorUuid2` (multiple siteHierarchyId
                requested) .
            site_id(str): siteId query parameter. The site UUID without the top level hierarchy. (Ex."floorUuid")
                Examples: `siteId=floorUuid` (single siteId requested)
                `siteId=floorUuid1&siteId=floorUuid2` (multiple siteId requested) .
            ipv4_address(str): ipv4Address query parameter. IPv4 Address of the network entity either network device
                or client This field supports wildcard (`*`) character-based search. Ex: `*1.1*` or
                `1.1*` or `*1.1` Examples: `ipv4Address=1.1.1.1` (single ipv4Address requested)
                `ipv4Address=1.1.1.1&ipv4Address=2.2.2.2` (multiple ipv4Address requested) .
            ipv6_address(str): ipv6Address query parameter. IPv6 Address of the network entity either network device
                or client This field supports wildcard (`*`) character-based search. Ex: `*2001:db8*` or
                `2001:db8*` or `*2001:db8` Examples: `ipv6Address=2001:db8:0:0:0:0:2:1` (single
                ipv6Address requested)
                `ipv6Address=2001:db8:0:0:0:0:2:1&ipv6Address=2001:db8:85a3:8d3:1319:8a2e:370:7348`
                (multiple ipv6Address requested) .
            mac_address(str): macAddress query parameter. The macAddress of the network device or client This field
                supports wildcard (`*`) character-based search. Ex: `*AB:AB:AB*` or `AB:AB:AB*` or
                `*AB:AB:AB` Examples: `macAddress=AB:AB:AB:CD:CD:CD` (single macAddress requested)
                `macAddress=AB:AB:AB:CD:CD:DC&macAddress=AB:AB:AB:CD:CD:FE` (multiple macAddress
                requested) .
            wlc_name(str): wlcName query parameter. Wireless Controller name that reports the wireless client. This
                field supports wildcard (`*`) character-based search. If the value contains the (`*`)
                character, please use the /query API for regex search. Ex: `*wlc-25*` or `wlc-25*` or
                `*wlc-25` Examples: `wlcName=wlc-25` (single wlcName requested) `wlcName=wlc-25&wlc-34`
                (multiple wlcName requested) .
            connected_network_device_name(str): connectedNetworkDeviceName query parameter. Name of the neighbor
                network device that client is connected to. This field supports wildcard (`*`)
                character-based search. If the value contains the (`*`) character, please use the /query
                API for regex search. Ex: `*ap-25*` or `ap-25*` or `*ap-25` Examples:
                `connectedNetworkDeviceName=ap-25` (single connectedNetworkDeviceName requested)
                `connectedNetworkDeviceName=ap-25&ap-34` (multiple connectedNetworkDeviceName requested)
                .
            ssid(str): ssid query parameter. SSID is the name of wireless network to which client connects to. It is
                also referred to as WLAN ID Wireless Local Area Network Identifier. This field supports
                wildcard (`*`) character-based search. If the value contains the (`*`) character, please
                use the /query API for regex search. Ex: `*Alpha*` or `Alpha*` or `*Alpha` Examples:
                `ssid=Alpha` (single ssid requested) `ssid=Alpha&ssid=Guest` (multiple ssid requested) .
            band(str): band query parameter. WiFi frequency band that client or Access Point operates. Band value is
                represented in Giga Hertz GHz Examples: `band=5GHZ` (single band requested)
                `band=2.4GHZ&band=6GHZ` (multiple band requested) .
            view(str): view query parameter. Client related Views Refer to ClientView schema for list of views
                supported Examples: `view=Wireless` (single view requested)
                `view=WirelessHealth&view=WirelessTraffic` (multiple view requested) .
            attribute(str): attribute query parameter. List of attributes related to resource that can be requested
                to only be part of the response along with the required attributes. Refer to
                ClientAttribute schema for list of attributes supported Examples: `attribute=band`
                (single attribute requested) `attribute=band&attribute=ssid&attribute=overallScore`
                (multiple attribute requested) .
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-the-list-of-clients-while-also-offering-basic-filtering-and-sorting-capabilities
        """
        check_type(headers, dict)
        check_type(start_time, int)
        check_type(end_time, int)
        check_type(limit, int)
        check_type(offset, int)
        check_type(sort_by, str)
        check_type(order, str)
        check_type(type, str)
        check_type(os_type, str)
        check_type(os_version, str)
        check_type(site_hierarchy, str)
        check_type(site_hierarchy_id, str)
        check_type(site_id, str)
        check_type(ipv4_address, str)
        check_type(ipv6_address, str)
        check_type(mac_address, str)
        check_type(wlc_name, str)
        check_type(connected_network_device_name, str)
        check_type(ssid, str)
        check_type(band, str)
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
            "type": type,
            "osType": os_type,
            "osVersion": os_version,
            "siteHierarchy": site_hierarchy,
            "siteHierarchyId": site_hierarchy_id,
            "siteId": site_id,
            "ipv4Address": ipv4_address,
            "ipv6Address": ipv6_address,
            "macAddress": mac_address,
            "wlcName": wlc_name,
            "connectedNetworkDeviceName": connected_network_device_name,
            "ssid": ssid,
            "band": band,
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

        e_url = "/dna/data/api/v1/clients"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_dfcf64acc1815459acc146cd924e9877_v2_3_7_9", json_data
        )

    def retrieves_the_total_count_of_clients_by_applying_basic_filtering(
        self,
        band=None,
        connected_network_device_name=None,
        end_time=None,
        ipv4_address=None,
        ipv6_address=None,
        mac_address=None,
        os_type=None,
        os_version=None,
        site_hierarchy=None,
        site_hierarchy_id=None,
        site_id=None,
        ssid=None,
        start_time=None,
        type=None,
        wlc_name=None,
        headers=None,
        **request_parameters
    ):
        """Retrieves the number of clients by applying basic filtering. For detailed information about the usage of the
        API, please refer to the Open API specification document https://github.com/cisco-en-
        programmability/catalyst-center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-
        clients1-1.0.0-resolved.yaml .

        Args:
            start_time(int): startTime query parameter. Start time from which API queries the data set related to
                the resource. It must be specified in UNIX epochtime in milliseconds. Value is
                inclusive. If `startTime` is not provided, API will default to current time. .
            end_time(int): endTime query parameter. End time to which API queries the data set related to the
                resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive. .
            type(str): type query parameter. The client device type whether client is connected to network through
                Wired or Wireless medium. .
            os_type(str): osType query parameter. Client device operating system type. This field supports wildcard
                (`*`) character-based search. If the value contains the (`*`) character, please use the
                /query API for regex search. Ex: `*iOS*` or `iOS*` or `*iOS` Examples: `osType=iOS`
                (single osType requested) `osType=iOS&osType=Android` (multiple osType requested) .
            os_version(str): osVersion query parameter. Client device operating system version This field supports
                wildcard (`*`) character-based search. If the value contains the (`*`) character, please
                use the /query API for regex search. Ex: `*14.3*` or `14.3*` or `*14.3` Examples:
                `osVersion=14.3` (single osVersion requested) `osVersion=14.3&osVersion=10.1` (multiple
                osVersion requested) .
            site_hierarchy(str): siteHierarchy query parameter. The full hierarchical breakdown of the site tree
                starting from Global site name and ending with the specific site name. The Root site is
                named "Global" (Ex. "Global/AreaName/BuildingName/FloorName") This field supports
                wildcard (`*`) character-based search. If the value contains the (`*`) character, please
                use the /query API for regex search.  Ex: `*BuildingName*` or `BuildingName*` or
                `*BuildingName` Examples: `siteHierarchy=Global/AreaName/BuildingName/FloorName` (single
                siteHierarchy requested) `siteHierarchy=Global/AreaName/BuildingName1/FloorName1&siteHie
                rarchy=Global/AreaName/BuildingName1/FloorName2` (multiple siteHierarchy requested) .
            site_hierarchy_id(str): siteHierarchyId query parameter. The full hierarchy breakdown of the site tree
                in id form starting from Global site UUID and ending with the specific site UUID. (Ex.
                "globalUuid/areaUuid/buildingUuid/floorUuid") This field supports wildcard (`*`)
                character-based search.  Ex: `*buildingUuid*` or `buildingUuid*` or `*buildingUuid`
                Examples: `siteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid` (single
                siteHierarchyId requested) `siteHierarchyId=globalUuid/areaUuid/buildingUuid1/floorUuid1
                &siteHierarchyId=globalUuid/areaUuid/buildingUuid1/floorUuid2` (multiple siteHierarchyId
                requested) .
            site_id(str): siteId query parameter. The site UUID without the top level hierarchy. (Ex."floorUuid")
                Examples: `siteId=floorUuid` (single siteId requested)
                `siteId=floorUuid1&siteId=floorUuid2` (multiple siteId requested) .
            ipv4_address(str): ipv4Address query parameter. IPv4 Address of the network entity either network device
                or client This field supports wildcard (`*`) character-based search. Ex: `*1.1*` or
                `1.1*` or `*1.1` Examples: `ipv4Address=1.1.1.1` (single ipv4Address requested)
                `ipv4Address=1.1.1.1&ipv4Address=2.2.2.2` (multiple ipv4Address requested) .
            ipv6_address(str): ipv6Address query parameter. IPv6 Address of the network entity either network device
                or client This field supports wildcard (`*`) character-based search. Ex: `*2001:db8*` or
                `2001:db8*` or `*2001:db8` Examples: `ipv6Address=2001:db8:0:0:0:0:2:1` (single
                ipv6Address requested)
                `ipv6Address=2001:db8:0:0:0:0:2:1&ipv6Address=2001:db8:85a3:8d3:1319:8a2e:370:7348`
                (multiple ipv6Address requested) .
            mac_address(str): macAddress query parameter. The macAddress of the network device or client This field
                supports wildcard (`*`) character-based search. Ex: `*AB:AB:AB*` or `AB:AB:AB*` or
                `*AB:AB:AB` Examples: `macAddress=AB:AB:AB:CD:CD:CD` (single macAddress requested)
                `macAddress=AB:AB:AB:CD:CD:DC&macAddress=AB:AB:AB:CD:CD:FE` (multiple macAddress
                requested) .
            wlc_name(str): wlcName query parameter. Wireless Controller name that reports the wireless client. This
                field supports wildcard (`*`) character-based search. If the value contains the (`*`)
                character, please use the /query API for regex search. Ex: `*wlc-25*` or `wlc-25*` or
                `*wlc-25` Examples: `wlcName=wlc-25` (single wlcName requested) `wlcName=wlc-25&wlc-34`
                (multiple wlcName requested) .
            connected_network_device_name(str): connectedNetworkDeviceName query parameter. Name of the neighbor
                network device that client is connected to. This field supports wildcard (`*`)
                character-based search. If the value contains the (`*`) character, please use the /query
                API for regex search. Ex: `*ap-25*` or `ap-25*` or `*ap-25` Examples:
                `connectedNetworkDeviceName=ap-25` (single connectedNetworkDeviceName requested)
                `connectedNetworkDeviceName=ap-25&ap-34` (multiple connectedNetworkDeviceName requested)
                .
            ssid(str): ssid query parameter. SSID is the name of wireless network to which client connects to. It is
                also referred to as WLAN ID Wireless Local Area Network Identifier. This field supports
                wildcard (`*`) character-based search. If the value contains the (`*`) character, please
                use the /query API for regex search. Ex: `*Alpha*` or `Alpha*` or `*Alpha` Examples:
                `ssid=Alpha` (single ssid requested) `ssid=Alpha&ssid=Guest` (multiple ssid requested) .
            band(str): band query parameter. WiFi frequency band that client or Access Point operates. Band value is
                represented in Giga Hertz GHz Examples: `band=5GHZ` (single band requested)
                `band=2.4GHZ&band=6GHZ` (multiple band requested) .
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-the-total-count-of-clients-by-applying-basic-filtering
        """
        check_type(headers, dict)
        check_type(start_time, int)
        check_type(end_time, int)
        check_type(type, str)
        check_type(os_type, str)
        check_type(os_version, str)
        check_type(site_hierarchy, str)
        check_type(site_hierarchy_id, str)
        check_type(site_id, str)
        check_type(ipv4_address, str)
        check_type(ipv6_address, str)
        check_type(mac_address, str)
        check_type(wlc_name, str)
        check_type(connected_network_device_name, str)
        check_type(ssid, str)
        check_type(band, str)
        if headers is not None:
            if "X-CALLER-ID" in headers:
                check_type(headers.get("X-CALLER-ID"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "startTime": start_time,
            "endTime": end_time,
            "type": type,
            "osType": os_type,
            "osVersion": os_version,
            "siteHierarchy": site_hierarchy,
            "siteHierarchyId": site_hierarchy_id,
            "siteId": site_id,
            "ipv4Address": ipv4_address,
            "ipv6Address": ipv6_address,
            "macAddress": mac_address,
            "wlcName": wlc_name,
            "connectedNetworkDeviceName": connected_network_device_name,
            "ssid": ssid,
            "band": band,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/clients/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ed18d78d455f9a51049a09ae12d48_v2_3_7_9", json_data
        )

    def retrieves_the_list_of_clients_by_applying_complex_filters_while_also_supporting_aggregate_attributes(
        self,
        aggregateAttributes=None,
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
        """Retrieves the list of clients by applying complex filters while also supporting aggregate attributes. For
        detailed information about the usage of the API, please refer to the Open API specification document
        https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-clients1-1.0.0-resolved.yaml .

        Args:
            aggregateAttributes(list): Clients's aggregateAttributes (list of objects).
            attributes(list): Clients's Attributes (list of strings).
            endTime(integer): Clients's End Time.
            filters(list): Clients's filters (list of objects).
            page(object): Clients's page.
            startTime(integer): Clients's Start Time.
            views(list): Clients's Views (list of strings).
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-the-list-of-clients-by-applying-complex-filters-while-also-supporting-aggregate-attributes
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
            "views": views,
            "attributes": attributes,
            "filters": filters,
            "aggregateAttributes": aggregateAttributes,
            "page": page,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_ea5f116c0cd152bbb4a92c043738ea57_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/clients/query"
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
            "bpm_ea5f116c0cd152bbb4a92c043738ea57_v2_3_7_9", json_data
        )

    def retrieves_the_number_of_clients_by_applying_complex_filters(
        self,
        endTime=None,
        filters=None,
        startTime=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Retrieves the number of clients by applying complex filters. For detailed information about the usage of the
        API, please refer to the Open API specification document https://github.com/cisco-en-
        programmability/catalyst-center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-
        clients1-1.0.0-resolved.yaml .

        Args:
            endTime(integer): Clients's End Time.
            filters(list): Clients's filters (list of objects).
            startTime(integer): Clients's Start Time.
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-the-number-of-clients-by-applying-complex-filters
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
                "jsd_a2131eae5c1d8e73cd55eebf6a83_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/clients/query/count"
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
            "bpm_a2131eae5c1d8e73cd55eebf6a83_v2_3_7_9", json_data
        )

    def retrieves_summary_analytics_data_related_to_clients(
        self,
        aggregateAttributes=None,
        attributes=None,
        endTime=None,
        filters=None,
        groupBy=None,
        page=None,
        startTime=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Retrieves summary analytics data related to clients while applying complex filtering, aggregate functions, and
        grouping. This API facilitates obtaining consolidated insights into the performance and status of the
        clients. For detailed information about the usage of the API, please refer to the Open API specification
        document https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-clients1-1.0.0-resolved.yaml .

        Args:
            aggregateAttributes(list): Clients's aggregateAttributes (list of objects).
            attributes(list): Clients's Attributes (list of strings).
            endTime(integer): Clients's End Time.
            filters(list): Clients's filters (list of objects).
            groupBy(list): Clients's Group By (list of strings).
            page(object): Clients's page.
            startTime(integer): Clients's Start Time.
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-summary-analytics-data-related-to-clients
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
            "groupBy": groupBy,
            "attributes": attributes,
            "filters": filters,
            "aggregateAttributes": aggregateAttributes,
            "page": page,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_f210ff2d89425b4790ce56f19da7be92_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/clients/summaryAnalytics"
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
            "bpm_f210ff2d89425b4790ce56f19da7be92_v2_3_7_9", json_data
        )

    def retrieves_the_top_n_analytics_data_related_to_clients(
        self,
        aggregateAttributes=None,
        attributes=None,
        endTime=None,
        filters=None,
        groupBy=None,
        page=None,
        startTime=None,
        topN=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Retrieves the top N analytics data related to clients based on the provided input data. This API facilitates
        obtaining insights into the top-performing or most impacted clients. For detailed information about the
        usage of the API, please refer to the Open API specification document https://github.com/cisco-en-
        programmability/catalyst-center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-
        clients1-1.0.0-resolved.yaml .

        Args:
            aggregateAttributes(list): Clients's aggregateAttributes (list of objects).
            attributes(list): Clients's Attributes (list of strings).
            endTime(integer): Clients's End Time.
            filters(list): Clients's filters (list of objects).
            groupBy(list): Clients's Group By (list of strings).
            page(object): Clients's page.
            startTime(integer): Clients's Start Time.
            topN(integer): Clients's Top N.
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-the-top-n-analytics-data-related-to-clients
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
            "topN": topN,
            "groupBy": groupBy,
            "attributes": attributes,
            "filters": filters,
            "aggregateAttributes": aggregateAttributes,
            "page": page,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_f44ddd3c38c5a9484f5cb4e125447bc_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/clients/topNAnalytics"
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
            "bpm_f44ddd3c38c5a9484f5cb4e125447bc_v2_3_7_9", json_data
        )

    def retrieves_the_trend_analytics_data_related_to_clients(
        self,
        aggregateAttributes=None,
        attributes=None,
        endTime=None,
        filters=None,
        groupBy=None,
        page=None,
        startTime=None,
        trendInterval=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Retrieves the trend analytics of client data for the specified time range. The data will be grouped based on the
        given trend time interval. This API facilitates obtaining consolidated insights into the performance and
        status of the clients over the specified start and end time. For detailed information about the usage of
        the API, please refer to the Open API specification document https://github.com/cisco-en-
        programmability/catalyst-center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-
        clients1-1.0.0-resolved.yaml .

        Args:
            aggregateAttributes(list): Clients's aggregateAttributes (list of objects).
            attributes(list): Clients's Attributes (list of strings).
            endTime(integer): Clients's End Time.
            filters(list): Clients's filters (list of objects).
            groupBy(list): Clients's Group By (list of strings).
            page(object): Clients's page.
            startTime(integer): Clients's Start Time.
            trendInterval(string): Clients's Trend Interval.
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-the-trend-analytics-data-related-to-clients
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
            "trendInterval": trendInterval,
            "groupBy": groupBy,
            "attributes": attributes,
            "filters": filters,
            "aggregateAttributes": aggregateAttributes,
            "page": page,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_ffd2fefb57d5523c87a5d941eb93ddc3_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/clients/trendAnalytics"
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
            "bpm_ffd2fefb57d5523c87a5d941eb93ddc3_v2_3_7_9", json_data
        )

    def retrieves_specific_client_information_matching_the_macaddress(
        self,
        id,
        attribute=None,
        end_time=None,
        start_time=None,
        view=None,
        headers=None,
        **request_parameters
    ):
        """Retrieves specific client information matching the MAC address. For detailed information about the usage of the
        API, please refer to the Open API specification document https://github.com/cisco-en-
        programmability/catalyst-center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-
        clients1-1.0.0-resolved.yaml .

        Args:
            id(str): id path parameter. id is the client mac address. It can be specified is any notational
                conventions 01:23:45:67:89:AB or 01-23-45-67-89-AB or 0123.4567.89AB and is case
                insensitive .
            start_time(int): startTime query parameter. Start time from which API queries the data set related to
                the resource. It must be specified in UNIX epochtime in milliseconds. Value is
                inclusive. If `startTime` is not provided, API will default to current time. .
            end_time(int): endTime query parameter. End time to which API queries the data set related to the
                resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive. .
            view(str): view query parameter. Client related Views Refer to ClientView schema for list of views
                supported Examples: `view=Wireless` (single view requested)
                `view=WirelessHealth&view=WirelessTraffic` (multiple view requested) .
            attribute(str): attribute query parameter. List of attributes related to resource that can be requested
                to only be part of the response along with the required attributes. Refer to
                ClientAttribute schema for list of attributes supported Examples: `attribute=band`
                (single attribute requested) `attribute=band&attribute=ssid&attribute=overallScore`
                (multiple attribute requested) .
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-specific-client-information-matching-the-m-a-c-address
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

        e_url = "/dna/data/api/v1/clients/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ee00176282fd54ef90fc96a2c23d50ec_v2_3_7_9", json_data
        )

    def retrieves_specific_client_information_over_a_specified_period_of_time(
        self,
        id,
        aggregateAttributes=None,
        attributes=None,
        endTime=None,
        filters=None,
        groupBy=None,
        page=None,
        startTime=None,
        trendInterval=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Retrieves the time series information of a specific client by applying complex filters, aggregate functions, and
        grouping. The data will be grouped based on the specified trend time interval. For detailed information
        about the usage of the API, please refer to the Open API specification document
        https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-clients1-1.0.0-resolved.yaml .

        Args:
            aggregateAttributes(list): Clients's aggregateAttributes (list of objects).
            attributes(list): Clients's Attributes (list of strings).
            endTime(integer): Clients's End Time.
            filters(list): Clients's filters (list of objects).
            groupBy(list): Clients's Group By (list of strings).
            page(object): Clients's page.
            startTime(integer): Clients's Start Time.
            trendInterval(string): Clients's Trend Interval.
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-specific-client-information-over-a-specified-period-of-time
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
            "trendInterval": trendInterval,
            "groupBy": groupBy,
            "attributes": attributes,
            "filters": filters,
            "aggregateAttributes": aggregateAttributes,
            "page": page,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator("jsd_d9a13d575abdc26d485af708e7_v2_3_7_9").validate(
                _payload
            )

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/clients/{id}/trendAnalytics"
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
            "bpm_d9a13d575abdc26d485af708e7_v2_3_7_9", json_data
        )

    def get_clients_energy(
        self,
        attribute=None,
        cursor=None,
        device_category=None,
        device_sub_category=None,
        end_time=None,
        id=None,
        limit=None,
        order=None,
        site_hierarchy=None,
        site_hierarchy_id=None,
        site_id=None,
        sort_by=None,
        start_time=None,
        view=None,
        headers=None,
        **request_parameters
    ):
        """Retrieves a list of client devices with energy data based on the specified query parameters. For detailed
        information about the usage of the API, please refer to the Open API specification document
        - https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-deviceEnergy_1.0-1.0.1-resolved.yaml .

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
            cursor(str): cursor query parameter. It's an opaque string field that indicates the next record in the
                requested collection. If no records remain, the API returns a response with a count of
                zero. The default value is an empty string, and the initial value must be an empty
                string. The cursor value is populated by the API in the response page block. If the user
                wants more records, the cursor in the subsequent request must be updated with the value
                from the previous response. .
            sort_by(str): sortBy query parameter. A field within the response to sort by. .
            order(str): order query parameter. The sort order of the field ascending or descending. .
            id(str): id query parameter. The list of Mac addresses (e.g., `54:9F:C6:43:FF:80`). Examples:
                `id=54:9F:C6:43:FF:80` (single device requested)
                `id=54:9F:C6:43:FF:80&id=01:23:45:67:89:AB` .
            site_id(str): siteId query parameter. The UUID of the site. (Ex. `flooruuid`) Examples: `?siteId=id1`
                (single id requested) `?siteId=id1&siteId=id2&siteId=id3` (multiple ids requested) .
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
            device_category(str): deviceCategory query parameter. The list of device deviceCategories. Examples:
                `deviceCategory=AccessPoint` (single device family requested)
                `deviceCategory=AccessPoint&deviceCategory=OtherPOEDevice` (multiple device categories
                with comma separator) .
            device_sub_category(str): deviceSubCategory query parameter. The list of device sub categories.
                Examples: `deviceSubCategory=IP Phone 7821` (single sub category requested)
                `deviceSubCategory=IP Phone 7821&deviceSubCategory=IEEE PD` .
            view(str): view query parameter. List of views. View and attribute work in union. Each view will include
                its attributes. For example, view device includes all the attributes related to device.
                Please refer to `ClientDeviceEnergyView` model for supported list of views Examples:
                `view=device&view=energy` .
            attribute(str): attribute query parameter. List of attributes. Please refer to
                `ClientDeviceEnergyAttribute` for supported list of attributes Examples:
                `attribute=id&attribute=energyConsumed` .
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
            https://developer.cisco.com/docs/dna-center/#!get-clients-energy
        """
        check_type(headers, dict)
        check_type(start_time, int)
        check_type(end_time, int)
        check_type(limit, int)
        check_type(cursor, str)
        check_type(sort_by, str)
        check_type(order, str)
        check_type(id, str)
        check_type(site_id, str)
        check_type(site_hierarchy, str)
        check_type(site_hierarchy_id, str)
        check_type(device_category, str)
        check_type(device_sub_category, str)
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
            "cursor": cursor,
            "sortBy": sort_by,
            "order": order,
            "id": id,
            "siteId": site_id,
            "siteHierarchy": site_hierarchy,
            "siteHierarchyId": site_hierarchy_id,
            "deviceCategory": device_category,
            "deviceSubCategory": device_sub_category,
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

        e_url = "/dna/data/api/v1/energy/clients"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_dddfb3bc2f59f1905e64f5905e2296_v2_3_7_9", json_data
        )

    def count_clients_energy(
        self,
        device_category=None,
        device_sub_category=None,
        end_time=None,
        id=None,
        site_hierarchy=None,
        site_hierarchy_id=None,
        site_id=None,
        start_time=None,
        headers=None,
        **request_parameters
    ):
        """Retrieves the total count of client devices that provide energy data, filtered according to the specified query
        parameters. For detailed information about the usage of the API, please refer to the Open API
        specification document - https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-deviceEnergy_1.0-1.0.1-resolved.yaml .

        Args:
            start_time(int): startTime query parameter. Start time from which API queries the data set related to
                the resource. It must be specified in UNIX epochtime in milliseconds. Value is
                inclusive. If `startTime` is not provided, API will default to one day before `endTime`.
                .
            end_time(int): endTime query parameter. End time to which API queries the data set related to the
                resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive. If
                `endTime` is not provided, API will default to one day after `startTime`. If `startTime`
                is not provided either, API will default to current time. .
            id(str): id query parameter. The list of Mac addresses (e.g., `54:9F:C6:43:FF:80`). Examples:
                `id=54:9F:C6:43:FF:80` (single device requested)
                `id=54:9F:C6:43:FF:80&id=01:23:45:67:89:AB` .
            site_id(str): siteId query parameter. The UUID of the site. (Ex. `flooruuid`) Examples: `?siteId=id1`
                (single id requested) `?siteId=id1&siteId=id2&siteId=id3` (multiple ids requested) .
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
            device_category(str): deviceCategory query parameter. The list of device deviceCategories. Examples:
                `deviceCategory=AccessPoint` (single device family requested)
                `deviceCategory=AccessPoint&deviceCategory=OtherPOEDevice` (multiple device categories
                with comma separator) .
            device_sub_category(str): deviceSubCategory query parameter. The list of device sub categories.
                Examples: `deviceSubCategory=IP Phone 7821` (single sub category requested)
                `deviceSubCategory=IP Phone 7821&deviceSubCategory=IEEE PD` .
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
            https://developer.cisco.com/docs/dna-center/#!count-clients-energy
        """
        check_type(headers, dict)
        check_type(start_time, int)
        check_type(end_time, int)
        check_type(id, str)
        check_type(site_id, str)
        check_type(site_hierarchy, str)
        check_type(site_hierarchy_id, str)
        check_type(device_category, str)
        check_type(device_sub_category, str)
        if headers is not None:
            if "X-CALLER-ID" in headers:
                check_type(headers.get("X-CALLER-ID"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "startTime": start_time,
            "endTime": end_time,
            "id": id,
            "siteId": site_id,
            "siteHierarchy": site_hierarchy,
            "siteHierarchyId": site_hierarchy_id,
            "deviceCategory": device_category,
            "deviceSubCategory": device_sub_category,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/energy/clients/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_bc8798815ab89147f2054720da4d_v2_3_7_9", json_data
        )

    def query_clients_energy(
        self,
        aggregateAttributes=None,
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
        """Retrieves a list of client devices along with their energy data for a specified time range, based on the filters
        provided in the request body. For detailed information about the usage of the API, please refer to the
        Open API specification document - https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-deviceEnergy_1.0-1.0.1-resolved.yaml .

        Args:
            aggregateAttributes(list): Clients's aggregateAttributes (list of objects).
            attributes(list): Clients's Attributes (list of strings).
            endTime(integer): Clients's End Time.
            filters(list): Clients's filters (list of objects).
            page(object): Clients's page.
            startTime(integer): Clients's Start Time.
            views(list): Clients's Views (list of strings).
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
            https://developer.cisco.com/docs/dna-center/#!query-clients-energy
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
            "views": views,
            "attributes": attributes,
            "aggregateAttributes": aggregateAttributes,
            "page": page,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator("jsd_c536ac5a318629fc3d6b3dc236_v2_3_7_9").validate(
                _payload
            )

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/energy/clients/query"
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
            "bpm_c536ac5a318629fc3d6b3dc236_v2_3_7_9", json_data
        )

    def count_clients_energy_from_query(
        self,
        aggregateAttributes=None,
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
        """Retrieves the total count of client devices based on the specified complex filters. For detailed information
        about the usage of the API, please refer to the Open API specification document
        - https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-deviceEnergy_1.0-1.0.1-resolved.yaml .

        Args:
            aggregateAttributes(list): Clients's aggregateAttributes (list of objects).
            attributes(list): Clients's Attributes (list of strings).
            endTime(integer): Clients's End Time.
            filters(list): Clients's filters (list of objects).
            page(object): Clients's page.
            startTime(integer): Clients's Start Time.
            views(list): Clients's Views (list of strings).
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
            https://developer.cisco.com/docs/dna-center/#!count-clients-energy-from-query
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
            "views": views,
            "attributes": attributes,
            "aggregateAttributes": aggregateAttributes,
            "page": page,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_c765afc72581d862cd61f5139d224_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/energy/clients/query/count"
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
            "bpm_c765afc72581d862cd61f5139d224_v2_3_7_9", json_data
        )

    def get_client_energy_by_id(
        self,
        id,
        attribute=None,
        end_time=None,
        start_time=None,
        view=None,
        headers=None,
        **request_parameters
    ):
        """Retrieves client device energy data for a specified time range based on the client ID. For detailed information
        about the usage of the API, please refer to the Open API specification document
        - https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-deviceEnergy_1.0-1.0.1-resolved.yaml .

        Args:
            id(str): id path parameter. Mac address of a client device (e.g., 54:9F:C6:43:FF:80). It can be
                specified is any notational conventions   01:23:45:67:89:AB or 01-23-45-67-89-AB or
                0123.4567.89AB and is case insensitive. .
            start_time(int): startTime query parameter. Start time from which API queries the data set related to
                the resource. It must be specified in UNIX epochtime in milliseconds. Value is
                inclusive. If `startTime` is not provided, API will default to one day before `endTime`.
                .
            end_time(int): endTime query parameter. End time to which API queries the data set related to the
                resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive. If
                `endTime` is not provided, API will default to one day after `startTime`. If `startTime`
                is not provided either, API will default to current time. .
            view(str): view query parameter. List of views. View and attribute work in union. Each view will include
                its attributes. For example, view device includes all the attributes related to device.
                Please refer to `ClientDeviceEnergyView` model for supported list of views Examples:
                `view=device&view=energy` .
            attribute(str): attribute query parameter. List of attributes. Please refer to
                `ClientDeviceEnergyAttribute` for supported list of attributes Examples:
                `attribute=id&attribute=energyConsumed` .
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
            https://developer.cisco.com/docs/dna-center/#!get-client-energy-by-i-d
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

        e_url = "/dna/data/api/v1/energy/clients/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_f090c2a6b325d32be55209cd6839f30_v2_3_7_9", json_data
        )

    def get_client_detail(
        self, mac_address, timestamp=None, headers=None, **request_parameters
    ):
        """Returns detailed Client information retrieved by Mac Address for any given point of time. .

        Args:
            mac_address(str): macAddress query parameter. MAC Address of the client .
            timestamp(int): timestamp query parameter. Epoch time(in milliseconds) when the Client health data is
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
            https://developer.cisco.com/docs/dna-center/#!get-client-detail
        """
        check_type(headers, dict)
        check_type(mac_address, str, may_be_none=False)
        check_type(timestamp, int)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "macAddress": mac_address,
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

        e_url = "/dna/intent/api/v1/client-detail"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_f2c6333d8eb05491a16c2d32095e4352_v2_3_7_9", json_data
        )

    def get_client_enrichment_details(self, headers=None, **request_parameters):
        """Enriches a given network End User context (a network user-id or end user’s device Mac Address) with details
        about the user, the devices that the user is connected to and the assurance issues that the user is
        impacted by .

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
            https://developer.cisco.com/docs/dna-center/#!get-client-enrichment-details
        """
        check_type(headers, dict)
        if headers is not None:
            if "entity_type" in headers:
                check_type(headers.get("entity_type"), str, may_be_none=False)
            if "entity_value" in headers:
                check_type(headers.get("entity_value"), str, may_be_none=False)
            if "issueCategory" in headers:
                check_type(headers.get("issueCategory"), str)
            if "__persistbapioutput" in headers:
                check_type(headers.get("__persistbapioutput"), bool)
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

        e_url = "/dna/intent/api/v1/client-enrichment-details"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_dfd2751065bfb8c2367dd726df316_v2_3_7_9", json_data
        )

    def get_overall_client_health(
        self, timestamp=None, headers=None, **request_parameters
    ):
        """Returns Overall Client Health information by Client type (Wired and Wireless) for any given point of time .

        Args:
            timestamp(int): timestamp query parameter. Epoch time(in milliseconds) when the Client health data is
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
            https://developer.cisco.com/docs/dna-center/#!get-overall-client-health
        """
        check_type(headers, dict)
        check_type(timestamp, int)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
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

        e_url = "/dna/intent/api/v1/client-health"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_f58ddf5cee095688aed79a9bb26e21e8_v2_3_7_9", json_data
        )

    def client_proximity(
        self,
        username,
        number_days=None,
        time_resolution=None,
        headers=None,
        **request_parameters
    ):
        """This intent API will provide client proximity information for a specific wireless user. Proximity is defined as
        presence on the same floor at the same time as the specified wireless user. The Proximity workflow
        requires the subscription to the following event (via the Event Notification workflow) prior to making
        this API call: NETWORK-CLIENTS-3-506 Client Proximity Report. .

        Args:
            username(str): username query parameter. Wireless client username for which proximity information is
                required .
            number_days(int): number_days query parameter. Number of days to track proximity until current date.
                Defaults and maximum up to 14 days. .
            time_resolution(int): time_resolution query parameter. Time interval (in minutes) to measure proximity.
                Defaults to 15 minutes with a minimum 5 minutes. .
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
            https://developer.cisco.com/docs/dna-center/#!client-proximity
        """
        check_type(headers, dict)
        check_type(username, str, may_be_none=False)
        check_type(number_days, int)
        check_type(time_resolution, int)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "username": username,
            "number_days": number_days,
            "time_resolution": time_resolution,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/client-proximity"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c141467ea25ec0aa91cbcaff070354_v2_3_7_9", json_data
        )


# Alias Functions

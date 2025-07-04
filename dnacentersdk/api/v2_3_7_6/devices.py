# -*- coding: utf-8 -*-
"""Cisco DNA Center Devices API wrapper.

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


class Devices(object):
    """Cisco DNA Center Devices API (version: 2.3.7.6).

    Wraps the DNA Center Devices
    API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new Devices
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the DNA Center service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(Devices, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def gets_the_total_number_network_devices_based_on_the_provided_complex_filters_and_aggregation_functions_v1(
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
        """Gets the total number Network Devices based on the provided complex filters and aggregation functions. For
        detailed information about the usage of the API, please refer to the Open API specification document
        https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-AssuranceNetworkDevices-1.0.2-resolved.yaml .

        Args:
            aggregateAttributes(list): Devices's aggregateAttributes (list of objects).
            attributes(list): Devices's Attributes (list of strings).
            endTime(integer): Devices's End Time.
            filters(list): Devices's filters (list of objects).
            page(object): Devices's page.
            startTime(integer): Devices's Start Time.
            views(list): Devices's Views (list of strings).
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
            https://developer.cisco.com/docs/dna-center/#!gets-the-total-number-network-devices-based-on-the-provided-complex-filters-and-aggregation-functions
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
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
                "jsd_a421626459dcbe382c43ffcbddae_v2_3_7_6"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/data/api/v1/networkDevices/query/count"
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
            "bpm_a421626459dcbe382c43ffcbddae_v2_3_7_6", json_data
        )

    def query_assurance_events_v1(
        self,
        device_family,
        ap_mac=None,
        attribute=None,
        client_mac=None,
        end_time=None,
        limit=None,
        message_type=None,
        network_device_id=None,
        network_device_name=None,
        offset=None,
        order=None,
        severity=None,
        site_hierarchy_id=None,
        site_id=None,
        sort_by=None,
        start_time=None,
        view=None,
        headers=None,
        **request_parameters
    ):
        """Returns the list of events discovered by DNA Center, determined by the complex filters. Please refer to the
        'API Support Documentation' section to understand which fields are supported. For detailed information
        about the usage of the API, please refer to the Open API specification document
        https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-AssuranceEvents-1.0.0-resolved.yaml .

        Args:
            device_family(str): deviceFamily query parameter. Device family. Please note that multiple
                families across network device type and client type is not allowed. For example,
                choosing `Routers` along with `Wireless Client` or `Unified AP` is not supported.
                Examples: `deviceFamily=Switches and Hubs` (single deviceFamily requested)
                `deviceFamily=Switches and Hubs&deviceFamily=Routers` (multiple deviceFamily requested)
                .
            start_time(int): startTime query parameter. Start time from which API queries the data set related to
                the resource. It must be specified in UNIX epochtime in milliseconds. Value is
                inclusive. If `startTime` is not provided, API will default to current time minus 24
                hours. .
            end_time(int): endTime query parameter. End time to which API queries the data set related to the
                resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive. If
                `endTime` is not provided, API will default to current time. .
            message_type(str): messageType query parameter. Message type for the event. Examples:
                `messageType=Syslog` (single messageType requested)
                `messageType=Trap&messageType=Syslog` (multiple messageType requested) .
            severity(int): severity query parameter. Severity of the event between 0 and 6. This is applicable only
                for events related to network devices (other than AP) and `Wired Client` events. (Value:
                Severity: 0: Emergency: 1: Alert: 2: Critical: 3: Error: 4: Warning: 5: Notice: 6:
                Info),  Examples: `severity=0` (single severity requested) `severity=0&severity=1`
                (multiple severity requested) .
            site_id(str): siteId query parameter. The UUID of the site. (Ex. `flooruuid`) Examples:
                `?siteId=id1` (single siteId requested) `?siteId=id1&siteId=id2&siteId=id3` (multiple
                siteId requested) .
            site_hierarchy_id(str): siteHierarchyId query parameter. The full hierarchy breakdown of the site
                tree in id form starting from Global site UUID and ending with the specific site UUID.
                (Ex. `globalUuid/areaUuid/buildingUuid/floorUuid`) This field supports wildcard asterisk
                (`*`) character search support. E.g. `*uuid*, *uuid, uuid*` Examples:
                `?siteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid `(single siteHierarchyId
                requested) `?siteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid&siteHierarchyId=
                globalUuid/areaUuid2/buildingUuid2/floorUuid2` (multiple siteHierarchyId requested) .
            network_device_name(str): networkDeviceName query parameter. Network device name. This parameter
                is applicable for network device related families. This field supports wildcard (`*`)
                character-based search. Ex: `*Branch*` or `Branch*` or `*Branch` Examples:
                `networkDeviceName=Branch-3-Gateway` (single networkDeviceName requested)
                `networkDeviceName=Branch-3-Gateway&networkDeviceName=Branch-3-Switch` (multiple
                networkDeviceName requested) .
            network_device_id(str): networkDeviceId query parameter. The list of Network Device Uuids. (Ex.
                `6bef213c-19ca-4170-8375-b694e251101c`) Examples:
                `networkDeviceId=6bef213c-19ca-4170-8375-b694e251101c` (single networkDeviceId
                requested) `networkDeviceId=6bef213c-19ca-4170-8375-
                b694e251101c&networkDeviceId=32219612-819e-4b5e-a96b-
                cf22aca13dd9&networkDeviceId=2541e9a7-b80d-4955-8aa2-79b233318ba0` (multiple
                networkDeviceId with & separator) .
            ap_mac(str): apMac query parameter. MAC address of the access point. This parameter is applicable
                for `Unified AP` and `Wireless Client` events. This field supports wildcard (`*`)
                character-based search. Ex: `*50:0F*` or `50:0F*` or `*50:0F` Examples:
                `apMac=50:0F:80:0F:F7:E0` (single apMac requested)
                `apMac=50:0F:80:0F:F7:E0&apMac=18:80:90:AB:7E:A0` (multiple apMac requested) .
            client_mac(str): clientMac query parameter. MAC address of the client. This parameter is
                applicable for `Wired Client` and `Wireless Client` events. This field supports wildcard
                (`*`) character-based search. Ex: `*66:2B*` or `66:2B*` or `*66:2B` Examples:
                `clientMac=66:2B:B8:D2:01:56` (single clientMac requested)
                `clientMac=66:2B:B8:D2:01:56&clientMac=DC:A6:32:F5:5A:89` (multiple clientMac requested)
                .
            attribute(str): attribute query parameter. The list of attributes that needs to be included in
                the response. If this parameter is not provided, then basic attributes (`id`, `name`,
                `timestamp`, `details`, `messageType`, `siteHierarchyId`, `siteHierarchy`,
                `deviceFamily`, `networkDeviceId`, `networkDeviceName`, `managementIpAddress`) would be
                part of the response.  Examples: `attribute=name` (single attribute requested)
                `attribute=name&attribute=networkDeviceName` (multiple attribute requested) .
            view(str): view query parameter. The list of events views. Please refer to `EventViews` for the
                supported list  Examples: `view=network` (single view requested) `view=network&view=ap`
                (multiple view requested) .
            offset(int): offset query parameter. Specifies the starting point within all records returned by the
                API. It's one based offset. The starting value is 1. .
            limit(int): limit query parameter. Maximum number of records to return .
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
            ApiError: If the DNA Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!query-assurance-events
        """
        check_type(headers, dict)
        check_type(device_family, str, may_be_none=False)
        check_type(start_time, int)
        check_type(end_time, int)
        check_type(message_type, str)
        check_type(severity, int)
        check_type(site_id, str)
        check_type(site_hierarchy_id, str)
        check_type(network_device_name, str)
        check_type(network_device_id, str)
        check_type(ap_mac, str)
        check_type(client_mac, str)
        check_type(attribute, str)
        check_type(view, str)
        check_type(offset, int)
        check_type(limit, int)
        check_type(sort_by, str)
        check_type(order, str)
        if headers is not None:
            if "X-CALLER-ID" in headers:
                check_type(headers.get("X-CALLER-ID"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "deviceFamily": device_family,
            "startTime": start_time,
            "endTime": end_time,
            "messageType": message_type,
            "severity": severity,
            "siteId": site_id,
            "siteHierarchyId": site_hierarchy_id,
            "networkDeviceName": network_device_name,
            "networkDeviceId": network_device_id,
            "apMac": ap_mac,
            "clientMac": client_mac,
            "attribute": attribute,
            "view": view,
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

        e_url = "/dna/data/api/v1/assuranceEvents"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_bc891de5102872b3415d23b7a0b_v2_3_7_6", json_data
        )

    def count_the_number_of_events_v1(
        self,
        device_family,
        ap_mac=None,
        client_mac=None,
        end_time=None,
        message_type=None,
        network_device_id=None,
        network_device_name=None,
        severity=None,
        site_hierarchy_id=None,
        site_id=None,
        start_time=None,
        headers=None,
        **request_parameters
    ):
        """API to fetch the count of assurance events that match the filter criteria. Please refer to the 'API Support
        Documentation' section to understand which fields are supported. For detailed information about the
        usage of the API, please refer to the Open API specification document https://github.com/cisco-en-
        programmability/catalyst-center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-
        AssuranceEvents-1.0.0-resolved.yaml .

        Args:
            device_family(str): deviceFamily query parameter. Device family. Please note that multiple
                families across network device type and client type is not allowed. For example,
                choosing `Routers` along with `Wireless Client` or `Unified AP` is not supported.
                Examples: `deviceFamily=Switches and Hubs` (single deviceFamily requested)
                `deviceFamily=Switches and Hubs&deviceFamily=Routers` (multiple deviceFamily requested)
                .
            start_time(str): startTime query parameter. Start time from which API queries the data set
                related to the resource. It must be specified in UNIX epochtime in milliseconds. Value
                is inclusive. If `startTime` is not provided, API will default to current time minus 24
                hours. .
            end_time(str): endTime query parameter. End time to which API queries the data set related to the
                resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive. If
                `endTime` is not provided, API will default to current time. .
            message_type(str): messageType query parameter. Message type for the event. Examples:
                `messageType=Syslog` (single messageType requested)
                `messageType=Trap&messageType=Syslog` (multiple messageType requested) .
            severity(str): severity query parameter. Severity of the event between 0 and 6. This is
                applicable only for events related to network devices (other than AP) and `Wired Client`
                events. (Value: Severity: 0: Emergency: 1: Alert: 2: Critical: 3: Error: 4: Warning: 5:
                Notice: 6: Info),  Examples: `severity=0` (single severity requested)
                `severity=0&severity=1` (multiple severity requested) .
            site_id(str): siteId query parameter. The UUID of the site. (Ex. `flooruuid`) Examples:
                `?siteId=id1` (single siteId requested) `?siteId=id1&siteId=id2&siteId=id3` (multiple
                siteId requested) .
            site_hierarchy_id(str): siteHierarchyId query parameter. The full hierarchy breakdown of the site
                tree in id form starting from Global site UUID and ending with the specific site UUID.
                (Ex. `globalUuid/areaUuid/buildingUuid/floorUuid`) This field supports wildcard asterisk
                (`*`) character search support. E.g. `*uuid*, *uuid, uuid*` Examples:
                `?siteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid `(single siteHierarchyId
                requested) `?siteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid&siteHierarchyId=
                globalUuid/areaUuid2/buildingUuid2/floorUuid2` (multiple siteHierarchyId requested) .
            network_device_name(str): networkDeviceName query parameter. Network device name. This parameter
                is applicable for network device related families. This field supports wildcard (`*`)
                character-based search. Ex: `*Branch*` or `Branch*` or `*Branch` Examples:
                `networkDeviceName=Branch-3-Gateway` (single networkDeviceName requested)
                `networkDeviceName=Branch-3-Gateway&networkDeviceName=Branch-3-Switch` (multiple
                networkDeviceName requested) .
            network_device_id(str): networkDeviceId query parameter. The list of Network Device Uuids. (Ex.
                `6bef213c-19ca-4170-8375-b694e251101c`) Examples:
                `networkDeviceId=6bef213c-19ca-4170-8375-b694e251101c` (single networkDeviceId
                requested) `networkDeviceId=6bef213c-19ca-4170-8375-
                b694e251101c&networkDeviceId=32219612-819e-4b5e-a96b-
                cf22aca13dd9&networkDeviceId=2541e9a7-b80d-4955-8aa2-79b233318ba0` (multiple
                networkDeviceId requested) .
            ap_mac(str): apMac query parameter. MAC address of the access point. This parameter is applicable
                for `Unified AP` and `Wireless Client` events. This field supports wildcard (`*`)
                character-based search. Ex: `*50:0F*` or `50:0F*` or `*50:0F` Examples:
                `apMac=50:0F:80:0F:F7:E0` (single apMac requested)
                `apMac=50:0F:80:0F:F7:E0&apMac=18:80:90:AB:7E:A0` (multiple apMac requested) .
            client_mac(str): clientMac query parameter. MAC address of the client. This parameter is
                applicable for `Wired Client` and `Wireless Client` events. This field supports wildcard
                (`*`) character-based search. Ex: `*66:2B*` or `66:2B*` or `*66:2B` Examples:
                `clientMac=66:2B:B8:D2:01:56` (single clientMac requested)
                `clientMac=66:2B:B8:D2:01:56&clientMac=DC:A6:32:F5:5A:89` (multiple clientMac requested)
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
            ApiError: If the DNA Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!count-the-number-of-events
        """
        check_type(headers, dict)
        check_type(device_family, str, may_be_none=False)
        check_type(start_time, str)
        check_type(end_time, str)
        check_type(message_type, str)
        check_type(severity, str)
        check_type(site_id, str)
        check_type(site_hierarchy_id, str)
        check_type(network_device_name, str)
        check_type(network_device_id, str)
        check_type(ap_mac, str)
        check_type(client_mac, str)
        if headers is not None:
            if "X-CALLER-ID" in headers:
                check_type(headers.get("X-CALLER-ID"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "deviceFamily": device_family,
            "startTime": start_time,
            "endTime": end_time,
            "messageType": message_type,
            "severity": severity,
            "siteId": site_id,
            "siteHierarchyId": site_hierarchy_id,
            "networkDeviceName": network_device_name,
            "networkDeviceId": network_device_id,
            "apMac": ap_mac,
            "clientMac": client_mac,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/assuranceEvents/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_abf597583520eb0a7a0b24e5c7f69_v2_3_7_6", json_data
        )

    def query_assurance_events_with_filters_v1(
        self,
        attributes=None,
        deviceFamily=None,
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
        """Returns the list of events discovered by DNA Center, determined by the complex filters. Please refer to the
        'API Support Documentation' section to understand which fields are supported. For detailed information
        about the usage of the API, please refer to the Open API specification document
        https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-AssuranceEvents-1.0.0-resolved.yaml .

        Args:
            attributes(list): Devices's Attributes (list of strings).
            deviceFamily(list): Devices's Device Family (list of strings).
            endTime(integer): Devices's End Time.
            filters(list): Devices's filters (list of objects).
            page(object): Devices's page.
            startTime(integer): Devices's Start Time.
            views(list): Devices's Views (list of strings).
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
            https://developer.cisco.com/docs/dna-center/#!query-assurance-events-with-filters
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
            "deviceFamily": deviceFamily,
            "startTime": startTime,
            "endTime": endTime,
            "attributes": attributes,
            "views": views,
            "filters": filters,
            "page": page,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_ef94c2c20ba15fd38e129ac75067de1e_v2_3_7_6"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/assuranceEvents/query"
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
            "bpm_ef94c2c20ba15fd38e129ac75067de1e_v2_3_7_6", json_data
        )

    def count_the_number_of_events_with_filters_v1(
        self,
        deviceFamily=None,
        endTime=None,
        filters=None,
        startTime=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """API to fetch the count of assurance events for the given complex query. Please refer to the 'API Support
        Documentation' section to understand which fields are supported. For detailed information about the
        usage of the API, please refer to the Open API specification document https://github.com/cisco-en-
        programmability/catalyst-center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-
        AssuranceEvents-1.0.0-resolved.yaml .

        Args:
            deviceFamily(list): Devices's Device Family (list of strings).
            endTime(integer): Devices's End Time.
            filters(list): Devices's filters (list of objects).
            startTime(integer): Devices's Start Time.
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
            https://developer.cisco.com/docs/dna-center/#!count-the-number-of-events-with-filters
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
            "deviceFamily": deviceFamily,
            "startTime": startTime,
            "endTime": endTime,
            "filters": filters,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_a91eed12dfc85dbdaacab22e6e9f04a5_v2_3_7_6"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/assuranceEvents/query/count"
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
            "bpm_a91eed12dfc85dbdaacab22e6e9f04a5_v2_3_7_6", json_data
        )

    def get_details_of_a_single_assurance_event_v1(
        self, id, attribute=None, view=None, headers=None, **request_parameters
    ):
        """API to fetch the details of an assurance event using event `id`. For detailed information about the usage of the
        API, please refer to the Open API specification document https://github.com/cisco-en-
        programmability/catalyst-center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-
        AssuranceEvents-1.0.0-resolved.yaml .

        Args:
            id(str): id path parameter. Unique identifier for the event .
            attribute(str): attribute query parameter. The list of attributes that needs to be included in
                the response. If this parameter is not provided, then basic attributes (`id`, `name`,
                `timestamp`, `details`, `messageType`, `siteHierarchyId`, `siteHierarchy`,
                `deviceFamily`, `networkDeviceId`, `networkDeviceName`, `managementIpAddress`) would be
                part of the response.  Examples: `attribute=name` (single attribute requested)
                `attribute=name&attribute=networkDeviceName` (multiple attribute requested) .
            view(str): view query parameter. The list of events views. Please refer to `EventViews` for the
                supported list  Examples: `view=network` (single view requested) `view=network&view=ap`
                (multiple view requested) .
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
            https://developer.cisco.com/docs/dna-center/#!get-details-of-a-single-assurance-event
        """
        check_type(headers, dict)
        check_type(attribute, str)
        check_type(view, str)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-CALLER-ID" in headers:
                check_type(headers.get("X-CALLER-ID"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
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

        e_url = "/dna/data/api/v1/assuranceEvents/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a36092e78528b9bd8730c93b5412d_v2_3_7_6", json_data
        )

    def get_list_of_child_events_for_the_given_wireless_client_event_v1(
        self, id, headers=None, **request_parameters
    ):
        """Wireless client event could have child events and this API can be used to fetch the same using parent event `id`
        as the input. For detailed information about the usage of the API, please refer to the Open API
        specification document https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-AssuranceEvents-1.0.0-resolved.yaml .

        Args:
            id(str): id path parameter. Unique identifier for the event .
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
            https://developer.cisco.com/docs/dna-center/#!get-list-of-child-events-for-the-given-wireless-client-event
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

        e_url = "/dna/data/api/v1/assuranceEvents/{id}/childEvents"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_d3cf1ace30895351b5b8c3f7919b972e_v2_3_7_6", json_data
        )

    def gets_interfaces_along_with_statistics_data_from_all_network_devices_v1(
        self,
        attribute=None,
        end_time=None,
        interface_id=None,
        interface_name=None,
        limit=None,
        network_device_id=None,
        network_device_ip_address=None,
        network_device_mac_address=None,
        offset=None,
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
        """Retrieves the list of the interfaces from all network devices based on the provided query parameters. The latest
        interfaces data in the specified start and end time range will be returned. When there is no start and
        end time specified returns the latest available data. The elements are grouped and sorted by deviceUuid
        first, and are then sorted by the given sort field, or by the default value: name.   The supported
        sorting options are: name, adminStatus, description, duplexConfig,
        duplexOper,interfaceIfIndex,interfaceType, macAddress,mediaType, operStatus,portChannelId, portMode,
        portType,speed, vlanId. For detailed information about the usage of the API, please refer to the Open
        API specification document https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-interfaces-1.0.2-resolved.yaml .

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
            site_id(str): siteId query parameter. The UUID of the site. (Ex. `flooruuid`) Examples:
                `?siteId=id1` (single id requested) `?siteId=id1&siteId=id2&siteId=id3` (multiple ids
                requested) .
            view(str): view query parameter. The specific summary view being requested. This is an optional
                parameter which can be passed to get one or more of the specific view associated fields.
                The default view is ``configuration``. ### Response data proviced by each view:   1.
                **configuration** [id,adminStatus,description,duplexConfig,duplexOper,interfaceIfIndex,i
                nterfaceType,ipv4Address,ipv6AddressList,isL3Interface,isWan,macAddress,mediaType,name,o
                perStatus, portChannelId,portMode, portType,speed,timestamp,vlanId,networkDeviceId,netwo
                rkDeviceIpAddress,networkDeviceMacAddress,siteName,siteHierarchy,siteHierarchyId]   2.
                **statistics** [id,name,rxDiscards,rxError,rxRate,rxUtilization,txDiscards,txError,txRat
                e,txUtilization,networkDeviceId,networkDeviceIpAddress,networkDeviceMacAddress,siteName,
                siteHierarchy,siteHierarchyId]   3. **stackPort** [id,name,peerStackMember,peerStackPort
                ,stackPortType,networkDeviceId,networkDeviceIpAddress,networkDeviceMacAddress,siteName,s
                iteHierarchy,siteHierarchyId]   The default view is configuration, If need to access an
                additional view, simply include the view name in the query parameter. Examples:
                view=configuration (single view requested) view=configuration&view=statistic&stackPort
                (multiple views requested) .
            attribute(str): attribute query parameter. The following list of attributes can be provided in
                the attribute field [id,adminStatus, description,duplexConfig,duplexOper,interfaceIfInde
                x,interfaceType,ipv4Address,ipv6AddressList,isL3Interface,isWan,macAddress,mediaType,nam
                e,operStatus,peerStackMember,peerStackPort, portChannelId,portMode, portType,rxDiscards,
                rxError,rxRate,rxUtilization,speed,stackPortType,timestamp,txDiscards,txError,txRate,txU
                tilization,vlanId,networkDeviceId,networkDeviceIpAddress,networkDeviceMacAddress,siteNam
                e,siteHierarchy,siteHierarchyId] If length of attribute list is too long, please use
                'views' param instead. Examples: attributes=name (single attribute requested)
                attributes=name,description,duplexOper (multiple attributes with comma separator) .
            network_device_id(str): networkDeviceId query parameter. The list of Network Device Uuids. (Ex.
                `6bef213c-19ca-4170-8375-b694e251101c`) Examples:
                `networkDeviceId=6bef213c-19ca-4170-8375-b694e251101c` (single networkDeviceId
                requested) `networkDeviceId=6bef213c-19ca-4170-8375-
                b694e251101c&networkDeviceId=32219612-819e-4b5e-a96b-
                cf22aca13dd9&networkDeviceId=2541e9a7-b80d-4955-8aa2-79b233318ba0` (multiple
                networkDeviceIds with & separator) .
            network_device_ip_address(str): networkDeviceIpAddress query parameter. The list of Network
                Device management IP Address. (Ex. `121.1.1.10`) This field supports wildcard (`*`)
                character-based search.  Ex: `*1.1*` or `1.1*` or `*1.1` Examples:
                `networkDeviceIpAddress=121.1.1.10` `networkDeviceIpAddress=121.1.1.10&networkDeviceIpAd
                dress=172.20.1.10&networkDeviceIpAddress=10.10.20.10` (multiple networkDevice IP Address
                with & separator) .
            network_device_mac_address(str): networkDeviceMacAddress query parameter. The list of Network
                Device MAC Address. (Ex. `64:f6:9d:07:9a:00`) This field supports wildcard (`*`)
                character-based search.  Ex: `*AB:AB:AB*` or `AB:AB:AB*` or `*AB:AB:AB` Examples:
                `networkDeviceMacAddress=64:f6:9d:07:9a:00`
                `networkDeviceMacAddress=64:f6:9d:07:9a:00&networkDeviceMacAddress=70:56:9d:07:ac:77`
                (multiple networkDevice MAC addresses with & separator) .
            interface_id(str): interfaceId query parameter. The list of Interface Uuids. (Ex.
                `6bef213c-19ca-4170-8375-b694e251101c`) Examples:
                `interfaceId=6bef213c-19ca-4170-8375-b694e251101c` (single interface uuid ) `interfaceId
                =6bef213c-19ca-4170-8375-b694e251101c&32219612-819e-4b5e-a96b-cf22aca13dd9&2541e9a7-
                b80d-4955-8aa2-79b233318ba0` (multiple Interface uuid with & separator) .
            interface_name(str): interfaceName query parameter. The list of Interface name (Ex.
                `GigabitEthernet1/0/1`) This field supports wildcard (`*`) character-based search.  Ex:
                `*1/0/1*` or `1/0/1*` or `*1/0/1` Examples: `interfaceNames=GigabitEthernet1/0/1`
                (single interface name)
                `interfaceNames=GigabitEthernet1/0/1&GigabitEthernet2/0/1&GigabitEthernet3/0/1`
                (multiple interface names with & separator) .
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
            https://developer.cisco.com/docs/dna-center/#!gets-interfaces-along-with-statistics-data-from-all-network-devices
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
        check_type(site_id, str)
        check_type(view, str)
        check_type(attribute, str)
        check_type(network_device_id, str)
        check_type(network_device_ip_address, str)
        check_type(network_device_mac_address, str)
        check_type(interface_id, str)
        check_type(interface_name, str)
        if headers is not None:
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
            "siteId": site_id,
            "view": view,
            "attribute": attribute,
            "networkDeviceId": network_device_id,
            "networkDeviceIpAddress": network_device_ip_address,
            "networkDeviceMacAddress": network_device_mac_address,
            "interfaceId": interface_id,
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

        e_url = "/dna/data/api/v1/interfaces"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_fc7a61a854f2b2015d3f1c059ce9_v2_3_7_6", json_data
        )

    def gets_the_total_network_device_interface_counts_v1(
        self,
        end_time=None,
        interface_id=None,
        interface_name=None,
        network_device_id=None,
        network_device_ip_address=None,
        network_device_mac_address=None,
        site_hierarchy=None,
        site_hierarchy_id=None,
        site_id=None,
        start_time=None,
        headers=None,
        **request_parameters
    ):
        """Gets the total Network device interface counts. For detailed information about the usage of the API, please
        refer to the Open API specification document https://github.com/cisco-en-programmability/catalyst-
        center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-interfaces-1.0.2-resolved.yaml .

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
            site_id(str): siteId query parameter. The UUID of the site. (Ex. `flooruuid`) Examples:
                `?siteId=id1` (single id requested) `?siteId=id1&siteId=id2&siteId=id3` (multiple ids
                requested) .
            network_device_id(str): networkDeviceId query parameter. The list of Network Device Uuids. (Ex.
                `6bef213c-19ca-4170-8375-b694e251101c`) Examples:
                `networkDeviceId=6bef213c-19ca-4170-8375-b694e251101c` (single networkDeviceId
                requested) `networkDeviceId=6bef213c-19ca-4170-8375-
                b694e251101c&networkDeviceId=32219612-819e-4b5e-a96b-
                cf22aca13dd9&networkDeviceId=2541e9a7-b80d-4955-8aa2-79b233318ba0` (multiple
                networkDeviceIds with & separator) .
            network_device_ip_address(str): networkDeviceIpAddress query parameter. The list of Network
                Device management IP Address. (Ex. `121.1.1.10`) This field supports wildcard (`*`)
                character-based search.  Ex: `*1.1*` or `1.1*` or `*1.1` Examples:
                `networkDeviceIpAddress=121.1.1.10` `networkDeviceIpAddress=121.1.1.10&networkDeviceIpAd
                dress=172.20.1.10&networkDeviceIpAddress=10.10.20.10` (multiple networkDevice IP Address
                with & separator) .
            network_device_mac_address(str): networkDeviceMacAddress query parameter. The list of Network
                Device MAC Address. (Ex. `64:f6:9d:07:9a:00`) This field supports wildcard (`*`)
                character-based search.  Ex: `*AB:AB:AB*` or `AB:AB:AB*` or `*AB:AB:AB` Examples:
                `networkDeviceMacAddress=64:f6:9d:07:9a:00`
                `networkDeviceMacAddress=64:f6:9d:07:9a:00&networkDeviceMacAddress=70:56:9d:07:ac:77`
                (multiple networkDevice MAC addresses with & separator) .
            interface_id(str): interfaceId query parameter. The list of Interface Uuids. (Ex.
                `6bef213c-19ca-4170-8375-b694e251101c`) Examples:
                `interfaceId=6bef213c-19ca-4170-8375-b694e251101c` (single interface uuid ) `interfaceId
                =6bef213c-19ca-4170-8375-b694e251101c&32219612-819e-4b5e-a96b-cf22aca13dd9&2541e9a7-
                b80d-4955-8aa2-79b233318ba0` (multiple Interface uuid with & separator) .
            interface_name(str): interfaceName query parameter. The list of Interface name (Ex.
                `GigabitEthernet1/0/1`) This field supports wildcard (`*`) character-based search.  Ex:
                `*1/0/1*` or `1/0/1*` or `*1/0/1` Examples: `interfaceNames=GigabitEthernet1/0/1`
                (single interface name)
                `interfaceNames=GigabitEthernet1/0/1&GigabitEthernet2/0/1&GigabitEthernet3/0/1`
                (multiple interface names with & separator) .
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
            https://developer.cisco.com/docs/dna-center/#!gets-the-total-network-device-interface-counts-in-the-specified-time-range-when-there-is-no-start-and-end-time-specified-returns-the-latest-interfaces-total-count
        """
        check_type(headers, dict)
        check_type(start_time, int)
        check_type(end_time, int)
        check_type(site_hierarchy, str)
        check_type(site_hierarchy_id, str)
        check_type(site_id, str)
        check_type(network_device_id, str)
        check_type(network_device_ip_address, str)
        check_type(network_device_mac_address, str)
        check_type(interface_id, str)
        check_type(interface_name, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "startTime": start_time,
            "endTime": end_time,
            "siteHierarchy": site_hierarchy,
            "siteHierarchyId": site_hierarchy_id,
            "siteId": site_id,
            "networkDeviceId": network_device_id,
            "networkDeviceIpAddress": network_device_ip_address,
            "networkDeviceMacAddress": network_device_mac_address,
            "interfaceId": interface_id,
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

        e_url = "/dna/data/api/v1/interfaces/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory("bpm_0f4b503bbce76ebb802f0ad7_v2_3_7_6", json_data)

    def gets_the_list_of_interfaces_across_the_network_devices_based_on_the_provided_complex_filters_and_aggregation_functions_v1(
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
        """Gets the list of interfaces across the Network Devices based on the provided complex filters and aggregation
        functions The elements are grouped and sorted by deviceUuid first, and are then sorted by the given sort
        field, or by the default value: name. The supported sorting options are: name, adminStatus, description,
        duplexConfig, duplexOper, interfaceIfIndex,interfaceType, macAddress,mediaType, operStatus,
        portChannelId, portMode, portType,speed, vlanId. For detailed information about the usage of the API,
        please refer to the Open API specification document https://github.com/cisco-en-
        programmability/catalyst-center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-
        interfaces-1.0.2-resolved.yaml .

        Args:
            aggregateAttributes(list): Devices's aggregateAttributes (list of objects).
            attributes(list): Devices's Attributes (list of strings).
            endTime(integer): Devices's End Time.
            filters(list): Devices's filters (list of objects).
            page(object): Devices's page.
            startTime(integer): Devices's Start Time.
            views(list): Devices's Views (list of strings).
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
            https://developer.cisco.com/docs/dna-center/#!gets-the-list-of-interfaces-across-the-network-devices-based-on-the-provided-complex-filters-and-aggregation-functions
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
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
                "jsd_f667322836d5527482ad2100bec7feb4_v2_3_7_6"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/interfaces/query"
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
            "bpm_f667322836d5527482ad2100bec7feb4_v2_3_7_6", json_data
        )

    def the_total_interfaces_count_across_the_network_devices_v1(
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
        """Gets the total number of interfaces across the Network devices based on the provided complex filters and
        aggregation functions. For detailed information about the usage of the API, please refer to the Open API
        specification document https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-interfaces-1.0.2-resolved.yaml .

        Args:
            aggregateAttributes(list): Devices's aggregateAttributes (list of objects).
            attributes(list): Devices's Attributes (list of strings).
            endTime(integer): Devices's End Time.
            filters(list): Devices's filters (list of objects).
            page(object): Devices's page.
            startTime(integer): Devices's Start Time.
            views(list): Devices's Views (list of strings).
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
            https://developer.cisco.com/docs/dna-center/#!the-total-interfaces-count-across-the-network-devices
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
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
                "jsd_b0b146a144a65aa296b8b939c2926158_v2_3_7_6"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/interfaces/query/count"
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
            "bpm_b0b146a144a65aa296b8b939c2926158_v2_3_7_6", json_data
        )

    def get_the_interface_data_for_the_given_interface_idinstance_uuid_along_with_the_statistics_data_v1(
        self,
        id,
        attribute=None,
        end_time=None,
        start_time=None,
        view=None,
        headers=None,
        **request_parameters
    ):
        """Returns the interface data for the given interface instance Uuid along with the statistics data. The latest
        interface data in the specified start and end time range will be returned. When there is no start and
        end time specified returns the latest available data for the given interface Id. For detailed
        information about the usage of the API, please refer to the Open API specification document
        https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-interfaces-1.0.2-resolved.yaml .

        Args:
            id(str): id path parameter. The interface Uuid .
            start_time(int): startTime query parameter. Start time from which API queries the data set related to
                the resource. It must be specified in UNIX epochtime in milliseconds. Value is
                inclusive. If `startTime` is not provided, API will default to current time. .
            end_time(int): endTime query parameter. End time to which API queries the data set related to the
                resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive. .
            view(str): view query parameter. Interface data model views .
            attribute(str): attribute query parameter. The following list of attributes can be provided in
                the attribute field [id,adminStatus, description,duplexConfig,duplexOper,interfaceIfInde
                x,interfaceType,ipv4Address,ipv6AddressList,isL3Interface,isWan,macAddress,mediaType,nam
                e,operStatus,peerStackMember,peerStackPort, portChannelId,portMode, portType,rxDiscards,
                rxError,rxRate,rxUtilization,speed,stackPortType,timestamp,txDiscards,txError,txRate,txU
                tilization,vlanId,networkDeviceId,networkDeviceIpAddress,networkDeviceMacAddress,siteNam
                e,siteHierarchy,siteHierarchyId] If length of attribute list is too long, please use
                'views' param instead. Examples: attributes=name (single attribute requested)
                attributes=name,description,duplexOper (multiple attributes with comma separator) .
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
            https://developer.cisco.com/docs/dna-center/#!get-the-interface-data-for-the-given-interface-idinstance-uuid-along-with-the-statistics-data
        """
        check_type(headers, dict)
        check_type(start_time, int)
        check_type(end_time, int)
        check_type(view, str)
        check_type(attribute, str)
        check_type(id, str, may_be_none=False)
        if headers is not None:
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

        e_url = "/dna/data/api/v1/interfaces/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_adcdf890505770af113b18b30c1b5f_v2_3_7_6", json_data
        )

    def gets_the_network_device_details_based_on_the_provided_query_parameters_v1(
        self,
        attribute=None,
        end_time=None,
        family=None,
        health_score=None,
        id=None,
        limit=None,
        mac_address=None,
        maintenance_mode=None,
        management_ip_address=None,
        offset=None,
        order=None,
        role=None,
        serial_number=None,
        site_hierarchy=None,
        site_hierarchy_id=None,
        site_id=None,
        software_version=None,
        sort_by=None,
        start_time=None,
        type=None,
        view=None,
        headers=None,
        **request_parameters
    ):
        """Gets the Network Device details based on the provided query parameters.  When there is no start and end time
        specified returns the latest device details. For detailed information about the usage of the API, please
        refer to the Open API specification document https://github.com/cisco-en-programmability/catalyst-
        center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-AssuranceNetworkDevices-1.0.2-resolved.yaml .

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
                supports wildcard asterisk (*) character search support. E.g. */San*, */San, /San*
                Examples: `?siteHierarchy=Global/AreaName/BuildingName/FloorName` (single siteHierarchy
                requested) `?siteHierarchy=Global/AreaName/BuildingName/FloorName&siteHierarchy=Global/A
                reaName2/BuildingName2/FloorName2` (multiple siteHierarchies requested) .
            site_hierarchy_id(str): siteHierarchyId query parameter. The full hierarchy breakdown of the site
                tree in id form starting from Global site UUID and ending with the specific site UUID.
                (Ex. `globalUuid/areaUuid/buildingUuid/floorUuid`) This field supports wildcard asterisk
                (*) character search support. E.g. `*uuid*, *uuid, uuid* Examples:
                `?siteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid `(single siteHierarchyId
                requested) `?siteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid&siteHierarchyId=
                globalUuid/areaUuid2/buildingUuid2/floorUuid2` (multiple siteHierarchyIds requested) .
            site_id(str): siteId query parameter. The UUID of the site. (Ex. `flooruuid`) This field supports
                wildcard asterisk (*) character search support. E.g.*flooruuid*, *flooruuid, flooruuid*
                Examples: `?siteId=id1` (single id requested) `?siteId=id1&siteId=id2&siteId=id3`
                (multiple ids requested) .
            id(str): id query parameter. The list of entity Uuids.
                (Ex."6bef213c-19ca-4170-8375-b694e251101c") Examples:
                id=6bef213c-19ca-4170-8375-b694e251101c (single entity uuid requested) id=6bef213c-19ca-
                4170-8375-b694e251101c&id=32219612-819e-4b5e-a96b-cf22aca13dd9&id=2541e9a7-b80d-4955-
                8aa2-79b233318ba0 (multiple entity uuid with '&' separator) .
            management_ip_address(str): managementIpAddress query parameter. The list of entity management IP
                Address. It can be either Ipv4 or Ipv6 address or combination of both(Ex. "121.1.1.10")
                This field supports wildcard (`*`) character-based search.  Ex: `*1.1*` or `1.1*` or
                `*1.1` Examples: managementIpAddresses=121.1.1.10 managementIpAddresses=121.1.1.10&manag
                ementIpAddresses=172.20.1.10&managementIpAddresses=200:10&=managementIpAddresses172.20.3
                .4 (multiple entity IP Address with & separator) .
            mac_address(str): macAddress query parameter. The macAddress of the network device or client This
                field supports wildcard (`*`) character-based search.  Ex: `*AB:AB:AB*` or `AB:AB:AB*`
                or `*AB:AB:AB` Examples: `macAddress=AB:AB:AB:CD:CD:CD` (single macAddress requested)
                `macAddress=AB:AB:AB:CD:CD:DC&macAddress=AB:AB:AB:CD:CD:FE` (multiple macAddress
                requested) .
            family(str): family query parameter. The list of network device family names
                Examples:family=Switches and Hubs (single network device family name )family=Switches
                and Hubs&family=Router&family=Wireless Controller (multiple Network device family names
                with & separator). This field is not case sensitive. .
            type(str): type query parameter. The list of network device type This field supports wildcard
                (`*`) character-based search. Ex: `*9407R*` or `*9407R` or `9407R*` Examples:
                type=SwitchesCisco DNA 9407R Switch (single network device types ) type=Cisco
                DNA 38xx stack-able ethernet switch&type=Cisco 3945 Integrated Services Router G2
                (multiple Network device types with & separator) .
            role(str): role query parameter. The list of network device role. Examples:role=CORE,
                role=CORE&role=ACCESS&role=ROUTER (multiple Network device roles with & separator). This
                field is not case sensitive. .
            serial_number(str): serialNumber query parameter. The list of network device serial numbers. This
                field supports wildcard (`*`) character-based search.  Ex: `*MS1SV*` or `MS1SV*` or
                `*MS1SV` Examples: serialNumber=9FUFMS1SVAX
                serialNumber=9FUFMS1SVAX&FCW2333Q0BY&FJC240617JX(multiple Network device serial number
                with & separator) .
            maintenance_mode(bool): maintenanceMode query parameter. The device maintenanceMode status true or false
                .
            software_version(str): softwareVersion query parameter. The list of network device software
                version This field supports wildcard (`*`) character-based search. Ex: `*17.8*` or
                `*17.8` or `17.8*` Examples: softwareVersion=2.3.4.0 (single network device software
                version ) softwareVersion=17.9.3.23&softwareVersion=17.7.1.2&softwareVersion=*.17.7
                (multiple Network device software versions with & separator) .
            health_score(str): healthScore query parameter. The list of entity health score categories
                Examples: healthScore=good, healthScore=good&healthScore=fair (multiple entity
                healthscore values with & separator). This field is not case sensitive. .
            view(str): view query parameter. The List of Network Device model views. Please refer to
                ```NetworkDeviceView``` for the supported list .
            attribute(str): attribute query parameter. The List of Network Device model attributes. This is
                helps to specify the interested fields in the request. .
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
            https://developer.cisco.com/docs/dna-center/#!gets-the-network-device-details-based-on-the-provided-query-parameters
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
        check_type(site_id, str)
        check_type(id, str)
        check_type(management_ip_address, str)
        check_type(mac_address, str)
        check_type(family, str)
        check_type(type, str)
        check_type(role, str)
        check_type(serial_number, str)
        check_type(maintenance_mode, bool)
        check_type(software_version, str)
        check_type(health_score, str)
        check_type(view, str)
        check_type(attribute, str)
        if headers is not None:
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
            "siteId": site_id,
            "id": id,
            "managementIpAddress": management_ip_address,
            "macAddress": mac_address,
            "family": family,
            "type": type,
            "role": role,
            "serialNumber": serial_number,
            "maintenanceMode": maintenance_mode,
            "softwareVersion": software_version,
            "healthScore": health_score,
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

        e_url = "/dna/data/api/v1/networkDevices"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c7314fc7e15dab859eb66f45b1e95a_v2_3_7_6", json_data
        )

    def gets_the_total_network_device_counts_based_on_the_provided_query_parameters_v1(
        self,
        attribute=None,
        end_time=None,
        family=None,
        health_score=None,
        id=None,
        mac_address=None,
        maintenance_mode=None,
        management_ip_address=None,
        role=None,
        serial_number=None,
        site_hierarchy=None,
        site_hierarchy_id=None,
        site_id=None,
        software_version=None,
        start_time=None,
        type=None,
        view=None,
        headers=None,
        **request_parameters
    ):
        """Gets the total Network device counts. When there is no start and end time specified returns the latest
        interfaces total count. For detailed information about the usage of the API, please refer to the Open
        API specification document https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-AssuranceNetworkDevices-1.0.2-resolved.yaml .

        Args:
            start_time(int): startTime query parameter. Start time from which API queries the data set related to
                the resource. It must be specified in UNIX epochtime in milliseconds. Value is
                inclusive. If `startTime` is not provided, API will default to current time. .
            end_time(int): endTime query parameter. End time to which API queries the data set related to the
                resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive. .
            id(str): id query parameter. The list of entity Uuids.
                (Ex."6bef213c-19ca-4170-8375-b694e251101c") Examples:
                id=6bef213c-19ca-4170-8375-b694e251101c (single entity uuid requested) id=6bef213c-19ca-
                4170-8375-b694e251101c&id=32219612-819e-4b5e-a96b-cf22aca13dd9&id=2541e9a7-b80d-4955-
                8aa2-79b233318ba0 (multiple entity uuid with '&' separator) .
            site_hierarchy(str): siteHierarchy query parameter. The full hierarchical breakdown of the site
                tree starting from Global site name and ending with the specific site name. The Root
                site is named "Global" (Ex. `Global/AreaName/BuildingName/FloorName`) This field
                supports wildcard asterisk (*) character search support. E.g. */San*, */San, /San*
                Examples: `?siteHierarchy=Global/AreaName/BuildingName/FloorName` (single siteHierarchy
                requested) `?siteHierarchy=Global/AreaName/BuildingName/FloorName&siteHierarchy=Global/A
                reaName2/BuildingName2/FloorName2` (multiple siteHierarchies requested) .
            site_hierarchy_id(str): siteHierarchyId query parameter. The full hierarchy breakdown of the site
                tree in id form starting from Global site UUID and ending with the specific site UUID.
                (Ex. `globalUuid/areaUuid/buildingUuid/floorUuid`) This field supports wildcard asterisk
                (*) character search support. E.g. `*uuid*, *uuid, uuid* Examples:
                `?siteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid `(single siteHierarchyId
                requested) `?siteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid&siteHierarchyId=
                globalUuid/areaUuid2/buildingUuid2/floorUuid2` (multiple siteHierarchyIds requested) .
            site_id(str): siteId query parameter. The UUID of the site. (Ex. `flooruuid`) This field supports
                wildcard asterisk (*) character search support. E.g.*flooruuid*, *flooruuid, flooruuid*
                Examples: `?siteId=id1` (single id requested) `?siteId=id1&siteId=id2&siteId=id3`
                (multiple ids requested) .
            management_ip_address(str): managementIpAddress query parameter. The list of entity management IP
                Address. It can be either Ipv4 or Ipv6 address or combination of both(Ex. "121.1.1.10")
                This field supports wildcard (`*`) character-based search.  Ex: `*1.1*` or `1.1*` or
                `*1.1` Examples: managementIpAddresses=121.1.1.10 managementIpAddresses=121.1.1.10&manag
                ementIpAddresses=172.20.1.10&managementIpAddresses=200:10&=managementIpAddresses172.20.3
                .4 (multiple entity IP Address with & separator) .
            mac_address(str): macAddress query parameter. The macAddress of the network device or client This
                field supports wildcard (`*`) character-based search.  Ex: `*AB:AB:AB*` or `AB:AB:AB*`
                or `*AB:AB:AB` Examples: `macAddress=AB:AB:AB:CD:CD:CD` (single macAddress requested)
                `macAddress=AB:AB:AB:CD:CD:DC&macAddress=AB:AB:AB:CD:CD:FE` (multiple macAddress
                requested) .
            family(str): family query parameter. The list of network device family names
                Examples:family=Switches and Hubs (single network device family name )family=Switches
                and Hubs&family=Router&family=Wireless Controller (multiple Network device family names
                with & separator). This field is not case sensitive. .
            type(str): type query parameter. The list of network device type This field supports wildcard
                (`*`) character-based search. Ex: `*9407R*` or `*9407R` or
                `9407R*`Examples:type=SwitchesCisco DNA 9407R Switch (single network device types
                )type=Cisco DNA 38xx stack-able ethernet switch&type=Cisco 3945 Integrated Services
                Router G2 (multiple Network device types with & separator) .
            role(str): role query parameter. The list of network device role. Examples:role=CORE,
                role=CORE&role=ACCESS&role=ROUTER (multiple Network device roles with & separator). This
                field is not case sensitive. .
            serial_number(str): serialNumber query parameter. The list of network device serial numbers. This
                field supports wildcard (`*`) character-based search.  Ex: `*MS1SV*` or `MS1SV*` or
                `*MS1SV` Examples: serialNumber=9FUFMS1SVAX
                serialNumber=9FUFMS1SVAX&FCW2333Q0BY&FJC240617JX(multiple Network device serial number
                with & separator) .
            maintenance_mode(bool): maintenanceMode query parameter. The device maintenanceMode status true or false
                .
            software_version(str): softwareVersion query parameter. The list of network device software
                version This field supports wildcard (`*`) character-based search. Ex: `*17.8*` or
                `*17.8` or `17.8*` Examples: softwareVersion=2.3.4.0 (single network device software
                version ) softwareVersion=17.9.3.23&softwareVersion=17.7.1.2&softwareVersion=*.17.7
                (multiple Network device software versions with & separator) .
            health_score(str): healthScore query parameter. The list of entity health score categories
                Examples:healthScore=good,healthScore=good&healthScore=fair (multiple entity healthscore
                values with & separator). This field is not case sensitive. .
            view(str): view query parameter. The List of Network Device model views. Please refer to
                ```NetworkDeviceView``` for the supported list .
            attribute(str): attribute query parameter. The List of Network Device model attributes. This is
                helps to specify the interested fields in the request. .
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
            https://developer.cisco.com/docs/dna-center/#!gets-the-total-network-device-counts-based-on-the-provided-query-parameters
        """
        check_type(headers, dict)
        check_type(start_time, int)
        check_type(end_time, int)
        check_type(id, str)
        check_type(site_hierarchy, str)
        check_type(site_hierarchy_id, str)
        check_type(site_id, str)
        check_type(management_ip_address, str)
        check_type(mac_address, str)
        check_type(family, str)
        check_type(type, str)
        check_type(role, str)
        check_type(serial_number, str)
        check_type(maintenance_mode, bool)
        check_type(software_version, str)
        check_type(health_score, str)
        check_type(view, str)
        check_type(attribute, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "startTime": start_time,
            "endTime": end_time,
            "id": id,
            "siteHierarchy": site_hierarchy,
            "siteHierarchyId": site_hierarchy_id,
            "siteId": site_id,
            "managementIpAddress": management_ip_address,
            "macAddress": mac_address,
            "family": family,
            "type": type,
            "role": role,
            "serialNumber": serial_number,
            "maintenanceMode": maintenance_mode,
            "softwareVersion": software_version,
            "healthScore": health_score,
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

        e_url = "/dna/data/api/v1/networkDevices/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_d8782f4d285506d9e1391f0190ff738_v2_3_7_6", json_data
        )

    def gets_the_list_of_network_devices_based_on_the_provided_complex_filters_and_aggregation_functions_v1(
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
        """Gets the list of Network Devices based on the provided complex filters and aggregation functions. For detailed
        information about the usage of the API, please refer to the Open API specification document
        https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-AssuranceNetworkDevices-1.0.2-resolved.yaml .

        Args:
            aggregateAttributes(list): Devices's aggregateAttributes (list of objects).
            attributes(list): Devices's Attributes (list of strings).
            endTime(integer): Devices's End Time.
            filters(list): Devices's filters (list of objects).
            page(object): Devices's page.
            startTime(integer): Devices's Start Time.
            views(list): Devices's Views (list of strings).
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
            https://developer.cisco.com/docs/dna-center/#!gets-the-list-of-network-devices-based-on-the-provided-complex-filters-and-aggregation-functions
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
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
                "jsd_bd1c59e9be75ac4a40decaa95ee9efd_v2_3_7_6"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/networkDevices/query"
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
            "bpm_bd1c59e9be75ac4a40decaa95ee9efd_v2_3_7_6", json_data
        )

    def gets_the_summary_analytics_data_related_to_network_devices_v1(
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
        """Gets the summary analytics data related to network devices based on the provided input data. This endpoint helps
        to obtain the consolidated insights into the performance and status of the monitored network devices.
        For detailed information about the usage of the API, please refer to the Open API specification document
        https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-AssuranceNetworkDevices-1.0.2-resolved.yaml .

        Args:
            aggregateAttributes(list): Devices's aggregateAttributes (list of objects).
            attributes(list): Devices's Attributes (list of strings).
            endTime(integer): Devices's End Time.
            filters(list): Devices's filters (list of objects).
            groupBy(list): Devices's Group By (list of strings).
            page(object): Devices's page.
            startTime(integer): Devices's Start Time.
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
            https://developer.cisco.com/docs/dna-center/#!gets-the-summary-analytics-data-related-to-network-devices
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
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
                "jsd_bb7c52e5225e9398a006fecf4da06f_v2_3_7_6"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/networkDevices/summaryAnalytics"
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
            "bpm_bb7c52e5225e9398a006fecf4da06f_v2_3_7_6", json_data
        )

    def gets_the_trend_analytics_data_v1(
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
        """Gets the Trend analytics Network device data for the given time range. The data will be grouped based on the
        given trend time Interval. The required property for this API is `trendInterval`. For detailed
        information about the usage of the API, please refer to the Open API specification document
        https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-AssuranceNetworkDevices-1.0.2-resolved.yaml .

        Args:
            aggregateAttributes(list): Devices's Aggregate Attributes (list of objects).
            attributes(list): Devices's Attributes (list of strings).
            endTime(integer): Devices's End Time.
            filters(list): Devices's filters (list of objects).
            groupBy(list): Devices's Group By (list of objects).
            page(object): Devices's page.
            startTime(integer): Devices's Start Time.
            trendInterval(string): Devices's Trend Interval.
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
            https://developer.cisco.com/docs/dna-center/#!gets-the-trend-analytics-data
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
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
                "jsd_ac7ce690e0f55a469b0a9bfa3d2c165e_v2_3_7_6"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/networkDevices/trendAnalytics"
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
            "bpm_ac7ce690e0f55a469b0a9bfa3d2c165e_v2_3_7_6", json_data
        )

    def get_the_device_data_for_the_given_device_id_uuid_v1(
        self,
        id,
        attribute=None,
        end_time=None,
        start_time=None,
        view=None,
        headers=None,
        **request_parameters
    ):
        """Returns the device data for the given device Uuid in the specified start and end time range. When there is no
        start and end time specified returns the latest available data for the given Id. For detailed
        information about the usage of the API, please refer to the Open API specification document
        https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-AssuranceNetworkDevices-1.0.2-resolved.yaml .

        Args:
            id(str): id path parameter. The device Uuid .
            start_time(int): startTime query parameter. Start time from which API queries the data set related to
                the resource. It must be specified in UNIX epochtime in milliseconds. Value is
                inclusive. If `startTime` is not provided, API will default to current time. .
            end_time(int): endTime query parameter. End time to which API queries the data set related to the
                resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive. .
            view(str): view query parameter. The List of Network Device model views. Please refer to
                ```NetworkDeviceView``` for the supported list .
            attribute(str): attribute query parameter. The List of Network Device model attributes. This is
                helps to specify the interested fields in the request. .
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
            https://developer.cisco.com/docs/dna-center/#!get-the-device-data-for-the-given-device-id-uuid
        """
        check_type(headers, dict)
        check_type(start_time, int)
        check_type(end_time, int)
        check_type(view, str)
        check_type(attribute, str)
        check_type(id, str, may_be_none=False)
        if headers is not None:
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

        e_url = "/dna/data/api/v1/networkDevices/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_f89c7ee84a615469b754add8feeabb5a_v2_3_7_6", json_data
        )

    def the_trend_analytics_data_for_the_network_device_in_the_specified_time_range_v1(
        self,
        id,
        aggregateAttributes=None,
        attributes=None,
        endTime=None,
        filters=None,
        groupBy=None,
        page=None,
        startTime=None,
        trendIntervalInMinutes=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """The Trend analytics data for the network Device in the specified time range. The data is grouped based on the
        trend time Interval, other input parameters like attribute and aggregate attributes. For detailed
        information about the usage of the API, please refer to the Open API specification document
        https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-AssuranceNetworkDevices-1.0.2-resolved.yaml .

        Args:
            aggregateAttributes(list): Devices's aggregateAttributes (list of objects).
            attributes(list): Devices's Attributes (list of strings).
            endTime(integer): Devices's End Time.
            filters(list): Devices's filters (list of objects).
            groupBy(list): Devices's Group By (list of strings).
            page(object): Devices's page.
            startTime(integer): Devices's Start Time.
            trendIntervalInMinutes(integer): Devices's Trend Interval In Minutes.
            id(str): id path parameter. The device Uuid .
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
            https://developer.cisco.com/docs/dna-center/#!the-trend-analytics-data-for-the-network-device-in-the-specified-time-range
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
            "startTime": startTime,
            "endTime": endTime,
            "trendIntervalInMinutes": trendIntervalInMinutes,
            "groupBy": groupBy,
            "filters": filters,
            "attributes": attributes,
            "aggregateAttributes": aggregateAttributes,
            "page": page,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_ca2f659b595c0ba7c649fd8c8bdad6_v2_3_7_6"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/data/api/v1/networkDevices/{id}/trendAnalytics"
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
            "bpm_ca2f659b595c0ba7c649fd8c8bdad6_v2_3_7_6", json_data
        )

    def get_planned_access_points_for_building_v1(
        self,
        building_id,
        limit=None,
        offset=None,
        radios=None,
        headers=None,
        **request_parameters
    ):
        """Provides a list of Planned Access Points for the Building it is requested for .

        Args:
            building_id(str): buildingId path parameter. The instance UUID of the building hierarchy element
                .
            limit(int): limit query parameter. The page size limit for the response, e.g. limit=100 will return a
                maximum of 100 records .
            offset(int): offset query parameter. The page offset for the response. E.g. if limit=100, offset=0 will
                return first 100 records, offset=1 will return next 100 records, etc. .
            radios(bool): radios query parameter. Whether to include the planned radio details of the planned access
                points .
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
            https://developer.cisco.com/docs/dna-center/#!get-planned-access-points-for-building
        """
        check_type(headers, dict)
        check_type(limit, int)
        check_type(offset, int)
        check_type(radios, bool)
        check_type(building_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "limit": limit,
            "offset": offset,
            "radios": radios,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "buildingId": building_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/buildings/{buildingId}/planned-" + "access-points"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_efc372d6eb577ca47e8c86f30c3d2f_v2_3_7_6", json_data
        )

    def get_device_detail_v1(
        self, identifier, search_by, timestamp=None, headers=None, **request_parameters
    ):
        """Returns detailed Network Device information retrieved by Mac Address, Device Name or UUID for any given point of
        time.  .

        Args:
            timestamp(int): timestamp query parameter. UTC timestamp of device data in milliseconds .
            identifier(str): identifier query parameter. One of "macAddress", "nwDeviceName", "uuid" (case
                insensitive) .
            search_by(str): searchBy query parameter. MAC Address, device name, or UUID of the network device
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
            ApiError: If the DNA Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-device-detail
        """
        check_type(headers, dict)
        check_type(timestamp, int)
        check_type(identifier, str, may_be_none=False)
        check_type(search_by, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "timestamp": timestamp,
            "identifier": identifier,
            "searchBy": search_by,
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

        e_url = "/dna/intent/api/v1/device-detail"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c9ee787eb5a0391309f45ddf392ca_v2_3_7_6", json_data
        )

    def get_device_enrichment_details_v1(self, headers=None, **request_parameters):
        """Enriches a given network device context (device id or device Mac Address or device management IP address) with
        details about the device and neighbor topology .

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
            https://developer.cisco.com/docs/dna-center/#!get-device-enrichment-details
        """
        check_type(headers, dict)
        if headers is not None:
            if "entity_type" in headers:
                check_type(headers.get("entity_type"), str, may_be_none=False)
            if "entity_value" in headers:
                check_type(headers.get("entity_value"), str, may_be_none=False)
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

        e_url = "/dna/intent/api/v1/device-enrichment-details"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a20c25e0fa518bb186fd7747450ef6_v2_3_7_6", json_data
        )

    def devices_v1(
        self,
        device_role=None,
        end_time=None,
        health=None,
        limit=None,
        offset=None,
        site_id=None,
        start_time=None,
        headers=None,
        **request_parameters
    ):
        """Intent API for accessing DNA Assurance Device object for generating reports, creating dashboards or creating
        additional value added services. .

        Args:
            device_role(str): deviceRole query parameter. CORE, ACCESS, DISTRIBUTION, ROUTER, WLC, or AP
                (case insensitive) .
            site_id(str): siteId query parameter. DNACenter site UUID .
            health(str): health query parameter. DNACenter health catagory: POOR, FAIR, or GOOD (case insensitive)
                .
            start_time(int): startTime query parameter. UTC epoch time in milliseconds .
            end_time(int): endTime query parameter. UTC epoch time in milliseconds .
            limit(int): limit query parameter. Max number of device entries in the response (default to 50. Max at
                500) .
            offset(int): offset query parameter. The offset of the first device in the returned data (Mutiple of
                'limit' + 1) .
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
            https://developer.cisco.com/docs/dna-center/#!devices
        """
        check_type(headers, dict)
        check_type(device_role, str)
        check_type(site_id, str)
        check_type(health, str)
        check_type(start_time, int)
        check_type(end_time, int)
        check_type(limit, int)
        check_type(offset, int)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "deviceRole": device_role,
            "siteId": site_id,
            "health": health,
            "startTime": start_time,
            "endTime": end_time,
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

        e_url = "/dna/intent/api/v1/device-health"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c75e364632e15384a18063458e2ba0e3_v2_3_7_6", json_data
        )

    def update_planned_access_point_for_floor_v1(
        self,
        floor_id,
        attributes=None,
        isSensor=None,
        location=None,
        position=None,
        radioCount=None,
        radios=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Allows updating a planned access point on an existing floor map including its planned radio and antenna details.
        Use the Get variant of this API to fetch the existing planned access points for the floor.  The payload
        to update a planned access point is in the same format, albeit a single object instead of a list, of
        that API. .

        Args:
            attributes(object): Devices's attributes.
            isSensor(boolean): Devices's Indicates that PAP is a sensor .
            location(object): Devices's location.
            position(object): Devices's position.
            radioCount(integer): Devices's Number of radios of the planned access point .
            radios(list): Devices's radios (list of objects).
            floor_id(str): floorId path parameter. The instance UUID of the floor hierarchy element .
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
            https://developer.cisco.com/docs/dna-center/#!update-planned-access-point-for-floor
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(floor_id, str, may_be_none=False)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "floorId": floor_id,
        }
        _payload = {
            "attributes": attributes,
            "isSensor": isSensor,
            "location": location,
            "position": position,
            "radioCount": radioCount,
            "radios": radios,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_f6f9dde38ce458fcaf27ffd4f84bfe68_v2_3_7_6"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/floors/{floorId}/planned-access-" + "points"
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
            "bpm_f6f9dde38ce458fcaf27ffd4f84bfe68_v2_3_7_6", json_data
        )

    def create_planned_access_point_for_floor_v1(
        self,
        floor_id,
        attributes=None,
        isSensor=None,
        location=None,
        position=None,
        radioCount=None,
        radios=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Allows creation of a new planned access point on an existing floor map including its planned radio and antenna
        details.  Use the Get variant of this API to fetch any existing planned access points for the floor.
        The payload to create a planned access point is in the same format, albeit a single object instead of a
        list, of that API. .

        Args:
            attributes(object): Devices's attributes.
            isSensor(boolean): Devices's Indicates that PAP is a sensor .
            location(object): Devices's location.
            position(object): Devices's position.
            radioCount(integer): Devices's Number of radios of the planned access point .
            radios(list): Devices's radios (list of objects).
            floor_id(str): floorId path parameter. The instance UUID of the floor hierarchy element .
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
            https://developer.cisco.com/docs/dna-center/#!create-planned-access-point-for-floor
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(floor_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "floorId": floor_id,
        }
        _payload = {
            "attributes": attributes,
            "isSensor": isSensor,
            "location": location,
            "position": position,
            "radioCount": radioCount,
            "radios": radios,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_ca2fe989a227585086452d24d32867a6_v2_3_7_6"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/floors/{floorId}/planned-access-" + "points"
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
            "bpm_ca2fe989a227585086452d24d32867a6_v2_3_7_6", json_data
        )

    def get_planned_access_points_for_floor_v1(
        self,
        floor_id,
        limit=None,
        offset=None,
        radios=None,
        headers=None,
        **request_parameters
    ):
        """Provides a list of Planned Access Points for the Floor it is requested for .

        Args:
            floor_id(str): floorId path parameter. The instance UUID of the floor hierarchy element .
            limit(int): limit query parameter. The page size limit for the response, e.g. limit=100 will return a
                maximum of 100 records .
            offset(int): offset query parameter. The page offset for the response. E.g. if limit=100, offset=0 will
                return first 100 records, offset=1 will return next 100 records, etc. .
            radios(bool): radios query parameter. Whether to include the planned radio details of the planned access
                points .
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
            https://developer.cisco.com/docs/dna-center/#!get-planned-access-points-for-floor
        """
        check_type(headers, dict)
        check_type(limit, int)
        check_type(offset, int)
        check_type(radios, bool)
        check_type(floor_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "limit": limit,
            "offset": offset,
            "radios": radios,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "floorId": floor_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/floors/{floorId}/planned-access-" + "points"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a570c5ee77b59d8b9cd203e566288e1_v2_3_7_6", json_data
        )

    def delete_planned_access_point_for_floor_v1(
        self, floor_id, planned_access_point_uuid, headers=None, **request_parameters
    ):
        """Allow to delete a planned access point from an existing floor map including its planned radio and antenna
        details.  Use the Get variant of this API to fetch the existing planned access points for the floor.
        The instanceUUID listed in each of the planned access point attributes acts as the path param input to
        this API to delete that specific instance. .

        Args:
            floor_id(str): floorId path parameter. The instance UUID of the floor hierarchy element .
            planned_access_point_uuid(str): plannedAccessPointUuid path parameter. The instance UUID of the
                planned access point to delete .
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
            https://developer.cisco.com/docs/dna-center/#!delete-planned-access-point-for-floor
        """
        check_type(headers, dict)
        check_type(floor_id, str, may_be_none=False)
        check_type(planned_access_point_uuid, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "floorId": floor_id,
            "plannedAccessPointUuid": planned_access_point_uuid,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/floors/{floorId}/planned-access-"
            + "points/{plannedAccessPointUuid}"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_cb644669ab8d5955826d23197015e208_v2_3_7_6", json_data
        )

    def get_all_health_score_definitions_for_given_filters_v1(
        self,
        attribute=None,
        device_type=None,
        id=None,
        include_for_overall_health=None,
        limit=None,
        offset=None,
        headers=None,
        **request_parameters
    ):
        """Get all health score defintions. Supported filters are id, name and overall health include status. A health
        score definition can be different across device type. So, deviceType in the query param is important and
        default is all device types. By default all supported attributes are listed in response. For detailed
        information about the usage of the API, please refer to the Open API specification document
        https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-issueAndHealthDefinitions-1.0.0-resolved.yaml .

        Args:
            device_type(str): deviceType query parameter. These are the device families supported for health
                score definitions. If no input is made on device family, all device families are
                considered. .
            id(str): id query parameter. The definition identifier. Examples:
                id=015d9cba-4f53-4087-8317-7e49e5ffef46 (single entity id request)
                id=015d9cba-4f53-4087-8317-7e49e5ffef46&id=015d9cba-4f53-4087-8317-7e49e5ffef47
                (multiple ids in the query param) .
            include_for_overall_health(bool): includeForOverallHealth query parameter. The inclusion status of the
                issue definition, either true or false. true indicates that particular health metric is
                included in overall health computation, otherwise false. By default it's set to true.  .
            attribute(str): attribute query parameter. These are the attributes supported in health score
                definitions response. By default, all properties are sent in response. .
            offset(int): offset query parameter. Specifies the starting point within all records returned by the
                API. It's one based offset. The starting value is 1. .
            limit(int): limit query parameter. Maximum number of records to return .
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
            https://developer.cisco.com/docs/dna-center/#!get-all-health-score-definitions-for-given-filters
        """
        check_type(headers, dict)
        check_type(device_type, str)
        check_type(id, str)
        check_type(include_for_overall_health, bool)
        check_type(attribute, str)
        check_type(offset, int)
        check_type(limit, int)
        if headers is not None:
            if "X-CALLER-ID" in headers:
                check_type(headers.get("X-CALLER-ID"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "deviceType": device_type,
            "id": id,
            "includeForOverallHealth": include_for_overall_health,
            "attribute": attribute,
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

        e_url = "/dna/intent/api/v1/healthScoreDefinitions"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_dea15738b550f3b147965f64050c97_v2_3_7_6", json_data
        )

    def update_health_score_definitions_v1(
        self, headers=None, payload=None, active_validation=True, **request_parameters
    ):
        """Update health thresholds, include status of overall health status for each metric. And also to synchronize with
        global profile issue thresholds of the definition for given metric. For detailed information about the
        usage of the API, please refer to the Open API specification document https://github.com/cisco-en-
        programmability/catalyst-center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-
        issueAndHealthDefinitions-1.0.0-resolved.yaml .

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
            ApiError: If the DNA Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!update-health-score-definitions
        """
        check_type(headers, dict)
        check_type(payload, list)
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
        _payload = payload or []
        if active_validation:
            self._request_validator(
                "jsd_b08f499f995f5f46ba52e0385b54721a_v2_3_7_6"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/healthScoreDefinitions/bulkUpdate"
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
            "bpm_b08f499f995f5f46ba52e0385b54721a_v2_3_7_6", json_data
        )

    def get_health_score_definition_for_the_given_id_v1(
        self, id, headers=None, **request_parameters
    ):
        """Get health score defintion for the given id. Definition includes all properties from HealthScoreDefinition
        schema by default. For detailed information about the usage of the API, please refer to the Open API
        specification document https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-issueAndHealthDefinitions-1.0.0-resolved.yaml .

        Args:
            id(str): id path parameter. Health score definition id. .
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
            https://developer.cisco.com/docs/dna-center/#!get-health-score-definition-for-the-given-id
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

        e_url = "/dna/intent/api/v1/healthScoreDefinitions/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_d2a0bbce2c5b6ba0b4aee3248ace42_v2_3_7_6", json_data
        )

    def update_health_score_definition_for_the_given_id_v1(
        self,
        id,
        includeForOverallHealth=None,
        synchronizeToIssueThreshold=None,
        thresholdValue=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Update health threshold, include status of overall health status. And also to synchronize with global profile
        issue thresholds of the definition for given id. For detailed information about the usage of the API,
        please refer to the Open API specification document https://github.com/cisco-en-
        programmability/catalyst-center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-
        issueAndHealthDefinitions-1.0.0-resolved.yaml .

        Args:
            includeForOverallHealth(boolean): Devices's Include For Overall Health.
            synchronizeToIssueThreshold(boolean): Devices's Synchronize To Issue Threshold.
            thresholdValue(number): Devices's Thresehold Value.
            id(str): id path parameter. Health score definition id. .
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
            https://developer.cisco.com/docs/dna-center/#!update-health-score-definition-for-the-given-id
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
            "includeForOverallHealth": includeForOverallHealth,
            "thresholdValue": thresholdValue,
            "synchronizeToIssueThreshold": synchronizeToIssueThreshold,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_b4f52e69ddca5b2583b28fb4c96447aa_v2_3_7_6"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/healthScoreDefinitions/{id}"
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
            "bpm_b4f52e69ddca5b2583b28fb4c96447aa_v2_3_7_6", json_data
        )

    def get_all_interfaces_v1(
        self,
        last_input_time=None,
        last_output_time=None,
        limit=None,
        offset=None,
        headers=None,
        **request_parameters
    ):
        """Returns all available interfaces. This endpoint can return a maximum of 500 interfaces .

        Args:
            offset(int): offset query parameter.
            limit(int): limit query parameter.
            last_input_time(str): lastInputTime query parameter. Last Input Time .
            last_output_time(str): lastOutputTime query parameter. Last Output Time .
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
            https://developer.cisco.com/docs/dna-center/#!get-all-interfaces
        """
        check_type(headers, dict)
        check_type(offset, int)
        check_type(limit, int)
        check_type(last_input_time, str)
        check_type(last_output_time, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "offset": offset,
            "limit": limit,
            "lastInputTime": last_input_time,
            "lastOutputTime": last_output_time,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/interface"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_d3d71136d95562afc211b40004d109_v2_3_7_6", json_data
        )

    def get_device_interface_count_v1(self, headers=None, **request_parameters):
        """Returns the count of interfaces for all devices .

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
            ApiError: If the DNA Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-device-interface-count-for-multiple-devices
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

        e_url = "/dna/intent/api/v1/interface/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_da44fbc3e415a99aac0bdd291e9a87a_v2_3_7_6", json_data
        )

    def get_interface_by_ip_v1(self, ip_address, headers=None, **request_parameters):
        """Returns list of interfaces for specified device management IP address .

        Args:
            ip_address(str): ipAddress path parameter. IP address of the interface .
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
            https://developer.cisco.com/docs/dna-center/#!get-interface-by-i-p
        """
        check_type(headers, dict)
        check_type(ip_address, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "ipAddress": ip_address,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/interface/ip-address/{ipAddress}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_cf7fa95e3ed4527aa5ba8ca871a8c142_v2_3_7_6", json_data
        )

    def get_isis_interfaces_v1(self, headers=None, **request_parameters):
        """Returns the interfaces that has ISIS enabled .

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
            ApiError: If the DNA Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-isis-interfaces
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

        e_url = "/dna/intent/api/v1/interface/isis"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_af71ea437c8755869b00d26ba9234dff_v2_3_7_6", json_data
        )

    def get_interface_info_by_id_v1(
        self, device_id, headers=None, **request_parameters
    ):
        """Returns list of interfaces by specified device .

        Args:
            device_id(str): deviceId path parameter. Device ID .
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
            https://developer.cisco.com/docs/dna-center/#!get-interface-info-by-id
        """
        check_type(headers, dict)
        check_type(device_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "deviceId": device_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/interface/network-device/{deviceId}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_e057192b97615f0d99a10e2b66bab13a_v2_3_7_6", json_data
        )

    def get_device_interface_count_by_id_v1(
        self, device_id, headers=None, **request_parameters
    ):
        """Returns the interface count for the given device .

        Args:
            device_id(str): deviceId path parameter. Device ID .
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
            https://developer.cisco.com/docs/dna-center/#!get-device-interface-count
        """
        check_type(headers, dict)
        check_type(device_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "deviceId": device_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/interface/network-" + "device/{deviceId}/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_b7d6c62ea6522081fcf55de7eb9fd7_v2_3_7_6", json_data
        )

    def get_interface_details_v1(
        self, device_id, name, headers=None, **request_parameters
    ):
        """Returns interface by specified device Id and interface name .

        Args:
            device_id(str): deviceId path parameter. Device ID .
            name(str): name query parameter. Interface name .
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
            https://developer.cisco.com/docs/dna-center/#!get-interface-details-by-device-id-and-interface-name
        """
        check_type(headers, dict)
        check_type(name, str, may_be_none=False)
        check_type(device_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "name": name,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "deviceId": device_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/interface/network-" + "device/{deviceId}/interface-name"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_bef9e9b306085d879b877598fad71b51_v2_3_7_6", json_data
        )

    def get_device_interfaces_by_specified_range_v1(
        self,
        device_id,
        records_to_return,
        start_index,
        headers=None,
        **request_parameters
    ):
        """Returns the list of interfaces for the device for the specified range .

        Args:
            device_id(str): deviceId path parameter. Device ID .
            start_index(int): startIndex path parameter. Start index .
            records_to_return(int): recordsToReturn path parameter. Number of records to return .
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
            https://developer.cisco.com/docs/dna-center/#!get-device-interfaces-by-specified-range
        """
        check_type(headers, dict)
        check_type(device_id, str, may_be_none=False)
        check_type(start_index, int, may_be_none=False)
        check_type(records_to_return, int, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "deviceId": device_id,
            "startIndex": start_index,
            "recordsToReturn": records_to_return,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/interface/network-"
            + "device/{deviceId}/{startIndex}/{recordsToReturn}"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a3d52c630ba5deaada16fe3b07af744_v2_3_7_6", json_data
        )

    def get_ospf_interfaces_v1(self, headers=None, **request_parameters):
        """Returns the interfaces that has OSPF enabled .

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
            ApiError: If the DNA Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-ospf-interfaces
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

        e_url = "/dna/intent/api/v1/interface/ospf"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a2868ff45f5621965f6ece01a742ce_v2_3_7_6", json_data
        )

    def get_interface_by_id_v1(self, id, headers=None, **request_parameters):
        """Returns the interface for the given interface ID .

        Args:
            id(str): id path parameter. Interface ID .
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
            https://developer.cisco.com/docs/dna-center/#!get-interface-by-id
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

        e_url = "/dna/intent/api/v1/interface/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_b16bff74ae54ca88a02b34df169218_v2_3_7_6", json_data
        )

    def update_interface_details_v1(
        self,
        interface_uuid,
        adminStatus=None,
        deployment_mode=None,
        description=None,
        vlanId=None,
        voiceVlanId=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Add/Update Interface description, VLAN membership, Voice VLAN and change Interface admin status ('UP'/'DOWN')
        from Request body. .

        Args:
            adminStatus(string): Devices's Admin status as ('UP'/'DOWN') .
            description(string): Devices's Description for the Interface .
            vlanId(integer): Devices's VLAN Id to be Updated .
            voiceVlanId(integer): Devices's Voice Vlan Id to be Updated .
            interface_uuid(str): interfaceUuid path parameter. Interface ID .
            deployment_mode(str): deploymentMode query parameter. Preview/Deploy ['Preview' means the
                configuration is not pushed to the device. 'Deploy' makes the configuration pushed to
                the device] .
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
            https://developer.cisco.com/docs/dna-center/#!update-interface-details
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(deployment_mode, str)
        check_type(interface_uuid, str, may_be_none=False)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "deploymentMode": deployment_mode,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "interfaceUuid": interface_uuid,
        }
        _payload = {
            "description": description,
            "adminStatus": adminStatus,
            "vlanId": vlanId,
            "voiceVlanId": voiceVlanId,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator("jsd_b887c55faaca726bbe4ac2564_v2_3_7_6").validate(
                _payload
            )

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/interface/{interfaceUuid}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(
                endpoint_full_url, params=_params, json=_payload, headers=_headers
            )
        else:
            json_data = self._session.put(
                endpoint_full_url, params=_params, json=_payload
            )

        return self._object_factory("bpm_b887c55faaca726bbe4ac2564_v2_3_7_6", json_data)

    def legit_operations_for_interface_v1(
        self, interface_uuid, headers=None, **request_parameters
    ):
        """Get list of all properties & operations valid for an interface. .

        Args:
            interface_uuid(str): interfaceUuid path parameter. Interface ID .
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
            https://developer.cisco.com/docs/dna-center/#!legit-operations-for-interface
        """
        check_type(headers, dict)
        check_type(interface_uuid, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "interfaceUuid": interface_uuid,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/interface/{interfaceUuid}/legit-" + "operation"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_fe6d62edcec25921926043ca25f75bed_v2_3_7_6", json_data
        )

    def clear_mac_address_table_v1(
        self,
        interface_uuid,
        deployment_mode=None,
        operation=None,
        payload=None,
        headers=None,
        active_validation=True,
        **request_parameters
    ):
        """Clear mac-address on an individual port. In request body, operation needs to be specified as 'ClearMacAddress'.
        In the future more possible operations will be added to this API .

        Args:
            operation(string): Devices's Operation needs to be specified as 'ClearMacAddress'. .
            payload(object): Devices's Payload is not applicable .
            interface_uuid(str): interfaceUuid path parameter. Interface Id .
            deployment_mode(str): deploymentMode query parameter. Preview/Deploy ['Preview' means the
                configuration is not pushed to the device. 'Deploy' makes the configuration pushed to
                the device] .
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
            https://developer.cisco.com/docs/dna-center/#!clear-mac-address-table
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(deployment_mode, str)
        check_type(interface_uuid, str, may_be_none=False)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "deploymentMode": deployment_mode,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "interfaceUuid": interface_uuid,
        }
        _payload = {
            "operation": operation,
            "payload": payload,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_e702d5786552992aa76b930780569_v2_3_7_6"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/interface/{interfaceUuid}/operation"
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
            "bpm_e702d5786552992aa76b930780569_v2_3_7_6", json_data
        )

    def get_device_list_v1(
        self,
        associated_wlc_ip=None,
        collection_interval=None,
        collection_status=None,
        device_support_level=None,
        error_code=None,
        error_description=None,
        family=None,
        hostname=None,
        id=None,
        license_name=None,
        license_status=None,
        license_type=None,
        limit=None,
        location=None,
        location_name=None,
        mac_address=None,
        management_ip_address=None,
        module_equpimenttype=None,
        module_name=None,
        module_operationstatecode=None,
        module_partnumber=None,
        module_servicestate=None,
        module_vendorequipmenttype=None,
        not_synced_for_minutes=None,
        offset=None,
        platform_id=None,
        reachability_status=None,
        role=None,
        serial_number=None,
        series=None,
        software_type=None,
        software_version=None,
        type=None,
        up_time=None,
        headers=None,
        **request_parameters
    ):
        """Returns list of network devices based on filter criteria such as management IP address, mac address, hostname,
        etc. You can use the .* in any value to conduct a wildcard search. For example, to find all hostnames
        beginning with myhost in the IP address range 192.25.18.n, issue the following request: GET
        /dna/intent/api/v1/network-device?hostname=myhost.*&managementIpAddress=192.25.18..* If id parameter is
        provided with comma separated ids, it will return the list of network-devices for the given ids and
        ignores the other request parameters. You can also specify offset & limit to get the required list. .

        Args:
            hostname(str, list, set, tuple): hostname query parameter.
            management_ip_address(str, list, set, tuple): managementIpAddress query parameter.
            mac_address(str, list, set, tuple): macAddress query parameter.
            location_name(str, list, set, tuple): locationName query parameter.
            serial_number(str, list, set, tuple): serialNumber query parameter.
            location(str, list, set, tuple): location query parameter.
            family(str, list, set, tuple): family query parameter.
            type(str, list, set, tuple): type query parameter.
            series(str, list, set, tuple): series query parameter.
            collection_status(str, list, set, tuple): collectionStatus query parameter.
            collection_interval(str, list, set, tuple): collectionInterval query parameter.
            not_synced_for_minutes(str, list, set, tuple): notSyncedForMinutes query parameter.
            error_code(str, list, set, tuple): errorCode query parameter.
            error_description(str, list, set, tuple): errorDescription query parameter.
            software_version(str, list, set, tuple): softwareVersion query parameter.
            software_type(str, list, set, tuple): softwareType query parameter.
            platform_id(str, list, set, tuple): platformId query parameter.
            role(str, list, set, tuple): role query parameter.
            reachability_status(str, list, set, tuple): reachabilityStatus query parameter.
            up_time(str, list, set, tuple): upTime query parameter.
            associated_wlc_ip(str, list, set, tuple): associatedWlcIp query parameter.
            license_name(str, list, set, tuple): license.name query parameter.
            license_type(str, list, set, tuple): license.type query parameter.
            license_status(str, list, set, tuple): license.status query parameter.
            module_name(str, list, set, tuple): module+name query parameter.
            module_equpimenttype(str, list, set, tuple): module+equpimenttype query parameter.
            module_servicestate(str, list, set, tuple): module+servicestate query parameter.
            module_vendorequipmenttype(str, list, set, tuple): module+vendorequipmenttype query parameter.
            module_partnumber(str, list, set, tuple): module+partnumber query parameter.
            module_operationstatecode(str, list, set, tuple): module+operationstatecode query parameter.
            id(str): id query parameter. Accepts comma separated ids and return list of network-devices for
                the given ids. If invalid or not-found ids are provided, null entry will be returned in
                the list. .
            device_support_level(str): deviceSupportLevel query parameter.
            offset(int): offset query parameter. offset >= 1 [X gives results from Xth device onwards] .
            limit(int): limit query parameter. 1 <= limit <= 500 [max. no. of devices to be returned in the result]
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
            ApiError: If the DNA Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-device-list
        """
        check_type(headers, dict)
        check_type(hostname, (str, list, set, tuple))
        check_type(management_ip_address, (str, list, set, tuple))
        check_type(mac_address, (str, list, set, tuple))
        check_type(location_name, (str, list, set, tuple))
        check_type(serial_number, (str, list, set, tuple))
        check_type(location, (str, list, set, tuple))
        check_type(family, (str, list, set, tuple))
        check_type(type, (str, list, set, tuple))
        check_type(series, (str, list, set, tuple))
        check_type(collection_status, (str, list, set, tuple))
        check_type(collection_interval, (str, list, set, tuple))
        check_type(not_synced_for_minutes, (str, list, set, tuple))
        check_type(error_code, (str, list, set, tuple))
        check_type(error_description, (str, list, set, tuple))
        check_type(software_version, (str, list, set, tuple))
        check_type(software_type, (str, list, set, tuple))
        check_type(platform_id, (str, list, set, tuple))
        check_type(role, (str, list, set, tuple))
        check_type(reachability_status, (str, list, set, tuple))
        check_type(up_time, (str, list, set, tuple))
        check_type(associated_wlc_ip, (str, list, set, tuple))
        check_type(license_name, (str, list, set, tuple))
        check_type(license_type, (str, list, set, tuple))
        check_type(license_status, (str, list, set, tuple))
        check_type(module_name, (str, list, set, tuple))
        check_type(module_equpimenttype, (str, list, set, tuple))
        check_type(module_servicestate, (str, list, set, tuple))
        check_type(module_vendorequipmenttype, (str, list, set, tuple))
        check_type(module_partnumber, (str, list, set, tuple))
        check_type(module_operationstatecode, (str, list, set, tuple))
        check_type(id, str)
        check_type(device_support_level, str)
        check_type(offset, int)
        check_type(limit, int)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "hostname": hostname,
            "managementIpAddress": management_ip_address,
            "macAddress": mac_address,
            "locationName": location_name,
            "serialNumber": serial_number,
            "location": location,
            "family": family,
            "type": type,
            "series": series,
            "collectionStatus": collection_status,
            "collectionInterval": collection_interval,
            "notSyncedForMinutes": not_synced_for_minutes,
            "errorCode": error_code,
            "errorDescription": error_description,
            "softwareVersion": software_version,
            "softwareType": software_type,
            "platformId": platform_id,
            "role": role,
            "reachabilityStatus": reachability_status,
            "upTime": up_time,
            "associatedWlcIp": associated_wlc_ip,
            "license.name": license_name,
            "license.type": license_type,
            "license.status": license_status,
            "module+name": module_name,
            "module+equpimenttype": module_equpimenttype,
            "module+servicestate": module_servicestate,
            "module+vendorequipmenttype": module_vendorequipmenttype,
            "module+partnumber": module_partnumber,
            "module+operationstatecode": module_operationstatecode,
            "id": id,
            "deviceSupportLevel": device_support_level,
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

        e_url = "/dna/intent/api/v1/network-device"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_fe602e8165035b5cbc304fada4ee2f26_v2_3_7_6", json_data
        )

    def add_device_v1(
        self,
        cliTransport=None,
        computeDevice=None,
        enablePassword=None,
        extendedDiscoveryInfo=None,
        httpPassword=None,
        httpPort=None,
        httpSecure=None,
        httpUserName=None,
        ipAddress=None,
        merakiOrgId=None,
        netconfPort=None,
        password=None,
        serialNumber=None,
        snmpAuthPassphrase=None,
        snmpAuthProtocol=None,
        snmpMode=None,
        snmpPrivPassphrase=None,
        snmpPrivProtocol=None,
        snmpROCommunity=None,
        snmpRWCommunity=None,
        snmpRetry=None,
        snmpTimeout=None,
        snmpUserName=None,
        snmpVersion=None,
        type=None,
        userName=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Adds the device with given credential .

        Args:
            cliTransport(string): Devices's CLI transport. Supported values: telnet, ssh. Required if type is
                NETWORK_DEVICE. .
            computeDevice(boolean): Devices's Compute Device or not. Options are true / false. .
            enablePassword(string): Devices's CLI enable password of the device. Required if device is configured to
                use enable password. .
            extendedDiscoveryInfo(string): Devices's This field holds that info as whether to add device with canned
                data or not. Supported values: DISCOVER_WITH_CANNED_DATA. .
            httpPassword(string): Devices's HTTP password of the device / API key for Meraki Dashboard. Required if
                type is MERAKI_DASHBOARD or COMPUTE_DEVICE. .
            httpPort(string): Devices's HTTP port of the device. Required if type is COMPUTE_DEVICE. .
            httpSecure(boolean): Devices's Flag to select HTTP / HTTPS protocol. Options are true / false. true for
                HTTPS and false for HTTP. Default is true. .
            httpUserName(string): Devices's HTTP Username of the device. Required if type is COMPUTE_DEVICE. .
            ipAddress(list): Devices's IP Address of the device. Required if type is NETWORK_DEVICE, COMPUTE_DEVICE
                or THIRD_PARTY_DEVICE.  (list of strings).
            merakiOrgId(list): Devices's Selected Meraki organization for which the devices needs to be imported.
                Required if type is MERAKI_DASHBOARD.  (list of strings).
            netconfPort(string): Devices's Netconf Port of the device. cliTransport must be 'ssh' if netconf is
                provided. .
            password(string): Devices's CLI Password of the device. Required if type is NETWORK_DEVICE. .
            serialNumber(string): Devices's Serial Number of the Device. Required if extendedDiscoveryInfo is
                'DISCOVER_WITH_CANNED_DATA'. .
            snmpAuthPassphrase(string): Devices's SNMPv3 auth passphrase of the device. Required if snmpMode is
                authNoPriv or authPriv. .
            snmpAuthProtocol(string): Devices's SNMPv3 auth protocol. Supported values: sha, md5. Required if
                snmpMode is authNoPriv or authPriv. .
            snmpMode(string): Devices's SNMPv3 mode. Supported values: noAuthnoPriv, authNoPriv, authPriv. Required
                if snmpVersion is v3. .
            snmpPrivPassphrase(string): Devices's SNMPv3 priv passphrase. Required if snmpMode is authPriv. .
            snmpPrivProtocol(string): Devices's SNMPv3 priv protocol. Supported values: AES128. Required if snmpMode
                is authPriv. .
            snmpROCommunity(string): Devices's SNMP Read Community of the device. If snmpVersion is v2, at least one
                of snmpROCommunity and snmpRWCommunity is required. .
            snmpRWCommunity(string): Devices's SNMP Write Community of the device. If snmpVersion is v2, at least
                one of snmpROCommunity and snmpRWCommunity is required. .
            snmpRetry(integer): Devices's SNMP retry count. Max value supported is 3. Default is Global SNMP retry
                (if exists) or 3. .
            snmpTimeout(integer): Devices's SNMP timeout in seconds. Max value supported is 300. Default is Global
                SNMP timeout (if exists) or 5. .
            snmpUserName(string): Devices's SNMPV3 user name of the device. Required if snmpVersion is v3. .
            snmpVersion(string): Devices's SNMP version. Values supported: v2, v3. Required if type is
                NETWORK_DEVICE, COMPUTE_DEVICE or THIRD_PARTY_DEVICE. .
            type(string): Devices's Type of device being added. Default is NETWORK_DEVICE. . Available values are
                'COMPUTE_DEVICE', 'MERAKI_DASHBOARD', 'THIRD_PARTY_DEVICE' and 'NETWORK_DEVICE'.
            userName(string): Devices's CLI user name of the device. Required if type is NETWORK_DEVICE. .
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
            https://developer.cisco.com/docs/dna-center/#!add-device-know-your-network
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
            "cliTransport": cliTransport,
            "computeDevice": computeDevice,
            "enablePassword": enablePassword,
            "extendedDiscoveryInfo": extendedDiscoveryInfo,
            "httpPassword": httpPassword,
            "httpPort": httpPort,
            "httpSecure": httpSecure,
            "httpUserName": httpUserName,
            "ipAddress": ipAddress,
            "merakiOrgId": merakiOrgId,
            "netconfPort": netconfPort,
            "password": password,
            "serialNumber": serialNumber,
            "snmpAuthPassphrase": snmpAuthPassphrase,
            "snmpAuthProtocol": snmpAuthProtocol,
            "snmpMode": snmpMode,
            "snmpPrivPassphrase": snmpPrivPassphrase,
            "snmpPrivProtocol": snmpPrivProtocol,
            "snmpROCommunity": snmpROCommunity,
            "snmpRWCommunity": snmpRWCommunity,
            "snmpRetry": snmpRetry,
            "snmpTimeout": snmpTimeout,
            "snmpUserName": snmpUserName,
            "snmpVersion": snmpVersion,
            "type": type,
            "userName": userName,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_fe3ec7651e79d891fce37a0d860_v2_3_7_6"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/network-device"
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
            "bpm_fe3ec7651e79d891fce37a0d860_v2_3_7_6", json_data
        )

    def sync_devices_v1(
        self,
        cliTransport=None,
        computeDevice=None,
        enablePassword=None,
        extendedDiscoveryInfo=None,
        httpPassword=None,
        httpPort=None,
        httpSecure=None,
        httpUserName=None,
        ipAddress=None,
        merakiOrgId=None,
        netconfPort=None,
        password=None,
        serialNumber=None,
        snmpAuthPassphrase=None,
        snmpAuthProtocol=None,
        snmpMode=None,
        snmpPrivPassphrase=None,
        snmpPrivProtocol=None,
        snmpROCommunity=None,
        snmpRWCommunity=None,
        snmpRetry=None,
        snmpTimeout=None,
        snmpUserName=None,
        snmpVersion=None,
        type=None,
        updateMgmtIPaddressList=None,
        userName=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Update the credentials, management IP address of a given device (or a set of devices) in DNA Center and
        trigger an inventory sync. .

        Args:
            cliTransport(string): Devices's CLI transport. Supported values: telnet, ssh. Use NO!$DATA!$ if no
                change is required. Required if type is NETWORK_DEVICE. .
            computeDevice(boolean): Devices's Compute Device or not. Options are true / false. .
            enablePassword(string): Devices's CLI enable password of the device. Required if device is configured to
                use enable password. Use NO!$DATA!$ if no change is required. .
            extendedDiscoveryInfo(string): Devices's This field holds that info as whether to add device with canned
                data or not. Supported values: DISCOVER_WITH_CANNED_DATA. .
            httpPassword(string): Devices's HTTP password of the device / API key for Meraki Dashboard. Required if
                type is MERAKI_DASHBOARD or COMPUTE_DEVICE. Use NO!$DATA!$ if no change is required. .
            httpPort(string): Devices's HTTP port of the device. Required if type is COMPUTE_DEVICE. .
            httpSecure(boolean): Devices's Flag to select HTTP / HTTPS protocol. Options are true / false. true for
                HTTPS and false for HTTP. .
            httpUserName(string): Devices's HTTP Username of the device. Required if type is COMPUTE_DEVICE. Use
                NO!$DATA!$ if no change is required. .
            ipAddress(list): Devices's IP Address of the device. Required. Use 'api.meraki.com' for Meraki
                Dashboard.  (list of strings).
            merakiOrgId(list): Devices's Selected Meraki organization for which the devices needs to be imported.
                Required if type is MERAKI_DASHBOARD.  (list of strings).
            netconfPort(string): Devices's Netconf Port of the device. cliTransport must be 'ssh' if netconf is
                provided. .
            password(string): Devices's CLI Password of the device. Required if type is NETWORK_DEVICE. Use
                NO!$DATA!$ if no change is required. .
            serialNumber(string): Devices's Serial Number of the Device. Required if extendedDiscoveryInfo is
                'DISCOVER_WITH_CANNED_DATA'. .
            snmpAuthPassphrase(string): Devices's SNMPv3 auth passphrase of the device. Required if snmpMode is
                authNoPriv or authPriv. Use NO!$DATA!$ if no change is required. .
            snmpAuthProtocol(string): Devices's SNMPv3 auth protocol. Supported values: sha, md5.  Required if
                snmpMode is authNoPriv or authPriv. Use NODATACHANGE if no change is required. .
            snmpMode(string): Devices's SNMPv3 mode. Supported values: noAuthnoPriv, authNoPriv, authPriv. Required
                if snmpVersion is v3. Use NODATACHANGE if no change is required. .
            snmpPrivPassphrase(string): Devices's SNMPv3 priv passphrase. Required if snmpMode is authPriv. Use
                NO!$DATA!$ if no change is required. .
            snmpPrivProtocol(string): Devices's SNMPv3 priv protocol. Supported values: AES128. Required if snmpMode
                is authPriv. Use NODATACHANGE if no change is required. .
            snmpROCommunity(string): Devices's SNMP Read Community of the device. If snmpVersion is v2, at least one
                of snmpROCommunity and snmpRWCommunity is required. Use NO!$DATA!$ if no change is
                required. .
            snmpRWCommunity(string): Devices's SNMP Write Community of the device. If snmpVersion is v2, at least
                one of snmpROCommunity and snmpRWCommunity is required. Use NO!$DATA!$ if no change is
                required. .
            snmpRetry(integer): Devices's SNMP retry count. Max value supported is 3. Default is Global SNMP retry
                (if exists) or 3. .
            snmpTimeout(integer): Devices's SNMP timeout in seconds. Max value supported is 300. Default is Global
                SNMP timeout (if exists) or 5. .
            snmpUserName(string): Devices's SNMPV3 user name of the device. Required if snmpVersion is v3. Use
                NO!$DATA!$ if no change is required. .
            snmpVersion(string): Devices's SNMP version. Values supported: v2, v3. Required if type is
                NETWORK_DEVICE, COMPUTE_DEVICE or THIRD_PARTY_DEVICE. Use NODATACHANGE if no change is
                required. .
            type(string): Devices's Type of device being edited. Default is NETWORK_DEVICE. . Available values are
                'COMPUTE_DEVICE', 'MERAKI_DASHBOARD', 'NETWORK_DEVICE', 'THIRD_PARTY_DEVICE' and
                'NODATACHANGE'.
            updateMgmtIPaddressList(list): Devices's updateMgmtIPaddressList (list of objects).
            userName(string): Devices's CLI user name of the device. Required if type is NETWORK_DEVICE. Use
                NO!$DATA!$ if no change is required. .
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
            https://developer.cisco.com/docs/dna-center/#!update-device-details
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
            "cliTransport": cliTransport,
            "computeDevice": computeDevice,
            "enablePassword": enablePassword,
            "extendedDiscoveryInfo": extendedDiscoveryInfo,
            "httpPassword": httpPassword,
            "httpPort": httpPort,
            "httpSecure": httpSecure,
            "httpUserName": httpUserName,
            "ipAddress": ipAddress,
            "merakiOrgId": merakiOrgId,
            "netconfPort": netconfPort,
            "password": password,
            "serialNumber": serialNumber,
            "snmpAuthPassphrase": snmpAuthPassphrase,
            "snmpAuthProtocol": snmpAuthProtocol,
            "snmpMode": snmpMode,
            "snmpPrivPassphrase": snmpPrivPassphrase,
            "snmpPrivProtocol": snmpPrivProtocol,
            "snmpROCommunity": snmpROCommunity,
            "snmpRWCommunity": snmpRWCommunity,
            "snmpRetry": snmpRetry,
            "snmpTimeout": snmpTimeout,
            "snmpUserName": snmpUserName,
            "snmpVersion": snmpVersion,
            "type": type,
            "updateMgmtIPaddressList": updateMgmtIPaddressList,
            "userName": userName,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_fe06867e548bba1919024b40d992_v2_3_7_6"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/network-device"
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
            "bpm_fe06867e548bba1919024b40d992_v2_3_7_6", json_data
        )

    def get_device_values_that_match_fully_or_partially_an_attribute_v1(
        self,
        associated_wlc_ip=None,
        collection_interval=None,
        collection_status=None,
        error_code=None,
        family=None,
        hostname=None,
        limit=None,
        mac_address=None,
        management_ip_address=None,
        offset=None,
        platform_id=None,
        reachability_failure_reason=None,
        reachability_status=None,
        role=None,
        role_source=None,
        serial_number=None,
        series=None,
        software_type=None,
        software_version=None,
        type=None,
        up_time=None,
        vrf_name=None,
        headers=None,
        **request_parameters
    ):
        """Returns the list of values of the first given required parameter. You can use the .* in any value to conduct a
        wildcard search. For example, to get all the devices with the management IP address starting with 10.10.
        , issue the following request: GET /dna/inten/api/v1/network-
        device/autocomplete?managementIpAddress=10.10..* It will return the device management IP addresses that
        match fully or partially the provided attribute. {[10.10.1.1, 10.10.20.2, …]}. .

        Args:
            vrf_name(str): vrfName query parameter.
            management_ip_address(str): managementIpAddress query parameter.
            hostname(str): hostname query parameter.
            mac_address(str): macAddress query parameter.
            family(str): family query parameter.
            collection_status(str): collectionStatus query parameter.
            collection_interval(str): collectionInterval query parameter.
            software_version(str): softwareVersion query parameter.
            software_type(str): softwareType query parameter.
            reachability_status(str): reachabilityStatus query parameter.
            reachability_failure_reason(str): reachabilityFailureReason query parameter.
            error_code(str): errorCode query parameter.
            platform_id(str): platformId query parameter.
            series(str): series query parameter.
            type(str): type query parameter.
            serial_number(str): serialNumber query parameter.
            up_time(str): upTime query parameter.
            role(str): role query parameter.
            role_source(str): roleSource query parameter.
            associated_wlc_ip(str): associatedWlcIp query parameter.
            offset(int): offset query parameter.
            limit(int): limit query parameter.
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
            https://developer.cisco.com/docs/dna-center/#!get-device-values-that-match-fully-or-partially-an-attribute
        """
        check_type(headers, dict)
        check_type(vrf_name, str)
        check_type(management_ip_address, str)
        check_type(hostname, str)
        check_type(mac_address, str)
        check_type(family, str)
        check_type(collection_status, str)
        check_type(collection_interval, str)
        check_type(software_version, str)
        check_type(software_type, str)
        check_type(reachability_status, str)
        check_type(reachability_failure_reason, str)
        check_type(error_code, str)
        check_type(platform_id, str)
        check_type(series, str)
        check_type(type, str)
        check_type(serial_number, str)
        check_type(up_time, str)
        check_type(role, str)
        check_type(role_source, str)
        check_type(associated_wlc_ip, str)
        check_type(offset, int)
        check_type(limit, int)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "vrfName": vrf_name,
            "managementIpAddress": management_ip_address,
            "hostname": hostname,
            "macAddress": mac_address,
            "family": family,
            "collectionStatus": collection_status,
            "collectionInterval": collection_interval,
            "softwareVersion": software_version,
            "softwareType": software_type,
            "reachabilityStatus": reachability_status,
            "reachabilityFailureReason": reachability_failure_reason,
            "errorCode": error_code,
            "platformId": platform_id,
            "series": series,
            "type": type,
            "serialNumber": serial_number,
            "upTime": up_time,
            "role": role,
            "roleSource": role_source,
            "associatedWlcIp": associated_wlc_ip,
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

        e_url = "/dna/intent/api/v1/network-device/autocomplete"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_b5a5c8da4aaa526da6a06e97c80a38be_v2_3_7_6", json_data
        )

    def update_device_role_v1(
        self,
        id=None,
        role=None,
        roleSource=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Updates the role of the device as access, core, distribution, border router .

        Args:
            id(string): Devices's DeviceId of the Device .
            role(string): Devices's Role of device as ACCESS, CORE, DISTRIBUTION, BORDER ROUTER .
            roleSource(string): Devices's Role source as MANUAL / AUTO .
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
            https://developer.cisco.com/docs/dna-center/#!update-device-role
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = {
            "id": id,
            "role": role,
            "roleSource": roleSource,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_aa11f09d28165f4ea6c81b8642e59cc4_v2_3_7_6"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/network-device/brief"
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
            "bpm_aa11f09d28165f4ea6c81b8642e59cc4_v2_3_7_6", json_data
        )

    def get_polling_interval_for_all_devices_v1(
        self, headers=None, **request_parameters
    ):
        """Returns polling interval of all devices .

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
            ApiError: If the DNA Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-polling-interval-for-all-devices
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

        e_url = "/dna/intent/api/v1/network-device/collection-" + "schedule/global"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ce94ab18ad505e8a9846f6c4c9df0d2b_v2_3_7_6", json_data
        )

    def get_device_config_for_all_devices_v1(self, headers=None, **request_parameters):
        """Returns the config for all devices. This API has been deprecated and will not be available in a Cisco DNA
        Center release after Nov 1st 2024 23:59:59 GMT. .

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
            ApiError: If the DNA Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-device-config-for-all-devices
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

        e_url = "/dna/intent/api/v1/network-device/config"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ed2bca4be412527198720a4dfec9604a_v2_3_7_6", json_data
        )

    def get_device_config_count_v1(self, headers=None, **request_parameters):
        """Returns the count of device configs .

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
            ApiError: If the DNA Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-device-config-count
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

        e_url = "/dna/intent/api/v1/network-device/config/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_dc0a72537a3578ca31cc5ef29131d35_v2_3_7_6", json_data
        )

    def get_device_count_v1(
        self,
        hostname=None,
        location_name=None,
        mac_address=None,
        management_ip_address=None,
        headers=None,
        **request_parameters
    ):
        """Returns the count of network devices based on the filter criteria by management IP address, mac address,
        hostname and location name .

        Args:
            hostname(str, list, set, tuple): hostname query parameter.
            management_ip_address(str, list, set, tuple): managementIpAddress query parameter.
            mac_address(str, list, set, tuple): macAddress query parameter.
            location_name(str, list, set, tuple): locationName query parameter.
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
            https://developer.cisco.com/docs/dna-center/#!get-device-count
        """
        check_type(headers, dict)
        check_type(hostname, (str, list, set, tuple))
        check_type(management_ip_address, (str, list, set, tuple))
        check_type(mac_address, (str, list, set, tuple))
        check_type(location_name, (str, list, set, tuple))
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "hostname": hostname,
            "managementIpAddress": management_ip_address,
            "macAddress": mac_address,
            "locationName": location_name,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/network-device/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_bbfe7340fe6752e5bc273a303d165654_v2_3_7_6", json_data
        )

    def export_device_list_v1(
        self,
        deviceUuids=None,
        operationEnum=None,
        parameters=None,
        password=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Exports the selected network device to a file .

        Args:
            deviceUuids(list): Devices's List of device uuids  (list of strings).
            operationEnum(string): Devices's 0 to export Device Credential Details Or 1 to export Device Details .
                Available values are 'CREDENTIALDETAILS' and 'DEVICEDETAILS'.
            parameters(list): Devices's List of device parameters that needs to be exported to file  (list of
                strings).
            password(string): Devices's Password is required when the operationEnum value is 0  .
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
            https://developer.cisco.com/docs/dna-center/#!export-device-list
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = {
            "deviceUuids": deviceUuids,
            "operationEnum": operationEnum,
            "parameters": parameters,
            "password": password,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_e6ec627d3c587288978990aae75228_v2_3_7_6"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/network-device/file"
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
            "bpm_e6ec627d3c587288978990aae75228_v2_3_7_6", json_data
        )

    def get_functional_capability_for_devices_v1(
        self, device_id, function_name=None, headers=None, **request_parameters
    ):
        """Returns the functional-capability for given devices .

        Args:
            device_id(str): deviceId query parameter. Accepts comma separated deviceid's and return list of
                functional-capabilities for the given id's. If invalid or not-found id's are provided,
                null entry will be returned in the list. .
            function_name(str, list, set, tuple): functionName query parameter.
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
            https://developer.cisco.com/docs/dna-center/#!get-functional-capability-for-devices
        """
        check_type(headers, dict)
        check_type(device_id, str, may_be_none=False)
        check_type(function_name, (str, list, set, tuple))
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "deviceId": device_id,
            "functionName": function_name,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/network-device/functional-capability"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ad8cea95d71352f0842a2c869765e6cf_v2_3_7_6", json_data
        )

    def get_functional_capability_by_id_v1(
        self, id, headers=None, **request_parameters
    ):
        """Returns functional capability with given Id .

        Args:
            id(str): id path parameter. Functional Capability UUID .
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
            https://developer.cisco.com/docs/dna-center/#!get-functional-capability-by-id
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

        e_url = "/dna/intent/api/v1/network-device/functional-" + "capability/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_f494532c45654fdaeda8d46a0d9753d_v2_3_7_6", json_data
        )

    def inventory_insight_device_link_mismatch_v1(
        self,
        category,
        site_id,
        limit=None,
        offset=None,
        order=None,
        sort_by=None,
        headers=None,
        **request_parameters
    ):
        """Find all devices with link mismatch (speed /  vlan) .

        Args:
            site_id(str): siteId path parameter.
            offset(int): offset query parameter. Row Number.  Default value is 1 .
            limit(int): limit query parameter. Default value is 500 .
            category(str): category query parameter. Links mismatch category.  Value can be speed-duplex or
                vlan. .
            sort_by(str): sortBy query parameter. Sort By .
            order(str): order query parameter. Order.  Value can be asc or desc.  Default value is asc .
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
            https://developer.cisco.com/docs/dna-center/#!inventory-insight-device-link-mismatch-api
        """
        check_type(headers, dict)
        check_type(offset, int)
        check_type(limit, int)
        check_type(category, str, may_be_none=False)
        check_type(sort_by, str)
        check_type(order, str)
        check_type(site_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "offset": offset,
            "limit": limit,
            "category": category,
            "sortBy": sort_by,
            "order": order,
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

        e_url = "/dna/intent/api/v1/network-" + "device/insight/{siteId}/device-link"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_eed1595442b757bf94938c858a257ced_v2_3_7_6", json_data
        )

    def get_network_device_by_ip_v1(
        self, ip_address, headers=None, **request_parameters
    ):
        """Returns the network device by specified IP address .

        Args:
            ip_address(str): ipAddress path parameter. Device IP address .
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
            https://developer.cisco.com/docs/dna-center/#!get-network-device-by-ip
        """
        check_type(headers, dict)
        check_type(ip_address, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "ipAddress": ip_address,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/network-device/ip-address/{ipAddress}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_dc74c2052a3a4eb7e2a01eaa8e7_v2_3_7_6", json_data
        )

    def get_modules_v1(
        self,
        device_id,
        limit=None,
        name_list=None,
        offset=None,
        operational_state_code_list=None,
        part_number_list=None,
        vendor_equipment_type_list=None,
        headers=None,
        **request_parameters
    ):
        """Returns modules by specified device id .

        Args:
            device_id(str): deviceId query parameter.
            limit(int): limit query parameter.
            offset(int): offset query parameter.
            name_list(str, list, set, tuple): nameList query parameter.
            vendor_equipment_type_list(str, list, set, tuple): vendorEquipmentTypeList query parameter.
            part_number_list(str, list, set, tuple): partNumberList query parameter.
            operational_state_code_list(str, list, set, tuple): operationalStateCodeList query parameter.
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
            https://developer.cisco.com/docs/dna-center/#!get-modules
        """
        check_type(headers, dict)
        check_type(device_id, str, may_be_none=False)
        check_type(limit, int)
        check_type(offset, int)
        check_type(name_list, (str, list, set, tuple))
        check_type(vendor_equipment_type_list, (str, list, set, tuple))
        check_type(part_number_list, (str, list, set, tuple))
        check_type(operational_state_code_list, (str, list, set, tuple))
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "deviceId": device_id,
            "limit": limit,
            "offset": offset,
            "nameList": name_list,
            "vendorEquipmentTypeList": vendor_equipment_type_list,
            "partNumberList": part_number_list,
            "operationalStateCodeList": operational_state_code_list,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/network-device/module"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ce9e547725c45c66824afda98179d12f_v2_3_7_6", json_data
        )

    def get_module_count_v1(
        self,
        device_id,
        name_list=None,
        operational_state_code_list=None,
        part_number_list=None,
        vendor_equipment_type_list=None,
        headers=None,
        **request_parameters
    ):
        """Returns Module Count .

        Args:
            device_id(str): deviceId query parameter.
            name_list(str, list, set, tuple): nameList query parameter.
            vendor_equipment_type_list(str, list, set, tuple): vendorEquipmentTypeList query parameter.
            part_number_list(str, list, set, tuple): partNumberList query parameter.
            operational_state_code_list(str, list, set, tuple): operationalStateCodeList query parameter.
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
            https://developer.cisco.com/docs/dna-center/#!get-module-count
        """
        check_type(headers, dict)
        check_type(device_id, str, may_be_none=False)
        check_type(name_list, (str, list, set, tuple))
        check_type(vendor_equipment_type_list, (str, list, set, tuple))
        check_type(part_number_list, (str, list, set, tuple))
        check_type(operational_state_code_list, (str, list, set, tuple))
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "deviceId": device_id,
            "nameList": name_list,
            "vendorEquipmentTypeList": vendor_equipment_type_list,
            "partNumberList": part_number_list,
            "operationalStateCodeList": operational_state_code_list,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/network-device/module/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_fb11f997009751c991884b5fc02087c5_v2_3_7_6", json_data
        )

    def get_module_info_by_id_v1(self, id, headers=None, **request_parameters):
        """Returns Module info by 'module id' .

        Args:
            id(str): id path parameter. Module id .
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
            https://developer.cisco.com/docs/dna-center/#!get-module-info-by-id
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

        e_url = "/dna/intent/api/v1/network-device/module/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a4588640da5b018b499c5760f4092a_v2_3_7_6", json_data
        )

    def get_device_by_serial_number_v1(
        self, serial_number, headers=None, **request_parameters
    ):
        """Returns the network device with given serial number .

        Args:
            serial_number(str): serialNumber path parameter. Device serial number .
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
            https://developer.cisco.com/docs/dna-center/#!get-device-by-serial-number
        """
        check_type(headers, dict)
        check_type(serial_number, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "serialNumber": serial_number,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/network-device/serial-" + "number/{serialNumber}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c53d56c282e5f108c659009d21f9d26_v2_3_7_6", json_data
        )

    def sync_devices_using_forcesync_v1(
        self,
        force_sync=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Synchronizes the devices. If forceSync param is false (default) then the sync would run in normal priority
        thread. If forceSync param is true then the sync would run in high priority thread if available, else
        the sync will fail. Result can be seen in the child task of each device .

        Args:
            force_sync(bool): forceSync query parameter.
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
            ApiError: If the DNA Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!sync-devices
        """
        check_type(headers, dict)
        check_type(payload, list)
        check_type(force_sync, bool)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "forceSync": force_sync,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = payload or []
        if active_validation:
            self._request_validator(
                "jsd_f2c120b855cb8c852806ce72e54d_v2_3_7_6"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/network-device/sync"
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
            "bpm_f2c120b855cb8c852806ce72e54d_v2_3_7_6", json_data
        )

    def get_devices_registered_for_wsa_notification_v1(
        self, macaddress=None, serial_number=None, headers=None, **request_parameters
    ):
        """It fetches devices which are registered to receive WSA notifications. The device serial number and/or MAC
        address are required to be provided as query parameters. .

        Args:
            serial_number(str): serialNumber query parameter. Serial number of the device .
            macaddress(str): macaddress query parameter. Mac addres of the device .
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
            https://developer.cisco.com/docs/dna-center/#!get-devices-registered-for-wsa-notification
        """
        check_type(headers, dict)
        check_type(serial_number, str)
        check_type(macaddress, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "serialNumber": serial_number,
            "macaddress": macaddress,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/network-device/tenantinfo/macaddress"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_b2c39feb5e48913492c33add7f13_v2_3_7_6", json_data
        )

    def get_all_user_defined_fields_v1(
        self, id=None, name=None, headers=None, **request_parameters
    ):
        """Gets existing global User Defined Fields. If no input is given, it fetches ALL the Global UDFs. Filter/search is
        supported by UDF Id(s) or UDF name(s) or both. .

        Args:
            id(str): id query parameter. Comma-seperated id(s) used for search/filtering .
            name(str): name query parameter. Comma-seperated name(s) used for search/filtering .
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
            https://developer.cisco.com/docs/dna-center/#!get-all-user-defined-fields
        """
        check_type(headers, dict)
        check_type(id, str)
        check_type(name, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "id": id,
            "name": name,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/network-device/user-defined-field"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_d31b0bb4bde55bb8a3078b66c81f3a22_v2_3_7_6", json_data
        )

    def create_user_defined_field_v1(
        self,
        description=None,
        name=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Creates a new global User Defined Field, which can be assigned to devices .

        Args:
            description(string): Devices's Description of UDF .
            name(string): Devices's Name of UDF .
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
            https://developer.cisco.com/docs/dna-center/#!create-user-defined-field
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
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_ed266e6eda225aedbf581508635da822_v2_3_7_6"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/network-device/user-defined-field"
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
            "bpm_ed266e6eda225aedbf581508635da822_v2_3_7_6", json_data
        )

    def update_user_defined_field_v1(
        self,
        id,
        description=None,
        name=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Updates an existing global User Defined Field, using it's id. .

        Args:
            description(string): Devices's Description of UDF .
            name(string): Devices's Name of UDF .
            id(str): id path parameter. UDF id .
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
            https://developer.cisco.com/docs/dna-center/#!update-user-defined-field
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
            "name": name,
            "description": description,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_d76a951f85a7a927afc2f1ea935c8_v2_3_7_6"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/network-device/user-defined-" + "field/{id}"
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
            "bpm_d76a951f85a7a927afc2f1ea935c8_v2_3_7_6", json_data
        )

    def delete_user_defined_field_v1(self, id, headers=None, **request_parameters):
        """Deletes an existing Global User-Defined-Field using it's id. .

        Args:
            id(str): id path parameter. UDF id .
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
            https://developer.cisco.com/docs/dna-center/#!delete-user-defined-field
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

        e_url = "/dna/intent/api/v1/network-device/user-defined-" + "field/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_f0f19119501094fb5fafe05dfbca_v2_3_7_6", json_data
        )

    def get_chassis_details_for_device_v1(
        self, device_id, headers=None, **request_parameters
    ):
        """Returns chassis details for given device ID .

        Args:
            device_id(str): deviceId path parameter. Device ID .
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
            https://developer.cisco.com/docs/dna-center/#!get-chassis-details-for-device
        """
        check_type(headers, dict)
        check_type(device_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "deviceId": device_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/network-device/{deviceId}/chassis"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a03cee8dfd7514487a134a422f5e0d7_v2_3_7_6", json_data
        )

    def get_stack_details_for_device_v1(
        self, device_id, headers=None, **request_parameters
    ):
        """Retrieves complete stack details for given device ID .

        Args:
            device_id(str): deviceId path parameter. Device ID .
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
            https://developer.cisco.com/docs/dna-center/#!get-stack-details-for-device
        """
        check_type(headers, dict)
        check_type(device_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "deviceId": device_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/network-device/{deviceId}/stack"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c07eaefa1fa45faa801764d9094336ae_v2_3_7_6", json_data
        )

    def remove_user_defined_field_from_device_v1(
        self, device_id, name, headers=None, **request_parameters
    ):
        """Remove a User-Defined-Field from device. Name of UDF has to be passed as the query parameter. Please note that
        Global UDF will not be deleted by this operation. .

        Args:
            device_id(str): deviceId path parameter. UUID of device from which UDF has to be removed .
            name(str): name query parameter. Name of UDF to be removed .
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
            https://developer.cisco.com/docs/dna-center/#!remove-user-defined-field-from-device
        """
        check_type(headers, dict)
        check_type(name, str, may_be_none=False)
        check_type(device_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "name": name,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "deviceId": device_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/network-device/{deviceId}/user-" + "defined-field"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c1144f7a496455f99f95d36d6474c4b4_v2_3_7_6", json_data
        )

    def add_user_defined_field_to_device_v1(
        self,
        device_id,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Assigns an existing Global User-Defined-Field to a device. If the UDF is already assigned to the specific
        device, then it updates the device UDF value accordingly. Please note that the assigning UDF 'name' must
        be an existing global UDF. Otherwise error shall be shown. .

        Args:
            device_id(str): deviceId path parameter. UUID of device to which UDF has to be added .
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
            ApiError: If the DNA Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!add-user-defined-field-to-device
        """
        check_type(headers, dict)
        check_type(payload, list)
        check_type(device_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "deviceId": device_id,
        }
        _payload = payload or []
        if active_validation:
            self._request_validator(
                "jsd_a73fbc67627e5bbbafe748de84d42df6_v2_3_7_6"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/network-device/{deviceId}/user-" + "defined-field"
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
            "bpm_a73fbc67627e5bbbafe748de84d42df6_v2_3_7_6", json_data
        )

    def get_the_details_of_physical_components_of_the_given_device_v1(
        self, device_uuid, type=None, headers=None, **request_parameters
    ):
        """Return all types of equipment details like PowerSupply, Fan, Chassis, Backplane, Module, PROCESSOR, Other and
        SFP for the Given device. .

        Args:
            device_uuid(str): deviceUuid path parameter.
            type(str): type query parameter. Type value can be PowerSupply, Fan, Chassis, Backplane, Module,
                PROCESSOR, Other, SFP. If no type is mentioned, All equipments are fetched for the
                device. .
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
            https://developer.cisco.com/docs/dna-center/#!get-the-details-of-physical-components-of-the-given-device
        """
        check_type(headers, dict)
        check_type(type, str)
        check_type(device_uuid, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "type": type,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "deviceUuid": device_uuid,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/network-device/{deviceUuid}/equipment"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c1cb24a2b53ce8d29d119c6ee1112_v2_3_7_6", json_data
        )

    def poe_interface_details_v1(
        self, device_uuid, interface_name_list=None, headers=None, **request_parameters
    ):
        """Returns POE interface details for the device, where deviceuuid is mandatory & accepts comma seperated interface
        names which is optional and returns information for that particular interfaces where(operStatus =
        operationalStatus) .

        Args:
            device_uuid(str): deviceUuid path parameter. uuid of the device .
            interface_name_list(str): interfaceNameList query parameter. comma seperated interface names .
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
            https://developer.cisco.com/docs/dna-center/#!returns-poe-interface-details-for-the-device
        """
        check_type(headers, dict)
        check_type(interface_name_list, str)
        check_type(device_uuid, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "interfaceNameList": interface_name_list,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "deviceUuid": device_uuid,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/network-" + "device/{deviceUuid}/interface/poe-detail"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ab3215d9be065533b7cbbc978cb4d905_v2_3_7_6", json_data
        )

    def get_connected_device_detail_v1(
        self, device_uuid, interface_uuid, headers=None, **request_parameters
    ):
        """Get connected device detail for given deviceUuid and interfaceUuid .

        Args:
            device_uuid(str): deviceUuid path parameter. instanceuuid of Device .
            interface_uuid(str): interfaceUuid path parameter. instanceuuid of interface .
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
            https://developer.cisco.com/docs/dna-center/#!get-connected-device-detail
        """
        check_type(headers, dict)
        check_type(device_uuid, str, may_be_none=False)
        check_type(interface_uuid, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "deviceUuid": device_uuid,
            "interfaceUuid": interface_uuid,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/network-"
            + "device/{deviceUuid}/interface/{interfaceUuid}/neighbor"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a1878314ffd35d29bea49f12d10b59c8_v2_3_7_6", json_data
        )

    def get_linecard_details_v1(self, device_uuid, headers=None, **request_parameters):
        """Get line card detail for a given deviceuuid.  Response will contain serial no, part no, switch no and slot no. .

        Args:
            device_uuid(str): deviceUuid path parameter. instanceuuid of device .
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
            https://developer.cisco.com/docs/dna-center/#!get-linecard-details
        """
        check_type(headers, dict)
        check_type(device_uuid, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "deviceUuid": device_uuid,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/network-device/{deviceUuid}/line-card"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_bd31690b61f45d9f880d74d4e682b070_v2_3_7_6", json_data
        )

    def poe_details_v1(self, device_uuid, headers=None, **request_parameters):
        """Returns POE details for device. .

        Args:
            device_uuid(str): deviceUuid path parameter. UUID of the device .
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
            https://developer.cisco.com/docs/dna-center/#!poe-details
        """
        check_type(headers, dict)
        check_type(device_uuid, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "deviceUuid": device_uuid,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/network-device/{deviceUuid}/poe"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_f7a67aba0b365a1e9dae62d148511a25_v2_3_7_6", json_data
        )

    def get_supervisor_card_detail_v1(
        self, device_uuid, headers=None, **request_parameters
    ):
        """Get supervisor card detail for a given deviceuuid. Response will contain serial no, part no, switch no and slot
        no. .

        Args:
            device_uuid(str): deviceUuid path parameter. instanceuuid of device .
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
            https://developer.cisco.com/docs/dna-center/#!get-supervisor-card-detail
        """
        check_type(headers, dict)
        check_type(device_uuid, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "deviceUuid": device_uuid,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/network-" + "device/{deviceUuid}/supervisor-card"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_eb13516155a28570e542dcf10a91_v2_3_7_6", json_data
        )

    def update_device_management_address_v1(
        self,
        deviceid,
        newIP=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This is a simple PUT API to edit the management IP Address of the device. .

        Args:
            newIP(string): Devices's New IP Address of the device to be Updated .
            deviceid(str): deviceid path parameter. The UUID of the device whose management IP address is to
                be updated. .
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
            https://developer.cisco.com/docs/dna-center/#!update-device-management-address
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(deviceid, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "deviceid": deviceid,
        }
        _payload = {
            "newIP": newIP,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_cb98464ddb5ee9ba7ebb4428443ba9_v2_3_7_6"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/network-device/{deviceid}/management-" + "address"
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
            "bpm_cb98464ddb5ee9ba7ebb4428443ba9_v2_3_7_6", json_data
        )

    def get_device_by_id_v1(self, id, headers=None, **request_parameters):
        """Returns the network device details for the given device ID .

        Args:
            id(str): id path parameter. Device ID .
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
            https://developer.cisco.com/docs/dna-center/#!get-device-by-id
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

        e_url = "/dna/intent/api/v1/network-device/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_d86f657f8592f97014d2ebf8d37ac_v2_3_7_6", json_data
        )

    def delete_device_by_id_v1(
        self, id, clean_config=None, headers=None, **request_parameters
    ):
        """This API allows any network device that is not currently provisioned to be removed from the inventory.
        Important: Devices currently provisioned cannot be deleted. To delete a provisioned device, the device
        must be first deprovisioned. .

        Args:
            id(str): id path parameter. Device ID .
            clean_config(bool): cleanConfig query parameter. Selecting the clean up configuration option will
                attempt to remove device settings that were configured during the addition of the device
                to the inventory and site assignment. Please note that this operation is different from
                deprovisioning. It does not remove configurations that were pushed during device
                provisioning. .
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
            https://developer.cisco.com/docs/dna-center/#!delete-device-by-id
        """
        check_type(headers, dict)
        check_type(clean_config, bool)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "cleanConfig": clean_config,
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

        e_url = "/dna/intent/api/v1/network-device/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_e01233fa258e393239c4b41882806_v2_3_7_6", json_data
        )

    def get_device_summary_v1(self, id, headers=None, **request_parameters):
        """Returns brief summary of device info such as hostname, management IP address for the given device Id .

        Args:
            id(str): id path parameter. Device ID .
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
            https://developer.cisco.com/docs/dna-center/#!get-device-summary
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

        e_url = "/dna/intent/api/v1/network-device/{id}/brief"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_fe0153ca24205608b8741d51f5a6d54a_v2_3_7_6", json_data
        )

    def get_polling_interval_by_id_v1(self, id, headers=None, **request_parameters):
        """Returns polling interval by device id .

        Args:
            id(str): id path parameter. Device ID .
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
            https://developer.cisco.com/docs/dna-center/#!get-polling-interval-by-id
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

        e_url = "/dna/intent/api/v1/network-device/{id}/collection-" + "schedule"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_f90daf1c279351f884ba3198d3b2d641_v2_3_7_6", json_data
        )

    def get_organization_list_for_meraki_v1(
        self, id, headers=None, **request_parameters
    ):
        """Returns list of organizations for meraki dashboard .

        Args:
            id(str): id path parameter. Device Id .
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
            https://developer.cisco.com/docs/dna-center/#!get-organization-list-for-meraki
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

        e_url = "/dna/intent/api/v1/network-device/{id}/meraki-" + "organization"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_b4ba6d23d5e7eb62cbba4c9e1a29d_v2_3_7_6", json_data
        )

    def get_device_interface_vlans_v1(
        self, id, interface_type=None, headers=None, **request_parameters
    ):
        """Returns Device Interface VLANs. If parameter value is null or empty, it won't return any value in response. .

        Args:
            id(str): id path parameter.
            interface_type(str): interfaceType query parameter. Vlan associated with sub-interface. If no
                interfaceType mentioned it will return all types of Vlan interfaces. If interfaceType is
                selected but not specified then it will take default value. .
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
            https://developer.cisco.com/docs/dna-center/#!get-device-interface-vlans
        """
        check_type(headers, dict)
        check_type(interface_type, str)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "interfaceType": interface_type,
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

        e_url = "/dna/intent/api/v1/network-device/{id}/vlan"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_fd5fb603cba6523abb25c8ec131fbb8b_v2_3_7_6", json_data
        )

    def get_wireless_lan_controller_details_by_id_v1(
        self, id, headers=None, **request_parameters
    ):
        """Returns the wireless lan controller info with given device ID .

        Args:
            id(str): id path parameter. Device ID .
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
            https://developer.cisco.com/docs/dna-center/#!get-wireless-lan-controller-details-by-id
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

        e_url = "/dna/intent/api/v1/network-device/{id}/wireless-info"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c01ee650fcf858789ca00c8deda969b9_v2_3_7_6", json_data
        )

    def get_device_config_by_id_v1(
        self, network_device_id, headers=None, **request_parameters
    ):
        """Returns the device config by specified device ID .

        Args:
            network_device_id(str): networkDeviceId path parameter.
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
            https://developer.cisco.com/docs/dna-center/#!get-device-config-by-id
        """
        check_type(headers, dict)
        check_type(network_device_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "networkDeviceId": network_device_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/network-" + "device/{networkDeviceId}/config"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_af0bbf34adb5146b931ec874fc2cc40_v2_3_7_6", json_data
        )

    def get_network_device_by_pagination_range_v1(
        self, records_to_return, start_index, headers=None, **request_parameters
    ):
        """Returns the list of network devices for the given pagination range. The maximum number of records that can be
        retrieved is 500 .

        Args:
            start_index(int): startIndex path parameter. Start index [>=1] .
            records_to_return(int): recordsToReturn path parameter. Number of records to return [1<= recordsToReturn
                <= 500] .
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
            https://developer.cisco.com/docs/dna-center/#!get-network-device-by-pagination-range
        """
        check_type(headers, dict)
        check_type(start_index, int, may_be_none=False)
        check_type(records_to_return, int, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "startIndex": start_index,
            "recordsToReturn": records_to_return,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/network-" + "device/{startIndex}/{recordsToReturn}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_d7b6ce5abd5dad837e22ace817a6f0_v2_3_7_6", json_data
        )

    def update_global_resync_interval_v1(
        self,
        interval=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Updates the resync interval (in minutes) globally for devices which do not have custom resync interval. To
        override this setting for all network devices refer to [/networkDevices/resyncIntervalSettings/override]
        .

        Args:
            interval(integer): Devices's Resync Interval should be between 25 to 1440 minutes .
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
            https://developer.cisco.com/docs/dna-center/#!update-global-resync-interval
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
            "interval": interval,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_a64bd4956649de3a61e10f0637e_v2_3_7_6"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/networkDevices/resyncIntervalSettings"
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
            "bpm_a64bd4956649de3a61e10f0637e_v2_3_7_6", json_data
        )

    def override_resync_interval_v1(self, headers=None, **request_parameters):
        """Overrides the global resync interval on all network devices. This essentially removes device specific intervals
        if set. .

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
            ApiError: If the DNA Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!override-resync-interval
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

        e_url = "/dna/intent/api/v1/networkDevices/resyncIntervalSettings" + "/override"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.post(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_dc239a9ab9e5562b93a45ea0b9708b84_v2_3_7_6", json_data
        )

    def update_resync_interval_for_the_network_device_v1(
        self,
        id,
        interval=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Update the resync interval (in minutes) for the given network device id. To disable periodic resync, set
        interval as `0`. To use global settings, set interval as `null`. .

        Args:
            interval(integer): Devices's Resync interval in minutes. To disable periodic resync, set interval as
                `0`. To use global settings, set interval as `null`. .
            id(str): id path parameter. The id of the network device. .
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
            https://developer.cisco.com/docs/dna-center/#!update-resync-interval-for-the-network-device
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
            "interval": interval,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_fdfc828270d950ecb75480fe03f7d573_v2_3_7_6"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/networkDevices/{id}/resyncIntervalSet" + "tings"
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
            "bpm_fdfc828270d950ecb75480fe03f7d573_v2_3_7_6", json_data
        )

    def get_resync_interval_for_the_network_device_v1(
        self, id, headers=None, **request_parameters
    ):
        """Fetch the reysnc interval for the given network device id. .

        Args:
            id(str): id path parameter. The id of the network device. .
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
            https://developer.cisco.com/docs/dna-center/#!get-resync-interval-for-the-network-device
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

        e_url = "/dna/intent/api/v1/networkDevices/{id}/resyncIntervalSet" + "tings"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_e56a4c0d91dd53ecb737da824115a050_v2_3_7_6", json_data
        )

    def rogue_additional_details_v1(
        self,
        endTime=None,
        limit=None,
        offset=None,
        siteId=None,
        startTime=None,
        threatLevel=None,
        threatType=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This API provides additional information of the rogue threats with details at BSSID level. The additional
        information includes Switch Port details in case of Rogue on Wire, first time when the rogue is seen in
        the network etc. .

        Args:
            endTime(number): Devices's This is the epoch end time in milliseconds upto which data need to be
                fetched. Default value is current time .
            limit(number): Devices's The maximum number of entries to return. Default value is 1000 .
            offset(number): Devices's The offset of the first item in the collection to return. Default value is 1 .
            siteId(list): Devices's Filter Rogues by location. Site IDs information can be fetched from "Get Site"
                API  (list of strings).
            startTime(number): Devices's This is the epoch start time in milliseconds from which data need to be
                fetched. Default value is 24 hours earlier to endTime .
            threatLevel(list): Devices's Filter Rogues by Threat Level. Threat Level information can be fetched from
                "Get Threat Levels" API  (list of strings).
            threatType(list): Devices's Filter Rogues by Threat Type. Threat Type information can be fetched from
                "Get Threat Types" API  (list of strings).
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
            https://developer.cisco.com/docs/dna-center/#!rogue-additional-details
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
            "offset": offset,
            "limit": limit,
            "startTime": startTime,
            "endTime": endTime,
            "siteId": siteId,
            "threatLevel": threatLevel,
            "threatType": threatType,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_c8354b61a36524cbb2e1037bd814807_v2_3_7_6"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/security/rogue/additional/details"
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
            "bpm_c8354b61a36524cbb2e1037bd814807_v2_3_7_6", json_data
        )

    def rogue_additional_detail_count_v1(
        self,
        endTime=None,
        siteId=None,
        startTime=None,
        threatLevel=None,
        threatType=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This API returns the count for the Rogue Additional Details. .

        Args:
            endTime(number): Devices's This is the epoch end time in milliseconds upto which data need to be
                fetched. Default value is current time .
            siteId(list): Devices's Filter Rogues by location. Site IDs information can be fetched from "Get Site"
                API  (list of strings).
            startTime(number): Devices's This is the epoch start time in milliseconds from which data need to be
                fetched. Default value is 24 hours earlier to endTime .
            threatLevel(list): Devices's This information can be fetched from "Get Threat Levels" API  (list of
                strings).
            threatType(list): Devices's This information can be fetched from "Get Threat Types" API  (list of
                strings).
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
            https://developer.cisco.com/docs/dna-center/#!rogue-additional-detail-count
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
            "siteId": siteId,
            "threatLevel": threatLevel,
            "threatType": threatType,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_de4c9b685250dfa8556ab1ec20407c_v2_3_7_6"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/security/rogue/additional/details/cou" + "nt"
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
            "bpm_de4c9b685250dfa8556ab1ec20407c_v2_3_7_6", json_data
        )

    def start_wireless_rogue_ap_containment_v1(
        self,
        macAddress=None,
        type=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Intent API to start the wireless rogue access point containment. This API will initiate the containment
        operation on the strongest detecting WLC for the given Rogue AP. This is a resource intensive operation
        which has legal implications since the rogue access point on whom it is triggered, might be a valid
        neighbor access point. .

        Args:
            macAddress(string): Devices's Mac Address.
            type(integer): Devices's Type.
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
            https://developer.cisco.com/docs/dna-center/#!start-wireless-rogue-ap-containment
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = {
            "macAddress": macAddress,
            "type": type,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_fe62979a925778bdb0a974a7d86a12_v2_3_7_6"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/security/rogue/wireless-" + "containment/start"
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
            "bpm_fe62979a925778bdb0a974a7d86a12_v2_3_7_6", json_data
        )

    def wireless_rogue_ap_containment_status_v1(
        self, mac_address, headers=None, **request_parameters
    ):
        """Intent API to check the wireless rogue access point containment status. The response includes all the details
        like containment status, contained by WLC, containment status of each BSSID etc. This API also includes
        the information of strongest detecting WLC for this rogue access point. .

        Args:
            mac_address(str): macAddress path parameter. MAC Address of the Wireless Rogue AP .
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
            https://developer.cisco.com/docs/dna-center/#!wireless-rogue-ap-containment-status
        """
        check_type(headers, dict)
        check_type(mac_address, str, may_be_none=False)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "macAddress": mac_address,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/security/rogue/wireless-"
            + "containment/status/{macAddress}"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_e81244d1a2d9513384d543f0362c35d1_v2_3_7_6", json_data
        )

    def stop_wireless_rogue_ap_containment_v1(
        self,
        macAddress=None,
        type=None,
        wlcIp=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Intent API to stop the wireless rogue access point containment. This API will stop the containment through
        single WLC. The response includes the details like WLC and BSSID on which the stop containment has been
        initiated. .

        Args:
            macAddress(string): Devices's Mac Address.
            type(integer): Devices's Type.
            wlcIp(string): Devices's Wlc Ip.
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
            https://developer.cisco.com/docs/dna-center/#!stop-wireless-rogue-ap-containment
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = {
            "macAddress": macAddress,
            "type": type,
            "wlcIp": wlcIp,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_d9ed5bba1155b9c8fe132640832f94e_v2_3_7_6"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/security/rogue/wireless-" + "containment/stop"
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
            "bpm_d9ed5bba1155b9c8fe132640832f94e_v2_3_7_6", json_data
        )

    def threat_details_v1(
        self,
        endTime=None,
        isNewThreat=None,
        limit=None,
        offset=None,
        siteId=None,
        startTime=None,
        threatLevel=None,
        threatType=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """The details for the Rogue and aWIPS threats .

        Args:
            endTime(integer): Devices's End Time.
            isNewThreat(boolean): Devices's Is New Threat.
            limit(integer): Devices's Limit.
            offset(integer): Devices's Offset.
            siteId(list): Devices's Site Id (list of strings).
            startTime(integer): Devices's Start Time.
            threatLevel(list): Devices's Threat Level (list of strings).
            threatType(list): Devices's Threat Type (list of strings).
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
            https://developer.cisco.com/docs/dna-center/#!threat-details
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = {
            "offset": offset,
            "limit": limit,
            "startTime": startTime,
            "endTime": endTime,
            "siteId": siteId,
            "threatLevel": threatLevel,
            "threatType": threatType,
            "isNewThreat": isNewThreat,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_f4ce55b5f235924903516ef31dc9e3c_v2_3_7_6"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/security/threats/details"
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
            "bpm_f4ce55b5f235924903516ef31dc9e3c_v2_3_7_6", json_data
        )

    def threat_detail_count_v1(
        self,
        endTime=None,
        isNewThreat=None,
        limit=None,
        offset=None,
        siteId=None,
        startTime=None,
        threatLevel=None,
        threatType=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """The details count for the Rogue and aWIPS threats .

        Args:
            endTime(integer): Devices's End Time.
            isNewThreat(boolean): Devices's Is New Threat.
            limit(integer): Devices's Limit.
            offset(integer): Devices's Offset.
            siteId(list): Devices's Site Id (list of strings).
            startTime(integer): Devices's Start Time.
            threatLevel(list): Devices's Threat Level (list of strings).
            threatType(list): Devices's Threat Type (list of strings).
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
            https://developer.cisco.com/docs/dna-center/#!threat-detail-count
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = {
            "offset": offset,
            "limit": limit,
            "startTime": startTime,
            "endTime": endTime,
            "siteId": siteId,
            "threatLevel": threatLevel,
            "threatType": threatType,
            "isNewThreat": isNewThreat,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_c7266d89581c9601b79b7304fda3_v2_3_7_6"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/security/threats/details/count"
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
            "bpm_c7266d89581c9601b79b7304fda3_v2_3_7_6", json_data
        )

    def get_threat_levels_v1(self, headers=None, **request_parameters):
        """Intent API to fetch all threat levels defined. .

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
            ApiError: If the DNA Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-threat-levels
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

        e_url = "/dna/intent/api/v1/security/threats/level"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_eb1bd16969ed5cee8eb0a208b7441edd_v2_3_7_6", json_data
        )

    def add_allowed_mac_address_v1(
        self, headers=None, payload=None, active_validation=True, **request_parameters
    ):
        """Intent API to add the threat mac address to allowed list. .

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
            ApiError: If the DNA Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!add-allowed-mac-address
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
                "jsd_fdd36dd2454547096bb65df3755710f_v2_3_7_6"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/security/threats/rogue/allowed-list"
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
            "bpm_fdd36dd2454547096bb65df3755710f_v2_3_7_6", json_data
        )

    def get_allowed_mac_address_v1(
        self, limit=None, offset=None, headers=None, **request_parameters
    ):
        """Intent API to fetch all the allowed mac addresses in the system. .

        Args:
            offset(int): offset query parameter. The offset of the first item in the collection to return. .
            limit(int): limit query parameter. The maximum number of entries to return. If the value exceeds the
                total count, then the maximum entries will be returned. .
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
            https://developer.cisco.com/docs/dna-center/#!get-allowed-mac-address
        """
        check_type(headers, dict)
        check_type(offset, int)
        check_type(limit, int)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
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

        e_url = "/dna/intent/api/v1/security/threats/rogue/allowed-list"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_b22e597335a8ba98dc758699726b3_v2_3_7_6", json_data
        )

    def get_allowed_mac_address_count_v1(self, headers=None, **request_parameters):
        """Intent API to fetch the count of allowed mac addresses in the system. .

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
            ApiError: If the DNA Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-allowed-mac-address-count
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

        e_url = "/dna/intent/api/v1/security/threats/rogue/allowed-" + "list/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_f1a062d6eeac569b9ab40cf2d3b0ffa7_v2_3_7_6", json_data
        )

    def remove_allowed_mac_address_v1(
        self, mac_address, headers=None, **request_parameters
    ):
        """Intent API to remove the threat mac address from allowed list. .

        Args:
            mac_address(str): macAddress path parameter. Threat mac address which needs to be removed from
                the allowed list. Multiple mac addresses will be removed if provided as comma separated
                values (example: 00:2A:10:51:22:43,00:2A:10:51:22:44). Note: In one request, maximum 100
                mac addresses can be removed.  .
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
            https://developer.cisco.com/docs/dna-center/#!remove-allowed-mac-address
        """
        check_type(headers, dict)
        check_type(mac_address, str, may_be_none=False)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "macAddress": mac_address,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/security/threats/rogue/allowed-" + "list/{macAddress}"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_dda7feeaa3a564d97eb01f9843ed720_v2_3_7_6", json_data
        )

    def threat_summary_v1(
        self,
        endTime=None,
        siteId=None,
        startTime=None,
        threatLevel=None,
        threatType=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """The Threat Summary for the Rogues and aWIPS .

        Args:
            endTime(integer): Devices's End Time.
            siteId(list): Devices's Site Id (list of strings).
            startTime(integer): Devices's Start Time.
            threatLevel(list): Devices's Threat Level (list of strings).
            threatType(list): Devices's Threat Type (list of strings).
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
            https://developer.cisco.com/docs/dna-center/#!threat-summary
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = {
            "startTime": startTime,
            "endTime": endTime,
            "siteId": siteId,
            "threatLevel": threatLevel,
            "threatType": threatType,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_e6eed78cb55d51a1bfe669729df25689_v2_3_7_6"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/security/threats/summary"
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
            "bpm_e6eed78cb55d51a1bfe669729df25689_v2_3_7_6", json_data
        )

    def get_threat_types_v1(self, headers=None, **request_parameters):
        """Intent API to fetch all threat types defined. .

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
            ApiError: If the DNA Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-threat-types
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

        e_url = "/dna/intent/api/v1/security/threats/type"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c1720793d71052418cadda1f9fd5f977_v2_3_7_6", json_data
        )

    def get_device_interface_stats_info_v2(
        self,
        device_id,
        endTime=None,
        query=None,
        startTime=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This API returns the Interface Stats for the given Device Id. Please refer to the Feature tab for the Request
        Body usage and the API filtering support. .

        Args:
            endTime(integer): Devices's UTC epoch timestamp in milliseconds .
            query(object): Devices's query.
            startTime(integer): Devices's UTC epoch timestamp in milliseconds .
            device_id(str): deviceId path parameter. Network Device Id .
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
            https://developer.cisco.com/docs/dna-center/#!get-device-interface-stats-info
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(device_id, str, may_be_none=False)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "deviceId": device_id,
        }
        _payload = {
            "startTime": startTime,
            "endTime": endTime,
            "query": query,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_a9e0722d184658c592bd130ff03e1dde_v2_3_7_6"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v2/networkDevices/{deviceId}/interfaces/" + "query"
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
            "bpm_a9e0722d184658c592bd130ff03e1dde_v2_3_7_6", json_data
        )

    def get_the_count_of_health_score_definitions_based_on_provided_filters_v1(
        self,
        device_type=None,
        id=None,
        include_for_overall_health=None,
        headers=None,
        **request_parameters
    ):
        """Get the count of health score definitions based on provided filters. Supported filters are id, name and overall
        health include status. For detailed information about the usage of the API, please refer to the Open API
        specification document https://github.com/cisco-en-programmability/catalyst-center-api-
        specs/blob/main/Assurance/CE_Cat_Center_Org-issueAndHealthDefinitions-1.0.0-resolved.yaml .

        Args:
            device_type(str): deviceType query parameter. These are the device families supported for health
                score definitions. If no input is made on device family, all device families are
                considered. .
            id(str): id query parameter. The definition identifier. Examples:
                id=015d9cba-4f53-4087-8317-7e49e5ffef46 (single entity id request)
                id=015d9cba-4f53-4087-8317-7e49e5ffef46&id=015d9cba-4f53-4087-8317-7e49e5ffef47
                (multiple ids in the query param) .
            include_for_overall_health(bool): includeForOverallHealth query parameter. The inclusion status of the
                issue definition, either true or false. true indicates that particular health metric is
                included in overall health computation, otherwise false. By default it's set to true. .
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
            https://developer.cisco.com/docs/dna-center/#!get-the-count-of-health-score-definitions-based-on-provided-filters
        """
        check_type(headers, dict)
        check_type(device_type, str)
        check_type(id, str)
        check_type(include_for_overall_health, bool)
        if headers is not None:
            if "X-CALLER-ID" in headers:
                check_type(headers.get("X-CALLER-ID"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "deviceType": device_type,
            "id": id,
            "includeForOverallHealth": include_for_overall_health,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/intent/api/v1/healthScoreDefinitions/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a51fd8467055ff1a69ade1ae8096993_v2_3_7_6", json_data
        )

    # Alias Function
    def get_interface_by_ip(self, ip_address, headers=None, **request_parameters):
        """This function is an alias of get_interface_by_ip_v1 .
        Args:
            ip_address(basestring): ipAddress path parameter. IP address of the interface .
            headers(dict): Dictionary of HTTP Headers to send with the Request.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_interface_by_ip_v1 .
        """
        return self.get_interface_by_ip_v1(
            ip_address=ip_address, headers=headers, **request_parameters
        )

    # Alias Function
    def get_supervisor_card_detail(
        self, device_uuid, headers=None, **request_parameters
    ):
        """This function is an alias of get_supervisor_card_detail_v1 .
        Args:
            device_uuid(basestring): deviceUuid path parameter. instanceuuid of device .
            headers(dict): Dictionary of HTTP Headers to send with the Request.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_supervisor_card_detail_v1 .
        """
        return self.get_supervisor_card_detail_v1(
            device_uuid=device_uuid, headers=headers, **request_parameters
        )

    # Alias Function
    def the_total_interfaces_count_across_the_network_devices(
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
        """This function is an alias of the_total_interfaces_count_across_the_network_devices_v1 .
        Args:
            aggregateAttributes(list): Devices's aggregateAttributes (list of objects).
            attributes(list): Devices's Attributes (list of strings).
            endTime(integer): Devices's End Time.
            filters(list): Devices's filters (list of objects).
            page(object): Devices's page.
            startTime(integer): Devices's Start Time.
            views(list): Devices's Views (list of strings).
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of the_total_interfaces_count_across_the_network_devices_v1 .
        """
        return self.the_total_interfaces_count_across_the_network_devices_v1(
            aggregateAttributes=aggregateAttributes,
            attributes=attributes,
            endTime=endTime,
            filters=filters,
            page=page,
            startTime=startTime,
            views=views,
            headers=headers,
            payload=payload,
            active_validation=active_validation,
            **request_parameters
        )

    # Alias Function
    def threat_details(
        self,
        endTime=None,
        isNewThreat=None,
        limit=None,
        offset=None,
        siteId=None,
        startTime=None,
        threatLevel=None,
        threatType=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This function is an alias of threat_details_v1 .
        Args:
            endTime(integer): Devices's End Time.
            isNewThreat(boolean): Devices's Is New Threat.
            limit(integer): Devices's Limit.
            offset(integer): Devices's Offset.
            siteId(list): Devices's Site Id (list of strings).
            startTime(integer): Devices's Start Time.
            threatLevel(list): Devices's Threat Level (list of strings).
            threatType(list): Devices's Threat Type (list of strings).
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of threat_details_v1 .
        """
        return self.threat_details_v1(
            endTime=endTime,
            isNewThreat=isNewThreat,
            limit=limit,
            offset=offset,
            siteId=siteId,
            startTime=startTime,
            threatLevel=threatLevel,
            threatType=threatType,
            headers=headers,
            payload=payload,
            active_validation=active_validation,
            **request_parameters
        )

    # Alias Function
    def gets_the_total_network_device_counts_based_on_the_provided_query_parameters(
        self,
        attribute=None,
        end_time=None,
        family=None,
        health_score=None,
        id=None,
        mac_address=None,
        maintenance_mode=None,
        management_ip_address=None,
        role=None,
        serial_number=None,
        site_hierarchy=None,
        site_hierarchy_id=None,
        site_id=None,
        software_version=None,
        start_time=None,
        type=None,
        view=None,
        headers=None,
        **request_parameters
    ):
        """This function is an alias of gets_the_total_network_device_counts_based_on_the_provided_query_parameters_v1 .
        Args:
            start_time(int): startTime query parameter. Start time from which API queries the data set related to
                the resource. It must be specified in UNIX epochtime in milliseconds. Value is
                inclusive. If `startTime` is not provided, API will default to current time. .
            end_time(int): endTime query parameter. End time to which API queries the data set related to the
                resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive. .
            id(basestring): id query parameter. The list of entity Uuids.
                (Ex."6bef213c-19ca-4170-8375-b694e251101c") Examples:
                id=6bef213c-19ca-4170-8375-b694e251101c (single entity uuid requested) id=6bef213c-19ca-
                4170-8375-b694e251101c&id=32219612-819e-4b5e-a96b-cf22aca13dd9&id=2541e9a7-b80d-4955-
                8aa2-79b233318ba0 (multiple entity uuid with '&' separator) .
            site_hierarchy(basestring): siteHierarchy query parameter. The full hierarchical breakdown of the site
                tree starting from Global site name and ending with the specific site name. The Root
                site is named "Global" (Ex. `Global/AreaName/BuildingName/FloorName`) This field
                supports wildcard asterisk (*) character search support. E.g. */San*, */San, /San*
                Examples: `?siteHierarchy=Global/AreaName/BuildingName/FloorName` (single siteHierarchy
                requested) `?siteHierarchy=Global/AreaName/BuildingName/FloorName&siteHierarchy=Global/A
                reaName2/BuildingName2/FloorName2` (multiple siteHierarchies requested) .
            site_hierarchy_id(basestring): siteHierarchyId query parameter. The full hierarchy breakdown of the site
                tree in id form starting from Global site UUID and ending with the specific site UUID.
                (Ex. `globalUuid/areaUuid/buildingUuid/floorUuid`) This field supports wildcard asterisk
                (*) character search support. E.g. `*uuid*, *uuid, uuid* Examples:
                `?siteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid `(single siteHierarchyId
                requested) `?siteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid&siteHierarchyId=
                globalUuid/areaUuid2/buildingUuid2/floorUuid2` (multiple siteHierarchyIds requested) .
            site_id(basestring): siteId query parameter. The UUID of the site. (Ex. `flooruuid`) This field supports
                wildcard asterisk (*) character search support. E.g.*flooruuid*, *flooruuid, flooruuid*
                Examples: `?siteId=id1` (single id requested) `?siteId=id1&siteId=id2&siteId=id3`
                (multiple ids requested) .
            management_ip_address(basestring): managementIpAddress query parameter. The list of entity management IP
                Address. It can be either Ipv4 or Ipv6 address or combination of both(Ex. "121.1.1.10")
                This field supports wildcard (`*`) character-based search.  Ex: `*1.1*` or `1.1*` or
                `*1.1` Examples: managementIpAddresses=121.1.1.10 managementIpAddresses=121.1.1.10&manag
                ementIpAddresses=172.20.1.10&managementIpAddresses=200:10&=managementIpAddresses172.20.3
                .4 (multiple entity IP Address with & separator) .
            mac_address(basestring): macAddress query parameter. The macAddress of the network device or client This
                field supports wildcard (`*`) character-based search.  Ex: `*AB:AB:AB*` or `AB:AB:AB*`
                or `*AB:AB:AB` Examples: `macAddress=AB:AB:AB:CD:CD:CD` (single macAddress requested)
                `macAddress=AB:AB:AB:CD:CD:DC&macAddress=AB:AB:AB:CD:CD:FE` (multiple macAddress
                requested) .
            family(basestring): family query parameter. The list of network device family names
                Examples:family=Switches and Hubs (single network device family name )family=Switches
                and Hubs&family=Router&family=Wireless Controller (multiple Network device family names
                with & separator). This field is not case sensitive. .
            type(basestring): type query parameter. The list of network device type This field supports wildcard
                (`*`) character-based search. Ex: `*9407R*` or `*9407R` or
                `9407R*`Examples:type=SwitchesCisco DNA 9407R Switch (single network device types
                )type=Cisco DNA 38xx stack-able ethernet switch&type=Cisco 3945 Integrated Services
                Router G2 (multiple Network device types with & separator) .
            role(basestring): role query parameter. The list of network device role. Examples:role=CORE,
                role=CORE&role=ACCESS&role=ROUTER (multiple Network device roles with & separator). This
                field is not case sensitive. .
            serial_number(basestring): serialNumber query parameter. The list of network device serial numbers. This
                field supports wildcard (`*`) character-based search.  Ex: `*MS1SV*` or `MS1SV*` or
                `*MS1SV` Examples: serialNumber=9FUFMS1SVAX
                serialNumber=9FUFMS1SVAX&FCW2333Q0BY&FJC240617JX(multiple Network device serial number
                with & separator) .
            maintenance_mode(bool): maintenanceMode query parameter. The device maintenanceMode status true or false
                .
            software_version(basestring): softwareVersion query parameter. The list of network device software
                version This field supports wildcard (`*`) character-based search. Ex: `*17.8*` or
                `*17.8` or `17.8*` Examples: softwareVersion=2.3.4.0 (single network device software
                version ) softwareVersion=17.9.3.23&softwareVersion=17.7.1.2&softwareVersion=*.17.7
                (multiple Network device software versions with & separator) .
            health_score(basestring): healthScore query parameter. The list of entity health score categories
                Examples:healthScore=good,healthScore=good&healthScore=fair (multiple entity healthscore
                values with & separator). This field is not case sensitive. .
            view(basestring): view query parameter. The List of Network Device model views. Please refer to
                ```NetworkDeviceView``` for the supported list .
            attribute(basestring): attribute query parameter. The List of Network Device model attributes. This is
                helps to specify the interested fields in the request. .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of gets_the_total_network_device_counts_based_on_the_provided_query_parameters_v1 .
        """
        return self.gets_the_total_network_device_counts_based_on_the_provided_query_parameters_v1(
            attribute=attribute,
            end_time=end_time,
            family=family,
            health_score=health_score,
            id=id,
            mac_address=mac_address,
            maintenance_mode=maintenance_mode,
            management_ip_address=management_ip_address,
            role=role,
            serial_number=serial_number,
            site_hierarchy=site_hierarchy,
            site_hierarchy_id=site_hierarchy_id,
            site_id=site_id,
            software_version=software_version,
            start_time=start_time,
            type=type,
            view=view,
            headers=headers,
            **request_parameters
        )

    # Alias Function
    def poe_details(self, device_uuid, headers=None, **request_parameters):
        """This function is an alias of poe_details_v1 .
        Args:
            device_uuid(basestring): deviceUuid path parameter. UUID of the device .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of poe_details_v1 .
        """
        return self.poe_details_v1(
            device_uuid=device_uuid, headers=headers, **request_parameters
        )

    # Alias Function
    def get_threat_levels(self, headers=None, **request_parameters):
        """This function is an alias of get_threat_levels_v1 .
        Args:
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_threat_levels_v1 .
        """
        return self.get_threat_levels_v1(headers=headers, **request_parameters)

    # Alias Function
    def get_connected_device_detail(
        self, device_uuid, interface_uuid, headers=None, **request_parameters
    ):
        """This function is an alias of get_connected_device_detail_v1 .
        Args:
            device_uuid(basestring): deviceUuid path parameter. instanceuuid of Device .
            interface_uuid(basestring): interfaceUuid path parameter. instanceuuid of interface .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_connected_device_detail_v1 .
        """
        return self.get_connected_device_detail_v1(
            device_uuid=device_uuid,
            interface_uuid=interface_uuid,
            headers=headers,
            **request_parameters
        )

    # Alias Function
    def export_device_list(
        self,
        deviceUuids=None,
        operationEnum=None,
        parameters=None,
        password=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This function is an alias of export_device_list_v1 .
        Args:
            deviceUuids(list): Devices's List of device uuids  (list of strings).
            operationEnum(string): Devices's 0 to export Device Credential Details Or 1 to export Device Details .
                Available values are 'CREDENTIALDETAILS' and 'DEVICEDETAILS'.
            parameters(list): Devices's List of device parameters that needs to be exported to file  (list of
                strings).
            password(string): Devices's Password is required when the operationEnum value is 0  .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of export_device_list_v1 .
        """
        return self.export_device_list_v1(
            deviceUuids=deviceUuids,
            operationEnum=operationEnum,
            parameters=parameters,
            password=password,
            headers=headers,
            payload=payload,
            active_validation=active_validation,
            **request_parameters
        )

    # Alias Function
    def gets_the_total_number_network_devices_based_on_the_provided_complex_filters_and_aggregation_functions(
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
        """This function is an alias of gets_the_total_number_network_devices_based_on_the_provided_complex_filters_and_aggregation_functions_v1 .
        Args:
            aggregateAttributes(list): Devices's aggregateAttributes (list of objects).
            attributes(list): Devices's Attributes (list of strings).
            endTime(integer): Devices's End Time.
            filters(list): Devices's filters (list of objects).
            page(object): Devices's page.
            startTime(integer): Devices's Start Time.
            views(list): Devices's Views (list of strings).
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of gets_the_total_number_network_devices_based_on_the_provided_complex_filters_and_aggregation_functions_v1 .
        """
        return self.gets_the_total_number_network_devices_based_on_the_provided_complex_filters_and_aggregation_functions_v1(
            aggregateAttributes=aggregateAttributes,
            attributes=attributes,
            endTime=endTime,
            filters=filters,
            page=page,
            startTime=startTime,
            views=views,
            headers=headers,
            payload=payload,
            active_validation=active_validation,
            **request_parameters
        )

    # Alias Function
    def get_organization_list_for_meraki(self, id, headers=None, **request_parameters):
        """This function is an alias of get_organization_list_for_meraki_v1 .
        Args:
            id(basestring): id path parameter. Device Id .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_organization_list_for_meraki_v1 .
        """
        return self.get_organization_list_for_meraki_v1(
            id=id, headers=headers, **request_parameters
        )

    # Alias Function
    def get_wireless_lan_controller_details_by_id(
        self, id, headers=None, **request_parameters
    ):
        """This function is an alias of get_wireless_lan_controller_details_by_id_v1 .
        Args:
            id(basestring): id path parameter. Device ID .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_wireless_lan_controller_details_by_id_v1 .
        """
        return self.get_wireless_lan_controller_details_by_id_v1(
            id=id, headers=headers, **request_parameters
        )

    # Alias Function
    def get_all_interfaces(
        self,
        last_input_time=None,
        last_output_time=None,
        limit=None,
        offset=None,
        headers=None,
        **request_parameters
    ):
        """This function is an alias of get_all_interfaces_v1 .
        Args:
            offset(int): offset query parameter.
            limit(int): limit query parameter.
            last_input_time(basestring): lastInputTime query parameter. Last Input Time .
            last_output_time(basestring): lastOutputTime query parameter. Last Output Time .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_all_interfaces_v1 .
        """
        return self.get_all_interfaces_v1(
            last_input_time=last_input_time,
            last_output_time=last_output_time,
            limit=limit,
            offset=offset,
            headers=headers,
            **request_parameters
        )

    # Alias Function
    def update_user_defined_field(
        self,
        id,
        description=None,
        name=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This function is an alias of update_user_defined_field_v1 .
        Args:
            description(string): Devices's Description of UDF .
            name(string): Devices's Name of UDF .
            id(basestring): id path parameter. UDF id .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of update_user_defined_field_v1 .
        """
        return self.update_user_defined_field_v1(
            id=id,
            description=description,
            name=name,
            headers=headers,
            payload=payload,
            active_validation=active_validation,
            **request_parameters
        )

    # Alias Function
    def get_device_interface_stats_info(
        self,
        device_id,
        endTime=None,
        query=None,
        startTime=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This function is an alias of get_device_interface_stats_info_v2 .
        Args:
            endTime(integer): Devices's UTC epoch timestamp in milliseconds .
            query(object): Devices's query.
            startTime(integer): Devices's UTC epoch timestamp in milliseconds .
            device_id(basestring): deviceId path parameter. Network Device Id .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_device_interface_stats_info_v2 .
        """
        return self.get_device_interface_stats_info_v2(
            device_id=device_id,
            endTime=endTime,
            query=query,
            startTime=startTime,
            headers=headers,
            payload=payload,
            active_validation=active_validation,
            **request_parameters
        )

    # Alias Function
    def get_network_device_by_pagination_range(
        self, records_to_return, start_index, headers=None, **request_parameters
    ):
        """This function is an alias of get_network_device_by_pagination_range_v1 .
        Args:
            start_index(int): startIndex path parameter. Start index [>=1] .
            records_to_return(int): recordsToReturn path parameter. Number of records to return [1<= recordsToReturn
                <= 500] .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_network_device_by_pagination_range_v1 .
        """
        return self.get_network_device_by_pagination_range_v1(
            records_to_return=records_to_return,
            start_index=start_index,
            headers=headers,
            **request_parameters
        )

    # Alias Function
    def stop_wireless_rogue_ap_containment(
        self,
        macAddress=None,
        type=None,
        wlcIp=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This function is an alias of stop_wireless_rogue_ap_containment_v1 .
        Args:
            macAddress(string): Devices's Mac Address.
            type(integer): Devices's Type.
            wlcIp(string): Devices's Wlc Ip.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of stop_wireless_rogue_ap_containment_v1 .
        """
        return self.stop_wireless_rogue_ap_containment_v1(
            macAddress=macAddress,
            type=type,
            wlcIp=wlcIp,
            headers=headers,
            payload=payload,
            active_validation=active_validation,
            **request_parameters
        )

    # Alias Function
    def inventory_insight_device_link_mismatch(
        self,
        category,
        site_id,
        limit=None,
        offset=None,
        order=None,
        sort_by=None,
        headers=None,
        **request_parameters
    ):
        """This function is an alias of inventory_insight_device_link_mismatch_v1 .
        Args:
            site_id(basestring): siteId path parameter.
            offset(int): offset query parameter. Row Number.  Default value is 1 .
            limit(int): limit query parameter. Default value is 500 .
            category(basestring): category query parameter. Links mismatch category.  Value can be speed-duplex or
                vlan. .
            sort_by(basestring): sortBy query parameter. Sort By .
            order(basestring): order query parameter. Order.  Value can be asc or desc.  Default value is asc .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of inventory_insight_device_link_mismatch_v1 .
        """
        return self.inventory_insight_device_link_mismatch_v1(
            category=category,
            site_id=site_id,
            limit=limit,
            offset=offset,
            order=order,
            sort_by=sort_by,
            headers=headers,
            **request_parameters
        )

    # Alias Function
    def get_devices_registered_for_wsa_notification(
        self, macaddress=None, serial_number=None, headers=None, **request_parameters
    ):
        """This function is an alias of get_devices_registered_for_wsa_notification_v1 .
        Args:
            serial_number(basestring): serialNumber query parameter. Serial number of the device .
            macaddress(basestring): macaddress query parameter. Mac addres of the device .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_devices_registered_for_wsa_notification_v1 .
        """
        return self.get_devices_registered_for_wsa_notification_v1(
            macaddress=macaddress,
            serial_number=serial_number,
            headers=headers,
            **request_parameters
        )

    # Alias Function
    def threat_detail_count(
        self,
        endTime=None,
        isNewThreat=None,
        limit=None,
        offset=None,
        siteId=None,
        startTime=None,
        threatLevel=None,
        threatType=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This function is an alias of threat_detail_count_v1 .
        Args:
            endTime(integer): Devices's End Time.
            isNewThreat(boolean): Devices's Is New Threat.
            limit(integer): Devices's Limit.
            offset(integer): Devices's Offset.
            siteId(list): Devices's Site Id (list of strings).
            startTime(integer): Devices's Start Time.
            threatLevel(list): Devices's Threat Level (list of strings).
            threatType(list): Devices's Threat Type (list of strings).
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of threat_detail_count_v1 .
        """
        return self.threat_detail_count_v1(
            endTime=endTime,
            isNewThreat=isNewThreat,
            limit=limit,
            offset=offset,
            siteId=siteId,
            startTime=startTime,
            threatLevel=threatLevel,
            threatType=threatType,
            headers=headers,
            payload=payload,
            active_validation=active_validation,
            **request_parameters
        )

    # Alias Function
    def get_device_enrichment_details(self, headers=None, **request_parameters):
        """This function is an alias of get_device_enrichment_details_v1 .
        Args:
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_device_enrichment_details_v1 .
        """
        return self.get_device_enrichment_details_v1(
            headers=headers, **request_parameters
        )

    # Alias Function
    def get_device_by_id(self, id, headers=None, **request_parameters):
        """This function is an alias of get_device_by_id_v1 .
        Args:
            id(basestring): id path parameter. Device ID .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_device_by_id_v1 .
        """
        return self.get_device_by_id_v1(id=id, headers=headers, **request_parameters)

    # Alias Function
    def get_device_interface_vlans(
        self, id, interface_type=None, headers=None, **request_parameters
    ):
        """This function is an alias of get_device_interface_vlans_v1 .
        Args:
            id(basestring): id path parameter.
            interface_type(basestring): interfaceType query parameter. Vlan associated with sub-interface. If no
                interfaceType mentioned it will return all types of Vlan interfaces. If interfaceType is
                selected but not specified then it will take default value. .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_device_interface_vlans_v1 .
        """
        return self.get_device_interface_vlans_v1(
            id=id, interface_type=interface_type, headers=headers, **request_parameters
        )

    # Alias Function
    def gets_the_summary_analytics_data_related_to_network_devices(
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
        """This function is an alias of gets_the_summary_analytics_data_related_to_network_devices_v1 .
        Args:
            aggregateAttributes(list): Devices's aggregateAttributes (list of objects).
            attributes(list): Devices's Attributes (list of strings).
            endTime(integer): Devices's End Time.
            filters(list): Devices's filters (list of objects).
            groupBy(list): Devices's Group By (list of strings).
            page(object): Devices's page.
            startTime(integer): Devices's Start Time.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of gets_the_summary_analytics_data_related_to_network_devices_v1 .
        """
        return self.gets_the_summary_analytics_data_related_to_network_devices_v1(
            aggregateAttributes=aggregateAttributes,
            attributes=attributes,
            endTime=endTime,
            filters=filters,
            groupBy=groupBy,
            page=page,
            startTime=startTime,
            headers=headers,
            payload=payload,
            active_validation=active_validation,
            **request_parameters
        )

    # Alias Function
    def get_linecard_details(self, device_uuid, headers=None, **request_parameters):
        """This function is an alias of get_linecard_details_v1 .
        Args:
            device_uuid(basestring): deviceUuid path parameter. instanceuuid of device .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_linecard_details_v1 .
        """
        return self.get_linecard_details_v1(
            device_uuid=device_uuid, headers=headers, **request_parameters
        )

    # Alias Function
    def delete_planned_access_point_for_floor(
        self, floor_id, planned_access_point_uuid, headers=None, **request_parameters
    ):
        """This function is an alias of delete_planned_access_point_for_floor_v1 .
        Args:
            floor_id(basestring): floorId path parameter. The instance UUID of the floor hierarchy element .
            planned_access_point_uuid(basestring): plannedAccessPointUuid path parameter. The instance UUID of the
                planned access point to delete .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of delete_planned_access_point_for_floor_v1 .
        """
        return self.delete_planned_access_point_for_floor_v1(
            floor_id=floor_id,
            planned_access_point_uuid=planned_access_point_uuid,
            headers=headers,
            **request_parameters
        )

    # Alias Function
    def legit_operations_for_interface(
        self, interface_uuid, headers=None, **request_parameters
    ):
        """This function is an alias of legit_operations_for_interface_v1 .
        Args:
            interface_uuid(basestring): interfaceUuid path parameter. Interface ID .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of legit_operations_for_interface_v1 .
        """
        return self.legit_operations_for_interface_v1(
            interface_uuid=interface_uuid, headers=headers, **request_parameters
        )

    # Alias Function
    def override_resync_interval(self, headers=None, **request_parameters):
        """This function is an alias of override_resync_interval_v1 .
        Args:
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of override_resync_interval_v1 .
        """
        return self.override_resync_interval_v1(headers=headers, **request_parameters)

    # Alias Function
    def get_threat_types(self, headers=None, **request_parameters):
        """This function is an alias of get_threat_types_v1 .
        Args:
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_threat_types_v1 .
        """
        return self.get_threat_types_v1(headers=headers, **request_parameters)

    # Alias Function
    def get_modules(
        self,
        device_id,
        limit=None,
        name_list=None,
        offset=None,
        operational_state_code_list=None,
        part_number_list=None,
        vendor_equipment_type_list=None,
        headers=None,
        **request_parameters
    ):
        """This function is an alias of get_modules_v1 .
        Args:
            device_id(basestring): deviceId query parameter.
            limit(int): limit query parameter.
            offset(int): offset query parameter.
            name_list(basestring, list, set, tuple): nameList query parameter.
            vendor_equipment_type_list(basestring, list, set, tuple): vendorEquipmentTypeList query parameter.
            part_number_list(basestring, list, set, tuple): partNumberList query parameter.
            operational_state_code_list(basestring, list, set, tuple): operationalStateCodeList query parameter.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_modules_v1 .
        """
        return self.get_modules_v1(
            device_id=device_id,
            limit=limit,
            name_list=name_list,
            offset=offset,
            operational_state_code_list=operational_state_code_list,
            part_number_list=part_number_list,
            vendor_equipment_type_list=vendor_equipment_type_list,
            headers=headers,
            **request_parameters
        )

    # Alias Function
    def update_planned_access_point_for_floor(
        self,
        floor_id,
        attributes=None,
        isSensor=None,
        location=None,
        position=None,
        radioCount=None,
        radios=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This function is an alias of update_planned_access_point_for_floor_v1 .
        Args:
            attributes(object): Devices's attributes.
            isSensor(boolean): Devices's Indicates that PAP is a sensor .
            location(object): Devices's location.
            position(object): Devices's position.
            radioCount(integer): Devices's Number of radios of the planned access point .
            radios(list): Devices's radios (list of objects).
            floor_id(basestring): floorId path parameter. The instance UUID of the floor hierarchy element .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of update_planned_access_point_for_floor_v1 .
        """
        return self.update_planned_access_point_for_floor_v1(
            floor_id=floor_id,
            attributes=attributes,
            isSensor=isSensor,
            location=location,
            position=position,
            radioCount=radioCount,
            radios=radios,
            headers=headers,
            payload=payload,
            active_validation=active_validation,
            **request_parameters
        )

    # Alias Function
    def sync_devices_using_forcesync(
        self,
        force_sync=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This function is an alias of sync_devices_using_forcesync_v1 .
        Args:
            force_sync(bool): forceSync query parameter.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of sync_devices_using_forcesync_v1 .
        """
        return self.sync_devices_using_forcesync_v1(
            force_sync=force_sync,
            headers=headers,
            payload=payload,
            active_validation=active_validation,
            **request_parameters
        )

    # Alias Function
    def create_planned_access_point_for_floor(
        self,
        floor_id,
        attributes=None,
        isSensor=None,
        location=None,
        position=None,
        radioCount=None,
        radios=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This function is an alias of create_planned_access_point_for_floor_v1 .
        Args:
            attributes(object): Devices's attributes.
            isSensor(boolean): Devices's Indicates that PAP is a sensor .
            location(object): Devices's location.
            position(object): Devices's position.
            radioCount(integer): Devices's Number of radios of the planned access point .
            radios(list): Devices's radios (list of objects).
            floor_id(basestring): floorId path parameter. The instance UUID of the floor hierarchy element .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of create_planned_access_point_for_floor_v1 .
        """
        return self.create_planned_access_point_for_floor_v1(
            floor_id=floor_id,
            attributes=attributes,
            isSensor=isSensor,
            location=location,
            position=position,
            radioCount=radioCount,
            radios=radios,
            headers=headers,
            payload=payload,
            active_validation=active_validation,
            **request_parameters
        )

    # Alias Function
    def gets_the_list_of_interfaces_across_the_network_devices_based_on_the_provided_complex_filters_and_aggregation_functions(
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
        """This function is an alias of gets_the_list_of_interfaces_across_the_network_devices_based_on_the_provided_complex_filters_and_aggregation_functions_v1 .
        Args:
            aggregateAttributes(list): Devices's aggregateAttributes (list of objects).
            attributes(list): Devices's Attributes (list of strings).
            endTime(integer): Devices's End Time.
            filters(list): Devices's filters (list of objects).
            page(object): Devices's page.
            startTime(integer): Devices's Start Time.
            views(list): Devices's Views (list of strings).
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of gets_the_list_of_interfaces_across_the_network_devices_based_on_the_provided_complex_filters_and_aggregation_functions_v1 .
        """
        return self.gets_the_list_of_interfaces_across_the_network_devices_based_on_the_provided_complex_filters_and_aggregation_functions_v1(
            aggregateAttributes=aggregateAttributes,
            attributes=attributes,
            endTime=endTime,
            filters=filters,
            page=page,
            startTime=startTime,
            views=views,
            headers=headers,
            payload=payload,
            active_validation=active_validation,
            **request_parameters
        )

    # Alias Function
    def get_polling_interval_by_id(self, id, headers=None, **request_parameters):
        """This function is an alias of get_polling_interval_by_id_v1 .
        Args:
            id(basestring): id path parameter. Device ID .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_polling_interval_by_id_v1 .
        """
        return self.get_polling_interval_by_id_v1(
            id=id, headers=headers, **request_parameters
        )

    # Alias Function
    def get_the_count_of_health_score_definitions_based_on_provided_filters(
        self,
        device_type=None,
        id=None,
        include_for_overall_health=None,
        headers=None,
        **request_parameters
    ):
        """This function is an alias of get_the_count_of_health_score_definitions_based_on_provided_filters_v1 .
        Args:
            device_type(basestring): deviceType query parameter. These are the device families supported for health
                score definitions. If no input is made on device family, all device families are
                considered. .
            id(basestring): id query parameter. The definition identifier. Examples:
                id=015d9cba-4f53-4087-8317-7e49e5ffef46 (single entity id request)
                id=015d9cba-4f53-4087-8317-7e49e5ffef46&id=015d9cba-4f53-4087-8317-7e49e5ffef47
                (multiple ids in the query param) .
            include_for_overall_health(bool): includeForOverallHealth query parameter. The inclusion status of the
                issue definition, either true or false. true indicates that particular health metric is
                included in overall health computation, otherwise false. By default it's set to true. .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_the_count_of_health_score_definitions_based_on_provided_filters_v1 .
        """
        return (
            self.get_the_count_of_health_score_definitions_based_on_provided_filters_v1(
                device_type=device_type,
                id=id,
                include_for_overall_health=include_for_overall_health,
                headers=headers,
                **request_parameters
            )
        )

    # Alias Function
    def threat_summary(
        self,
        endTime=None,
        siteId=None,
        startTime=None,
        threatLevel=None,
        threatType=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This function is an alias of threat_summary_v1 .
        Args:
            endTime(integer): Devices's End Time.
            siteId(list): Devices's Site Id (list of strings).
            startTime(integer): Devices's Start Time.
            threatLevel(list): Devices's Threat Level (list of strings).
            threatType(list): Devices's Threat Type (list of strings).
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of threat_summary_v1 .
        """
        return self.threat_summary_v1(
            endTime=endTime,
            siteId=siteId,
            startTime=startTime,
            threatLevel=threatLevel,
            threatType=threatType,
            headers=headers,
            payload=payload,
            active_validation=active_validation,
            **request_parameters
        )

    # Alias Function
    def get_interface_info_by_id(self, device_id, headers=None, **request_parameters):
        """This function is an alias of get_interface_info_by_id_v1 .
        Args:
            device_id(basestring): deviceId path parameter. Device ID .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_interface_info_by_id_v1 .
        """
        return self.get_interface_info_by_id_v1(
            device_id=device_id, headers=headers, **request_parameters
        )

    # Alias Function
    def get_health_score_definition_for_the_given_id(
        self, id, headers=None, **request_parameters
    ):
        """This function is an alias of get_health_score_definition_for_the_given_id_v1 .
        Args:
            id(basestring): id path parameter. Health score definition id. .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_health_score_definition_for_the_given_id_v1 .
        """
        return self.get_health_score_definition_for_the_given_id_v1(
            id=id, headers=headers, **request_parameters
        )

    # Alias Function
    def count_the_number_of_events_with_filters(
        self,
        deviceFamily=None,
        endTime=None,
        filters=None,
        startTime=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This function is an alias of count_the_number_of_events_with_filters_v1 .
        Args:
            deviceFamily(list): Devices's Device Family (list of strings).
            endTime(integer): Devices's End Time.
            filters(list): Devices's filters (list of objects).
            startTime(integer): Devices's Start Time.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of count_the_number_of_events_with_filters_v1 .
        """
        return self.count_the_number_of_events_with_filters_v1(
            deviceFamily=deviceFamily,
            endTime=endTime,
            filters=filters,
            startTime=startTime,
            headers=headers,
            payload=payload,
            active_validation=active_validation,
            **request_parameters
        )

    # Alias Function
    def remove_user_defined_field_from_device(
        self, device_id, name, headers=None, **request_parameters
    ):
        """This function is an alias of remove_user_defined_field_from_device_v1 .
        Args:
            device_id(basestring): deviceId path parameter. UUID of device from which UDF has to be removed .
            name(basestring): name query parameter. Name of UDF to be removed .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of remove_user_defined_field_from_device_v1 .
        """
        return self.remove_user_defined_field_from_device_v1(
            device_id=device_id, name=name, headers=headers, **request_parameters
        )

    # Alias Function
    def delete_user_defined_field(self, id, headers=None, **request_parameters):
        """This function is an alias of delete_user_defined_field_v1 .
        Args:
            id(basestring): id path parameter. UDF id .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of delete_user_defined_field_v1 .
        """
        return self.delete_user_defined_field_v1(
            id=id, headers=headers, **request_parameters
        )

    # Alias Function
    def delete_device_by_id(
        self, id, clean_config=None, headers=None, **request_parameters
    ):
        """This function is an alias of delete_device_by_id_v1 .
        Args:
            id(basestring): id path parameter. Device ID .
            clean_config(bool): cleanConfig query parameter. Selecting the clean up configuration option will
                attempt to remove device settings that were configured during the addition of the device
                to the inventory and site assignment. Please note that this operation is different from
                deprovisioning. It does not remove configurations that were pushed during device
                provisioning. .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of delete_device_by_id_v1 .
        """
        return self.delete_device_by_id_v1(
            id=id, clean_config=clean_config, headers=headers, **request_parameters
        )

    # Alias Function
    def update_global_resync_interval(
        self,
        interval=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This function is an alias of update_global_resync_interval_v1 .
        Args:
            interval(integer): Devices's Resync Interval should be between 25 to 1440 minutes .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of update_global_resync_interval_v1 .
        """
        return self.update_global_resync_interval_v1(
            interval=interval,
            headers=headers,
            payload=payload,
            active_validation=active_validation,
            **request_parameters
        )

    # Alias Function
    def get_module_info_by_id(self, id, headers=None, **request_parameters):
        """This function is an alias of get_module_info_by_id_v1 .
        Args:
            id(basestring): id path parameter. Module id .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_module_info_by_id_v1 .
        """
        return self.get_module_info_by_id_v1(
            id=id, headers=headers, **request_parameters
        )

    # Alias Function
    def get_device_list(
        self,
        associated_wlc_ip=None,
        collection_interval=None,
        collection_status=None,
        device_support_level=None,
        error_code=None,
        error_description=None,
        family=None,
        hostname=None,
        id=None,
        license_name=None,
        license_status=None,
        license_type=None,
        limit=None,
        location=None,
        location_name=None,
        mac_address=None,
        management_ip_address=None,
        module_equpimenttype=None,
        module_name=None,
        module_operationstatecode=None,
        module_partnumber=None,
        module_servicestate=None,
        module_vendorequipmenttype=None,
        not_synced_for_minutes=None,
        offset=None,
        platform_id=None,
        reachability_status=None,
        role=None,
        serial_number=None,
        series=None,
        software_type=None,
        software_version=None,
        type=None,
        up_time=None,
        headers=None,
        **request_parameters
    ):
        """This function is an alias of get_device_list_v1 .
        Args:
            hostname(basestring, list, set, tuple): hostname query parameter.
            management_ip_address(basestring, list, set, tuple): managementIpAddress query parameter.
            mac_address(basestring, list, set, tuple): macAddress query parameter.
            location_name(basestring, list, set, tuple): locationName query parameter.
            serial_number(basestring, list, set, tuple): serialNumber query parameter.
            location(basestring, list, set, tuple): location query parameter.
            family(basestring, list, set, tuple): family query parameter.
            type(basestring, list, set, tuple): type query parameter.
            series(basestring, list, set, tuple): series query parameter.
            collection_status(basestring, list, set, tuple): collectionStatus query parameter.
            collection_interval(basestring, list, set, tuple): collectionInterval query parameter.
            not_synced_for_minutes(basestring, list, set, tuple): notSyncedForMinutes query parameter.
            error_code(basestring, list, set, tuple): errorCode query parameter.
            error_description(basestring, list, set, tuple): errorDescription query parameter.
            software_version(basestring, list, set, tuple): softwareVersion query parameter.
            software_type(basestring, list, set, tuple): softwareType query parameter.
            platform_id(basestring, list, set, tuple): platformId query parameter.
            role(basestring, list, set, tuple): role query parameter.
            reachability_status(basestring, list, set, tuple): reachabilityStatus query parameter.
            up_time(basestring, list, set, tuple): upTime query parameter.
            associated_wlc_ip(basestring, list, set, tuple): associatedWlcIp query parameter.
            license_name(basestring, list, set, tuple): license.name query parameter.
            license_type(basestring, list, set, tuple): license.type query parameter.
            license_status(basestring, list, set, tuple): license.status query parameter.
            module_name(basestring, list, set, tuple): module+name query parameter.
            module_equpimenttype(basestring, list, set, tuple): module+equpimenttype query parameter.
            module_servicestate(basestring, list, set, tuple): module+servicestate query parameter.
            module_vendorequipmenttype(basestring, list, set, tuple): module+vendorequipmenttype query parameter.
            module_partnumber(basestring, list, set, tuple): module+partnumber query parameter.
            module_operationstatecode(basestring, list, set, tuple): module+operationstatecode query parameter.
            id(basestring): id query parameter. Accepts comma separated ids and return list of network-devices for
                the given ids. If invalid or not-found ids are provided, null entry will be returned in
                the list. .
            device_support_level(basestring): deviceSupportLevel query parameter.
            offset(int): offset query parameter. offset >= 1 [X gives results from Xth device onwards] .
            limit(int): limit query parameter. 1 <= limit <= 500 [max. no. of devices to be returned in the result]
                .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_device_list_v1 .
        """
        return self.get_device_list_v1(
            associated_wlc_ip=associated_wlc_ip,
            collection_interval=collection_interval,
            collection_status=collection_status,
            device_support_level=device_support_level,
            error_code=error_code,
            error_description=error_description,
            family=family,
            hostname=hostname,
            id=id,
            license_name=license_name,
            license_status=license_status,
            license_type=license_type,
            limit=limit,
            location=location,
            location_name=location_name,
            mac_address=mac_address,
            management_ip_address=management_ip_address,
            module_equpimenttype=module_equpimenttype,
            module_name=module_name,
            module_operationstatecode=module_operationstatecode,
            module_partnumber=module_partnumber,
            module_servicestate=module_servicestate,
            module_vendorequipmenttype=module_vendorequipmenttype,
            not_synced_for_minutes=not_synced_for_minutes,
            offset=offset,
            platform_id=platform_id,
            reachability_status=reachability_status,
            role=role,
            serial_number=serial_number,
            series=series,
            software_type=software_type,
            software_version=software_version,
            type=type,
            up_time=up_time,
            headers=headers,
            **request_parameters
        )

    # Alias Function
    def gets_the_total_network_device_interface_counts(
        self,
        end_time=None,
        interface_id=None,
        interface_name=None,
        network_device_id=None,
        network_device_ip_address=None,
        network_device_mac_address=None,
        site_hierarchy=None,
        site_hierarchy_id=None,
        site_id=None,
        start_time=None,
        headers=None,
        **request_parameters
    ):
        """This function is an alias of gets_the_total_network_device_interface_counts_v1 .
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
            site_id(basestring): siteId query parameter. The UUID of the site. (Ex. `flooruuid`) Examples:
                `?siteId=id1` (single id requested) `?siteId=id1&siteId=id2&siteId=id3` (multiple ids
                requested) .
            network_device_id(basestring): networkDeviceId query parameter. The list of Network Device Uuids. (Ex.
                `6bef213c-19ca-4170-8375-b694e251101c`) Examples:
                `networkDeviceId=6bef213c-19ca-4170-8375-b694e251101c` (single networkDeviceId
                requested) `networkDeviceId=6bef213c-19ca-4170-8375-
                b694e251101c&networkDeviceId=32219612-819e-4b5e-a96b-
                cf22aca13dd9&networkDeviceId=2541e9a7-b80d-4955-8aa2-79b233318ba0` (multiple
                networkDeviceIds with & separator) .
            network_device_ip_address(basestring): networkDeviceIpAddress query parameter. The list of Network
                Device management IP Address. (Ex. `121.1.1.10`) This field supports wildcard (`*`)
                character-based search.  Ex: `*1.1*` or `1.1*` or `*1.1` Examples:
                `networkDeviceIpAddress=121.1.1.10` `networkDeviceIpAddress=121.1.1.10&networkDeviceIpAd
                dress=172.20.1.10&networkDeviceIpAddress=10.10.20.10` (multiple networkDevice IP Address
                with & separator) .
            network_device_mac_address(basestring): networkDeviceMacAddress query parameter. The list of Network
                Device MAC Address. (Ex. `64:f6:9d:07:9a:00`) This field supports wildcard (`*`)
                character-based search.  Ex: `*AB:AB:AB*` or `AB:AB:AB*` or `*AB:AB:AB` Examples:
                `networkDeviceMacAddress=64:f6:9d:07:9a:00`
                `networkDeviceMacAddress=64:f6:9d:07:9a:00&networkDeviceMacAddress=70:56:9d:07:ac:77`
                (multiple networkDevice MAC addresses with & separator) .
            interface_id(basestring): interfaceId query parameter. The list of Interface Uuids. (Ex.
                `6bef213c-19ca-4170-8375-b694e251101c`) Examples:
                `interfaceId=6bef213c-19ca-4170-8375-b694e251101c` (single interface uuid ) `interfaceId
                =6bef213c-19ca-4170-8375-b694e251101c&32219612-819e-4b5e-a96b-cf22aca13dd9&2541e9a7-
                b80d-4955-8aa2-79b233318ba0` (multiple Interface uuid with & separator) .
            interface_name(basestring): interfaceName query parameter. The list of Interface name (Ex.
                `GigabitEthernet1/0/1`) This field supports wildcard (`*`) character-based search.  Ex:
                `*1/0/1*` or `1/0/1*` or `*1/0/1` Examples: `interfaceNames=GigabitEthernet1/0/1`
                (single interface name)
                `interfaceNames=GigabitEthernet1/0/1&GigabitEthernet2/0/1&GigabitEthernet3/0/1`
                (multiple interface names with & separator) .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of gets_the_total_network_device_interface_counts_v1 .
        """
        return self.gets_the_total_network_device_interface_counts_v1(
            end_time=end_time,
            interface_id=interface_id,
            interface_name=interface_name,
            network_device_id=network_device_id,
            network_device_ip_address=network_device_ip_address,
            network_device_mac_address=network_device_mac_address,
            site_hierarchy=site_hierarchy,
            site_hierarchy_id=site_hierarchy_id,
            site_id=site_id,
            start_time=start_time,
            headers=headers,
            **request_parameters
        )

    # Alias Function
    def add_device(
        self,
        cliTransport=None,
        computeDevice=None,
        enablePassword=None,
        extendedDiscoveryInfo=None,
        httpPassword=None,
        httpPort=None,
        httpSecure=None,
        httpUserName=None,
        ipAddress=None,
        merakiOrgId=None,
        netconfPort=None,
        password=None,
        serialNumber=None,
        snmpAuthPassphrase=None,
        snmpAuthProtocol=None,
        snmpMode=None,
        snmpPrivPassphrase=None,
        snmpPrivProtocol=None,
        snmpROCommunity=None,
        snmpRWCommunity=None,
        snmpRetry=None,
        snmpTimeout=None,
        snmpUserName=None,
        snmpVersion=None,
        type=None,
        userName=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This function is an alias of add_device_v1 .
        Args:
            cliTransport(string): Devices's CLI transport. Supported values: telnet, ssh. Required if type is
                NETWORK_DEVICE. .
            computeDevice(boolean): Devices's Compute Device or not. Options are true / false. .
            enablePassword(string): Devices's CLI enable password of the device. Required if device is configured to
                use enable password. .
            extendedDiscoveryInfo(string): Devices's This field holds that info as whether to add device with canned
                data or not. Supported values: DISCOVER_WITH_CANNED_DATA. .
            httpPassword(string): Devices's HTTP password of the device / API key for Meraki Dashboard. Required if
                type is MERAKI_DASHBOARD or COMPUTE_DEVICE. .
            httpPort(string): Devices's HTTP port of the device. Required if type is COMPUTE_DEVICE. .
            httpSecure(boolean): Devices's Flag to select HTTP / HTTPS protocol. Options are true / false. true for
                HTTPS and false for HTTP. Default is true. .
            httpUserName(string): Devices's HTTP Username of the device. Required if type is COMPUTE_DEVICE. .
            ipAddress(list): Devices's IP Address of the device. Required if type is NETWORK_DEVICE, COMPUTE_DEVICE
                or THIRD_PARTY_DEVICE.  (list of strings).
            merakiOrgId(list): Devices's Selected Meraki organization for which the devices needs to be imported.
                Required if type is MERAKI_DASHBOARD.  (list of strings).
            netconfPort(string): Devices's Netconf Port of the device. cliTransport must be 'ssh' if netconf is
                provided. .
            password(string): Devices's CLI Password of the device. Required if type is NETWORK_DEVICE. .
            serialNumber(string): Devices's Serial Number of the Device. Required if extendedDiscoveryInfo is
                'DISCOVER_WITH_CANNED_DATA'. .
            snmpAuthPassphrase(string): Devices's SNMPv3 auth passphrase of the device. Required if snmpMode is
                authNoPriv or authPriv. .
            snmpAuthProtocol(string): Devices's SNMPv3 auth protocol. Supported values: sha, md5. Required if
                snmpMode is authNoPriv or authPriv. .
            snmpMode(string): Devices's SNMPv3 mode. Supported values: noAuthnoPriv, authNoPriv, authPriv. Required
                if snmpVersion is v3. .
            snmpPrivPassphrase(string): Devices's SNMPv3 priv passphrase. Required if snmpMode is authPriv. .
            snmpPrivProtocol(string): Devices's SNMPv3 priv protocol. Supported values: AES128. Required if snmpMode
                is authPriv. .
            snmpROCommunity(string): Devices's SNMP Read Community of the device. If snmpVersion is v2, at least one
                of snmpROCommunity and snmpRWCommunity is required. .
            snmpRWCommunity(string): Devices's SNMP Write Community of the device. If snmpVersion is v2, at least
                one of snmpROCommunity and snmpRWCommunity is required. .
            snmpRetry(integer): Devices's SNMP retry count. Max value supported is 3. Default is Global SNMP retry
                (if exists) or 3. .
            snmpTimeout(integer): Devices's SNMP timeout in seconds. Max value supported is 300. Default is Global
                SNMP timeout (if exists) or 5. .
            snmpUserName(string): Devices's SNMPV3 user name of the device. Required if snmpVersion is v3. .
            snmpVersion(string): Devices's SNMP version. Values supported: v2, v3. Required if type is
                NETWORK_DEVICE, COMPUTE_DEVICE or THIRD_PARTY_DEVICE. .
            type(string): Devices's Type of device being added. Default is NETWORK_DEVICE. . Available values are
                'COMPUTE_DEVICE', 'MERAKI_DASHBOARD', 'THIRD_PARTY_DEVICE' and 'NETWORK_DEVICE'.
            userName(string): Devices's CLI user name of the device. Required if type is NETWORK_DEVICE. .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of add_device_v1 .
        """
        return self.add_device_v1(
            cliTransport=cliTransport,
            computeDevice=computeDevice,
            enablePassword=enablePassword,
            extendedDiscoveryInfo=extendedDiscoveryInfo,
            httpPassword=httpPassword,
            httpPort=httpPort,
            httpSecure=httpSecure,
            httpUserName=httpUserName,
            ipAddress=ipAddress,
            merakiOrgId=merakiOrgId,
            netconfPort=netconfPort,
            password=password,
            serialNumber=serialNumber,
            snmpAuthPassphrase=snmpAuthPassphrase,
            snmpAuthProtocol=snmpAuthProtocol,
            snmpMode=snmpMode,
            snmpPrivPassphrase=snmpPrivPassphrase,
            snmpPrivProtocol=snmpPrivProtocol,
            snmpROCommunity=snmpROCommunity,
            snmpRWCommunity=snmpRWCommunity,
            snmpRetry=snmpRetry,
            snmpTimeout=snmpTimeout,
            snmpUserName=snmpUserName,
            snmpVersion=snmpVersion,
            type=type,
            userName=userName,
            headers=headers,
            payload=payload,
            active_validation=active_validation,
            **request_parameters
        )

    # Alias Function
    def update_resync_interval_for_the_network_device(
        self,
        id,
        interval=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This function is an alias of update_resync_interval_for_the_network_device_v1 .
        Args:
            interval(integer): Devices's Resync interval in minutes. To disable periodic resync, set interval as
                `0`. To use global settings, set interval as `null`. .
            id(basestring): id path parameter. The id of the network device. .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of update_resync_interval_for_the_network_device_v1 .
        """
        return self.update_resync_interval_for_the_network_device_v1(
            id=id,
            interval=interval,
            headers=headers,
            payload=payload,
            active_validation=active_validation,
            **request_parameters
        )

    # Alias Function
    def the_trend_analytics_data_for_the_network_device_in_the_specified_time_range(
        self,
        id,
        aggregateAttributes=None,
        attributes=None,
        endTime=None,
        filters=None,
        groupBy=None,
        page=None,
        startTime=None,
        trendIntervalInMinutes=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This function is an alias of the_trend_analytics_data_for_the_network_device_in_the_specified_time_range_v1 .
        Args:
            aggregateAttributes(list): Devices's aggregateAttributes (list of objects).
            attributes(list): Devices's Attributes (list of strings).
            endTime(integer): Devices's End Time.
            filters(list): Devices's filters (list of objects).
            groupBy(list): Devices's Group By (list of strings).
            page(object): Devices's page.
            startTime(integer): Devices's Start Time.
            trendIntervalInMinutes(integer): Devices's Trend Interval In Minutes.
            id(basestring): id path parameter. The device Uuid .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of the_trend_analytics_data_for_the_network_device_in_the_specified_time_range_v1 .
        """
        return self.the_trend_analytics_data_for_the_network_device_in_the_specified_time_range_v1(
            id=id,
            aggregateAttributes=aggregateAttributes,
            attributes=attributes,
            endTime=endTime,
            filters=filters,
            groupBy=groupBy,
            page=page,
            startTime=startTime,
            trendIntervalInMinutes=trendIntervalInMinutes,
            headers=headers,
            payload=payload,
            active_validation=active_validation,
            **request_parameters
        )

    # Alias Function
    def get_isis_interfaces(self, headers=None, **request_parameters):
        """This function is an alias of get_isis_interfaces_v1 .
        Args:
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_isis_interfaces_v1 .
        """
        return self.get_isis_interfaces_v1(headers=headers, **request_parameters)

    # Alias Function
    def get_device_by_serial_number(
        self, serial_number, headers=None, **request_parameters
    ):
        """This function is an alias of get_device_by_serial_number_v1 .
        Args:
            serial_number(basestring): serialNumber path parameter. Device serial number .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_device_by_serial_number_v1 .
        """
        return self.get_device_by_serial_number_v1(
            serial_number=serial_number, headers=headers, **request_parameters
        )

    # Alias Function
    def get_device_config_count(self, headers=None, **request_parameters):
        """This function is an alias of get_device_config_count_v1 .
        Args:
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_device_config_count_v1 .
        """
        return self.get_device_config_count_v1(headers=headers, **request_parameters)

    # Alias Function
    def get_chassis_details_for_device(
        self, device_id, headers=None, **request_parameters
    ):
        """This function is an alias of get_chassis_details_for_device_v1 .
        Args:
            device_id(basestring): deviceId path parameter. Device ID .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_chassis_details_for_device_v1 .
        """
        return self.get_chassis_details_for_device_v1(
            device_id=device_id, headers=headers, **request_parameters
        )

    # Alias Function
    def get_device_config_by_id(
        self, network_device_id, headers=None, **request_parameters
    ):
        """This function is an alias of get_device_config_by_id_v1 .
        Args:
            network_device_id(basestring): networkDeviceId path parameter.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_device_config_by_id_v1 .
        """
        return self.get_device_config_by_id_v1(
            network_device_id=network_device_id, headers=headers, **request_parameters
        )

    # Alias Function
    def rogue_additional_details(
        self,
        endTime=None,
        limit=None,
        offset=None,
        siteId=None,
        startTime=None,
        threatLevel=None,
        threatType=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This function is an alias of rogue_additional_details_v1 .
        Args:
            endTime(number): Devices's This is the epoch end time in milliseconds upto which data need to be
                fetched. Default value is current time .
            limit(number): Devices's The maximum number of entries to return. Default value is 1000 .
            offset(number): Devices's The offset of the first item in the collection to return. Default value is 1 .
            siteId(list): Devices's Filter Rogues by location. Site IDs information can be fetched from "Get Site"
                API  (list of strings).
            startTime(number): Devices's This is the epoch start time in milliseconds from which data need to be
                fetched. Default value is 24 hours earlier to endTime .
            threatLevel(list): Devices's Filter Rogues by Threat Level. Threat Level information can be fetched from
                "Get Threat Levels" API  (list of strings).
            threatType(list): Devices's Filter Rogues by Threat Type. Threat Type information can be fetched from
                "Get Threat Types" API  (list of strings).
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of rogue_additional_details_v1 .
        """
        return self.rogue_additional_details_v1(
            endTime=endTime,
            limit=limit,
            offset=offset,
            siteId=siteId,
            startTime=startTime,
            threatLevel=threatLevel,
            threatType=threatType,
            headers=headers,
            payload=payload,
            active_validation=active_validation,
            **request_parameters
        )

    # Alias Function
    def get_all_health_score_definitions_for_given_filters(
        self,
        attribute=None,
        device_type=None,
        id=None,
        include_for_overall_health=None,
        limit=None,
        offset=None,
        headers=None,
        **request_parameters
    ):
        """This function is an alias of get_all_health_score_definitions_for_given_filters_v1 .
        Args:
            device_type(basestring): deviceType query parameter. These are the device families supported for health
                score definitions. If no input is made on device family, all device families are
                considered. .
            id(basestring): id query parameter. The definition identifier. Examples:
                id=015d9cba-4f53-4087-8317-7e49e5ffef46 (single entity id request)
                id=015d9cba-4f53-4087-8317-7e49e5ffef46&id=015d9cba-4f53-4087-8317-7e49e5ffef47
                (multiple ids in the query param) .
            include_for_overall_health(bool): includeForOverallHealth query parameter. The inclusion status of the
                issue definition, either true or false. true indicates that particular health metric is
                included in overall health computation, otherwise false. By default it's set to true.  .
            attribute(basestring): attribute query parameter. These are the attributes supported in health score
                definitions response. By default, all properties are sent in response. .
            offset(int): offset query parameter. Specifies the starting point within all records returned by the
                API. It's one based offset. The starting value is 1. .
            limit(int): limit query parameter. Maximum number of records to return .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_all_health_score_definitions_for_given_filters_v1 .
        """
        return self.get_all_health_score_definitions_for_given_filters_v1(
            attribute=attribute,
            device_type=device_type,
            id=id,
            include_for_overall_health=include_for_overall_health,
            limit=limit,
            offset=offset,
            headers=headers,
            **request_parameters
        )

    # Alias Function
    def get_planned_access_points_for_building(
        self,
        building_id,
        limit=None,
        offset=None,
        radios=None,
        headers=None,
        **request_parameters
    ):
        """This function is an alias of get_planned_access_points_for_building_v1 .
        Args:
            building_id(basestring): buildingId path parameter. The instance UUID of the building hierarchy element
                .
            limit(int): limit query parameter. The page size limit for the response, e.g. limit=100 will return a
                maximum of 100 records .
            offset(int): offset query parameter. The page offset for the response. E.g. if limit=100, offset=0 will
                return first 100 records, offset=1 will return next 100 records, etc. .
            radios(bool): radios query parameter. Whether to include the planned radio details of the planned access
                points .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_planned_access_points_for_building_v1 .
        """
        return self.get_planned_access_points_for_building_v1(
            building_id=building_id,
            limit=limit,
            offset=offset,
            radios=radios,
            headers=headers,
            **request_parameters
        )

    # Alias Function
    def remove_allowed_mac_address(
        self, mac_address, headers=None, **request_parameters
    ):
        """This function is an alias of remove_allowed_mac_address_v1 .
        Args:
            mac_address(basestring): macAddress path parameter. Threat mac address which needs to be removed from
                the allowed list. Multiple mac addresses will be removed if provided as comma separated
                values (example: 00:2A:10:51:22:43,00:2A:10:51:22:44). Note: In one request, maximum 100
                mac addresses can be removed.  .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of remove_allowed_mac_address_v1 .
        """
        return self.remove_allowed_mac_address_v1(
            mac_address=mac_address, headers=headers, **request_parameters
        )

    # Alias Function
    def devices(
        self,
        device_role=None,
        end_time=None,
        health=None,
        limit=None,
        offset=None,
        site_id=None,
        start_time=None,
        headers=None,
        **request_parameters
    ):
        """This function is an alias of devices_v1 .
        Args:
            device_role(basestring): deviceRole query parameter. CORE, ACCESS, DISTRIBUTION, ROUTER, WLC, or AP
                (case insensitive) .
            site_id(basestring): siteId query parameter. DNAC site UUID .
            health(basestring): health query parameter. DNAC health catagory: POOR, FAIR, or GOOD (case insensitive)
                .
            start_time(int): startTime query parameter. UTC epoch time in milliseconds .
            end_time(int): endTime query parameter. UTC epoch time in milliseconds .
            limit(int): limit query parameter. Max number of device entries in the response (default to 50. Max at
                500) .
            offset(int): offset query parameter. The offset of the first device in the returned data (Mutiple of
                'limit' + 1) .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of devices_v1 .
        """
        return self.devices_v1(
            device_role=device_role,
            end_time=end_time,
            health=health,
            limit=limit,
            offset=offset,
            site_id=site_id,
            start_time=start_time,
            headers=headers,
            **request_parameters
        )

    # Alias Function
    def update_device_role(
        self,
        id=None,
        role=None,
        roleSource=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This function is an alias of update_device_role_v1 .
        Args:
            id(string): Devices's DeviceId of the Device .
            role(string): Devices's Role of device as ACCESS, CORE, DISTRIBUTION, BORDER ROUTER .
            roleSource(string): Devices's Role source as MANUAL / AUTO .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of update_device_role_v1 .
        """
        return self.update_device_role_v1(
            id=id,
            role=role,
            roleSource=roleSource,
            headers=headers,
            payload=payload,
            active_validation=active_validation,
            **request_parameters
        )

    # Alias Function
    def gets_the_network_device_details_based_on_the_provided_query_parameters(
        self,
        attribute=None,
        end_time=None,
        family=None,
        health_score=None,
        id=None,
        limit=None,
        mac_address=None,
        maintenance_mode=None,
        management_ip_address=None,
        offset=None,
        order=None,
        role=None,
        serial_number=None,
        site_hierarchy=None,
        site_hierarchy_id=None,
        site_id=None,
        software_version=None,
        sort_by=None,
        start_time=None,
        type=None,
        view=None,
        headers=None,
        **request_parameters
    ):
        """This function is an alias of gets_the_network_device_details_based_on_the_provided_query_parameters_v1 .
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
                supports wildcard asterisk (*) character search support. E.g. */San*, */San, /San*
                Examples: `?siteHierarchy=Global/AreaName/BuildingName/FloorName` (single siteHierarchy
                requested) `?siteHierarchy=Global/AreaName/BuildingName/FloorName&siteHierarchy=Global/A
                reaName2/BuildingName2/FloorName2` (multiple siteHierarchies requested) .
            site_hierarchy_id(basestring): siteHierarchyId query parameter. The full hierarchy breakdown of the site
                tree in id form starting from Global site UUID and ending with the specific site UUID.
                (Ex. `globalUuid/areaUuid/buildingUuid/floorUuid`) This field supports wildcard asterisk
                (*) character search support. E.g. `*uuid*, *uuid, uuid* Examples:
                `?siteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid `(single siteHierarchyId
                requested) `?siteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid&siteHierarchyId=
                globalUuid/areaUuid2/buildingUuid2/floorUuid2` (multiple siteHierarchyIds requested) .
            site_id(basestring): siteId query parameter. The UUID of the site. (Ex. `flooruuid`) This field supports
                wildcard asterisk (*) character search support. E.g.*flooruuid*, *flooruuid, flooruuid*
                Examples: `?siteId=id1` (single id requested) `?siteId=id1&siteId=id2&siteId=id3`
                (multiple ids requested) .
            id(basestring): id query parameter. The list of entity Uuids.
                (Ex."6bef213c-19ca-4170-8375-b694e251101c") Examples:
                id=6bef213c-19ca-4170-8375-b694e251101c (single entity uuid requested) id=6bef213c-19ca-
                4170-8375-b694e251101c&id=32219612-819e-4b5e-a96b-cf22aca13dd9&id=2541e9a7-b80d-4955-
                8aa2-79b233318ba0 (multiple entity uuid with '&' separator) .
            management_ip_address(basestring): managementIpAddress query parameter. The list of entity management IP
                Address. It can be either Ipv4 or Ipv6 address or combination of both(Ex. "121.1.1.10")
                This field supports wildcard (`*`) character-based search.  Ex: `*1.1*` or `1.1*` or
                `*1.1` Examples: managementIpAddresses=121.1.1.10 managementIpAddresses=121.1.1.10&manag
                ementIpAddresses=172.20.1.10&managementIpAddresses=200:10&=managementIpAddresses172.20.3
                .4 (multiple entity IP Address with & separator) .
            mac_address(basestring): macAddress query parameter. The macAddress of the network device or client This
                field supports wildcard (`*`) character-based search.  Ex: `*AB:AB:AB*` or `AB:AB:AB*`
                or `*AB:AB:AB` Examples: `macAddress=AB:AB:AB:CD:CD:CD` (single macAddress requested)
                `macAddress=AB:AB:AB:CD:CD:DC&macAddress=AB:AB:AB:CD:CD:FE` (multiple macAddress
                requested) .
            family(basestring): family query parameter. The list of network device family names
                Examples:family=Switches and Hubs (single network device family name )family=Switches
                and Hubs&family=Router&family=Wireless Controller (multiple Network device family names
                with & separator). This field is not case sensitive. .
            type(basestring): type query parameter. The list of network device type This field supports wildcard
                (`*`) character-based search. Ex: `*9407R*` or `*9407R` or `9407R*` Examples:
                type=SwitchesCisco DNA 9407R Switch (single network device types ) type=Cisco
                DNA 38xx stack-able ethernet switch&type=Cisco 3945 Integrated Services Router G2
                (multiple Network device types with & separator) .
            role(basestring): role query parameter. The list of network device role. Examples:role=CORE,
                role=CORE&role=ACCESS&role=ROUTER (multiple Network device roles with & separator). This
                field is not case sensitive. .
            serial_number(basestring): serialNumber query parameter. The list of network device serial numbers. This
                field supports wildcard (`*`) character-based search.  Ex: `*MS1SV*` or `MS1SV*` or
                `*MS1SV` Examples: serialNumber=9FUFMS1SVAX
                serialNumber=9FUFMS1SVAX&FCW2333Q0BY&FJC240617JX(multiple Network device serial number
                with & separator) .
            maintenance_mode(bool): maintenanceMode query parameter. The device maintenanceMode status true or false
                .
            software_version(basestring): softwareVersion query parameter. The list of network device software
                version This field supports wildcard (`*`) character-based search. Ex: `*17.8*` or
                `*17.8` or `17.8*` Examples: softwareVersion=2.3.4.0 (single network device software
                version ) softwareVersion=17.9.3.23&softwareVersion=17.7.1.2&softwareVersion=*.17.7
                (multiple Network device software versions with & separator) .
            health_score(basestring): healthScore query parameter. The list of entity health score categories
                Examples: healthScore=good, healthScore=good&healthScore=fair (multiple entity
                healthscore values with & separator). This field is not case sensitive. .
            view(basestring): view query parameter. The List of Network Device model views. Please refer to
                ```NetworkDeviceView``` for the supported list .
            attribute(basestring): attribute query parameter. The List of Network Device model attributes. This is
                helps to specify the interested fields in the request. .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of gets_the_network_device_details_based_on_the_provided_query_parameters_v1 .
        """
        return self.gets_the_network_device_details_based_on_the_provided_query_parameters_v1(
            attribute=attribute,
            end_time=end_time,
            family=family,
            health_score=health_score,
            id=id,
            limit=limit,
            mac_address=mac_address,
            maintenance_mode=maintenance_mode,
            management_ip_address=management_ip_address,
            offset=offset,
            order=order,
            role=role,
            serial_number=serial_number,
            site_hierarchy=site_hierarchy,
            site_hierarchy_id=site_hierarchy_id,
            site_id=site_id,
            software_version=software_version,
            sort_by=sort_by,
            start_time=start_time,
            type=type,
            view=view,
            headers=headers,
            **request_parameters
        )

    # Alias Function
    def get_device_interface_count(self, headers=None, **request_parameters):
        """This function is an alias of get_device_interface_count_v1 .
        Args:
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_device_interface_count_v1 .
        """
        return self.get_device_interface_count_v1(headers=headers, **request_parameters)

    # Alias Function
    def get_resync_interval_for_the_network_device(
        self, id, headers=None, **request_parameters
    ):
        """This function is an alias of get_resync_interval_for_the_network_device_v1 .
        Args:
            id(basestring): id path parameter. The id of the network device. .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_resync_interval_for_the_network_device_v1 .
        """
        return self.get_resync_interval_for_the_network_device_v1(
            id=id, headers=headers, **request_parameters
        )

    # Alias Function
    def get_all_user_defined_fields(
        self, id=None, name=None, headers=None, **request_parameters
    ):
        """This function is an alias of get_all_user_defined_fields_v1 .
        Args:
            id(basestring): id query parameter. Comma-seperated id(s) used for search/filtering .
            name(basestring): name query parameter. Comma-seperated name(s) used for search/filtering .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_all_user_defined_fields_v1 .
        """
        return self.get_all_user_defined_fields_v1(
            id=id, name=name, headers=headers, **request_parameters
        )

    # Alias Function
    def gets_the_list_of_network_devices_based_on_the_provided_complex_filters_and_aggregation_functions(
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
        """This function is an alias of gets_the_list_of_network_devices_based_on_the_provided_complex_filters_and_aggregation_functions_v1 .
        Args:
            aggregateAttributes(list): Devices's aggregateAttributes (list of objects).
            attributes(list): Devices's Attributes (list of strings).
            endTime(integer): Devices's End Time.
            filters(list): Devices's filters (list of objects).
            page(object): Devices's page.
            startTime(integer): Devices's Start Time.
            views(list): Devices's Views (list of strings).
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of gets_the_list_of_network_devices_based_on_the_provided_complex_filters_and_aggregation_functions_v1 .
        """
        return self.gets_the_list_of_network_devices_based_on_the_provided_complex_filters_and_aggregation_functions_v1(
            aggregateAttributes=aggregateAttributes,
            attributes=attributes,
            endTime=endTime,
            filters=filters,
            page=page,
            startTime=startTime,
            views=views,
            headers=headers,
            payload=payload,
            active_validation=active_validation,
            **request_parameters
        )

    # Alias Function
    def get_device_values_that_match_fully_or_partially_an_attribute(
        self,
        associated_wlc_ip=None,
        collection_interval=None,
        collection_status=None,
        error_code=None,
        family=None,
        hostname=None,
        limit=None,
        mac_address=None,
        management_ip_address=None,
        offset=None,
        platform_id=None,
        reachability_failure_reason=None,
        reachability_status=None,
        role=None,
        role_source=None,
        serial_number=None,
        series=None,
        software_type=None,
        software_version=None,
        type=None,
        up_time=None,
        vrf_name=None,
        headers=None,
        **request_parameters
    ):
        """This function is an alias of get_device_values_that_match_fully_or_partially_an_attribute_v1 .
        Args:
            vrf_name(basestring): vrfName query parameter.
            management_ip_address(basestring): managementIpAddress query parameter.
            hostname(basestring): hostname query parameter.
            mac_address(basestring): macAddress query parameter.
            family(basestring): family query parameter.
            collection_status(basestring): collectionStatus query parameter.
            collection_interval(basestring): collectionInterval query parameter.
            software_version(basestring): softwareVersion query parameter.
            software_type(basestring): softwareType query parameter.
            reachability_status(basestring): reachabilityStatus query parameter.
            reachability_failure_reason(basestring): reachabilityFailureReason query parameter.
            error_code(basestring): errorCode query parameter.
            platform_id(basestring): platformId query parameter.
            series(basestring): series query parameter.
            type(basestring): type query parameter.
            serial_number(basestring): serialNumber query parameter.
            up_time(basestring): upTime query parameter.
            role(basestring): role query parameter.
            role_source(basestring): roleSource query parameter.
            associated_wlc_ip(basestring): associatedWlcIp query parameter.
            offset(int): offset query parameter.
            limit(int): limit query parameter.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_device_values_that_match_fully_or_partially_an_attribute_v1 .
        """
        return self.get_device_values_that_match_fully_or_partially_an_attribute_v1(
            associated_wlc_ip=associated_wlc_ip,
            collection_interval=collection_interval,
            collection_status=collection_status,
            error_code=error_code,
            family=family,
            hostname=hostname,
            limit=limit,
            mac_address=mac_address,
            management_ip_address=management_ip_address,
            offset=offset,
            platform_id=platform_id,
            reachability_failure_reason=reachability_failure_reason,
            reachability_status=reachability_status,
            role=role,
            role_source=role_source,
            serial_number=serial_number,
            series=series,
            software_type=software_type,
            software_version=software_version,
            type=type,
            up_time=up_time,
            vrf_name=vrf_name,
            headers=headers,
            **request_parameters
        )

    # Alias Function
    def poe_interface_details(
        self, device_uuid, interface_name_list=None, headers=None, **request_parameters
    ):
        """This function is an alias of poe_interface_details_v1 .
        Args:
            device_uuid(basestring): deviceUuid path parameter. uuid of the device .
            interface_name_list(basestring): interfaceNameList query parameter. comma seperated interface names .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of poe_interface_details_v1 .
        """
        return self.poe_interface_details_v1(
            device_uuid=device_uuid,
            interface_name_list=interface_name_list,
            headers=headers,
            **request_parameters
        )

    # Alias Function
    def get_module_count(
        self,
        device_id,
        name_list=None,
        operational_state_code_list=None,
        part_number_list=None,
        vendor_equipment_type_list=None,
        headers=None,
        **request_parameters
    ):
        """This function is an alias of get_module_count_v1 .
        Args:
            device_id(basestring): deviceId query parameter.
            name_list(basestring, list, set, tuple): nameList query parameter.
            vendor_equipment_type_list(basestring, list, set, tuple): vendorEquipmentTypeList query parameter.
            part_number_list(basestring, list, set, tuple): partNumberList query parameter.
            operational_state_code_list(basestring, list, set, tuple): operationalStateCodeList query parameter.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_module_count_v1 .
        """
        return self.get_module_count_v1(
            device_id=device_id,
            name_list=name_list,
            operational_state_code_list=operational_state_code_list,
            part_number_list=part_number_list,
            vendor_equipment_type_list=vendor_equipment_type_list,
            headers=headers,
            **request_parameters
        )

    # Alias Function
    def get_polling_interval_for_all_devices(self, headers=None, **request_parameters):
        """This function is an alias of get_polling_interval_for_all_devices_v1 .
        Args:
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_polling_interval_for_all_devices_v1 .
        """
        return self.get_polling_interval_for_all_devices_v1(
            headers=headers, **request_parameters
        )

    # Alias Function
    def get_planned_access_points_for_floor(
        self,
        floor_id,
        limit=None,
        offset=None,
        radios=None,
        headers=None,
        **request_parameters
    ):
        """This function is an alias of get_planned_access_points_for_floor_v1 .
        Args:
            floor_id(basestring): floorId path parameter. The instance UUID of the floor hierarchy element .
            limit(int): limit query parameter. The page size limit for the response, e.g. limit=100 will return a
                maximum of 100 records .
            offset(int): offset query parameter. The page offset for the response. E.g. if limit=100, offset=0 will
                return first 100 records, offset=1 will return next 100 records, etc. .
            radios(bool): radios query parameter. Whether to include the planned radio details of the planned access
                points .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_planned_access_points_for_floor_v1 .
        """
        return self.get_planned_access_points_for_floor_v1(
            floor_id=floor_id,
            limit=limit,
            offset=offset,
            radios=radios,
            headers=headers,
            **request_parameters
        )

    # Alias Function
    def clear_mac_address_table(
        self,
        interface_uuid,
        deployment_mode=None,
        operation=None,
        payload=None,
        headers=None,
        active_validation=True,
        **request_parameters
    ):
        """This function is an alias of clear_mac_address_table_v1 .
        Args:
            operation(string): Devices's Operation needs to be specified as 'ClearMacAddress'. .
            payload(object): Devices's Payload is not applicable .
            interface_uuid(basestring): interfaceUuid path parameter. Interface Id .
            deployment_mode(basestring): deploymentMode query parameter. Preview/Deploy ['Preview' means the
                configuration is not pushed to the device. 'Deploy' makes the configuration pushed to
                the device] .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of clear_mac_address_table_v1 .
        """
        return self.clear_mac_address_table_v1(
            interface_uuid=interface_uuid,
            deployment_mode=deployment_mode,
            operation=operation,
            payload=payload,
            headers=headers,
            active_validation=active_validation,
            **request_parameters
        )

    # Alias Function
    def wireless_rogue_ap_containment_status(
        self, mac_address, headers=None, **request_parameters
    ):
        """This function is an alias of wireless_rogue_ap_containment_status_v1 .
        Args:
            mac_address(basestring): macAddress path parameter. MAC Address of the Wireless Rogue AP .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of wireless_rogue_ap_containment_status_v1 .
        """
        return self.wireless_rogue_ap_containment_status_v1(
            mac_address=mac_address, headers=headers, **request_parameters
        )

    # Alias Function
    def gets_the_trend_analytics_data(
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
        """This function is an alias of gets_the_trend_analytics_data_v1 .
        Args:
            aggregateAttributes(list): Devices's Aggregate Attributes (list of objects).
            attributes(list): Devices's Attributes (list of strings).
            endTime(integer): Devices's End Time.
            filters(list): Devices's filters (list of objects).
            groupBy(list): Devices's Group By (list of objects).
            page(object): Devices's page.
            startTime(integer): Devices's Start Time.
            trendInterval(string): Devices's Trend Interval.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of gets_the_trend_analytics_data_v1 .
        """
        return self.gets_the_trend_analytics_data_v1(
            aggregateAttributes=aggregateAttributes,
            attributes=attributes,
            endTime=endTime,
            filters=filters,
            groupBy=groupBy,
            page=page,
            startTime=startTime,
            trendInterval=trendInterval,
            headers=headers,
            payload=payload,
            active_validation=active_validation,
            **request_parameters
        )

    # Alias Function
    def get_device_config_for_all_devices(self, headers=None, **request_parameters):
        """This function is an alias of get_device_config_for_all_devices_v1 .
        Args:
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_device_config_for_all_devices_v1 .
        """
        return self.get_device_config_for_all_devices_v1(
            headers=headers, **request_parameters
        )

    # Alias Function
    def add_user_defined_field_to_device(
        self,
        device_id,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This function is an alias of add_user_defined_field_to_device_v1 .
        Args:
            device_id(basestring): deviceId path parameter. UUID of device to which UDF has to be added .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of add_user_defined_field_to_device_v1 .
        """
        return self.add_user_defined_field_to_device_v1(
            device_id=device_id,
            headers=headers,
            payload=payload,
            active_validation=active_validation,
            **request_parameters
        )

    # Alias Function
    def get_stack_details_for_device(
        self, device_id, headers=None, **request_parameters
    ):
        """This function is an alias of get_stack_details_for_device_v1 .
        Args:
            device_id(basestring): deviceId path parameter. Device ID .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_stack_details_for_device_v1 .
        """
        return self.get_stack_details_for_device_v1(
            device_id=device_id, headers=headers, **request_parameters
        )

    # Alias Function
    def rogue_additional_detail_count(
        self,
        endTime=None,
        siteId=None,
        startTime=None,
        threatLevel=None,
        threatType=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This function is an alias of rogue_additional_detail_count_v1 .
        Args:
            endTime(number): Devices's This is the epoch end time in milliseconds upto which data need to be
                fetched. Default value is current time .
            siteId(list): Devices's Filter Rogues by location. Site IDs information can be fetched from "Get Site"
                API  (list of strings).
            startTime(number): Devices's This is the epoch start time in milliseconds from which data need to be
                fetched. Default value is 24 hours earlier to endTime .
            threatLevel(list): Devices's This information can be fetched from "Get Threat Levels" API  (list of
                strings).
            threatType(list): Devices's This information can be fetched from "Get Threat Types" API  (list of
                strings).
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of rogue_additional_detail_count_v1 .
        """
        return self.rogue_additional_detail_count_v1(
            endTime=endTime,
            siteId=siteId,
            startTime=startTime,
            threatLevel=threatLevel,
            threatType=threatType,
            headers=headers,
            payload=payload,
            active_validation=active_validation,
            **request_parameters
        )

    # Alias Function
    def get_list_of_child_events_for_the_given_wireless_client_event(
        self, id, headers=None, **request_parameters
    ):
        """This function is an alias of get_list_of_child_events_for_the_given_wireless_client_event_v1 .
        Args:
            id(basestring): id path parameter. Unique identifier for the event .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_list_of_child_events_for_the_given_wireless_client_event_v1 .
        """
        return self.get_list_of_child_events_for_the_given_wireless_client_event_v1(
            id=id, headers=headers, **request_parameters
        )

    # Alias Function
    def get_network_device_by_ip(self, ip_address, headers=None, **request_parameters):
        """This function is an alias of get_network_device_by_ip_v1 .
        Args:
            ip_address(basestring): ipAddress path parameter. Device IP address .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_network_device_by_ip_v1 .
        """
        return self.get_network_device_by_ip_v1(
            ip_address=ip_address, headers=headers, **request_parameters
        )

    # Alias Function
    def get_device_summary(self, id, headers=None, **request_parameters):
        """This function is an alias of get_device_summary_v1 .
        Args:
            id(basestring): id path parameter. Device ID .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_device_summary_v1 .
        """
        return self.get_device_summary_v1(id=id, headers=headers, **request_parameters)

    # Alias Function
    def gets_interfaces_along_with_statistics_data_from_all_network_devices(
        self,
        attribute=None,
        end_time=None,
        interface_id=None,
        interface_name=None,
        limit=None,
        network_device_id=None,
        network_device_ip_address=None,
        network_device_mac_address=None,
        offset=None,
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
        """This function is an alias of gets_interfaces_along_with_statistics_data_from_all_network_devices_v1 .
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
            site_id(basestring): siteId query parameter. The UUID of the site. (Ex. `flooruuid`) Examples:
                `?siteId=id1` (single id requested) `?siteId=id1&siteId=id2&siteId=id3` (multiple ids
                requested) .
            view(basestring): view query parameter. The specific summary view being requested. This is an optional
                parameter which can be passed to get one or more of the specific view associated fields.
                The default view is ``configuration``. ### Response data proviced by each view:   1.
                **configuration** [id,adminStatus,description,duplexConfig,duplexOper,interfaceIfIndex,i
                nterfaceType,ipv4Address,ipv6AddressList,isL3Interface,isWan,macAddress,mediaType,name,o
                perStatus, portChannelId,portMode, portType,speed,timestamp,vlanId,networkDeviceId,netwo
                rkDeviceIpAddress,networkDeviceMacAddress,siteName,siteHierarchy,siteHierarchyId]   2.
                **statistics** [id,name,rxDiscards,rxError,rxRate,rxUtilization,txDiscards,txError,txRat
                e,txUtilization,networkDeviceId,networkDeviceIpAddress,networkDeviceMacAddress,siteName,
                siteHierarchy,siteHierarchyId]   3. **stackPort** [id,name,peerStackMember,peerStackPort
                ,stackPortType,networkDeviceId,networkDeviceIpAddress,networkDeviceMacAddress,siteName,s
                iteHierarchy,siteHierarchyId]   The default view is configuration, If need to access an
                additional view, simply include the view name in the query parameter. Examples:
                view=configuration (single view requested) view=configuration&view=statistic&stackPort
                (multiple views requested) .
            attribute(basestring): attribute query parameter. The following list of attributes can be provided in
                the attribute field [id,adminStatus, description,duplexConfig,duplexOper,interfaceIfInde
                x,interfaceType,ipv4Address,ipv6AddressList,isL3Interface,isWan,macAddress,mediaType,nam
                e,operStatus,peerStackMember,peerStackPort, portChannelId,portMode, portType,rxDiscards,
                rxError,rxRate,rxUtilization,speed,stackPortType,timestamp,txDiscards,txError,txRate,txU
                tilization,vlanId,networkDeviceId,networkDeviceIpAddress,networkDeviceMacAddress,siteNam
                e,siteHierarchy,siteHierarchyId] If length of attribute list is too long, please use
                'views' param instead. Examples: attributes=name (single attribute requested)
                attributes=name,description,duplexOper (multiple attributes with comma separator) .
            network_device_id(basestring): networkDeviceId query parameter. The list of Network Device Uuids. (Ex.
                `6bef213c-19ca-4170-8375-b694e251101c`) Examples:
                `networkDeviceId=6bef213c-19ca-4170-8375-b694e251101c` (single networkDeviceId
                requested) `networkDeviceId=6bef213c-19ca-4170-8375-
                b694e251101c&networkDeviceId=32219612-819e-4b5e-a96b-
                cf22aca13dd9&networkDeviceId=2541e9a7-b80d-4955-8aa2-79b233318ba0` (multiple
                networkDeviceIds with & separator) .
            network_device_ip_address(basestring): networkDeviceIpAddress query parameter. The list of Network
                Device management IP Address. (Ex. `121.1.1.10`) This field supports wildcard (`*`)
                character-based search.  Ex: `*1.1*` or `1.1*` or `*1.1` Examples:
                `networkDeviceIpAddress=121.1.1.10` `networkDeviceIpAddress=121.1.1.10&networkDeviceIpAd
                dress=172.20.1.10&networkDeviceIpAddress=10.10.20.10` (multiple networkDevice IP Address
                with & separator) .
            network_device_mac_address(basestring): networkDeviceMacAddress query parameter. The list of Network
                Device MAC Address. (Ex. `64:f6:9d:07:9a:00`) This field supports wildcard (`*`)
                character-based search.  Ex: `*AB:AB:AB*` or `AB:AB:AB*` or `*AB:AB:AB` Examples:
                `networkDeviceMacAddress=64:f6:9d:07:9a:00`
                `networkDeviceMacAddress=64:f6:9d:07:9a:00&networkDeviceMacAddress=70:56:9d:07:ac:77`
                (multiple networkDevice MAC addresses with & separator) .
            interface_id(basestring): interfaceId query parameter. The list of Interface Uuids. (Ex.
                `6bef213c-19ca-4170-8375-b694e251101c`) Examples:
                `interfaceId=6bef213c-19ca-4170-8375-b694e251101c` (single interface uuid ) `interfaceId
                =6bef213c-19ca-4170-8375-b694e251101c&32219612-819e-4b5e-a96b-cf22aca13dd9&2541e9a7-
                b80d-4955-8aa2-79b233318ba0` (multiple Interface uuid with & separator) .
            interface_name(basestring): interfaceName query parameter. The list of Interface name (Ex.
                `GigabitEthernet1/0/1`) This field supports wildcard (`*`) character-based search.  Ex:
                `*1/0/1*` or `1/0/1*` or `*1/0/1` Examples: `interfaceNames=GigabitEthernet1/0/1`
                (single interface name)
                `interfaceNames=GigabitEthernet1/0/1&GigabitEthernet2/0/1&GigabitEthernet3/0/1`
                (multiple interface names with & separator) .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of gets_interfaces_along_with_statistics_data_from_all_network_devices_v1 .
        """
        return (
            self.gets_interfaces_along_with_statistics_data_from_all_network_devices_v1(
                attribute=attribute,
                end_time=end_time,
                interface_id=interface_id,
                interface_name=interface_name,
                limit=limit,
                network_device_id=network_device_id,
                network_device_ip_address=network_device_ip_address,
                network_device_mac_address=network_device_mac_address,
                offset=offset,
                order=order,
                site_hierarchy=site_hierarchy,
                site_hierarchy_id=site_hierarchy_id,
                site_id=site_id,
                sort_by=sort_by,
                start_time=start_time,
                view=view,
                headers=headers,
                **request_parameters
            )
        )

    # Alias Function
    def add_allowed_mac_address(
        self, headers=None, payload=None, active_validation=True, **request_parameters
    ):
        """This function is an alias of add_allowed_mac_address_v1 .
        Args:
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of add_allowed_mac_address_v1 .
        """
        return self.add_allowed_mac_address_v1(
            headers=headers,
            payload=payload,
            active_validation=active_validation,
            **request_parameters
        )

    # Alias Function
    def get_functional_capability_by_id(self, id, headers=None, **request_parameters):
        """This function is an alias of get_functional_capability_by_id_v1 .
        Args:
            id(basestring): id path parameter. Functional Capability UUID .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_functional_capability_by_id_v1 .
        """
        return self.get_functional_capability_by_id_v1(
            id=id, headers=headers, **request_parameters
        )

    # Alias Function
    def query_assurance_events(
        self,
        device_family,
        ap_mac=None,
        attribute=None,
        client_mac=None,
        end_time=None,
        limit=None,
        message_type=None,
        network_device_id=None,
        network_device_name=None,
        offset=None,
        order=None,
        severity=None,
        site_hierarchy_id=None,
        site_id=None,
        sort_by=None,
        start_time=None,
        view=None,
        headers=None,
        **request_parameters
    ):
        """This function is an alias of query_assurance_events_v1 .
        Args:
            device_family(basestring): deviceFamily query parameter. Device family. Please note that multiple
                families across network device type and client type is not allowed. For example,
                choosing `Routers` along with `Wireless Client` or `Unified AP` is not supported.
                Examples: `deviceFamily=Switches and Hubs` (single deviceFamily requested)
                `deviceFamily=Switches and Hubs&deviceFamily=Routers` (multiple deviceFamily requested)
                .
            start_time(int): startTime query parameter. Start time from which API queries the data set related to
                the resource. It must be specified in UNIX epochtime in milliseconds. Value is
                inclusive. If `startTime` is not provided, API will default to current time minus 24
                hours. .
            end_time(int): endTime query parameter. End time to which API queries the data set related to the
                resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive. If
                `endTime` is not provided, API will default to current time. .
            message_type(basestring): messageType query parameter. Message type for the event. Examples:
                `messageType=Syslog` (single messageType requested)
                `messageType=Trap&messageType=Syslog` (multiple messageType requested) .
            severity(int): severity query parameter. Severity of the event between 0 and 6. This is applicable only
                for events related to network devices (other than AP) and `Wired Client` events. (Value:
                Severity: 0: Emergency: 1: Alert: 2: Critical: 3: Error: 4: Warning: 5: Notice: 6:
                Info),  Examples: `severity=0` (single severity requested) `severity=0&severity=1`
                (multiple severity requested) .
            site_id(basestring): siteId query parameter. The UUID of the site. (Ex. `flooruuid`) Examples:
                `?siteId=id1` (single siteId requested) `?siteId=id1&siteId=id2&siteId=id3` (multiple
                siteId requested) .
            site_hierarchy_id(basestring): siteHierarchyId query parameter. The full hierarchy breakdown of the site
                tree in id form starting from Global site UUID and ending with the specific site UUID.
                (Ex. `globalUuid/areaUuid/buildingUuid/floorUuid`) This field supports wildcard asterisk
                (`*`) character search support. E.g. `*uuid*, *uuid, uuid*` Examples:
                `?siteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid `(single siteHierarchyId
                requested) `?siteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid&siteHierarchyId=
                globalUuid/areaUuid2/buildingUuid2/floorUuid2` (multiple siteHierarchyId requested) .
            network_device_name(basestring): networkDeviceName query parameter. Network device name. This parameter
                is applicable for network device related families. This field supports wildcard (`*`)
                character-based search. Ex: `*Branch*` or `Branch*` or `*Branch` Examples:
                `networkDeviceName=Branch-3-Gateway` (single networkDeviceName requested)
                `networkDeviceName=Branch-3-Gateway&networkDeviceName=Branch-3-Switch` (multiple
                networkDeviceName requested) .
            network_device_id(basestring): networkDeviceId query parameter. The list of Network Device Uuids. (Ex.
                `6bef213c-19ca-4170-8375-b694e251101c`) Examples:
                `networkDeviceId=6bef213c-19ca-4170-8375-b694e251101c` (single networkDeviceId
                requested) `networkDeviceId=6bef213c-19ca-4170-8375-
                b694e251101c&networkDeviceId=32219612-819e-4b5e-a96b-
                cf22aca13dd9&networkDeviceId=2541e9a7-b80d-4955-8aa2-79b233318ba0` (multiple
                networkDeviceId with & separator) .
            ap_mac(basestring): apMac query parameter. MAC address of the access point. This parameter is applicable
                for `Unified AP` and `Wireless Client` events. This field supports wildcard (`*`)
                character-based search. Ex: `*50:0F*` or `50:0F*` or `*50:0F` Examples:
                `apMac=50:0F:80:0F:F7:E0` (single apMac requested)
                `apMac=50:0F:80:0F:F7:E0&apMac=18:80:90:AB:7E:A0` (multiple apMac requested) .
            client_mac(basestring): clientMac query parameter. MAC address of the client. This parameter is
                applicable for `Wired Client` and `Wireless Client` events. This field supports wildcard
                (`*`) character-based search. Ex: `*66:2B*` or `66:2B*` or `*66:2B` Examples:
                `clientMac=66:2B:B8:D2:01:56` (single clientMac requested)
                `clientMac=66:2B:B8:D2:01:56&clientMac=DC:A6:32:F5:5A:89` (multiple clientMac requested)
                .
            attribute(basestring): attribute query parameter. The list of attributes that needs to be included in
                the response. If this parameter is not provided, then basic attributes (`id`, `name`,
                `timestamp`, `details`, `messageType`, `siteHierarchyId`, `siteHierarchy`,
                `deviceFamily`, `networkDeviceId`, `networkDeviceName`, `managementIpAddress`) would be
                part of the response.  Examples: `attribute=name` (single attribute requested)
                `attribute=name&attribute=networkDeviceName` (multiple attribute requested) .
            view(basestring): view query parameter. The list of events views. Please refer to `EventViews` for the
                supported list  Examples: `view=network` (single view requested) `view=network&view=ap`
                (multiple view requested) .
            offset(int): offset query parameter. Specifies the starting point within all records returned by the
                API. It's one based offset. The starting value is 1. .
            limit(int): limit query parameter. Maximum number of records to return .
            sort_by(basestring): sortBy query parameter. A field within the response to sort by. .
            order(basestring): order query parameter. The sort order of the field ascending or descending. .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of query_assurance_events_v1 .
        """
        return self.query_assurance_events_v1(
            device_family=device_family,
            ap_mac=ap_mac,
            attribute=attribute,
            client_mac=client_mac,
            end_time=end_time,
            limit=limit,
            message_type=message_type,
            network_device_id=network_device_id,
            network_device_name=network_device_name,
            offset=offset,
            order=order,
            severity=severity,
            site_hierarchy_id=site_hierarchy_id,
            site_id=site_id,
            sort_by=sort_by,
            start_time=start_time,
            view=view,
            headers=headers,
            **request_parameters
        )

    # Alias Function
    def get_allowed_mac_address_count(self, headers=None, **request_parameters):
        """This function is an alias of get_allowed_mac_address_count_v1 .
        Args:
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_allowed_mac_address_count_v1 .
        """
        return self.get_allowed_mac_address_count_v1(
            headers=headers, **request_parameters
        )

    # Alias Function
    def update_health_score_definitions(
        self, headers=None, payload=None, active_validation=True, **request_parameters
    ):
        """This function is an alias of update_health_score_definitions_v1 .
        Args:
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of update_health_score_definitions_v1 .
        """
        return self.update_health_score_definitions_v1(
            headers=headers,
            payload=payload,
            active_validation=active_validation,
            **request_parameters
        )

    # Alias Function
    def get_device_interface_count_by_id(
        self, device_id, headers=None, **request_parameters
    ):
        """This function is an alias of get_device_interface_count_by_id_v1 .
        Args:
            device_id(basestring): deviceId path parameter. Device ID .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_device_interface_count_by_id_v1 .
        """
        return self.get_device_interface_count_by_id_v1(
            device_id=device_id, headers=headers, **request_parameters
        )

    # Alias Function
    def get_interface_by_id(self, id, headers=None, **request_parameters):
        """This function is an alias of get_interface_by_id_v1 .
        Args:
            id(basestring): id path parameter. Interface ID .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_interface_by_id_v1 .
        """
        return self.get_interface_by_id_v1(id=id, headers=headers, **request_parameters)

    # Alias Function
    def get_allowed_mac_address(
        self, limit=None, offset=None, headers=None, **request_parameters
    ):
        """This function is an alias of get_allowed_mac_address_v1 .
        Args:
            offset(int): offset query parameter. The offset of the first item in the collection to return. .
            limit(int): limit query parameter. The maximum number of entries to return. If the value exceeds the
                total count, then the maximum entries will be returned. .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_allowed_mac_address_v1 .
        """
        return self.get_allowed_mac_address_v1(
            limit=limit, offset=offset, headers=headers, **request_parameters
        )

    # Alias Function
    def get_device_detail(
        self, identifier, search_by, timestamp=None, headers=None, **request_parameters
    ):
        """This function is an alias of get_device_detail_v1 .
        Args:
            timestamp(int): timestamp query parameter. UTC timestamp of device data in milliseconds .
            identifier(basestring): identifier query parameter. One of "macAddress", "nwDeviceName", "uuid" (case
                insensitive) .
            search_by(basestring): searchBy query parameter. MAC Address, device name, or UUID of the network device
                .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_device_detail_v1 .
        """
        return self.get_device_detail_v1(
            identifier=identifier,
            search_by=search_by,
            timestamp=timestamp,
            headers=headers,
            **request_parameters
        )

    # Alias Function
    def update_health_score_definition_for_the_given_id(
        self,
        id,
        includeForOverallHealth=None,
        synchronizeToIssueThreshold=None,
        thresholdValue=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This function is an alias of update_health_score_definition_for_the_given_id_v1 .
        Args:
            includeForOverallHealth(boolean): Devices's Include For Overall Health.
            synchronizeToIssueThreshold(boolean): Devices's Synchronize To Issue Threshold.
            thresholdValue(number): Devices's Thresehold Value.
            id(basestring): id path parameter. Health score definition id. .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of update_health_score_definition_for_the_given_id_v1 .
        """
        return self.update_health_score_definition_for_the_given_id_v1(
            id=id,
            includeForOverallHealth=includeForOverallHealth,
            synchronizeToIssueThreshold=synchronizeToIssueThreshold,
            thresholdValue=thresholdValue,
            headers=headers,
            payload=payload,
            active_validation=active_validation,
            **request_parameters
        )

    # Alias Function
    def get_details_of_a_single_assurance_event(
        self, id, attribute=None, view=None, headers=None, **request_parameters
    ):
        """This function is an alias of get_details_of_a_single_assurance_event_v1 .
        Args:
            id(basestring): id path parameter. Unique identifier for the event .
            attribute(basestring): attribute query parameter. The list of attributes that needs to be included in
                the response. If this parameter is not provided, then basic attributes (`id`, `name`,
                `timestamp`, `details`, `messageType`, `siteHierarchyId`, `siteHierarchy`,
                `deviceFamily`, `networkDeviceId`, `networkDeviceName`, `managementIpAddress`) would be
                part of the response.  Examples: `attribute=name` (single attribute requested)
                `attribute=name&attribute=networkDeviceName` (multiple attribute requested) .
            view(basestring): view query parameter. The list of events views. Please refer to `EventViews` for the
                supported list  Examples: `view=network` (single view requested) `view=network&view=ap`
                (multiple view requested) .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_details_of_a_single_assurance_event_v1 .
        """
        return self.get_details_of_a_single_assurance_event_v1(
            id=id, attribute=attribute, view=view, headers=headers, **request_parameters
        )

    # Alias Function
    def get_device_interfaces_by_specified_range(
        self,
        device_id,
        records_to_return,
        start_index,
        headers=None,
        **request_parameters
    ):
        """This function is an alias of get_device_interfaces_by_specified_range_v1 .
        Args:
            device_id(basestring): deviceId path parameter. Device ID .
            start_index(int): startIndex path parameter. Start index .
            records_to_return(int): recordsToReturn path parameter. Number of records to return .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_device_interfaces_by_specified_range_v1 .
        """
        return self.get_device_interfaces_by_specified_range_v1(
            device_id=device_id,
            records_to_return=records_to_return,
            start_index=start_index,
            headers=headers,
            **request_parameters
        )

    # Alias Function
    def query_assurance_events_with_filters(
        self,
        attributes=None,
        deviceFamily=None,
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
        """This function is an alias of query_assurance_events_with_filters_v1 .
        Args:
            attributes(list): Devices's Attributes (list of strings).
            deviceFamily(list): Devices's Device Family (list of strings).
            endTime(integer): Devices's End Time.
            filters(list): Devices's filters (list of objects).
            page(object): Devices's page.
            startTime(integer): Devices's Start Time.
            views(list): Devices's Views (list of strings).
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of query_assurance_events_with_filters_v1 .
        """
        return self.query_assurance_events_with_filters_v1(
            attributes=attributes,
            deviceFamily=deviceFamily,
            endTime=endTime,
            filters=filters,
            page=page,
            startTime=startTime,
            views=views,
            headers=headers,
            payload=payload,
            active_validation=active_validation,
            **request_parameters
        )

    # Alias Function
    def get_device_count(
        self,
        hostname=None,
        location_name=None,
        mac_address=None,
        management_ip_address=None,
        headers=None,
        **request_parameters
    ):
        """This function is an alias of get_device_count_v1 .
        Args:
            hostname(basestring, list, set, tuple): hostname query parameter.
            management_ip_address(basestring, list, set, tuple): managementIpAddress query parameter.
            mac_address(basestring, list, set, tuple): macAddress query parameter.
            location_name(basestring, list, set, tuple): locationName query parameter.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_device_count_v1 .
        """
        return self.get_device_count_v1(
            hostname=hostname,
            location_name=location_name,
            mac_address=mac_address,
            management_ip_address=management_ip_address,
            headers=headers,
            **request_parameters
        )

    # Alias Function
    def start_wireless_rogue_ap_containment(
        self,
        macAddress=None,
        type=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This function is an alias of start_wireless_rogue_ap_containment_v1 .
        Args:
            macAddress(string): Devices's Mac Address.
            type(integer): Devices's Type.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of start_wireless_rogue_ap_containment_v1 .
        """
        return self.start_wireless_rogue_ap_containment_v1(
            macAddress=macAddress,
            type=type,
            headers=headers,
            payload=payload,
            active_validation=active_validation,
            **request_parameters
        )

    # Alias Function
    def create_user_defined_field(
        self,
        description=None,
        name=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This function is an alias of create_user_defined_field_v1 .
        Args:
            description(string): Devices's Description of UDF .
            name(string): Devices's Name of UDF .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of create_user_defined_field_v1 .
        """
        return self.create_user_defined_field_v1(
            description=description,
            name=name,
            headers=headers,
            payload=payload,
            active_validation=active_validation,
            **request_parameters
        )

    # Alias Function
    def update_device_management_address(
        self,
        deviceid,
        newIP=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This function is an alias of update_device_management_address_v1 .
        Args:
            newIP(string): Devices's New IP Address of the device to be Updated .
            deviceid(basestring): deviceid path parameter. The UUID of the device whose management IP address is to
                be updated. .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of update_device_management_address_v1 .
        """
        return self.update_device_management_address_v1(
            deviceid=deviceid,
            newIP=newIP,
            headers=headers,
            payload=payload,
            active_validation=active_validation,
            **request_parameters
        )

    # Alias Function
    def get_interface_details(
        self, device_id, name, headers=None, **request_parameters
    ):
        """This function is an alias of get_interface_details_v1 .
        Args:
            device_id(basestring): deviceId path parameter. Device ID .
            name(basestring): name query parameter. Interface name .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_interface_details_v1 .
        """
        return self.get_interface_details_v1(
            device_id=device_id, name=name, headers=headers, **request_parameters
        )

    # Alias Function
    def sync_devices(
        self,
        cliTransport=None,
        computeDevice=None,
        enablePassword=None,
        extendedDiscoveryInfo=None,
        httpPassword=None,
        httpPort=None,
        httpSecure=None,
        httpUserName=None,
        ipAddress=None,
        merakiOrgId=None,
        netconfPort=None,
        password=None,
        serialNumber=None,
        snmpAuthPassphrase=None,
        snmpAuthProtocol=None,
        snmpMode=None,
        snmpPrivPassphrase=None,
        snmpPrivProtocol=None,
        snmpROCommunity=None,
        snmpRWCommunity=None,
        snmpRetry=None,
        snmpTimeout=None,
        snmpUserName=None,
        snmpVersion=None,
        type=None,
        updateMgmtIPaddressList=None,
        userName=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This function is an alias of sync_devices_v1 .
        Args:
            cliTransport(string): Devices's CLI transport. Supported values: telnet, ssh. Use NO!$DATA!$ if no
                change is required. Required if type is NETWORK_DEVICE. .
            computeDevice(boolean): Devices's Compute Device or not. Options are true / false. .
            enablePassword(string): Devices's CLI enable password of the device. Required if device is configured to
                use enable password. Use NO!$DATA!$ if no change is required. .
            extendedDiscoveryInfo(string): Devices's This field holds that info as whether to add device with canned
                data or not. Supported values: DISCOVER_WITH_CANNED_DATA. .
            httpPassword(string): Devices's HTTP password of the device / API key for Meraki Dashboard. Required if
                type is MERAKI_DASHBOARD or COMPUTE_DEVICE. Use NO!$DATA!$ if no change is required. .
            httpPort(string): Devices's HTTP port of the device. Required if type is COMPUTE_DEVICE. .
            httpSecure(boolean): Devices's Flag to select HTTP / HTTPS protocol. Options are true / false. true for
                HTTPS and false for HTTP. .
            httpUserName(string): Devices's HTTP Username of the device. Required if type is COMPUTE_DEVICE. Use
                NO!$DATA!$ if no change is required. .
            ipAddress(list): Devices's IP Address of the device. Required. Use 'api.meraki.com' for Meraki
                Dashboard.  (list of strings).
            merakiOrgId(list): Devices's Selected Meraki organization for which the devices needs to be imported.
                Required if type is MERAKI_DASHBOARD.  (list of strings).
            netconfPort(string): Devices's Netconf Port of the device. cliTransport must be 'ssh' if netconf is
                provided. .
            password(string): Devices's CLI Password of the device. Required if type is NETWORK_DEVICE. Use
                NO!$DATA!$ if no change is required. .
            serialNumber(string): Devices's Serial Number of the Device. Required if extendedDiscoveryInfo is
                'DISCOVER_WITH_CANNED_DATA'. .
            snmpAuthPassphrase(string): Devices's SNMPv3 auth passphrase of the device. Required if snmpMode is
                authNoPriv or authPriv. Use NO!$DATA!$ if no change is required. .
            snmpAuthProtocol(string): Devices's SNMPv3 auth protocol. Supported values: sha, md5.  Required if
                snmpMode is authNoPriv or authPriv. Use NODATACHANGE if no change is required. .
            snmpMode(string): Devices's SNMPv3 mode. Supported values: noAuthnoPriv, authNoPriv, authPriv. Required
                if snmpVersion is v3. Use NODATACHANGE if no change is required. .
            snmpPrivPassphrase(string): Devices's SNMPv3 priv passphrase. Required if snmpMode is authPriv. Use
                NO!$DATA!$ if no change is required. .
            snmpPrivProtocol(string): Devices's SNMPv3 priv protocol. Supported values: AES128. Required if snmpMode
                is authPriv. Use NODATACHANGE if no change is required. .
            snmpROCommunity(string): Devices's SNMP Read Community of the device. If snmpVersion is v2, at least one
                of snmpROCommunity and snmpRWCommunity is required. Use NO!$DATA!$ if no change is
                required. .
            snmpRWCommunity(string): Devices's SNMP Write Community of the device. If snmpVersion is v2, at least
                one of snmpROCommunity and snmpRWCommunity is required. Use NO!$DATA!$ if no change is
                required. .
            snmpRetry(integer): Devices's SNMP retry count. Max value supported is 3. Default is Global SNMP retry
                (if exists) or 3. .
            snmpTimeout(integer): Devices's SNMP timeout in seconds. Max value supported is 300. Default is Global
                SNMP timeout (if exists) or 5. .
            snmpUserName(string): Devices's SNMPV3 user name of the device. Required if snmpVersion is v3. Use
                NO!$DATA!$ if no change is required. .
            snmpVersion(string): Devices's SNMP version. Values supported: v2, v3. Required if type is
                NETWORK_DEVICE, COMPUTE_DEVICE or THIRD_PARTY_DEVICE. Use NODATACHANGE if no change is
                required. .
            type(string): Devices's Type of device being edited. Default is NETWORK_DEVICE. . Available values are
                'COMPUTE_DEVICE', 'MERAKI_DASHBOARD', 'NETWORK_DEVICE', 'THIRD_PARTY_DEVICE' and
                'NODATACHANGE'.
            updateMgmtIPaddressList(list): Devices's updateMgmtIPaddressList (list of objects).
            userName(string): Devices's CLI user name of the device. Required if type is NETWORK_DEVICE. Use
                NO!$DATA!$ if no change is required. .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of sync_devices_v1 .
        """
        return self.sync_devices_v1(
            cliTransport=cliTransport,
            computeDevice=computeDevice,
            enablePassword=enablePassword,
            extendedDiscoveryInfo=extendedDiscoveryInfo,
            httpPassword=httpPassword,
            httpPort=httpPort,
            httpSecure=httpSecure,
            httpUserName=httpUserName,
            ipAddress=ipAddress,
            merakiOrgId=merakiOrgId,
            netconfPort=netconfPort,
            password=password,
            serialNumber=serialNumber,
            snmpAuthPassphrase=snmpAuthPassphrase,
            snmpAuthProtocol=snmpAuthProtocol,
            snmpMode=snmpMode,
            snmpPrivPassphrase=snmpPrivPassphrase,
            snmpPrivProtocol=snmpPrivProtocol,
            snmpROCommunity=snmpROCommunity,
            snmpRWCommunity=snmpRWCommunity,
            snmpRetry=snmpRetry,
            snmpTimeout=snmpTimeout,
            snmpUserName=snmpUserName,
            snmpVersion=snmpVersion,
            type=type,
            updateMgmtIPaddressList=updateMgmtIPaddressList,
            userName=userName,
            headers=headers,
            payload=payload,
            active_validation=active_validation,
            **request_parameters
        )

    # Alias Function
    def get_the_details_of_physical_components_of_the_given_device(
        self, device_uuid, type=None, headers=None, **request_parameters
    ):
        """This function is an alias of get_the_details_of_physical_components_of_the_given_device_v1 .
        Args:
            device_uuid(basestring): deviceUuid path parameter.
            type(basestring): type query parameter. Type value can be PowerSupply, Fan, Chassis, Backplane, Module,
                PROCESSOR, Other, SFP. If no type is mentioned, All equipments are fetched for the
                device. .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_the_details_of_physical_components_of_the_given_device_v1 .
        """
        return self.get_the_details_of_physical_components_of_the_given_device_v1(
            device_uuid=device_uuid, type=type, headers=headers, **request_parameters
        )

    # Alias Function
    def get_functional_capability_for_devices(
        self, device_id, function_name=None, headers=None, **request_parameters
    ):
        """This function is an alias of get_functional_capability_for_devices_v1 .
        Args:
            device_id(basestring): deviceId query parameter. Accepts comma separated deviceid's and return list of
                functional-capabilities for the given id's. If invalid or not-found id's are provided,
                null entry will be returned in the list. .
            function_name(basestring, list, set, tuple): functionName query parameter.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_functional_capability_for_devices_v1 .
        """
        return self.get_functional_capability_for_devices_v1(
            device_id=device_id,
            function_name=function_name,
            headers=headers,
            **request_parameters
        )

    # Alias Function
    def update_interface_details(
        self,
        interface_uuid,
        adminStatus=None,
        deployment_mode=None,
        description=None,
        vlanId=None,
        voiceVlanId=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This function is an alias of update_interface_details_v1 .
        Args:
            adminStatus(string): Devices's Admin status as ('UP'/'DOWN') .
            description(string): Devices's Description for the Interface .
            vlanId(integer): Devices's VLAN Id to be Updated .
            voiceVlanId(integer): Devices's Voice Vlan Id to be Updated .
            interface_uuid(basestring): interfaceUuid path parameter. Interface ID .
            deployment_mode(basestring): deploymentMode query parameter. Preview/Deploy ['Preview' means the
                configuration is not pushed to the device. 'Deploy' makes the configuration pushed to
                the device] .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of update_interface_details_v1 .
        """
        return self.update_interface_details_v1(
            interface_uuid=interface_uuid,
            adminStatus=adminStatus,
            deployment_mode=deployment_mode,
            description=description,
            vlanId=vlanId,
            voiceVlanId=voiceVlanId,
            headers=headers,
            payload=payload,
            active_validation=active_validation,
            **request_parameters
        )

    # Alias Function
    def count_the_number_of_events(
        self,
        device_family,
        ap_mac=None,
        client_mac=None,
        end_time=None,
        message_type=None,
        network_device_id=None,
        network_device_name=None,
        severity=None,
        site_hierarchy_id=None,
        site_id=None,
        start_time=None,
        headers=None,
        **request_parameters
    ):
        """This function is an alias of count_the_number_of_events_v1 .
        Args:
            device_family(basestring): deviceFamily query parameter. Device family. Please note that multiple
                families across network device type and client type is not allowed. For example,
                choosing `Routers` along with `Wireless Client` or `Unified AP` is not supported.
                Examples: `deviceFamily=Switches and Hubs` (single deviceFamily requested)
                `deviceFamily=Switches and Hubs&deviceFamily=Routers` (multiple deviceFamily requested)
                .
            start_time(basestring): startTime query parameter. Start time from which API queries the data set
                related to the resource. It must be specified in UNIX epochtime in milliseconds. Value
                is inclusive. If `startTime` is not provided, API will default to current time minus 24
                hours. .
            end_time(basestring): endTime query parameter. End time to which API queries the data set related to the
                resource. It must be specified in UNIX epochtime in milliseconds. Value is inclusive. If
                `endTime` is not provided, API will default to current time. .
            message_type(basestring): messageType query parameter. Message type for the event. Examples:
                `messageType=Syslog` (single messageType requested)
                `messageType=Trap&messageType=Syslog` (multiple messageType requested) .
            severity(basestring): severity query parameter. Severity of the event between 0 and 6. This is
                applicable only for events related to network devices (other than AP) and `Wired Client`
                events. (Value: Severity: 0: Emergency: 1: Alert: 2: Critical: 3: Error: 4: Warning: 5:
                Notice: 6: Info),  Examples: `severity=0` (single severity requested)
                `severity=0&severity=1` (multiple severity requested) .
            site_id(basestring): siteId query parameter. The UUID of the site. (Ex. `flooruuid`) Examples:
                `?siteId=id1` (single siteId requested) `?siteId=id1&siteId=id2&siteId=id3` (multiple
                siteId requested) .
            site_hierarchy_id(basestring): siteHierarchyId query parameter. The full hierarchy breakdown of the site
                tree in id form starting from Global site UUID and ending with the specific site UUID.
                (Ex. `globalUuid/areaUuid/buildingUuid/floorUuid`) This field supports wildcard asterisk
                (`*`) character search support. E.g. `*uuid*, *uuid, uuid*` Examples:
                `?siteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid `(single siteHierarchyId
                requested) `?siteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid&siteHierarchyId=
                globalUuid/areaUuid2/buildingUuid2/floorUuid2` (multiple siteHierarchyId requested) .
            network_device_name(basestring): networkDeviceName query parameter. Network device name. This parameter
                is applicable for network device related families. This field supports wildcard (`*`)
                character-based search. Ex: `*Branch*` or `Branch*` or `*Branch` Examples:
                `networkDeviceName=Branch-3-Gateway` (single networkDeviceName requested)
                `networkDeviceName=Branch-3-Gateway&networkDeviceName=Branch-3-Switch` (multiple
                networkDeviceName requested) .
            network_device_id(basestring): networkDeviceId query parameter. The list of Network Device Uuids. (Ex.
                `6bef213c-19ca-4170-8375-b694e251101c`) Examples:
                `networkDeviceId=6bef213c-19ca-4170-8375-b694e251101c` (single networkDeviceId
                requested) `networkDeviceId=6bef213c-19ca-4170-8375-
                b694e251101c&networkDeviceId=32219612-819e-4b5e-a96b-
                cf22aca13dd9&networkDeviceId=2541e9a7-b80d-4955-8aa2-79b233318ba0` (multiple
                networkDeviceId requested) .
            ap_mac(basestring): apMac query parameter. MAC address of the access point. This parameter is applicable
                for `Unified AP` and `Wireless Client` events. This field supports wildcard (`*`)
                character-based search. Ex: `*50:0F*` or `50:0F*` or `*50:0F` Examples:
                `apMac=50:0F:80:0F:F7:E0` (single apMac requested)
                `apMac=50:0F:80:0F:F7:E0&apMac=18:80:90:AB:7E:A0` (multiple apMac requested) .
            client_mac(basestring): clientMac query parameter. MAC address of the client. This parameter is
                applicable for `Wired Client` and `Wireless Client` events. This field supports wildcard
                (`*`) character-based search. Ex: `*66:2B*` or `66:2B*` or `*66:2B` Examples:
                `clientMac=66:2B:B8:D2:01:56` (single clientMac requested)
                `clientMac=66:2B:B8:D2:01:56&clientMac=DC:A6:32:F5:5A:89` (multiple clientMac requested)
                .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of count_the_number_of_events_v1 .
        """
        return self.count_the_number_of_events_v1(
            device_family=device_family,
            ap_mac=ap_mac,
            client_mac=client_mac,
            end_time=end_time,
            message_type=message_type,
            network_device_id=network_device_id,
            network_device_name=network_device_name,
            severity=severity,
            site_hierarchy_id=site_hierarchy_id,
            site_id=site_id,
            start_time=start_time,
            headers=headers,
            **request_parameters
        )

    # Alias Function
    def get_ospf_interfaces(self, headers=None, **request_parameters):
        """This function is an alias of get_ospf_interfaces_v1 .
        Args:
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_ospf_interfaces_v1 .
        """
        return self.get_ospf_interfaces_v1(headers=headers, **request_parameters)

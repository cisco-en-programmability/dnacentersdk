# -*- coding: utf-8 -*-
"""Cisco DNA Center Devices API wrapper.

Copyright (c) 2019-2021 Cisco Systems.

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

    def get_planned_access_points_for_building(self,
                                               building_id,
                                               limit=None,
                                               offset=None,
                                               radios=None,
                                               headers=None,
                                               **request_parameters):
        """Provides a list of Planned Access Points for the Building it is requested for .

        Args:
            building_id(str): buildingId path parameter. Building Id .
            limit(int,str): limit query parameter.
            offset(int,str): offset query parameter.
            radios(bool): radios query parameter. inlcude planned radio details .
            headers(dict): Dictionary of HTTP Headers to send with the Request
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
        """
        check_type(headers, dict)
        check_type(limit, (int, str))
        check_type(offset, (int, str))
        check_type(radios, bool)
        check_type(building_id, str,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'limit':
                limit,
            'offset':
                offset,
            'radios':
                radios,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'buildingId': building_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/buildings/{buildingId}/planned-'
                 + 'access-points')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_efc372d6eb577ca47e8c86f30c3d2f_v2_3_7_6', json_data)

    def get_device_detail(self,
                          identifier,
                          search_by,
                          timestamp=None,
                          headers=None,
                          **request_parameters):
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
        """
        check_type(headers, dict)
        check_type(timestamp, int)
        check_type(identifier, str,
                   may_be_none=False)
        check_type(search_by, str,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'timestamp':
                timestamp,
            'identifier':
                identifier,
            'searchBy':
                search_by,
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

        e_url = ('/dna/intent/api/v1/device-detail')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_c9ee787eb5a0391309f45ddf392ca_v2_3_7_6', json_data)

    def get_device_enrichment_details(self,
                                      headers=None,
                                      **request_parameters):
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
        """
        check_type(headers, dict)
        if headers is not None:
            if 'entity_type' in headers:
                check_type(headers.get('entity_type'),
                           str, may_be_none=False)
            if 'entity_value' in headers:
                check_type(headers.get('entity_value'),
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

        e_url = ('/dna/intent/api/v1/device-enrichment-details')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_a20c25e0fa518bb186fd7747450ef6_v2_3_7_6', json_data)

    def devices(self,
                device_role=None,
                end_time=None,
                health=None,
                limit=None,
                offset=None,
                site_id=None,
                start_time=None,
                headers=None,
                **request_parameters):
        """Intent API for accessing DNA Assurance Device object for generating reports, creating dashboards or creating
        additional value added services. .

        Args:
            device_role(str): deviceRole query parameter. CORE, ACCESS, DISTRIBUTION, ROUTER, WLC, or AP
                (case insensitive) .
            site_id(str): siteId query parameter. DNAC site UUID .
            health(str): health query parameter. DNAC health catagory: POOR, FAIR, or GOOD (case insensitive)
                .
            start_time(int): startTime query parameter. UTC epoch time in milliseconds .
            end_time(int): endTime query parameter. UTC epoch time in milliseconds .
            limit(int,str): limit query parameter. Max number of device entries in the response (default to 50. Max at
                500) .
            offset(int,str): offset query parameter. The offset of the first device in the returned data (Mutiple of
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
        """
        check_type(headers, dict)
        check_type(device_role, str)
        check_type(site_id, str)
        check_type(health, str)
        check_type(start_time, int)
        check_type(end_time, int)
        check_type(limit, (int, str))
        check_type(offset, (int, str))
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'deviceRole':
                device_role,
            'siteId':
                site_id,
            'health':
                health,
            'startTime':
                start_time,
            'endTime':
                end_time,
            'limit':
                limit,
            'offset':
                offset,
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

        e_url = ('/dna/intent/api/v1/device-health')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_c75e364632e15384a18063458e2ba0e3_v2_3_7_6', json_data)

    def update_planned_access_point_for_floor(self,
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
                                              **request_parameters):
        """Allows updating a planned access point on an existing floor map including its planned radio and antenna details.
        Use the Get variant of this API to fetch the existing planned access points for the floor.  The payload
        to update a planned access point is in the same format, albeit a single object instead of a list, of
        that API. .

        Args:
            attributes(object): Devices's attributes.
            isSensor(boolean): Devices's isSensor.
            location(object): Devices's location.
            position(object): Devices's position.
            radioCount(integer): Devices's radioCount.
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
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(floor_id, str,
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
            'floorId': floor_id,
        }
        _payload = {
            'attributes':
                attributes,
            'isSensor':
                isSensor,
            'location':
                location,
            'position':
                position,
            'radioCount':
                radioCount,
            'radios':
                radios,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_f6f9dde38ce458fcaf27ffd4f84bfe68_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/floors/{floorId}/planned-access-'
                 + 'points')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload,
                                          headers=_headers)
        else:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload)

        return self._object_factory('bpm_f6f9dde38ce458fcaf27ffd4f84bfe68_v2_3_7_6', json_data)

    def create_planned_access_point_for_floor(self,
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
                                              **request_parameters):
        """Allows creation of a new planned access point on an existing floor map including its planned radio and antenna
        details.  Use the Get variant of this API to fetch any existing planned access points for the floor.
        The payload to create a planned access point is in the same format, albeit a single object instead of a
        list, of that API. .

        Args:
            attributes(object): Devices's attributes.
            isSensor(boolean): Devices's isSensor.
            location(object): Devices's location.
            position(object): Devices's position.
            radioCount(integer): Devices's radioCount.
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
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(floor_id, str,
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
            'floorId': floor_id,
        }
        _payload = {
            'attributes':
                attributes,
            'isSensor':
                isSensor,
            'location':
                location,
            'position':
                position,
            'radioCount':
                radioCount,
            'radios':
                radios,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_ca2fe989a227585086452d24d32867a6_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/floors/{floorId}/planned-access-'
                 + 'points')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_ca2fe989a227585086452d24d32867a6_v2_3_7_6', json_data)

    def get_planned_access_points_for_floor(self,
                                            floor_id,
                                            limit=None,
                                            offset=None,
                                            radios=None,
                                            headers=None,
                                            **request_parameters):
        """Provides a list of Planned Access Points for the Floor it is requested for .

        Args:
            floor_id(str): floorId path parameter. Floor Id .
            limit(int,str): limit query parameter.
            offset(int,str): offset query parameter.
            radios(bool): radios query parameter. inlcude planned radio details .
            headers(dict): Dictionary of HTTP Headers to send with the Request
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
        """
        check_type(headers, dict)
        check_type(limit, (int, str))
        check_type(offset, (int, str))
        check_type(radios, bool)
        check_type(floor_id, str,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'limit':
                limit,
            'offset':
                offset,
            'radios':
                radios,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'floorId': floor_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/floors/{floorId}/planned-access-'
                 + 'points')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_a570c5ee77b59d8b9cd203e566288e1_v2_3_7_6', json_data)

    def delete_planned_access_point_for_floor(self,
                                              floor_id,
                                              planned_access_point_uuid,
                                              headers=None,
                                              **request_parameters):
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
        """
        check_type(headers, dict)
        check_type(floor_id, str,
                   may_be_none=False)
        check_type(planned_access_point_uuid, str,
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
            'floorId': floor_id,
            'plannedAccessPointUuid': planned_access_point_uuid,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/floors/{floorId}/planned-access-'
                 + 'points/{plannedAccessPointUuid}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(endpoint_full_url, params=_params,
                                             headers=_headers)
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_cb644669ab8d5955826d23197015e208_v2_3_7_6', json_data)

    def get_all_interfaces(self,
                           last_input_time=None,
                           last_output_time=None,
                           limit=None,
                           offset=None,
                           headers=None,
                           **request_parameters):
        """Returns all available interfaces. This endpoint can return a maximum of 500 interfaces .

        Args:
            offset(int,str): offset query parameter.
            limit(int,str): limit query parameter.
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
        """
        check_type(headers, dict)
        check_type(offset, (int, str))
        check_type(limit, (int, str))
        check_type(last_input_time, str)
        check_type(last_output_time, str)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'offset':
                offset,
            'limit':
                limit,
            'lastInputTime':
                last_input_time,
            'lastOutputTime':
                last_output_time,
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

        e_url = ('/dna/intent/api/v1/interface')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_d3d71136d95562afc211b40004d109_v2_3_7_6', json_data)

    def get_device_interface_count(self,
                                   headers=None,
                                   **request_parameters):
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

        e_url = ('/dna/intent/api/v1/interface/count')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_da44fbc3e415a99aac0bdd291e9a87a_v2_3_7_6', json_data)

    def get_interface_by_ip(self,
                            ip_address,
                            headers=None,
                            **request_parameters):
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
        """
        check_type(headers, dict)
        check_type(ip_address, str,
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
            'ipAddress': ip_address,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/interface/ip-address/{ipAddress}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_cf7fa95e3ed4527aa5ba8ca871a8c142_v2_3_7_6', json_data)

    def get_isis_interfaces(self,
                            headers=None,
                            **request_parameters):
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

        e_url = ('/dna/intent/api/v1/interface/isis')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_af71ea437c8755869b00d26ba9234dff_v2_3_7_6', json_data)

    def get_interface_info_by_id(self,
                                 device_id,
                                 headers=None,
                                 **request_parameters):
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
        """
        check_type(headers, dict)
        check_type(device_id, str,
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
            'deviceId': device_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/interface/network-device/{deviceId}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_e057192b97615f0d99a10e2b66bab13a_v2_3_7_6', json_data)

    def get_device_interface_count_by_id(self,
                                         device_id,
                                         headers=None,
                                         **request_parameters):
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
        """
        check_type(headers, dict)
        check_type(device_id, str,
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
            'deviceId': device_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/interface/network-'
                 + 'device/{deviceId}/count')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_b7d6c62ea6522081fcf55de7eb9fd7_v2_3_7_6', json_data)

    def get_interface_details(self,
                              device_id,
                              name,
                              headers=None,
                              **request_parameters):
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
        """
        check_type(headers, dict)
        check_type(name, str,
                   may_be_none=False)
        check_type(device_id, str,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'name':
                name,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'deviceId': device_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/interface/network-'
                 + 'device/{deviceId}/interface-name')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_bef9e9b306085d879b877598fad71b51_v2_3_7_6', json_data)

    def get_device_interfaces_by_specified_range(self,
                                                 device_id,
                                                 records_to_return,
                                                 start_index,
                                                 headers=None,
                                                 **request_parameters):
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
        """
        check_type(headers, dict)
        check_type(device_id, str,
                   may_be_none=False)
        check_type(start_index, int,
                   may_be_none=False)
        check_type(records_to_return, int,
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
            'deviceId': device_id,
            'startIndex': start_index,
            'recordsToReturn': records_to_return,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/interface/network-'
                 + 'device/{deviceId}/{startIndex}/{recordsToReturn}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_a3d52c630ba5deaada16fe3b07af744_v2_3_7_6', json_data)

    def get_ospf_interfaces(self,
                            headers=None,
                            **request_parameters):
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

        e_url = ('/dna/intent/api/v1/interface/ospf')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_a2868ff45f5621965f6ece01a742ce_v2_3_7_6', json_data)

    def get_interface_by_id(self,
                            id,
                            headers=None,
                            **request_parameters):
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
        """
        check_type(headers, dict)
        check_type(id, str,
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
            'id': id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/interface/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_b16bff74ae54ca88a02b34df169218_v2_3_7_6', json_data)

    def update_interface_details(self,
                                 interface_uuid,
                                 adminStatus=None,
                                 deployment_mode=None,
                                 description=None,
                                 vlanId=None,
                                 voiceVlanId=None,
                                 headers=None,
                                 payload=None,
                                 active_validation=True,
                                 **request_parameters):
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
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(deployment_mode, str)
        check_type(interface_uuid, str,
                   may_be_none=False)
        if headers is not None:
            if 'Content-Type' in headers:
                check_type(headers.get('Content-Type'),
                           str, may_be_none=False)
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'deploymentMode':
                deployment_mode,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'interfaceUuid': interface_uuid,
        }
        _payload = {
            'description':
                description,
            'adminStatus':
                adminStatus,
            'vlanId':
                vlanId,
            'voiceVlanId':
                voiceVlanId,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_b887c55faaca726bbe4ac2564_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/interface/{interfaceUuid}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload,
                                          headers=_headers)
        else:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload)

        return self._object_factory('bpm_b887c55faaca726bbe4ac2564_v2_3_7_6', json_data)

    def legit_operations_for_interface(self,
                                       interface_uuid,
                                       headers=None,
                                       **request_parameters):
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
        """
        check_type(headers, dict)
        check_type(interface_uuid, str,
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
            'interfaceUuid': interface_uuid,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/interface/{interfaceUuid}/legit-'
                 + 'operation')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_fe6d62edcec25921926043ca25f75bed_v2_3_7_6', json_data)

    def clear_mac_address_table(self,
                                interface_uuid,
                                deployment_mode=None,
                                operation=None,
                                payload=None,
                                headers=None,
                                active_validation=True,
                                **request_parameters):
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
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(deployment_mode, str)
        check_type(interface_uuid, str,
                   may_be_none=False)
        if headers is not None:
            if 'Content-Type' in headers:
                check_type(headers.get('Content-Type'),
                           str)
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'deploymentMode':
                deployment_mode,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'interfaceUuid': interface_uuid,
        }
        _payload = {
            'operation':
                operation,
            'payload':
                payload,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_e702d5786552992aa76b930780569_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/interface/{interfaceUuid}/operation')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_e702d5786552992aa76b930780569_v2_3_7_6', json_data)

    def get_device_list(self,
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
                        **request_parameters):
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
            offset(int,str): offset query parameter. offset >= 1 [X gives results from Xth device onwards] .
            limit(int,str): limit query parameter. 1 <= limit <= 500 [max. no. of devices to be returned in the result]
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
        check_type(offset, (int, str))
        check_type(limit, (int, str))
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'hostname':
                hostname,
            'managementIpAddress':
                management_ip_address,
            'macAddress':
                mac_address,
            'locationName':
                location_name,
            'serialNumber':
                serial_number,
            'location':
                location,
            'family':
                family,
            'type':
                type,
            'series':
                series,
            'collectionStatus':
                collection_status,
            'collectionInterval':
                collection_interval,
            'notSyncedForMinutes':
                not_synced_for_minutes,
            'errorCode':
                error_code,
            'errorDescription':
                error_description,
            'softwareVersion':
                software_version,
            'softwareType':
                software_type,
            'platformId':
                platform_id,
            'role':
                role,
            'reachabilityStatus':
                reachability_status,
            'upTime':
                up_time,
            'associatedWlcIp':
                associated_wlc_ip,
            'license.name':
                license_name,
            'license.type':
                license_type,
            'license.status':
                license_status,
            'module+name':
                module_name,
            'module+equpimenttype':
                module_equpimenttype,
            'module+servicestate':
                module_servicestate,
            'module+vendorequipmenttype':
                module_vendorequipmenttype,
            'module+partnumber':
                module_partnumber,
            'module+operationstatecode':
                module_operationstatecode,
            'id':
                id,
            'deviceSupportLevel':
                device_support_level,
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

        e_url = ('/dna/intent/api/v1/network-device')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_fe602e8165035b5cbc304fada4ee2f26_v2_3_7_6', json_data)

    def add_device(self,
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
                   **request_parameters):
        """Adds the device with given credential .

        Args:
            cliTransport(string): Devices's CLI transport. Supported values: telnet, ssh2 .
            computeDevice(boolean): Devices's Compute Device or not. Options are TRUE / FALSE .
            enablePassword(string): Devices's CLI enable password of the device  .
            extendedDiscoveryInfo(string): Devices's This field holds that info as whether to add device with canned
                data or not. Supported values: DISCOVER_WITH_CANNED_DATA .
            httpPassword(string): Devices's HTTP password of the device .
            httpPort(string): Devices's HTTP port of the device .
            httpSecure(boolean): Devices's Flag to select HTTP / HTTPS protocol. Options are TRUE / FALSE. TRUE for
                HTTPS and FALSE for HTTP .
            httpUserName(string): Devices's HTTP Username of the device .
            ipAddress(list): Devices's IP Address of the device  (list of strings).
            merakiOrgId(list): Devices's Selected meraki organization for which the devices needs to be imported
                (list of strings).
            netconfPort(string): Devices's Netconf Port of the device .
            password(string): Devices's CLI Password of the device .
            serialNumber(string): Devices's Serial Number of the Device .
            snmpAuthPassphrase(string): Devices's SNMPV3 auth passphrase of the device .
            snmpAuthProtocol(string): Devices's SNMPV3 auth protocol. Supported values: sha, md5 .
            snmpMode(string): Devices's SNMPV3 mode. Supported values: noAuthnoPriv, authNoPriv, authPriv .
            snmpPrivPassphrase(string): Devices's SNMPV3 priv passphrase .
            snmpPrivProtocol(string): Devices's SNMPV3 priv protocol. Supported values: AES128 .
            snmpROCommunity(string): Devices's SNMP Read Community of the device .
            snmpRWCommunity(string): Devices's SNMP Write Community of the device .
            snmpRetry(integer): Devices's SNMP retry count. Max value supported is 3. Default is Global SNMP retry
                (if exists) or 3. .
            snmpTimeout(integer): Devices's SNMP timeout in seconds. Max value supported is 300. Default is Global
                SNMP timeout (if exists) or 5. .
            snmpUserName(string): Devices's SNMPV3 user name of the device .
            snmpVersion(string): Devices's SNMP version. Values supported: v2, v3. Default is v2 .
            type(string): Devices's Type of device being added. . Available values are 'COMPUTE_DEVICE',
                'MERAKI_DASHBOARD', 'NETWORK_DEVICE', 'FIREPOWER MANAGEMENT CENTER', 'THIRD PARTY
                DEVICE' and 'NODATACHANGE'.
            userName(string): Devices's CLI user name of the device .
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
        """
        check_type(headers, dict)
        check_type(payload, dict)
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
        _payload = {
            'cliTransport':
                cliTransport,
            'computeDevice':
                computeDevice,
            'enablePassword':
                enablePassword,
            'extendedDiscoveryInfo':
                extendedDiscoveryInfo,
            'httpPassword':
                httpPassword,
            'httpPort':
                httpPort,
            'httpSecure':
                httpSecure,
            'httpUserName':
                httpUserName,
            'ipAddress':
                ipAddress,
            'merakiOrgId':
                merakiOrgId,
            'netconfPort':
                netconfPort,
            'password':
                password,
            'serialNumber':
                serialNumber,
            'snmpAuthPassphrase':
                snmpAuthPassphrase,
            'snmpAuthProtocol':
                snmpAuthProtocol,
            'snmpMode':
                snmpMode,
            'snmpPrivPassphrase':
                snmpPrivPassphrase,
            'snmpPrivProtocol':
                snmpPrivProtocol,
            'snmpROCommunity':
                snmpROCommunity,
            'snmpRWCommunity':
                snmpRWCommunity,
            'snmpRetry':
                snmpRetry,
            'snmpTimeout':
                snmpTimeout,
            'snmpUserName':
                snmpUserName,
            'snmpVersion':
                snmpVersion,
            'type':
                type,
            'userName':
                userName,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_fe3ec7651e79d891fce37a0d860_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/network-device')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_fe3ec7651e79d891fce37a0d860_v2_3_7_6', json_data)

    def sync_devices(self,
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
                     **request_parameters):
        """Update the credentials, management IP address of a given device (or a set of devices) in Catalyst Center and
        trigger an inventory sync. .

        Args:
            cliTransport(string): Devices's CLI transport. Supported values: telnet, ssh2 .
            computeDevice(boolean): Devices's Compute Device or not. Options are TRUE / FALSE .
            enablePassword(string): Devices's CLI enable password of the device .
            extendedDiscoveryInfo(string): Devices's This field holds that info as whether to add device with canned
                data or not. Supported values: DISCOVER_WITH_CANNED_DATA .
            httpPassword(string): Devices's HTTP password of the device .
            httpPort(string): Devices's HTTP port of the device .
            httpSecure(boolean): Devices's Flag to select HTTP / HTTPS protocol. Options are TRUE / FALSE. TRUE for
                HTTPS and FALSE for HTTP .
            httpUserName(string): Devices's HTTP Username of the device .
            ipAddress(list): Devices's IP Address of the device  (list of strings).
            merakiOrgId(list): Devices's Selected meraki organization for which the devices needs to be imported
                (list of strings).
            netconfPort(string): Devices's Netconf Port of the device .
            password(string): Devices's CLI Password of the device .
            serialNumber(string): Devices's Serial Number of the Device .
            snmpAuthPassphrase(string): Devices's SNMPV3 auth passphrase of the device .
            snmpAuthProtocol(string): Devices's SNMPV3 auth protocol. Supported values: sha, md5 .
            snmpMode(string): Devices's SNMPV3 mode. Supported values: noAuthnoPriv, authNoPriv, authPriv .
            snmpPrivPassphrase(string): Devices's SNMPV3 priv passphrase .
            snmpPrivProtocol(string): Devices's SNMPV3 priv protocol. Supported values: AES128 .
            snmpROCommunity(string): Devices's SNMP Read Community of the device .
            snmpRWCommunity(string): Devices's SNMP Write Community of the device .
            snmpRetry(integer): Devices's SNMP retry count. Max value supported is 3. Default is Global SNMP retry
                (if exists) or 3. .
            snmpTimeout(integer): Devices's SNMP timeout in seconds. Max value supported is 300. Default is Global
                SNMP timeout (if exists) or 5. .
            snmpUserName(string): Devices's SNMPV3 user name of the device .
            snmpVersion(string): Devices's SNMP version. Values supported: v2, v3. Default is v2 .
            type(string): Devices's Type of device being added. . Available values are 'COMPUTE_DEVICE',
                'MERAKI_DASHBOARD', 'NETWORK_DEVICE' and 'NODATACHANGE'.
            updateMgmtIPaddressList(list): Devices's updateMgmtIPaddressList (list of objects).
            userName(string): Devices's CLI user name of the device .
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
        """
        check_type(headers, dict)
        check_type(payload, dict)
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
        _payload = {
            'cliTransport':
                cliTransport,
            'computeDevice':
                computeDevice,
            'enablePassword':
                enablePassword,
            'extendedDiscoveryInfo':
                extendedDiscoveryInfo,
            'httpPassword':
                httpPassword,
            'httpPort':
                httpPort,
            'httpSecure':
                httpSecure,
            'httpUserName':
                httpUserName,
            'ipAddress':
                ipAddress,
            'merakiOrgId':
                merakiOrgId,
            'netconfPort':
                netconfPort,
            'password':
                password,
            'serialNumber':
                serialNumber,
            'snmpAuthPassphrase':
                snmpAuthPassphrase,
            'snmpAuthProtocol':
                snmpAuthProtocol,
            'snmpMode':
                snmpMode,
            'snmpPrivPassphrase':
                snmpPrivPassphrase,
            'snmpPrivProtocol':
                snmpPrivProtocol,
            'snmpROCommunity':
                snmpROCommunity,
            'snmpRWCommunity':
                snmpRWCommunity,
            'snmpRetry':
                snmpRetry,
            'snmpTimeout':
                snmpTimeout,
            'snmpUserName':
                snmpUserName,
            'snmpVersion':
                snmpVersion,
            'type':
                type,
            'updateMgmtIPaddressList':
                updateMgmtIPaddressList,
            'userName':
                userName,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_fe06867e548bba1919024b40d992_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/network-device')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload,
                                          headers=_headers)
        else:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload)

        return self._object_factory('bpm_fe06867e548bba1919024b40d992_v2_3_7_6', json_data)

    def get_device_values_that_match_fully_or_partially_an_attribute(self,
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
                                                                     **request_parameters):
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
            offset(int,str): offset query parameter.
            limit(int,str): limit query parameter.
            headers(dict): Dictionary of HTTP Headers to send with the Request
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
        check_type(offset, (int, str))
        check_type(limit, (int, str))
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'vrfName':
                vrf_name,
            'managementIpAddress':
                management_ip_address,
            'hostname':
                hostname,
            'macAddress':
                mac_address,
            'family':
                family,
            'collectionStatus':
                collection_status,
            'collectionInterval':
                collection_interval,
            'softwareVersion':
                software_version,
            'softwareType':
                software_type,
            'reachabilityStatus':
                reachability_status,
            'reachabilityFailureReason':
                reachability_failure_reason,
            'errorCode':
                error_code,
            'platformId':
                platform_id,
            'series':
                series,
            'type':
                type,
            'serialNumber':
                serial_number,
            'upTime':
                up_time,
            'role':
                role,
            'roleSource':
                role_source,
            'associatedWlcIp':
                associated_wlc_ip,
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

        e_url = ('/dna/intent/api/v1/network-device/autocomplete')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_b5a5c8da4aaa526da6a06e97c80a38be_v2_3_7_6', json_data)

    def update_device_role(self,
                           id=None,
                           role=None,
                           roleSource=None,
                           headers=None,
                           payload=None,
                           active_validation=True,
                           **request_parameters):
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
            'id':
                id,
            'role':
                role,
            'roleSource':
                roleSource,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_aa11f09d28165f4ea6c81b8642e59cc4_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/network-device/brief')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload,
                                          headers=_headers)
        else:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload)

        return self._object_factory('bpm_aa11f09d28165f4ea6c81b8642e59cc4_v2_3_7_6', json_data)

    def get_polling_interval_for_all_devices(self,
                                             headers=None,
                                             **request_parameters):
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

        e_url = ('/dna/intent/api/v1/network-device/collection-'
                 + 'schedule/global')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_ce94ab18ad505e8a9846f6c4c9df0d2b_v2_3_7_6', json_data)

    def get_device_config_for_all_devices(self,
                                          headers=None,
                                          **request_parameters):
        """Returns the config for all devices. This API has been deprecated and will not be available in a Cisco Catalyst
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

        e_url = ('/dna/intent/api/v1/network-device/config')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_ed2bca4be412527198720a4dfec9604a_v2_3_7_6', json_data)

    def get_device_config_count(self,
                                headers=None,
                                **request_parameters):
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

        e_url = ('/dna/intent/api/v1/network-device/config/count')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_dc0a72537a3578ca31cc5ef29131d35_v2_3_7_6', json_data)

    def get_device_count(self,
                         hostname=None,
                         location_name=None,
                         mac_address=None,
                         management_ip_address=None,
                         headers=None,
                         **request_parameters):
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
        """
        check_type(headers, dict)
        check_type(hostname, (str, list, set, tuple))
        check_type(management_ip_address, (str, list, set, tuple))
        check_type(mac_address, (str, list, set, tuple))
        check_type(location_name, (str, list, set, tuple))
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'hostname':
                hostname,
            'managementIpAddress':
                management_ip_address,
            'macAddress':
                mac_address,
            'locationName':
                location_name,
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

        e_url = ('/dna/intent/api/v1/network-device/count')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_bbfe7340fe6752e5bc273a303d165654_v2_3_7_6', json_data)

    def export_device_list(self,
                           deviceUuids=None,
                           operationEnum=None,
                           parameters=None,
                           password=None,
                           headers=None,
                           payload=None,
                           active_validation=True,
                           **request_parameters):
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
            'deviceUuids':
                deviceUuids,
            'operationEnum':
                operationEnum,
            'parameters':
                parameters,
            'password':
                password,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_e6ec627d3c587288978990aae75228_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/network-device/file')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_e6ec627d3c587288978990aae75228_v2_3_7_6', json_data)

    def get_functional_capability_for_devices(self,
                                              device_id,
                                              function_name=None,
                                              headers=None,
                                              **request_parameters):
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
        """
        check_type(headers, dict)
        check_type(device_id, str,
                   may_be_none=False)
        check_type(function_name, (str, list, set, tuple))
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'deviceId':
                device_id,
            'functionName':
                function_name,
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

        e_url = ('/dna/intent/api/v1/network-device/functional-capability')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_ad8cea95d71352f0842a2c869765e6cf_v2_3_7_6', json_data)

    def get_functional_capability_by_id(self,
                                        id,
                                        headers=None,
                                        **request_parameters):
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
        """
        check_type(headers, dict)
        check_type(id, str,
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
            'id': id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/network-device/functional-'
                 + 'capability/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_f494532c45654fdaeda8d46a0d9753d_v2_3_7_6', json_data)

    def inventory_insight_device_link_mismatch(self,
                                               category,
                                               site_id,
                                               limit=None,
                                               offset=None,
                                               order=None,
                                               sort_by=None,
                                               headers=None,
                                               **request_parameters):
        """Find all devices with link mismatch (speed /  vlan) .

        Args:
            site_id(str): siteId path parameter.
            offset(int,str): offset query parameter. Row Number.  Default value is 1 .
            limit(int,str): limit query parameter. Default value is 500 .
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
        """
        check_type(headers, dict)
        check_type(offset, (int, str))
        check_type(limit, (int, str))
        check_type(category, str,
                   may_be_none=False)
        check_type(sort_by, str)
        check_type(order, str)
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
            'category':
                category,
            'sortBy':
                sort_by,
            'order':
                order,
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

        e_url = ('/dna/intent/api/v1/network-'
                 + 'device/insight/{siteId}/device-link')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_eed1595442b757bf94938c858a257ced_v2_3_7_6', json_data)

    def get_network_device_by_ip(self,
                                 ip_address,
                                 headers=None,
                                 **request_parameters):
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
        """
        check_type(headers, dict)
        check_type(ip_address, str,
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
            'ipAddress': ip_address,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/network-device/ip-address/{ipAddress}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_dc74c2052a3a4eb7e2a01eaa8e7_v2_3_7_6', json_data)

    def get_modules(self,
                    device_id,
                    limit=None,
                    name_list=None,
                    offset=None,
                    operational_state_code_list=None,
                    part_number_list=None,
                    vendor_equipment_type_list=None,
                    headers=None,
                    **request_parameters):
        """Returns modules by specified device id .

        Args:
            device_id(str): deviceId query parameter.
            limit(int,str): limit query parameter.
            offset(int,str): offset query parameter.
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
        """
        check_type(headers, dict)
        check_type(device_id, str,
                   may_be_none=False)
        check_type(limit, (int, str))
        check_type(offset, (int, str))
        check_type(name_list, (str, list, set, tuple))
        check_type(vendor_equipment_type_list, (str, list, set, tuple))
        check_type(part_number_list, (str, list, set, tuple))
        check_type(operational_state_code_list, (str, list, set, tuple))
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'deviceId':
                device_id,
            'limit':
                limit,
            'offset':
                offset,
            'nameList':
                name_list,
            'vendorEquipmentTypeList':
                vendor_equipment_type_list,
            'partNumberList':
                part_number_list,
            'operationalStateCodeList':
                operational_state_code_list,
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

        e_url = ('/dna/intent/api/v1/network-device/module')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_ce9e547725c45c66824afda98179d12f_v2_3_7_6', json_data)

    def get_module_count(self,
                         device_id,
                         name_list=None,
                         operational_state_code_list=None,
                         part_number_list=None,
                         vendor_equipment_type_list=None,
                         headers=None,
                         **request_parameters):
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
        """
        check_type(headers, dict)
        check_type(device_id, str,
                   may_be_none=False)
        check_type(name_list, (str, list, set, tuple))
        check_type(vendor_equipment_type_list, (str, list, set, tuple))
        check_type(part_number_list, (str, list, set, tuple))
        check_type(operational_state_code_list, (str, list, set, tuple))
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'deviceId':
                device_id,
            'nameList':
                name_list,
            'vendorEquipmentTypeList':
                vendor_equipment_type_list,
            'partNumberList':
                part_number_list,
            'operationalStateCodeList':
                operational_state_code_list,
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

        e_url = ('/dna/intent/api/v1/network-device/module/count')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_fb11f997009751c991884b5fc02087c5_v2_3_7_6', json_data)

    def get_module_info_by_id(self,
                              id,
                              headers=None,
                              **request_parameters):
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
        """
        check_type(headers, dict)
        check_type(id, str,
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
            'id': id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/network-device/module/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_a4588640da5b018b499c5760f4092a_v2_3_7_6', json_data)

    def get_device_by_serial_number(self,
                                    serial_number,
                                    headers=None,
                                    **request_parameters):
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
        """
        check_type(headers, dict)
        check_type(serial_number, str,
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
            'serialNumber': serial_number,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/network-device/serial-'
                 + 'number/{serialNumber}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_c53d56c282e5f108c659009d21f9d26_v2_3_7_6', json_data)

    def sync_devices_using_forcesync(self,
                                     force_sync=None,
                                     headers=None,
                                     payload=None,
                                     active_validation=True,
                                     **request_parameters):
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
        """
        check_type(headers, dict)
        check_type(payload, list)
        check_type(force_sync, bool)
        if headers is not None:
            if 'Content-Type' in headers:
                check_type(headers.get('Content-Type'),
                           str, may_be_none=False)
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'forceSync':
                force_sync,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }
        _payload = payload or []
        if active_validation:
            self._request_validator('jsd_f2c120b855cb8c852806ce72e54d_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/network-device/sync')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload,
                                          headers=_headers)
        else:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload)

        return self._object_factory('bpm_f2c120b855cb8c852806ce72e54d_v2_3_7_6', json_data)

    def get_devices_registered_for_wsa_notification(self,
                                                    macaddress=None,
                                                    serial_number=None,
                                                    headers=None,
                                                    **request_parameters):
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
        """
        check_type(headers, dict)
        check_type(serial_number, str)
        check_type(macaddress, str)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'serialNumber':
                serial_number,
            'macaddress':
                macaddress,
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

        e_url = ('/dna/intent/api/v1/network-device/tenantinfo/macaddress')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_b2c39feb5e48913492c33add7f13_v2_3_7_6', json_data)

    def get_all_user_defined_fields(self,
                                    id=None,
                                    name=None,
                                    headers=None,
                                    **request_parameters):
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
        """
        check_type(headers, dict)
        check_type(id, str)
        check_type(name, str)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'id':
                id,
            'name':
                name,
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

        e_url = ('/dna/intent/api/v1/network-device/user-defined-field')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_d31b0bb4bde55bb8a3078b66c81f3a22_v2_3_7_6', json_data)

    def create_user_defined_field(self,
                                  description=None,
                                  name=None,
                                  headers=None,
                                  payload=None,
                                  active_validation=True,
                                  **request_parameters):
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
        """
        check_type(headers, dict)
        check_type(payload, dict)
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
        _payload = {
            'name':
                name,
            'description':
                description,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_ed266e6eda225aedbf581508635da822_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/network-device/user-defined-field')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_ed266e6eda225aedbf581508635da822_v2_3_7_6', json_data)

    def update_user_defined_field(self,
                                  id,
                                  description=None,
                                  name=None,
                                  headers=None,
                                  payload=None,
                                  active_validation=True,
                                  **request_parameters):
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
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(id, str,
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
            'id': id,
        }
        _payload = {
            'name':
                name,
            'description':
                description,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_d76a951f85a7a927afc2f1ea935c8_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/network-device/user-defined-'
                 + 'field/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload,
                                          headers=_headers)
        else:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload)

        return self._object_factory('bpm_d76a951f85a7a927afc2f1ea935c8_v2_3_7_6', json_data)

    def delete_user_defined_field(self,
                                  id,
                                  headers=None,
                                  **request_parameters):
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
        """
        check_type(headers, dict)
        check_type(id, str,
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
            'id': id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/network-device/user-defined-'
                 + 'field/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(endpoint_full_url, params=_params,
                                             headers=_headers)
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_f0f19119501094fb5fafe05dfbca_v2_3_7_6', json_data)

    def get_chassis_details_for_device(self,
                                       device_id,
                                       headers=None,
                                       **request_parameters):
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
        """
        check_type(headers, dict)
        check_type(device_id, str,
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
            'deviceId': device_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/network-device/{deviceId}/chassis')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_a03cee8dfd7514487a134a422f5e0d7_v2_3_7_6', json_data)

    def get_stack_details_for_device(self,
                                     device_id,
                                     headers=None,
                                     **request_parameters):
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
        """
        check_type(headers, dict)
        check_type(device_id, str,
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
            'deviceId': device_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/network-device/{deviceId}/stack')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_c07eaefa1fa45faa801764d9094336ae_v2_3_7_6', json_data)

    def remove_user_defined_field_from_device(self,
                                              device_id,
                                              name,
                                              headers=None,
                                              **request_parameters):
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
        """
        check_type(headers, dict)
        check_type(name, str,
                   may_be_none=False)
        check_type(device_id, str,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'name':
                name,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'deviceId': device_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/network-device/{deviceId}/user-'
                 + 'defined-field')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(endpoint_full_url, params=_params,
                                             headers=_headers)
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_c1144f7a496455f99f95d36d6474c4b4_v2_3_7_6', json_data)

    def add_user_defined_field_to_device(self,
                                         device_id,
                                         headers=None,
                                         payload=None,
                                         active_validation=True,
                                         **request_parameters):
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
        """
        check_type(headers, dict)
        check_type(payload, list)
        check_type(device_id, str,
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
            'deviceId': device_id,
        }
        _payload = payload or []
        if active_validation:
            self._request_validator('jsd_a73fbc67627e5bbbafe748de84d42df6_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/network-device/{deviceId}/user-'
                 + 'defined-field')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload,
                                          headers=_headers)
        else:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload)

        return self._object_factory('bpm_a73fbc67627e5bbbafe748de84d42df6_v2_3_7_6', json_data)

    def get_the_details_of_physical_components_of_the_given_device(self,
                                                                   device_uuid,
                                                                   type=None,
                                                                   headers=None,
                                                                   **request_parameters):
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
        """
        check_type(headers, dict)
        check_type(type, str)
        check_type(device_uuid, str,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'type':
                type,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'deviceUuid': device_uuid,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/network-device/{deviceUuid}/equipment')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_c1cb24a2b53ce8d29d119c6ee1112_v2_3_7_6', json_data)

    def poe_interface_details(self,
                              device_uuid,
                              interface_name_list=None,
                              headers=None,
                              **request_parameters):
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
        """
        check_type(headers, dict)
        check_type(interface_name_list, str)
        check_type(device_uuid, str,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'interfaceNameList':
                interface_name_list,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'deviceUuid': device_uuid,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/network-'
                 + 'device/{deviceUuid}/interface/poe-detail')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_ab3215d9be065533b7cbbc978cb4d905_v2_3_7_6', json_data)

    def get_connected_device_detail(self,
                                    device_uuid,
                                    interface_uuid,
                                    headers=None,
                                    **request_parameters):
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
        """
        check_type(headers, dict)
        check_type(device_uuid, str,
                   may_be_none=False)
        check_type(interface_uuid, str,
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
            'deviceUuid': device_uuid,
            'interfaceUuid': interface_uuid,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/network-'
                 + 'device/{deviceUuid}/interface/{interfaceUuid}/neighbor')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_a1878314ffd35d29bea49f12d10b59c8_v2_3_7_6', json_data)

    def get_linecard_details(self,
                             device_uuid,
                             headers=None,
                             **request_parameters):
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
        """
        check_type(headers, dict)
        check_type(device_uuid, str,
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
            'deviceUuid': device_uuid,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/network-device/{deviceUuid}/line-card')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_bd31690b61f45d9f880d74d4e682b070_v2_3_7_6', json_data)

    def poe_details_(self,
                     device_uuid,
                     headers=None,
                     **request_parameters):
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
        """
        return self.poe_details(device_uuid,
                                headers=headers,
                                **request_parameters)

    def poe_details(self,
                    device_uuid,
                    headers=None,
                    **request_parameters):
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
        """
        check_type(headers, dict)
        check_type(device_uuid, str,
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
            'deviceUuid': device_uuid,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/network-device/{deviceUuid}/poe')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_f7a67aba0b365a1e9dae62d148511a25_v2_3_7_6', json_data)

    def get_supervisor_card_detail(self,
                                   device_uuid,
                                   headers=None,
                                   **request_parameters):
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
        """
        check_type(headers, dict)
        check_type(device_uuid, str,
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
            'deviceUuid': device_uuid,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/network-'
                 + 'device/{deviceUuid}/supervisor-card')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_eb13516155a28570e542dcf10a91_v2_3_7_6', json_data)

    def update_device_management_address(self,
                                         deviceid,
                                         newIP=None,
                                         headers=None,
                                         payload=None,
                                         active_validation=True,
                                         **request_parameters):
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
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(deviceid, str,
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
            'deviceid': deviceid,
        }
        _payload = {
            'newIP':
                newIP,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_cb98464ddb5ee9ba7ebb4428443ba9_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/network-device/{deviceid}/management-'
                 + 'address')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload,
                                          headers=_headers)
        else:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload)

        return self._object_factory('bpm_cb98464ddb5ee9ba7ebb4428443ba9_v2_3_7_6', json_data)

    def get_device_by_id(self,
                         id,
                         headers=None,
                         **request_parameters):
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
        """
        check_type(headers, dict)
        check_type(id, str,
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
            'id': id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/network-device/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_d86f657f8592f97014d2ebf8d37ac_v2_3_7_6', json_data)

    def delete_device_by_id(self,
                            id,
                            clean_config=None,
                            headers=None,
                            **request_parameters):
        """Deletes the network device for the given Id .

        Args:
            id(str): id path parameter. Device ID .
            clean_config(bool): cleanConfig query parameter.
            headers(dict): Dictionary of HTTP Headers to send with the Request
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
        """
        check_type(headers, dict)
        check_type(clean_config, bool)
        check_type(id, str,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'cleanConfig':
                clean_config,
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

        e_url = ('/dna/intent/api/v1/network-device/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(endpoint_full_url, params=_params,
                                             headers=_headers)
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_e01233fa258e393239c4b41882806_v2_3_7_6', json_data)

    def get_device_summary(self,
                           id,
                           headers=None,
                           **request_parameters):
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
        """
        check_type(headers, dict)
        check_type(id, str,
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
            'id': id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/network-device/{id}/brief')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_fe0153ca24205608b8741d51f5a6d54a_v2_3_7_6', json_data)

    def get_polling_interval_by_id(self,
                                   id,
                                   headers=None,
                                   **request_parameters):
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
        """
        check_type(headers, dict)
        check_type(id, str,
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
            'id': id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/network-device/{id}/collection-'
                 + 'schedule')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_f90daf1c279351f884ba3198d3b2d641_v2_3_7_6', json_data)

    def get_organization_list_for_meraki(self,
                                         id,
                                         headers=None,
                                         **request_parameters):
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
        """
        check_type(headers, dict)
        check_type(id, str,
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
            'id': id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/network-device/{id}/meraki-'
                 + 'organization')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_b4ba6d23d5e7eb62cbba4c9e1a29d_v2_3_7_6', json_data)

    def get_device_interface_vlans(self,
                                   id,
                                   interface_type=None,
                                   headers=None,
                                   **request_parameters):
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
        """
        check_type(headers, dict)
        check_type(interface_type, str)
        check_type(id, str,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'interfaceType':
                interface_type,
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

        e_url = ('/dna/intent/api/v1/network-device/{id}/vlan')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_fd5fb603cba6523abb25c8ec131fbb8b_v2_3_7_6', json_data)

    def get_wireless_lan_controller_details_by_id(self,
                                                  id,
                                                  headers=None,
                                                  **request_parameters):
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
        """
        check_type(headers, dict)
        check_type(id, str,
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
            'id': id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/network-device/{id}/wireless-info')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_c01ee650fcf858789ca00c8deda969b9_v2_3_7_6', json_data)

    def get_device_config_by_id(self,
                                network_device_id,
                                headers=None,
                                **request_parameters):
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
        """
        check_type(headers, dict)
        check_type(network_device_id, str,
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
            'networkDeviceId': network_device_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/network-'
                 + 'device/{networkDeviceId}/config')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_af0bbf34adb5146b931ec874fc2cc40_v2_3_7_6', json_data)

    def get_network_device_by_pagination_range(self,
                                               records_to_return,
                                               start_index,
                                               headers=None,
                                               **request_parameters):
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
        """
        check_type(headers, dict)
        check_type(start_index, int,
                   may_be_none=False)
        check_type(records_to_return, int,
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
            'startIndex': start_index,
            'recordsToReturn': records_to_return,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/network-'
                 + 'device/{startIndex}/{recordsToReturn}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_d7b6ce5abd5dad837e22ace817a6f0_v2_3_7_6', json_data)

    def get_device_interface_stats_info(self,
                                        device_id,
                                        endTime=None,
                                        query=None,
                                        startTime=None,
                                        headers=None,
                                        payload=None,
                                        active_validation=True,
                                        **request_parameters):
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
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(device_id, str,
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
            'deviceId': device_id,
        }
        _payload = {
            'startTime':
                startTime,
            'endTime':
                endTime,
            'query':
                query,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_a9e0722d184658c592bd130ff03e1dde_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v2/networkDevices/{deviceId}/interfaces/'
                 + 'query')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_a9e0722d184658c592bd130ff03e1dde_v2_3_7_6', json_data)

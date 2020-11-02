# -*- coding: utf-8 -*-
"""DNA Center Devices API wrapper.

Copyright (c) 2019-2020 Cisco and/or its affiliates.

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


from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

from builtins import *

from past.builtins import basestring

from ...restsession import RestSession
from ...utils import (
    check_type,
    dict_from_items_with_values,
    apply_path_params,
    dict_of_str,
)


class Devices(object):
    """DNA Center Devices API (version: 1.2.10).

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

    def get_module_info_by_id(self,
                              id,
                              headers=None,
                              **request_parameters):
        """Returns Module info by id.

        Args:
            id(basestring): Module UUID.
            headers(dict): Dictionary of HTTP Headers to send with the Request
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
        check_type(id, basestring,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        params = {
        }
        params.update(request_parameters)
        params = dict_from_items_with_values(params)

        path_params = {
            'id': id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/network-device/module/${id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=params)

        return self._object_factory('bpm_0db7da744c0b83d8_v1_2_10', json_data)

    def get_device_interface_count(self,
                                   headers=None,
                                   **request_parameters):
        """Returns the count of interfaces for all devices.

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
                           basestring, may_be_none=False)

        params = {
        }
        params.update(request_parameters)
        params = dict_from_items_with_values(params)

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
            json_data = self._session.get(endpoint_full_url, params=params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=params)

        return self._object_factory('bpm_3d923b184dc9a4ca_v1_2_10', json_data)

    def sync_devices_using_forcesync(self,
                                     force_sync=None,
                                     headers=None,
                                     payload=None,
                                     active_validation=True,
                                     **request_parameters):
        """Synchronizes the devices. If forceSync param is false (default)
        then the sync would run in normal priority thread. If
        forceSync param is true then the sync would run in high
        priority thread if available, else the sync will fail.
        Result can be seen in the child task of each device.

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
                           basestring, may_be_none=False)
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        params = {
            'forceSync':
                force_sync,
        }
        params.update(request_parameters)
        params = dict_from_items_with_values(params)

        path_params = {
        }

        _payload = payload or []
        if active_validation:
            self._request_validator('jsd_3b9ef9674429be4c_v1_2_10')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/network-device/sync')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(endpoint_full_url, params=params,
                                          json=_payload,
                                          headers=_headers)
        else:
            json_data = self._session.put(endpoint_full_url, params=params,
                                          json=_payload)

        return self._object_factory('bpm_3b9ef9674429be4c_v1_2_10', json_data)

    def get_device_list(self,
                        associated_wlc_ip=None,
                        collection_interval=None,
                        collection_status=None,
                        error_code=None,
                        error_description=None,
                        family=None,
                        hostname=None,
                        id=None,
                        license_name=None,
                        license_status=None,
                        license_type=None,
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
        """Returns list of network devices based on filter criteria such as
        management IP address, mac address, hostname, location
        name and a wide variety of additional criteria. You can
        also use the asterisk in any value to conduct a wildcard
        search. For example, to find all hostnames beginning
        with myhost in the IP address range 192.25.18.n, issue
        the following request: GET
        fqdnoripofdnacenterplatform/dna/intent/api/v1/network-
        device? hostname=myhost* &
        managementIpAddress=192.25.18.* For a complete list of
        parameter names that you can use for filtering this
        request, see the DNA Center API Reference documentation.
        Note: If id parameter is provided, it will return the
        list of network-devices for the given ids and ignores
        the other request parameters. .

        Args:
            hostname(basestring): hostname query parameter. Accepts
                comma separated values.
            management_ip_address(basestring): managementIpAddress
                query parameter. Accepts comma separated
                values.
            mac_address(basestring): macAddress query parameter.
                Accepts comma separated values.
            location_name(basestring): locationName query parameter.
                Accepts comma separated values.
            serial_number(basestring): serialNumber query parameter.
                Accepts comma separated values.
            location(basestring): location query parameter. Accepts
                comma separated values.
            family(basestring): family query parameter. Accepts
                comma separated values.
            type(basestring): type query parameter. Accepts comma
                separated values.
            series(basestring): series query parameter. Accepts
                comma separated values.
            collection_status(basestring): collectionStatus query
                parameter. Accepts comma separated
                values.
            collection_interval(basestring): collectionInterval
                query parameter. Accepts comma separated
                values.
            not_synced_for_minutes(basestring): notSyncedForMinutes
                query parameter. Accepts comma separated
                values.
            error_code(basestring): errorCode query parameter.
                Accepts comma separated values.
            error_description(basestring): errorDescription query
                parameter. Accepts comma separated
                values.
            software_version(basestring): softwareVersion query
                parameter. Accepts comma separated
                values.
            software_type(basestring): softwareType query parameter.
                Accepts comma separated values.
            platform_id(basestring): platformId query parameter.
                Accepts comma separated values.
            role(basestring): role query parameter. Accepts comma
                separated values.
            reachability_status(basestring): reachabilityStatus
                query parameter. Accepts comma separated
                values.
            up_time(basestring): upTime query parameter. Accepts
                comma separated values.
            associated_wlc_ip(basestring): associatedWlcIp query
                parameter. Accepts comma separated
                values.
            license_name(basestring): license.name query parameter.
                Accepts comma separated values.
            license_type(basestring): license.type query parameter.
                Accepts comma separated values.
            license_status(basestring): license.status query
                parameter. Accepts comma separated
                values.
            module_name(basestring): module+name query parameter.
                Accepts comma separated values.
            module_equpimenttype(basestring): module+equpimenttype
                query parameter. Accepts comma separated
                values.
            module_servicestate(basestring): module+servicestate
                query parameter. Accepts comma separated
                values.
            module_vendorequipmenttype(basestring):
                module+vendorequipmenttype query
                parameter. Accepts comma separated
                values.
            module_partnumber(basestring): module+partnumber query
                parameter. Accepts comma separated
                values.
            module_operationstatecode(basestring):
                module+operationstatecode query
                parameter. Accepts comma separated
                values.
            id(basestring): Accepts comma separated id's and return
                list of network-devices for the given
                id's. If invalid or not-found id's are
                provided, null entry will be returned in
                the list.
            headers(dict): Dictionary of HTTP Headers to send with the Request
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
        check_type(hostname, basestring)
        check_type(management_ip_address, basestring)
        check_type(mac_address, basestring)
        check_type(location_name, basestring)
        check_type(serial_number, basestring)
        check_type(location, basestring)
        check_type(family, basestring)
        check_type(type, basestring)
        check_type(series, basestring)
        check_type(collection_status, basestring)
        check_type(collection_interval, basestring)
        check_type(not_synced_for_minutes, basestring)
        check_type(error_code, basestring)
        check_type(error_description, basestring)
        check_type(software_version, basestring)
        check_type(software_type, basestring)
        check_type(platform_id, basestring)
        check_type(role, basestring)
        check_type(reachability_status, basestring)
        check_type(up_time, basestring)
        check_type(associated_wlc_ip, basestring)
        check_type(license_name, basestring)
        check_type(license_type, basestring)
        check_type(license_status, basestring)
        check_type(module_name, basestring)
        check_type(module_equpimenttype, basestring)
        check_type(module_servicestate, basestring)
        check_type(module_vendorequipmenttype, basestring)
        check_type(module_partnumber, basestring)
        check_type(module_operationstatecode, basestring)
        check_type(id, basestring)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        params = {
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
        }
        params.update(request_parameters)
        params = dict_from_items_with_values(params)

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
            json_data = self._session.get(endpoint_full_url, params=params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=params)

        return self._object_factory('bpm_20b19b52464b8972_v1_2_10', json_data)

    def get_polling_interval_for_all_devices(self,
                                             headers=None,
                                             **request_parameters):
        """Returns polling interval of all devices.

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
                           basestring, may_be_none=False)

        params = {
        }
        params.update(request_parameters)
        params = dict_from_items_with_values(params)

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
            json_data = self._session.get(endpoint_full_url, params=params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=params)

        return self._object_factory('bpm_38bd0b884b89a785_v1_2_10', json_data)

    def get_device_count(self,
                         headers=None,
                         **request_parameters):
        """Returns the count of network devices based on the filter
        criteria by management IP address, mac address, hostname
        and location name.

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
                           basestring, may_be_none=False)

        params = {
        }
        params.update(request_parameters)
        params = dict_from_items_with_values(params)

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
            json_data = self._session.get(endpoint_full_url, params=params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=params)

        return self._object_factory('bpm_5db21b8e43fab7d8_v1_2_10', json_data)

    def get_device_interface_vlans(self,
                                   id,
                                   interface_type=None,
                                   headers=None,
                                   **request_parameters):
        """Returns Device Interface VLANs.

        Args:
            id(basestring): id path parameter.
            interface_type(basestring): Vlan assocaited with sub-
                interface.
            headers(dict): Dictionary of HTTP Headers to send with the Request
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
        check_type(interface_type, basestring)
        check_type(id, basestring,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        params = {
            'interfaceType':
                interface_type,
        }
        params.update(request_parameters)
        params = dict_from_items_with_values(params)

        path_params = {
            'id': id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/network-device/${id}/vlan')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=params)

        return self._object_factory('bpm_288df9494f2a9746_v1_2_10', json_data)

    def get_device_interfaces_by_specified_range(self,
                                                 device_id,
                                                 records_to_return,
                                                 start_index,
                                                 headers=None,
                                                 **request_parameters):
        """Returns the list of interfaces for the device for the specified
        range.

        Args:
            device_id(basestring): Device ID.
            start_index(int): Start index.
            records_to_return(int): Number of records to return.
            headers(dict): Dictionary of HTTP Headers to send with the Request
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
        check_type(device_id, basestring,
                   may_be_none=False)
        check_type(start_index, int,
                   may_be_none=False)
        check_type(records_to_return, int,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        params = {
        }
        params.update(request_parameters)
        params = dict_from_items_with_values(params)

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
                 + 'device/${deviceId}/${startIndex}/${recordsToReturn}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=params)

        return self._object_factory('bpm_349c888443b89a58_v1_2_10', json_data)

    def delete_device_by_id(self,
                            id,
                            is_force_delete=None,
                            headers=None,
                            **request_parameters):
        """Deletes the network device for the given Id.

        Args:
            id(basestring): Device ID.
            is_force_delete(bool): isForceDelete query parameter.
            headers(dict): Dictionary of HTTP Headers to send with the Request
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
        check_type(is_force_delete, bool)
        check_type(id, basestring,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        params = {
            'isForceDelete':
                is_force_delete,
        }
        params.update(request_parameters)
        params = dict_from_items_with_values(params)

        path_params = {
            'id': id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/network-device/${id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(endpoint_full_url, params=params,
                                             headers=_headers)
        else:
            json_data = self._session.delete(endpoint_full_url, params=params)

        return self._object_factory('bpm_1c894b5848eab214_v1_2_10', json_data)

    def get_device_config_by_id(self,
                                network_device_id,
                                headers=None,
                                **request_parameters):
        """Returns the device config by specified device ID.

        Args:
            network_device_id(basestring): networkDeviceId path
                parameter.
            headers(dict): Dictionary of HTTP Headers to send with the Request
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
        check_type(network_device_id, basestring,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        params = {
        }
        params.update(request_parameters)
        params = dict_from_items_with_values(params)

        path_params = {
            'networkDeviceId': network_device_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/network-'
                 + 'device/${networkDeviceId}/config')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=params)

        return self._object_factory('bpm_84b33a9e480abcaf_v1_2_10', json_data)

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
                   updateMgmtIPaddressList=None,
                   userName=None,
                   headers=None,
                   payload=None,
                   active_validation=True,
                   **request_parameters):
        """Adds the device with given credential.

        Args:
            cliTransport(string): InventoryDeviceInfo's
                cliTransport.
            computeDevice(boolean): InventoryDeviceInfo's
                computeDevice.
            enablePassword(string): InventoryDeviceInfo's
                enablePassword.
            extendedDiscoveryInfo(string): InventoryDeviceInfo's
                extendedDiscoveryInfo.
            httpPassword(string): InventoryDeviceInfo's
                httpPassword.
            httpPort(string): InventoryDeviceInfo's httpPort.
            httpSecure(boolean): InventoryDeviceInfo's httpSecure.
            httpUserName(string): InventoryDeviceInfo's
                httpUserName.
            ipAddress(list): InventoryDeviceInfo's ipAddress (list
                of strings).
            merakiOrgId(list): InventoryDeviceInfo's merakiOrgId
                (list of strings).
            netconfPort(string): InventoryDeviceInfo's netconfPort.
            password(string): InventoryDeviceInfo's password.
            serialNumber(string): InventoryDeviceInfo's
                serialNumber.
            snmpAuthPassphrase(string): InventoryDeviceInfo's
                snmpAuthPassphrase.
            snmpAuthProtocol(string): InventoryDeviceInfo's
                snmpAuthProtocol.
            snmpMode(string): InventoryDeviceInfo's snmpMode.
            snmpPrivPassphrase(string): InventoryDeviceInfo's
                snmpPrivPassphrase.
            snmpPrivProtocol(string): InventoryDeviceInfo's
                snmpPrivProtocol.
            snmpROCommunity(string): InventoryDeviceInfo's
                snmpROCommunity.
            snmpRWCommunity(string): InventoryDeviceInfo's
                snmpRWCommunity.
            snmpRetry(number): InventoryDeviceInfo's snmpRetry.
            snmpTimeout(number): InventoryDeviceInfo's snmpTimeout.
            snmpUserName(string): InventoryDeviceInfo's
                snmpUserName.
            snmpVersion(string): InventoryDeviceInfo's snmpVersion.
            type(string): InventoryDeviceInfo's type. Available
                values are 'COMPUTE_DEVICE',
                'MERAKI_DASHBOARD', 'NETWORK_DEVICE' and
                'NODATACHANGE'.
            updateMgmtIPaddressList(list): InventoryDeviceInfo's
                updateMgmtIPaddressList (list of
                objects).
            userName(string): InventoryDeviceInfo's userName.
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
                           basestring, may_be_none=False)
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        params = {
        }
        params.update(request_parameters)
        params = dict_from_items_with_values(params)

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
            self._request_validator('jsd_4bb22af046fa8f08_v1_2_10')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/network-device')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=params,
                                           json=_payload)

        return self._object_factory('bpm_4bb22af046fa8f08_v1_2_10', json_data)

    def get_device_config_count(self,
                                headers=None,
                                **request_parameters):
        """Returns the count of device configs.

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
                           basestring, may_be_none=False)

        params = {
        }
        params.update(request_parameters)
        params = dict_from_items_with_values(params)

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
            json_data = self._session.get(endpoint_full_url, params=params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=params)

        return self._object_factory('bpm_888f585c49b88441_v1_2_10', json_data)

    def get_interface_details(self,
                              device_id,
                              name,
                              headers=None,
                              **request_parameters):
        """Returns interface by specified device Id and interface name.

        Args:
            device_id(basestring): Device ID.
            name(basestring): Interface name.
            headers(dict): Dictionary of HTTP Headers to send with the Request
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
        check_type(name, basestring,
                   may_be_none=False)
        check_type(device_id, basestring,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        params = {
            'name':
                name,
        }
        params.update(request_parameters)
        params = dict_from_items_with_values(params)

        path_params = {
            'deviceId': device_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/interface/network-'
                 + 'device/${deviceId}/interface-name')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=params)

        return self._object_factory('bpm_4eb56a614cc9a2d2_v1_2_10', json_data)

    def get_polling_interval_by_id(self,
                                   id,
                                   headers=None,
                                   **request_parameters):
        """Returns polling interval by device id.

        Args:
            id(basestring): Device ID.
            headers(dict): Dictionary of HTTP Headers to send with the Request
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
        check_type(id, basestring,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        params = {
        }
        params.update(request_parameters)
        params = dict_from_items_with_values(params)

        path_params = {
            'id': id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/network-device/${id}/collection-'
                 + 'schedule')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=params)

        return self._object_factory('bpm_82918a1b4d289c5c_v1_2_10', json_data)

    def get_module_count(self,
                         device_id,
                         name_list=None,
                         operational_state_code_list=None,
                         part_number_list=None,
                         vendor_equipment_type_list=None,
                         headers=None,
                         **request_parameters):
        """Returns Module Count.

        Args:
            device_id(basestring): deviceId query parameter.
            name_list(basestring): nameList query parameter. Accepts
                comma separated values.
            vendor_equipment_type_list(basestring):
                vendorEquipmentTypeList query parameter.
                Accepts comma separated values.
            part_number_list(basestring): partNumberList query
                parameter. Accepts comma separated
                values.
            operational_state_code_list(basestring):
                operationalStateCodeList query
                parameter. Accepts comma separated
                values.
            headers(dict): Dictionary of HTTP Headers to send with the Request
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
        check_type(device_id, basestring,
                   may_be_none=False)
        check_type(name_list, basestring)
        check_type(vendor_equipment_type_list, basestring)
        check_type(part_number_list, basestring)
        check_type(operational_state_code_list, basestring)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        params = {
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
        params.update(request_parameters)
        params = dict_from_items_with_values(params)

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
            json_data = self._session.get(endpoint_full_url, params=params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=params)

        return self._object_factory('bpm_8db939744649a782_v1_2_10', json_data)

    def get_device_interface_count_by_id(self,
                                         device_id,
                                         headers=None,
                                         **request_parameters):
        """Returns the interface count for the given device.

        Args:
            device_id(basestring): Device ID.
            headers(dict): Dictionary of HTTP Headers to send with the Request
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
        check_type(device_id, basestring,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        params = {
        }
        params.update(request_parameters)
        params = dict_from_items_with_values(params)

        path_params = {
            'deviceId': device_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/interface/network-'
                 + 'device/${deviceId}/count')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=params)

        return self._object_factory('bpm_5b8639224cd88ea7_v1_2_10', json_data)

    def get_organization_list_for_meraki(self,
                                         id,
                                         headers=None,
                                         **request_parameters):
        """Returns list of organizations for meraki dashboard.

        Args:
            id(basestring): Device ID.
            headers(dict): Dictionary of HTTP Headers to send with the Request
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
        check_type(id, basestring,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        params = {
        }
        params.update(request_parameters)
        params = dict_from_items_with_values(params)

        path_params = {
            'id': id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/network-device/${id}/meraki-'
                 + 'organization')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=params)

        return self._object_factory('bpm_84b37ae54c59ab28_v1_2_10', json_data)

    def get_ospf_interfaces(self,
                            headers=None,
                            **request_parameters):
        """Returns the interfaces that has OSPF enabled.

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
                           basestring, may_be_none=False)

        params = {
        }
        params.update(request_parameters)
        params = dict_from_items_with_values(params)

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
            json_data = self._session.get(endpoint_full_url, params=params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=params)

        return self._object_factory('bpm_70ad397649e9b4d3_v1_2_10', json_data)

    def get_functional_capability_by_id(self,
                                        id,
                                        headers=None,
                                        **request_parameters):
        """Returns functional capability with given Id.

        Args:
            id(basestring): Functional Capability UUID.
            headers(dict): Dictionary of HTTP Headers to send with the Request
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
        check_type(id, basestring,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        params = {
        }
        params.update(request_parameters)
        params = dict_from_items_with_values(params)

        path_params = {
            'id': id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/network-device/functional-'
                 + 'capability/${id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=params)

        return self._object_factory('bpm_81bb4804405a8d2f_v1_2_10', json_data)

    def get_isis_interfaces(self,
                            headers=None,
                            **request_parameters):
        """Returns the interfaces that has ISIS enabled.

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
                           basestring, may_be_none=False)

        params = {
        }
        params.update(request_parameters)
        params = dict_from_items_with_values(params)

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
            json_data = self._session.get(endpoint_full_url, params=params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=params)

        return self._object_factory('bpm_84ad8b0e42cab48a_v1_2_10', json_data)

    def get_device_config_for_all_devices(self,
                                          headers=None,
                                          **request_parameters):
        """Returns the config for all devices.

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
                           basestring, may_be_none=False)

        params = {
        }
        params.update(request_parameters)
        params = dict_from_items_with_values(params)

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
            json_data = self._session.get(endpoint_full_url, params=params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=params)

        return self._object_factory('bpm_b7bcaa084e2b90d0_v1_2_10', json_data)

    def update_device_role(self,
                           id=None,
                           role=None,
                           roleSource=None,
                           headers=None,
                           payload=None,
                           active_validation=True,
                           **request_parameters):
        """Updates the role of the device as access, core, distribution,
        border router.

        Args:
            id(string): NetworkDeviceBriefNIO's id.
            role(string): NetworkDeviceBriefNIO's role.
            roleSource(string): NetworkDeviceBriefNIO's roleSource.
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
                           basestring, may_be_none=False)
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        params = {
        }
        params.update(request_parameters)
        params = dict_from_items_with_values(params)

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
            self._request_validator('jsd_b9855ad54ae98156_v1_2_10')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/network-device/brief')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(endpoint_full_url, params=params,
                                          json=_payload,
                                          headers=_headers)
        else:
            json_data = self._session.put(endpoint_full_url, params=params,
                                          json=_payload)

        return self._object_factory('bpm_b9855ad54ae98156_v1_2_10', json_data)

    def get_interface_info_by_id(self,
                                 device_id,
                                 headers=None,
                                 **request_parameters):
        """Returns list of interfaces by specified device.

        Args:
            device_id(basestring): Device ID.
            headers(dict): Dictionary of HTTP Headers to send with the Request
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
        check_type(device_id, basestring,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        params = {
        }
        params.update(request_parameters)
        params = dict_from_items_with_values(params)

        path_params = {
            'deviceId': device_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/interface/network-device/${deviceId}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=params)

        return self._object_factory('bpm_ba9dc85b4b8a9a17_v1_2_10', json_data)

    def get_interface_by_ip(self,
                            ip_address,
                            headers=None,
                            **request_parameters):
        """Returns list of interfaces by specified IP address.

        Args:
            ip_address(basestring): IP address of the interface.
            headers(dict): Dictionary of HTTP Headers to send with the Request
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
        check_type(ip_address, basestring,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        params = {
        }
        params.update(request_parameters)
        params = dict_from_items_with_values(params)

        path_params = {
            'ipAddress': ip_address,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/interface/ip-address/${ipAddress}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=params)

        return self._object_factory('bpm_cd8469e647caab0e_v1_2_10', json_data)

    def get_network_device_by_ip(self,
                                 ip_address,
                                 headers=None,
                                 **request_parameters):
        """Returns the network device by specified IP address.

        Args:
            ip_address(basestring): Device IP address.
            headers(dict): Dictionary of HTTP Headers to send with the Request
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
        check_type(ip_address, basestring,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        params = {
        }
        params.update(request_parameters)
        params = dict_from_items_with_values(params)

        path_params = {
            'ipAddress': ip_address,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/network-device/ip-'
                 + 'address/${ipAddress}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=params)

        return self._object_factory('bpm_d0a4b88145aabb51_v1_2_10', json_data)

    def get_device_summary(self,
                           id,
                           headers=None,
                           **request_parameters):
        """Returns brief summary of device info such as hostname,
        management IP address for the given device Id.

        Args:
            id(basestring): Device ID.
            headers(dict): Dictionary of HTTP Headers to send with the Request
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
        check_type(id, basestring,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        params = {
        }
        params.update(request_parameters)
        params = dict_from_items_with_values(params)

        path_params = {
            'id': id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/network-device/${id}/brief')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=params)

        return self._object_factory('bpm_819f9aa54feab7bf_v1_2_10', json_data)

    def get_device_by_id(self,
                         id,
                         headers=None,
                         **request_parameters):
        """Returns the network device details for the given device ID.

        Args:
            id(basestring): Device ID.
            headers(dict): Dictionary of HTTP Headers to send with the Request
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
        check_type(id, basestring,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        params = {
        }
        params.update(request_parameters)
        params = dict_from_items_with_values(params)

        path_params = {
            'id': id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/network-device/${id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=params)

        return self._object_factory('bpm_8fa8eb404a4a8d96_v1_2_10', json_data)

    def get_all_interfaces(self,
                           limit=500,
                           offset=1,
                           headers=None,
                           **request_parameters):
        """Returns all available interfaces. This endpoint can return a
        maximum of 500 interfaces.

        Args:
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
        """
        check_type(headers, dict)
        check_type(offset, int)
        check_type(limit, int)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        params = {
            'offset':
                offset,
            'limit':
                limit,
        }
        params.update(request_parameters)
        params = dict_from_items_with_values(params)

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
            json_data = self._session.get(endpoint_full_url, params=params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=params)

        return self._object_factory('bpm_f5947a4c439a8bf0_v1_2_10', json_data)

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
        """Sync the devices provided as input.

        Args:
            cliTransport(string): InventoryDeviceInfo's
                cliTransport.
            computeDevice(boolean): InventoryDeviceInfo's
                computeDevice.
            enablePassword(string): InventoryDeviceInfo's
                enablePassword.
            extendedDiscoveryInfo(string): InventoryDeviceInfo's
                extendedDiscoveryInfo.
            httpPassword(string): InventoryDeviceInfo's
                httpPassword.
            httpPort(string): InventoryDeviceInfo's httpPort.
            httpSecure(boolean): InventoryDeviceInfo's httpSecure.
            httpUserName(string): InventoryDeviceInfo's
                httpUserName.
            ipAddress(list): InventoryDeviceInfo's ipAddress (list
                of strings).
            merakiOrgId(list): InventoryDeviceInfo's merakiOrgId
                (list of strings).
            netconfPort(string): InventoryDeviceInfo's netconfPort.
            password(string): InventoryDeviceInfo's password.
            serialNumber(string): InventoryDeviceInfo's
                serialNumber.
            snmpAuthPassphrase(string): InventoryDeviceInfo's
                snmpAuthPassphrase.
            snmpAuthProtocol(string): InventoryDeviceInfo's
                snmpAuthProtocol.
            snmpMode(string): InventoryDeviceInfo's snmpMode.
            snmpPrivPassphrase(string): InventoryDeviceInfo's
                snmpPrivPassphrase.
            snmpPrivProtocol(string): InventoryDeviceInfo's
                snmpPrivProtocol.
            snmpROCommunity(string): InventoryDeviceInfo's
                snmpROCommunity.
            snmpRWCommunity(string): InventoryDeviceInfo's
                snmpRWCommunity.
            snmpRetry(number): InventoryDeviceInfo's snmpRetry.
            snmpTimeout(number): InventoryDeviceInfo's snmpTimeout.
            snmpUserName(string): InventoryDeviceInfo's
                snmpUserName.
            snmpVersion(string): InventoryDeviceInfo's snmpVersion.
            type(string): InventoryDeviceInfo's type. Available
                values are 'COMPUTE_DEVICE',
                'MERAKI_DASHBOARD', 'NETWORK_DEVICE' and
                'NODATACHANGE'.
            updateMgmtIPaddressList(list): InventoryDeviceInfo's
                updateMgmtIPaddressList (list of
                objects).
            userName(string): InventoryDeviceInfo's userName.
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
                           basestring, may_be_none=False)
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        params = {
        }
        params.update(request_parameters)
        params = dict_from_items_with_values(params)

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
            self._request_validator('jsd_aeb9eb67460b92df_v1_2_10')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/network-device')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(endpoint_full_url, params=params,
                                          json=_payload,
                                          headers=_headers)
        else:
            json_data = self._session.put(endpoint_full_url, params=params,
                                          json=_payload)

        return self._object_factory('bpm_aeb9eb67460b92df_v1_2_10', json_data)

    def get_interface_by_id(self,
                            id,
                            headers=None,
                            **request_parameters):
        """Returns the interface for the given interface ID.

        Args:
            id(basestring): Interface ID.
            headers(dict): Dictionary of HTTP Headers to send with the Request
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
        check_type(id, basestring,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        params = {
        }
        params.update(request_parameters)
        params = dict_from_items_with_values(params)

        path_params = {
            'id': id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/interface/${id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=params)

        return self._object_factory('bpm_b888792d43baba46_v1_2_10', json_data)

    def get_functional_capability_for_devices(self,
                                              device_id,
                                              function_name=None,
                                              headers=None,
                                              **request_parameters):
        """Returns the functional-capability for given devices.

        Args:
            device_id(basestring): Accepts comma separated
                deviceid's and return list of
                functional-capabilities for the given
                id's. If invalid or not-found id's are
                provided, null entry will be returned in
                the list.
            function_name(basestring): functionName query parameter.
                Accepts comma separated values.
            headers(dict): Dictionary of HTTP Headers to send with the Request
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
        check_type(device_id, basestring,
                   may_be_none=False)
        check_type(function_name, basestring)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        params = {
            'deviceId':
                device_id,
            'functionName':
                function_name,
        }
        params.update(request_parameters)
        params = dict_from_items_with_values(params)

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
            json_data = self._session.get(endpoint_full_url, params=params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=params)

        return self._object_factory('bpm_c3b3c9ef4e6b8a09_v1_2_10', json_data)

    def register_device_for_wsa(self,
                                macaddress=None,
                                serial_number=None,
                                headers=None,
                                **request_parameters):
        """Registers a device for WSA notification.

        Args:
            serial_number(basestring): Serial number of the device.
            macaddress(basestring): Mac addres of the device.
            headers(dict): Dictionary of HTTP Headers to send with the Request
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
        check_type(serial_number, basestring)
        check_type(macaddress, basestring)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        params = {
            'serialNumber':
                serial_number,
            'macaddress':
                macaddress,
        }
        params.update(request_parameters)
        params = dict_from_items_with_values(params)

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
            json_data = self._session.get(endpoint_full_url, params=params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=params)

        return self._object_factory('bpm_c9809b6744f8a502_v1_2_10', json_data)

    def get_device_by_serial_number(self,
                                    serial_number,
                                    headers=None,
                                    **request_parameters):
        """Returns the network device with given serial number.

        Args:
            serial_number(basestring): Device serial number.
            headers(dict): Dictionary of HTTP Headers to send with the Request
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
        check_type(serial_number, basestring,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        params = {
        }
        params.update(request_parameters)
        params = dict_from_items_with_values(params)

        path_params = {
            'serialNumber': serial_number,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/network-device/serial-'
                 + 'number/${serialNumber}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=params)

        return self._object_factory('bpm_d888ab6d4d59a8c1_v1_2_10', json_data)

    def export_device_list(self,
                           deviceUuids=None,
                           id=None,
                           operationEnum=None,
                           parameters=None,
                           password=None,
                           headers=None,
                           payload=None,
                           active_validation=True,
                           **request_parameters):
        """Exports the selected network device to a file.

        Args:
            deviceUuids(list): ExportDeviceDTO's deviceUuids (list
                of strings).
            id(string): ExportDeviceDTO's id.
            operationEnum(string): ExportDeviceDTO's operationEnum.
                Available values are 'CREDENTIALDETAILS'
                and 'DEVICEDETAILS'.
            parameters(list): ExportDeviceDTO's parameters (list of
                strings).
            password(string): ExportDeviceDTO's password.
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
                           basestring, may_be_none=False)
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        params = {
        }
        params.update(request_parameters)
        params = dict_from_items_with_values(params)

        path_params = {
        }

        _payload = {
            'deviceUuids':
                deviceUuids,
            'id':
                id,
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
            self._request_validator('jsd_cd98780f4888a66d_v1_2_10')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/network-device/file')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=params,
                                           json=_payload)

        return self._object_factory('bpm_cd98780f4888a66d_v1_2_10', json_data)

    def get_network_device_by_pagination_range(self,
                                               records_to_return,
                                               start_index,
                                               headers=None,
                                               **request_parameters):
        """Returns the list of network devices for the given pagination
        range.

        Args:
            start_index(int): Start index.
            records_to_return(int): Number of records to return.
            headers(dict): Dictionary of HTTP Headers to send with the Request
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
                           basestring, may_be_none=False)

        params = {
        }
        params.update(request_parameters)
        params = dict_from_items_with_values(params)

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
                 + 'device/${startIndex}/${recordsToReturn}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=params)

        return self._object_factory('bpm_f49548c54be8a3e2_v1_2_10', json_data)

    def retrieves_all_network_devices(self,
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
        """Gets the list of first 500 network devices sorted
        lexicographically based on host name. It can be filtered
        using management IP address, mac address, hostname and
        location name. If id param is provided, it will be
        returning the list of network-devices for the given id's
        and other request params will be ignored. In case of
        autocomplete request, returns the list of specified
        attributes.

        Args:
            vrf_name(basestring): vrfName query parameter.
            management_ip_address(basestring): managementIpAddress
                query parameter.
            hostname(basestring): hostname query parameter.
            mac_address(basestring): macAddress query parameter.
            family(basestring): family query parameter.
            collection_status(basestring): collectionStatus query
                parameter.
            collection_interval(basestring): collectionInterval
                query parameter.
            software_version(basestring): softwareVersion query
                parameter.
            software_type(basestring): softwareType query parameter.
            reachability_status(basestring): reachabilityStatus
                query parameter.
            reachability_failure_reason(basestring):
                reachabilityFailureReason query
                parameter.
            error_code(basestring): errorCode query parameter.
            platform_id(basestring): platformId query parameter.
            series(basestring): series query parameter.
            type(basestring): type query parameter.
            serial_number(basestring): serialNumber query parameter.
            up_time(basestring): upTime query parameter.
            role(basestring): role query parameter.
            role_source(basestring): roleSource query parameter.
            associated_wlc_ip(basestring): associatedWlcIp query
                parameter.
            offset(basestring): offset query parameter.
            limit(basestring): limit query parameter.
            headers(dict): Dictionary of HTTP Headers to send with the Request
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
        check_type(vrf_name, basestring)
        check_type(management_ip_address, basestring)
        check_type(hostname, basestring)
        check_type(mac_address, basestring)
        check_type(family, basestring)
        check_type(collection_status, basestring)
        check_type(collection_interval, basestring)
        check_type(software_version, basestring)
        check_type(software_type, basestring)
        check_type(reachability_status, basestring)
        check_type(reachability_failure_reason, basestring)
        check_type(error_code, basestring)
        check_type(platform_id, basestring)
        check_type(series, basestring)
        check_type(type, basestring)
        check_type(serial_number, basestring)
        check_type(up_time, basestring)
        check_type(role, basestring)
        check_type(role_source, basestring)
        check_type(associated_wlc_ip, basestring)
        check_type(offset, basestring)
        check_type(limit, basestring)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        params = {
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
        params.update(request_parameters)
        params = dict_from_items_with_values(params)

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
            json_data = self._session.get(endpoint_full_url, params=params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=params)

        return self._object_factory('bpm_ffa748cc44e9a437_v1_2_10', json_data)

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
        """Returns modules by specified device id.

        Args:
            device_id(basestring): deviceId query parameter.
            limit(basestring): limit query parameter.
            offset(basestring): offset query parameter.
            name_list(basestring): nameList query parameter. Accepts
                comma separated values.
            vendor_equipment_type_list(basestring):
                vendorEquipmentTypeList query parameter.
                Accepts comma separated values.
            part_number_list(basestring): partNumberList query
                parameter. Accepts comma separated
                values.
            operational_state_code_list(basestring):
                operationalStateCodeList query
                parameter. Accepts comma separated
                values.
            headers(dict): Dictionary of HTTP Headers to send with the Request
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
        check_type(device_id, basestring,
                   may_be_none=False)
        check_type(limit, basestring)
        check_type(offset, basestring)
        check_type(name_list, basestring)
        check_type(vendor_equipment_type_list, basestring)
        check_type(part_number_list, basestring)
        check_type(operational_state_code_list, basestring)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        params = {
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
        params.update(request_parameters)
        params = dict_from_items_with_values(params)

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
            json_data = self._session.get(endpoint_full_url, params=params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=params)

        return self._object_factory('bpm_eb8249e34f69b0f1_v1_2_10', json_data)

    def get_wireless_lan_controller_details_by_id(self,
                                                  id,
                                                  headers=None,
                                                  **request_parameters):
        """Returns the wireless lan controller info with given device ID.

        Args:
            id(basestring): Device ID.
            headers(dict): Dictionary of HTTP Headers to send with the Request
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
        check_type(id, basestring,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        params = {
        }
        params.update(request_parameters)
        params = dict_from_items_with_values(params)

        path_params = {
            'id': id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/network-device/${id}/wireless-info')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=params)

        return self._object_factory('bpm_f6826a8e41bba242_v1_2_10', json_data)

    def get_device_detail(self,
                          identifier,
                          search_by,
                          timestamp=None,
                          headers=None,
                          **request_parameters):
        """Returns detailed Network Device information retrieved by Mac
        Address, Device Name or UUID for any given point of
        time. .

        Args:
            timestamp(int, basestring): Epoch time(in milliseconds)
                when the device data is required.
            search_by(basestring): MAC Address or Device Name value
                or UUID of the network device.
            identifier(basestring): One of keywords : macAddress or
                uuid or nwDeviceName.
            headers(dict): Dictionary of HTTP Headers to send with the Request
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
        check_type(timestamp, (int, basestring))
        check_type(search_by, basestring,
                   may_be_none=False)
        check_type(identifier, basestring,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        params = {
            'timestamp':
                timestamp,
            'searchBy':
                search_by,
            'identifier':
                identifier,
        }

        if params['timestamp'] is None:
            params['timestamp'] = ''

        params.update(request_parameters)
        params = dict_from_items_with_values(params)

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
            json_data = self._session.get(endpoint_full_url, params=params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=params)

        return self._object_factory('bpm_89b2fb144f5bb09b_v1_2_10', json_data)

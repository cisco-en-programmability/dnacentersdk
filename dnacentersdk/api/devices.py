# -*- coding: utf-8 -*-
"""DNA Center Devices API wrapper.

Copyright (c) 2019 Cisco and/or its affiliates.

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

from ..generator_containers import generator_container
from ..restsession import RestSession
from ..utils import (
    check_type,
    dict_from_items_with_values,
    apply_path_params,
    dict_filt,
)

class Devices( object ):
    """DNA Center Devices API.

    Wraps the DNA Center Devices API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new Devices object with the provided RestSession.

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


    # Get Module Info by Id
    def get_module_info_by_id(self, path_param_id, headers=None,payload=None,**request_parameters):
        check_type( path_param_id, basestring, may_be_none=False)
        if headers is not None:
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = { }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
            'id': path_param_id,
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_0db7da744c0b83d8').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.get(apply_path_params('/api/v1/network-device/module/${id}', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.get(apply_path_params('/api/v1/network-device/module/${id}', path_params), params=params, json=payload)

        return self._object_factory('bpm_0db7da744c0b83d8', json_data)


    # Delete Device by Id
    def delete_device_by_id(self, path_param_id, param_is_force_delete = None, headers=None,payload=None,**request_parameters):
        check_type( param_is_force_delete, bool)
        check_type( path_param_id, basestring, may_be_none=False)
        if headers is not None:
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = { }
        if param_is_force_delete is not None: params.update( { 'isForceDelete': param_is_force_delete })
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
            'id': path_param_id,
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_1c894b5848eab214').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.delete(apply_path_params('/api/v1/network-device/${id}', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.delete(apply_path_params('/api/v1/network-device/${id}', path_params), params=params, json=payload)

        return self._object_factory('bpm_1c894b5848eab214', json_data)


    # Sync Devices
    def sync_devices(self, param_force_sync = None, headers=None,payload=None,**request_parameters):
        check_type( param_force_sync, bool)
        if headers is not None:
            check_type( headers.get('Content-Type', self._session.headers.get('Content-Type')), basestring, may_be_none=False)
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = { }
        if param_force_sync is not None: params.update( { 'forceSync': param_force_sync })
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or []

        self._request_validator('jsd_3b9ef9674429be4c').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.put(apply_path_params('/api/v1/network-device/sync', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.put(apply_path_params('/api/v1/network-device/sync', path_params), params=params, json=payload)

        return self._object_factory('bpm_3b9ef9674429be4c', json_data)


    # Get Device list
    def get_device_list(self, param_associated_wlc_ip = None, param_collection_interval = None, param_collection_status = None, param_error_code = None, param_error_description = None, param_family = None, param_hostname = None, param_id = None, param_license_name = None, param_license_status = None, param_license_type = None, param_location = None, param_location_name = None, param_mac_address = None, param_management_ip_address = None, param_module_equpimenttype = None, param_module_name = None, param_module_operationstatecode = None, param_module_partnumber = None, param_module_servicestate = None, param_module_vendorequipmenttype = None, param_not_synced_for_minutes = None, param_platform_id = None, param_reachability_status = None, param_role = None, param_serial_number = None, param_series = None, param_software_type = None, param_software_version = None, param_type = None, param_up_time = None, headers=None,payload=None,**request_parameters):
        check_type( param_hostname, basestring)
        check_type( param_management_ip_address, basestring)
        check_type( param_mac_address, basestring)
        check_type( param_location_name, basestring)
        check_type( param_serial_number, basestring)
        check_type( param_location, basestring)
        check_type( param_family, basestring)
        check_type( param_type, basestring)
        check_type( param_series, basestring)
        check_type( param_collection_status, basestring)
        check_type( param_collection_interval, basestring)
        check_type( param_not_synced_for_minutes, basestring)
        check_type( param_error_code, basestring)
        check_type( param_error_description, basestring)
        check_type( param_software_version, basestring)
        check_type( param_software_type, basestring)
        check_type( param_platform_id, basestring)
        check_type( param_role, basestring)
        check_type( param_reachability_status, basestring)
        check_type( param_up_time, basestring)
        check_type( param_associated_wlc_ip, basestring)
        check_type( param_license_name, basestring)
        check_type( param_license_type, basestring)
        check_type( param_license_status, basestring)
        check_type( param_module_name, basestring)
        check_type( param_module_equpimenttype, basestring)
        check_type( param_module_servicestate, basestring)
        check_type( param_module_vendorequipmenttype, basestring)
        check_type( param_module_partnumber, basestring)
        check_type( param_module_operationstatecode, basestring)
        check_type( param_id, basestring)
        if headers is not None:
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = { }
        if param_hostname is not None: params.update( { 'hostname': param_hostname })
        if param_management_ip_address is not None: params.update( { 'managementIpAddress': param_management_ip_address })
        if param_mac_address is not None: params.update( { 'macAddress': param_mac_address })
        if param_location_name is not None: params.update( { 'locationName': param_location_name })
        if param_serial_number is not None: params.update( { 'serialNumber': param_serial_number })
        if param_location is not None: params.update( { 'location': param_location })
        if param_family is not None: params.update( { 'family': param_family })
        if param_type is not None: params.update( { 'type': param_type })
        if param_series is not None: params.update( { 'series': param_series })
        if param_collection_status is not None: params.update( { 'collectionStatus': param_collection_status })
        if param_collection_interval is not None: params.update( { 'collectionInterval': param_collection_interval })
        if param_not_synced_for_minutes is not None: params.update( { 'notSyncedForMinutes': param_not_synced_for_minutes })
        if param_error_code is not None: params.update( { 'errorCode': param_error_code })
        if param_error_description is not None: params.update( { 'errorDescription': param_error_description })
        if param_software_version is not None: params.update( { 'softwareVersion': param_software_version })
        if param_software_type is not None: params.update( { 'softwareType': param_software_type })
        if param_platform_id is not None: params.update( { 'platformId': param_platform_id })
        if param_role is not None: params.update( { 'role': param_role })
        if param_reachability_status is not None: params.update( { 'reachabilityStatus': param_reachability_status })
        if param_up_time is not None: params.update( { 'upTime': param_up_time })
        if param_associated_wlc_ip is not None: params.update( { 'associatedWlcIp': param_associated_wlc_ip })
        if param_license_name is not None: params.update( { 'license.name': param_license_name })
        if param_license_type is not None: params.update( { 'license.type': param_license_type })
        if param_license_status is not None: params.update( { 'license.status': param_license_status })
        if param_module_name is not None: params.update( { 'module+name': param_module_name })
        if param_module_equpimenttype is not None: params.update( { 'module+equpimenttype': param_module_equpimenttype })
        if param_module_servicestate is not None: params.update( { 'module+servicestate': param_module_servicestate })
        if param_module_vendorequipmenttype is not None: params.update( { 'module+vendorequipmenttype': param_module_vendorequipmenttype })
        if param_module_partnumber is not None: params.update( { 'module+partnumber': param_module_partnumber })
        if param_module_operationstatecode is not None: params.update( { 'module+operationstatecode': param_module_operationstatecode })
        if param_id is not None: params.update( { 'id': param_id })
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_20b19b52464b8972').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.get(apply_path_params('/api/v1/network-device', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.get(apply_path_params('/api/v1/network-device', path_params), params=params, json=payload)

        return self._object_factory('bpm_20b19b52464b8972', json_data)


    # Get Device Interface VLANs
    def get_device_interface_vlans(self, path_param_id, param_interface_type = None, headers=None,payload=None,**request_parameters):
        check_type( param_interface_type, basestring)
        check_type( path_param_id, basestring, may_be_none=False)
        if headers is not None:
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = { }
        if param_interface_type is not None: params.update( { 'interfaceType': param_interface_type })
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
            'id': path_param_id,
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_288df9494f2a9746').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.get(apply_path_params('/api/v1/network-device/${id}/vlan', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.get(apply_path_params('/api/v1/network-device/${id}/vlan', path_params), params=params, json=payload)

        return self._object_factory('bpm_288df9494f2a9746', json_data)


    # Get Polling Interval for all devices
    def get_polling_interval_for_all_devices(self, headers=None,payload=None,**request_parameters):
        if headers is not None:
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = { }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_38bd0b884b89a785').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.get(apply_path_params('/api/v1/network-device/collection-schedule/global', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.get(apply_path_params('/api/v1/network-device/collection-schedule/global', path_params), params=params, json=payload)

        return self._object_factory('bpm_38bd0b884b89a785', json_data)


    # Get Device Interfaces by specified range
    def get_device_interfaces_by_specified_range(self, path_param_device_id, path_param_records_to_return, path_param_start_index, headers=None,payload=None,**request_parameters):
        check_type( path_param_device_id, basestring, may_be_none=False)
        check_type( path_param_start_index, int, may_be_none=False)
        check_type( path_param_records_to_return, int, may_be_none=False)
        if headers is not None:
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = { }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
            'deviceId': path_param_device_id,
            'startIndex': path_param_start_index,
            'recordsToReturn': path_param_records_to_return,
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_349c888443b89a58').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.get(apply_path_params('/api/v1/interface/network-device/${deviceId}/${startIndex}/${recordsToReturn}', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.get(apply_path_params('/api/v1/interface/network-device/${deviceId}/${startIndex}/${recordsToReturn}', path_params), params=params, json=payload)

        return self._object_factory('bpm_349c888443b89a58', json_data)


    # Get Device Interface Count
    def get_device_interface_count(self, headers=None,payload=None,**request_parameters):
        if headers is not None:
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = { }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_3d923b184dc9a4ca').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.get(apply_path_params('/api/v1/interface/count', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.get(apply_path_params('/api/v1/interface/count', path_params), params=params, json=payload)

        return self._object_factory('bpm_3d923b184dc9a4ca', json_data)


    # Add Device
    def add_device(self, rq_cliTransport = None, rq_computeDevice = None, rq_enablePassword = None, rq_extendedDiscoveryInfo = None, rq_httpPassword = None, rq_httpPort = None, rq_httpSecure = None, rq_httpUserName = None, rq_ipAddress = None, rq_merakiOrgId = None, rq_netconfPort = None, rq_password = None, rq_serialNumber = None, rq_snmpAuthPassphrase = None, rq_snmpAuthProtocol = None, rq_snmpMode = None, rq_snmpPrivPassphrase = None, rq_snmpPrivProtocol = None, rq_snmpROCommunity = None, rq_snmpRWCommunity = None, rq_snmpRetry = None, rq_snmpTimeout = None, rq_snmpUserName = None, rq_snmpVersion = None, rq_type = None, rq_updateMgmtIPaddressList = None, rq_userName = None, headers=None,payload=None,**request_parameters):
        if headers is not None:
            check_type( headers.get('Content-Type', self._session.headers.get('Content-Type')), basestring, may_be_none=False)
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = { }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        if rq_cliTransport is not None: payload.update( { 'cliTransport':  rq_cliTransport })
        if rq_computeDevice is not None: payload.update( { 'computeDevice':  rq_computeDevice })
        if rq_enablePassword is not None: payload.update( { 'enablePassword':  rq_enablePassword })
        if rq_extendedDiscoveryInfo is not None: payload.update( { 'extendedDiscoveryInfo':  rq_extendedDiscoveryInfo })
        if rq_httpPassword is not None: payload.update( { 'httpPassword':  rq_httpPassword })
        if rq_httpPort is not None: payload.update( { 'httpPort':  rq_httpPort })
        if rq_httpSecure is not None: payload.update( { 'httpSecure':  rq_httpSecure })
        if rq_httpUserName is not None: payload.update( { 'httpUserName':  rq_httpUserName })
        if rq_ipAddress is not None: payload.update( { 'ipAddress':  rq_ipAddress })
        if rq_merakiOrgId is not None: payload.update( { 'merakiOrgId':  rq_merakiOrgId })
        if rq_netconfPort is not None: payload.update( { 'netconfPort':  rq_netconfPort })
        if rq_password is not None: payload.update( { 'password':  rq_password })
        if rq_serialNumber is not None: payload.update( { 'serialNumber':  rq_serialNumber })
        if rq_snmpAuthPassphrase is not None: payload.update( { 'snmpAuthPassphrase':  rq_snmpAuthPassphrase })
        if rq_snmpAuthProtocol is not None: payload.update( { 'snmpAuthProtocol':  rq_snmpAuthProtocol })
        if rq_snmpMode is not None: payload.update( { 'snmpMode':  rq_snmpMode })
        if rq_snmpPrivPassphrase is not None: payload.update( { 'snmpPrivPassphrase':  rq_snmpPrivPassphrase })
        if rq_snmpPrivProtocol is not None: payload.update( { 'snmpPrivProtocol':  rq_snmpPrivProtocol })
        if rq_snmpROCommunity is not None: payload.update( { 'snmpROCommunity':  rq_snmpROCommunity })
        if rq_snmpRWCommunity is not None: payload.update( { 'snmpRWCommunity':  rq_snmpRWCommunity })
        if rq_snmpRetry is not None: payload.update( { 'snmpRetry':  rq_snmpRetry })
        if rq_snmpTimeout is not None: payload.update( { 'snmpTimeout':  rq_snmpTimeout })
        if rq_snmpUserName is not None: payload.update( { 'snmpUserName':  rq_snmpUserName })
        if rq_snmpVersion is not None: payload.update( { 'snmpVersion':  rq_snmpVersion })
        if rq_type is not None: payload.update( { 'type':  rq_type })
        if rq_updateMgmtIPaddressList is not None: payload.update( { 'updateMgmtIPaddressList':  rq_updateMgmtIPaddressList })
        if rq_userName is not None: payload.update( { 'userName':  rq_userName })
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_4bb22af046fa8f08').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.post(apply_path_params('/api/v1/network-device', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.post(apply_path_params('/api/v1/network-device', path_params), params=params, json=payload)

        return self._object_factory('bpm_4bb22af046fa8f08', json_data)


    # Get Interface details by device Id and interface name
    def get_interface_details_by_device_id_and_interface_name(self, param_name, path_param_device_id, headers=None,payload=None,**request_parameters):
        check_type( param_name, basestring, may_be_none=False)
        check_type( path_param_device_id, basestring, may_be_none=False)
        if headers is not None:
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = { }
        if param_name is not None: params.update( { 'name': param_name })
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
            'deviceId': path_param_device_id,
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_4eb56a614cc9a2d2').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.get(apply_path_params('/api/v1/interface/network-device/${deviceId}/interface-name', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.get(apply_path_params('/api/v1/interface/network-device/${deviceId}/interface-name', path_params), params=params, json=payload)

        return self._object_factory('bpm_4eb56a614cc9a2d2', json_data)


    # Get Device Interface count
    def get_device_interface_count(self, path_param_device_id, headers=None,payload=None,**request_parameters):
        check_type( path_param_device_id, basestring, may_be_none=False)
        if headers is not None:
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = { }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
            'deviceId': path_param_device_id,
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_5b8639224cd88ea7').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.get(apply_path_params('/api/v1/interface/network-device/${deviceId}/count', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.get(apply_path_params('/api/v1/interface/network-device/${deviceId}/count', path_params), params=params, json=payload)

        return self._object_factory('bpm_5b8639224cd88ea7', json_data)


    # Get Device Count
    def get_device_count(self, headers=None,payload=None,**request_parameters):
        if headers is not None:
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = { }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_5db21b8e43fab7d8').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.get(apply_path_params('/api/v1/network-device/count', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.get(apply_path_params('/api/v1/network-device/count', path_params), params=params, json=payload)

        return self._object_factory('bpm_5db21b8e43fab7d8', json_data)


    # Get OSPF interfaces
    def get_ospf_interfaces(self, headers=None,payload=None,**request_parameters):
        if headers is not None:
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = { }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_70ad397649e9b4d3').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.get(apply_path_params('/api/v1/interface/ospf', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.get(apply_path_params('/api/v1/interface/ospf', path_params), params=params, json=payload)

        return self._object_factory('bpm_70ad397649e9b4d3', json_data)


    # Get Polling Interval by Id
    def get_polling_interval_by_id(self, path_param_id, headers=None,payload=None,**request_parameters):
        check_type( path_param_id, basestring, may_be_none=False)
        if headers is not None:
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = { }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
            'id': path_param_id,
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_82918a1b4d289c5c').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.get(apply_path_params('/api/v1/network-device/${id}/collection-schedule', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.get(apply_path_params('/api/v1/network-device/${id}/collection-schedule', path_params), params=params, json=payload)

        return self._object_factory('bpm_82918a1b4d289c5c', json_data)


    # Get Organization list for Meraki
    def get_organization_list_for_meraki(self, path_param_id, headers=None,payload=None,**request_parameters):
        check_type( path_param_id, basestring, may_be_none=False)
        if headers is not None:
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = { }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
            'id': path_param_id,
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_84b37ae54c59ab28').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.get(apply_path_params('/api/v1/network-device/${id}/meraki-organization', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.get(apply_path_params('/api/v1/network-device/${id}/meraki-organization', path_params), params=params, json=payload)

        return self._object_factory('bpm_84b37ae54c59ab28', json_data)


    # Get Functional Capability by Id
    def get_functional_capability_by_id(self, path_param_id, headers=None,payload=None,**request_parameters):
        check_type( path_param_id, basestring, may_be_none=False)
        if headers is not None:
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = { }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
            'id': path_param_id,
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_81bb4804405a8d2f').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.get(apply_path_params('/api/v1/network-device/functional-capability/${id}', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.get(apply_path_params('/api/v1/network-device/functional-capability/${id}', path_params), params=params, json=payload)

        return self._object_factory('bpm_81bb4804405a8d2f', json_data)


    # Get ISIS interfaces
    def get_isis_interfaces(self, headers=None,payload=None,**request_parameters):
        if headers is not None:
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = { }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_84ad8b0e42cab48a').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.get(apply_path_params('/api/v1/interface/isis', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.get(apply_path_params('/api/v1/interface/isis', path_params), params=params, json=payload)

        return self._object_factory('bpm_84ad8b0e42cab48a', json_data)


    # Get Device Config by Id
    def get_device_config_by_id(self, path_param_network_device_id, headers=None,payload=None,**request_parameters):
        check_type( path_param_network_device_id, basestring, may_be_none=False)
        if headers is not None:
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = { }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
            'networkDeviceId': path_param_network_device_id,
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_84b33a9e480abcaf').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.get(apply_path_params('/api/v1/network-device/${networkDeviceId}/config', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.get(apply_path_params('/api/v1/network-device/${networkDeviceId}/config', path_params), params=params, json=payload)

        return self._object_factory('bpm_84b33a9e480abcaf', json_data)


    # Get Device Summary
    def get_device_summary(self, path_param_id, headers=None,payload=None,**request_parameters):
        check_type( path_param_id, basestring, may_be_none=False)
        if headers is not None:
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = { }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
            'id': path_param_id,
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_819f9aa54feab7bf').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.get(apply_path_params('/api/v1/network-device/${id}/brief', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.get(apply_path_params('/api/v1/network-device/${id}/brief', path_params), params=params, json=payload)

        return self._object_factory('bpm_819f9aa54feab7bf', json_data)


    # Get Device by ID
    def get_device_by_id(self, path_param_id, headers=None,payload=None,**request_parameters):
        check_type( path_param_id, basestring, may_be_none=False)
        if headers is not None:
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = { }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
            'id': path_param_id,
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_8fa8eb404a4a8d96').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.get(apply_path_params('/api/v1/network-device/${id}', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.get(apply_path_params('/api/v1/network-device/${id}', path_params), params=params, json=payload)

        return self._object_factory('bpm_8fa8eb404a4a8d96', json_data)


    # Get Interface info by Id
    def get_interface_info_by_id(self, path_param_device_id, headers=None,payload=None,**request_parameters):
        check_type( path_param_device_id, basestring, may_be_none=False)
        if headers is not None:
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = { }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
            'deviceId': path_param_device_id,
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_ba9dc85b4b8a9a17').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.get(apply_path_params('/api/v1/interface/network-device/${deviceId}', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.get(apply_path_params('/api/v1/interface/network-device/${deviceId}', path_params), params=params, json=payload)

        return self._object_factory('bpm_ba9dc85b4b8a9a17', json_data)


    # Register device for WSA
    def register_device_for_wsa(self, param_macaddress = None, param_serial_number = None, headers=None,payload=None,**request_parameters):
        check_type( param_serial_number, basestring)
        check_type( param_macaddress, basestring)
        if headers is not None:
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = { }
        if param_serial_number is not None: params.update( { 'serialNumber': param_serial_number })
        if param_macaddress is not None: params.update( { 'macaddress': param_macaddress })
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_c9809b6744f8a502').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.get(apply_path_params('/api/v1/network-device/tenantinfo/macaddress', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.get(apply_path_params('/api/v1/network-device/tenantinfo/macaddress', path_params), params=params, json=payload)

        return self._object_factory('bpm_c9809b6744f8a502', json_data)


    # Update Device role
    def update_device_role(self, rq_id = None, rq_role = None, rq_roleSource = None, headers=None,payload=None,**request_parameters):
        if headers is not None:
            check_type( headers.get('Content-Type', self._session.headers.get('Content-Type')), basestring, may_be_none=False)
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = { }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        if rq_id is not None: payload.update( { 'id':  rq_id })
        if rq_role is not None: payload.update( { 'role':  rq_role })
        if rq_roleSource is not None: payload.update( { 'roleSource':  rq_roleSource })
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_b9855ad54ae98156').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.put(apply_path_params('/api/v1/network-device/brief', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.put(apply_path_params('/api/v1/network-device/brief', path_params), params=params, json=payload)

        return self._object_factory('bpm_b9855ad54ae98156', json_data)


    # Get Device Config for all devices
    def get_device_config_for_all_devices(self, headers=None,payload=None,**request_parameters):
        if headers is not None:
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = { }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_b7bcaa084e2b90d0').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.get(apply_path_params('/api/v1/network-device/config', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.get(apply_path_params('/api/v1/network-device/config', path_params), params=params, json=payload)

        return self._object_factory('bpm_b7bcaa084e2b90d0', json_data)


    # Export Device list
    def export_device_list(self, rq_deviceUuids = None, rq_id = None, rq_operationEnum = None, rq_parameters = None, rq_password = None, headers=None,payload=None,**request_parameters):
        if headers is not None:
            check_type( headers.get('Content-Type', self._session.headers.get('Content-Type')), basestring, may_be_none=False)
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = { }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        if rq_deviceUuids is not None: payload.update( { 'deviceUuids':  rq_deviceUuids })
        if rq_id is not None: payload.update( { 'id':  rq_id })
        if rq_operationEnum is not None: payload.update( { 'operationEnum':  rq_operationEnum })
        if rq_parameters is not None: payload.update( { 'parameters':  rq_parameters })
        if rq_password is not None: payload.update( { 'password':  rq_password })
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_cd98780f4888a66d').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.post(apply_path_params('/api/v1/network-device/file', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.post(apply_path_params('/api/v1/network-device/file', path_params), params=params, json=payload)

        return self._object_factory('bpm_cd98780f4888a66d', json_data)


    # Get Interface by IP
    def get_interface_by_ip(self, path_param_ip_address, headers=None,payload=None,**request_parameters):
        check_type( path_param_ip_address, basestring, may_be_none=False)
        if headers is not None:
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = { }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
            'ipAddress': path_param_ip_address,
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_cd8469e647caab0e').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.get(apply_path_params('/api/v1/interface/ip-address/${ipAddress}', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.get(apply_path_params('/api/v1/interface/ip-address/${ipAddress}', path_params), params=params, json=payload)

        return self._object_factory('bpm_cd8469e647caab0e', json_data)


    # Get Network Device by IP
    def get_network_device_by_ip(self, path_param_ip_address, headers=None,payload=None,**request_parameters):
        check_type( path_param_ip_address, basestring, may_be_none=False)
        if headers is not None:
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = { }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
            'ipAddress': path_param_ip_address,
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_d0a4b88145aabb51').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.get(apply_path_params('/api/v1/network-device/ip-address/${ipAddress}', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.get(apply_path_params('/api/v1/network-device/ip-address/${ipAddress}', path_params), params=params, json=payload)

        return self._object_factory('bpm_d0a4b88145aabb51', json_data)


    # Get Device Config Count
    def get_device_config_count(self, headers=None,payload=None,**request_parameters):
        if headers is not None:
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = { }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_888f585c49b88441').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.get(apply_path_params('/api/v1/network-device/config/count', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.get(apply_path_params('/api/v1/network-device/config/count', path_params), params=params, json=payload)

        return self._object_factory('bpm_888f585c49b88441', json_data)


    # Get Device by Serial number
    def get_device_by_serial_number(self, path_param_serial_number, headers=None,payload=None,**request_parameters):
        check_type( path_param_serial_number, basestring, may_be_none=False)
        if headers is not None:
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = { }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
            'serialNumber': path_param_serial_number,
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_d888ab6d4d59a8c1').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.get(apply_path_params('/api/v1/network-device/serial-number/${serialNumber}', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.get(apply_path_params('/api/v1/network-device/serial-number/${serialNumber}', path_params), params=params, json=payload)

        return self._object_factory('bpm_d888ab6d4d59a8c1', json_data)


    # Get all interfaces
    def get_all_interfaces(self, headers=None,payload=None,**request_parameters):
        if headers is not None:
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = { }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_f5947a4c439a8bf0').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.get(apply_path_params('/api/v1/interface', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.get(apply_path_params('/api/v1/interface', path_params), params=params, json=payload)

        return self._object_factory('bpm_f5947a4c439a8bf0', json_data)


    # Get Module count
    def get_module_count(self, param_device_id, param_name_list = None, param_operational_state_code_list = None, param_part_number_list = None, param_vendor_equipment_type_list = None, headers=None,payload=None,**request_parameters):
        check_type( param_device_id, basestring, may_be_none=False)
        check_type( param_name_list, basestring)
        check_type( param_vendor_equipment_type_list, basestring)
        check_type( param_part_number_list, basestring)
        check_type( param_operational_state_code_list, basestring)
        if headers is not None:
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = { }
        if param_device_id is not None: params.update( { 'deviceId': param_device_id })
        if param_name_list is not None: params.update( { 'nameList': param_name_list })
        if param_vendor_equipment_type_list is not None: params.update( { 'vendorEquipmentTypeList': param_vendor_equipment_type_list })
        if param_part_number_list is not None: params.update( { 'partNumberList': param_part_number_list })
        if param_operational_state_code_list is not None: params.update( { 'operationalStateCodeList': param_operational_state_code_list })
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_8db939744649a782').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.get(apply_path_params('/api/v1/network-device/module/count', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.get(apply_path_params('/api/v1/network-device/module/count', path_params), params=params, json=payload)

        return self._object_factory('bpm_8db939744649a782', json_data)


    # Get Modules
    def get_modules(self, param_device_id, param_limit = None, param_name_list = None, param_offset = None, param_operational_state_code_list = None, param_part_number_list = None, param_vendor_equipment_type_list = None, headers=None,payload=None,**request_parameters):
        check_type( param_device_id, basestring, may_be_none=False)
        check_type( param_limit, basestring)
        check_type( param_offset, basestring)
        check_type( param_name_list, basestring)
        check_type( param_vendor_equipment_type_list, basestring)
        check_type( param_part_number_list, basestring)
        check_type( param_operational_state_code_list, basestring)
        if headers is not None:
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = { }
        if param_device_id is not None: params.update( { 'deviceId': param_device_id })
        if param_limit is not None: params.update( { 'limit': param_limit })
        if param_offset is not None: params.update( { 'offset': param_offset })
        if param_name_list is not None: params.update( { 'nameList': param_name_list })
        if param_vendor_equipment_type_list is not None: params.update( { 'vendorEquipmentTypeList': param_vendor_equipment_type_list })
        if param_part_number_list is not None: params.update( { 'partNumberList': param_part_number_list })
        if param_operational_state_code_list is not None: params.update( { 'operationalStateCodeList': param_operational_state_code_list })
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_eb8249e34f69b0f1').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.get(apply_path_params('/api/v1/network-device/module', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.get(apply_path_params('/api/v1/network-device/module', path_params), params=params, json=payload)

        return self._object_factory('bpm_eb8249e34f69b0f1', json_data)


    # Get wireless lan controller details by Id
    def get_wireless_lan_controller_details_by_id(self, path_param_id, headers=None,payload=None,**request_parameters):
        check_type( path_param_id, basestring, may_be_none=False)
        if headers is not None:
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = { }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
            'id': path_param_id,
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_f6826a8e41bba242').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.get(apply_path_params('/api/v1/network-device/${id}/wireless-info', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.get(apply_path_params('/api/v1/network-device/${id}/wireless-info', path_params), params=params, json=payload)

        return self._object_factory('bpm_f6826a8e41bba242', json_data)


    # Sync Devices
    def sync_devices(self, rq_cliTransport = None, rq_computeDevice = None, rq_enablePassword = None, rq_extendedDiscoveryInfo = None, rq_httpPassword = None, rq_httpPort = None, rq_httpSecure = None, rq_httpUserName = None, rq_ipAddress = None, rq_merakiOrgId = None, rq_netconfPort = None, rq_password = None, rq_serialNumber = None, rq_snmpAuthPassphrase = None, rq_snmpAuthProtocol = None, rq_snmpMode = None, rq_snmpPrivPassphrase = None, rq_snmpPrivProtocol = None, rq_snmpROCommunity = None, rq_snmpRWCommunity = None, rq_snmpRetry = None, rq_snmpTimeout = None, rq_snmpUserName = None, rq_snmpVersion = None, rq_type = None, rq_updateMgmtIPaddressList = None, rq_userName = None, headers=None,payload=None,**request_parameters):
        if headers is not None:
            check_type( headers.get('Content-Type', self._session.headers.get('Content-Type')), basestring, may_be_none=False)
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = { }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        if rq_cliTransport is not None: payload.update( { 'cliTransport':  rq_cliTransport })
        if rq_computeDevice is not None: payload.update( { 'computeDevice':  rq_computeDevice })
        if rq_enablePassword is not None: payload.update( { 'enablePassword':  rq_enablePassword })
        if rq_extendedDiscoveryInfo is not None: payload.update( { 'extendedDiscoveryInfo':  rq_extendedDiscoveryInfo })
        if rq_httpPassword is not None: payload.update( { 'httpPassword':  rq_httpPassword })
        if rq_httpPort is not None: payload.update( { 'httpPort':  rq_httpPort })
        if rq_httpSecure is not None: payload.update( { 'httpSecure':  rq_httpSecure })
        if rq_httpUserName is not None: payload.update( { 'httpUserName':  rq_httpUserName })
        if rq_ipAddress is not None: payload.update( { 'ipAddress':  rq_ipAddress })
        if rq_merakiOrgId is not None: payload.update( { 'merakiOrgId':  rq_merakiOrgId })
        if rq_netconfPort is not None: payload.update( { 'netconfPort':  rq_netconfPort })
        if rq_password is not None: payload.update( { 'password':  rq_password })
        if rq_serialNumber is not None: payload.update( { 'serialNumber':  rq_serialNumber })
        if rq_snmpAuthPassphrase is not None: payload.update( { 'snmpAuthPassphrase':  rq_snmpAuthPassphrase })
        if rq_snmpAuthProtocol is not None: payload.update( { 'snmpAuthProtocol':  rq_snmpAuthProtocol })
        if rq_snmpMode is not None: payload.update( { 'snmpMode':  rq_snmpMode })
        if rq_snmpPrivPassphrase is not None: payload.update( { 'snmpPrivPassphrase':  rq_snmpPrivPassphrase })
        if rq_snmpPrivProtocol is not None: payload.update( { 'snmpPrivProtocol':  rq_snmpPrivProtocol })
        if rq_snmpROCommunity is not None: payload.update( { 'snmpROCommunity':  rq_snmpROCommunity })
        if rq_snmpRWCommunity is not None: payload.update( { 'snmpRWCommunity':  rq_snmpRWCommunity })
        if rq_snmpRetry is not None: payload.update( { 'snmpRetry':  rq_snmpRetry })
        if rq_snmpTimeout is not None: payload.update( { 'snmpTimeout':  rq_snmpTimeout })
        if rq_snmpUserName is not None: payload.update( { 'snmpUserName':  rq_snmpUserName })
        if rq_snmpVersion is not None: payload.update( { 'snmpVersion':  rq_snmpVersion })
        if rq_type is not None: payload.update( { 'type':  rq_type })
        if rq_updateMgmtIPaddressList is not None: payload.update( { 'updateMgmtIPaddressList':  rq_updateMgmtIPaddressList })
        if rq_userName is not None: payload.update( { 'userName':  rq_userName })
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_aeb9eb67460b92df').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.put(apply_path_params('/api/v1/network-device', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.put(apply_path_params('/api/v1/network-device', path_params), params=params, json=payload)

        return self._object_factory('bpm_aeb9eb67460b92df', json_data)


    # Get Interface by Id
    def get_interface_by_id(self, path_param_id, headers=None,payload=None,**request_parameters):
        check_type( path_param_id, basestring, may_be_none=False)
        if headers is not None:
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = { }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
            'id': path_param_id,
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_b888792d43baba46').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.get(apply_path_params('/api/v1/interface/${id}', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.get(apply_path_params('/api/v1/interface/${id}', path_params), params=params, json=payload)

        return self._object_factory('bpm_b888792d43baba46', json_data)


    # Get Functional Capability for devices
    def get_functional_capability_for_devices(self, param_device_id = None, param_function_name = None, headers=None,payload=None,**request_parameters):
        check_type( param_device_id, basestring)
        check_type( param_function_name, basestring)
        if headers is not None:
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = { }
        if param_device_id is not None: params.update( { 'deviceId': param_device_id })
        if param_function_name is not None: params.update( { 'functionName': param_function_name })
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_c3b3c9ef4e6b8a09').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.get(apply_path_params('/api/v1/network-device/functional-capability', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.get(apply_path_params('/api/v1/network-device/functional-capability', path_params), params=params, json=payload)

        return self._object_factory('bpm_c3b3c9ef4e6b8a09', json_data)


    # Get Device Detail
    def get_device_detail(self, param_identifier, param_search_by, param_timestamp = None, headers=None,payload=None,**request_parameters):
        check_type( param_timestamp, basestring)
        check_type( param_search_by, basestring, may_be_none=False)
        check_type( param_identifier, basestring, may_be_none=False)
        if headers is not None:
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = { }
        if param_timestamp is not None: params.update( { 'timestamp': param_timestamp })
        if param_search_by is not None: params.update( { 'searchBy': param_search_by })
        if param_identifier is not None: params.update( { 'identifier': param_identifier })
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_89b2fb144f5bb09b').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.get(apply_path_params('/dna/intent/api/v1/device-detail', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.get(apply_path_params('/dna/intent/api/v1/device-detail', path_params), params=params, json=payload)

        return self._object_factory('bpm_89b2fb144f5bb09b', json_data)


    # Get Network Device by pagination range
    def get_network_device_by_pagination_range(self, path_param_records_to_return, path_param_start_index, headers=None,payload=None,**request_parameters):
        check_type( path_param_start_index, int, may_be_none=False)
        check_type( path_param_records_to_return, int, may_be_none=False)
        if headers is not None:
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = { }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
            'startIndex': path_param_start_index,
            'recordsToReturn': path_param_records_to_return,
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_f49548c54be8a3e2').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.get(apply_path_params('/api/v1/network-device/${startIndex}/${recordsToReturn}', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.get(apply_path_params('/api/v1/network-device/${startIndex}/${recordsToReturn}', path_params), params=params, json=payload)

        return self._object_factory('bpm_f49548c54be8a3e2', json_data)


    # Retrieves all network devices
    def retrieves_all_network_devices(self, param_associated_wlc_ip = None, param_collection_interval = None, param_collection_status = None, param_error_code = None, param_family = None, param_hostname = None, param_limit = None, param_mac_address = None, param_management_ip_address = None, param_offset = None, param_platform_id = None, param_reachability_failure_reason = None, param_reachability_status = None, param_role = None, param_role_source = None, param_serial_number = None, param_series = None, param_software_type = None, param_software_version = None, param_type = None, param_up_time = None, param_vrf_name = None, headers=None,payload=None,**request_parameters):
        check_type( param_vrf_name, basestring)
        check_type( param_management_ip_address, basestring)
        check_type( param_hostname, basestring)
        check_type( param_mac_address, basestring)
        check_type( param_family, basestring)
        check_type( param_collection_status, basestring)
        check_type( param_collection_interval, basestring)
        check_type( param_software_version, basestring)
        check_type( param_software_type, basestring)
        check_type( param_reachability_status, basestring)
        check_type( param_reachability_failure_reason, basestring)
        check_type( param_error_code, basestring)
        check_type( param_platform_id, basestring)
        check_type( param_series, basestring)
        check_type( param_type, basestring)
        check_type( param_serial_number, basestring)
        check_type( param_up_time, basestring)
        check_type( param_role, basestring)
        check_type( param_role_source, basestring)
        check_type( param_associated_wlc_ip, basestring)
        check_type( param_offset, basestring)
        check_type( param_limit, basestring)
        if headers is not None:
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = { }
        if param_vrf_name is not None: params.update( { 'vrfName': param_vrf_name })
        if param_management_ip_address is not None: params.update( { 'managementIpAddress': param_management_ip_address })
        if param_hostname is not None: params.update( { 'hostname': param_hostname })
        if param_mac_address is not None: params.update( { 'macAddress': param_mac_address })
        if param_family is not None: params.update( { 'family': param_family })
        if param_collection_status is not None: params.update( { 'collectionStatus': param_collection_status })
        if param_collection_interval is not None: params.update( { 'collectionInterval': param_collection_interval })
        if param_software_version is not None: params.update( { 'softwareVersion': param_software_version })
        if param_software_type is not None: params.update( { 'softwareType': param_software_type })
        if param_reachability_status is not None: params.update( { 'reachabilityStatus': param_reachability_status })
        if param_reachability_failure_reason is not None: params.update( { 'reachabilityFailureReason': param_reachability_failure_reason })
        if param_error_code is not None: params.update( { 'errorCode': param_error_code })
        if param_platform_id is not None: params.update( { 'platformId': param_platform_id })
        if param_series is not None: params.update( { 'series': param_series })
        if param_type is not None: params.update( { 'type': param_type })
        if param_serial_number is not None: params.update( { 'serialNumber': param_serial_number })
        if param_up_time is not None: params.update( { 'upTime': param_up_time })
        if param_role is not None: params.update( { 'role': param_role })
        if param_role_source is not None: params.update( { 'roleSource': param_role_source })
        if param_associated_wlc_ip is not None: params.update( { 'associatedWlcIp': param_associated_wlc_ip })
        if param_offset is not None: params.update( { 'offset': param_offset })
        if param_limit is not None: params.update( { 'limit': param_limit })
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_ffa748cc44e9a437').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.get(apply_path_params('/api/v1/network-device/autocomplete', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.get(apply_path_params('/api/v1/network-device/autocomplete', path_params), params=params, json=payload)

        return self._object_factory('bpm_ffa748cc44e9a437', json_data)



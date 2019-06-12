# -*- coding: utf-8 -*-
"""DNA Center Network Discovery API wrapper.

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

class NetworkDiscovery( object ):
    """DNA Center Network Discovery API.

    Wraps the DNA Center Network Discovery API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new NetworkDiscovery object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the DNA Center service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(NetworkDiscovery, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator


    # Get count of all discovery jobs
    def get_count_of_all_discovery_jobs(self, headers=None,payload=None,**request_parameters):
        if headers is not None:
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = {
        }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_069d9823451b892d').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.get(apply_path_params('/dna/intent/api/v1/discovery/count', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.get(apply_path_params('/dna/intent/api/v1/discovery/count', path_params), params=params, json=payload)

        return self._object_factory('bpm_069d9823451b892d', json_data)


    # Create Netconf credentials
    def create_netconf_credentials(self, headers=None,payload=None,**request_parameters):
        if headers is not None:
            check_type( headers.get('Content-Type', self._session.headers.get('Content-Type')), basestring, may_be_none=False)
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = {
        }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or []

        self._request_validator('jsd_17929bc7465bb564').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.post(apply_path_params('/dna/intent/api/v1/global-credential/netconf', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.post(apply_path_params('/dna/intent/api/v1/global-credential/netconf', path_params), params=params, json=payload)

        return self._object_factory('bpm_17929bc7465bb564', json_data)


    # Update SNMP write community
    def update_snmp_write_community(self, rq_comments = None, rq_credentialType = None, rq_description = None, rq_id = None, rq_instanceTenantId = None, rq_instanceUuid = None, rq_writeCommunity = None, headers=None,payload=None,**request_parameters):
        if headers is not None:
            check_type( headers.get('Content-Type', self._session.headers.get('Content-Type')), basestring, may_be_none=False)
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = {
        }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        if rq_comments is not None: payload.update( { 'comments':  rq_comments })
        if rq_credentialType is not None: payload.update( { 'credentialType':  rq_credentialType })
        if rq_description is not None: payload.update( { 'description':  rq_description })
        if rq_id is not None: payload.update( { 'id':  rq_id })
        if rq_instanceTenantId is not None: payload.update( { 'instanceTenantId':  rq_instanceTenantId })
        if rq_instanceUuid is not None: payload.update( { 'instanceUuid':  rq_instanceUuid })
        if rq_writeCommunity is not None: payload.update( { 'writeCommunity':  rq_writeCommunity })
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_10b06a6a4f7bb3cb').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.put(apply_path_params('/dna/intent/api/v1/global-credential/snmpv2-write-community', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.put(apply_path_params('/dna/intent/api/v1/global-credential/snmpv2-write-community', path_params), params=params, json=payload)

        return self._object_factory('bpm_10b06a6a4f7bb3cb', json_data)


    # Update SNMPv3 credentials
    def update_snmpv3_credentials(self, rq_authPassword = None, rq_authType = None, rq_comments = None, rq_credentialType = None, rq_description = None, rq_id = None, rq_instanceTenantId = None, rq_instanceUuid = None, rq_privacyPassword = None, rq_privacyType = None, rq_snmpMode = None, rq_username = None, headers=None,payload=None,**request_parameters):
        if headers is not None:
            check_type( headers.get('Content-Type', self._session.headers.get('Content-Type')), basestring, may_be_none=False)
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = {
        }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        if rq_authPassword is not None: payload.update( { 'authPassword':  rq_authPassword })
        if rq_authType is not None: payload.update( { 'authType':  rq_authType })
        if rq_comments is not None: payload.update( { 'comments':  rq_comments })
        if rq_credentialType is not None: payload.update( { 'credentialType':  rq_credentialType })
        if rq_description is not None: payload.update( { 'description':  rq_description })
        if rq_id is not None: payload.update( { 'id':  rq_id })
        if rq_instanceTenantId is not None: payload.update( { 'instanceTenantId':  rq_instanceTenantId })
        if rq_instanceUuid is not None: payload.update( { 'instanceUuid':  rq_instanceUuid })
        if rq_privacyPassword is not None: payload.update( { 'privacyPassword':  rq_privacyPassword })
        if rq_privacyType is not None: payload.update( { 'privacyType':  rq_privacyType })
        if rq_snmpMode is not None: payload.update( { 'snmpMode':  rq_snmpMode })
        if rq_username is not None: payload.update( { 'username':  rq_username })
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_1da5ebdd434aacfe').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.put(apply_path_params('/dna/intent/api/v1/global-credential/snmpv3', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.put(apply_path_params('/dna/intent/api/v1/global-credential/snmpv3', path_params), params=params, json=payload)

        return self._object_factory('bpm_1da5ebdd434aacfe', json_data)


    # Get SNMP properties
    def get_snmp_properties(self, headers=None,payload=None,**request_parameters):
        if headers is not None:
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = {
        }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_44974ba5435a801d').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.get(apply_path_params('/dna/intent/api/v1/snmp-property', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.get(apply_path_params('/dna/intent/api/v1/snmp-property', path_params), params=params, json=payload)

        return self._object_factory('bpm_44974ba5435a801d', json_data)


    # Delete discovery by Id
    def delete_discovery_by_id(self, path_param_id, headers=None,payload=None,**request_parameters):
        check_type( path_param_id, basestring, may_be_none=False)
        if headers is not None:
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = {
        }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
            'id': path_param_id,
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_4c8cab5f435a80f4').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.delete(apply_path_params('/dna/intent/api/v1/discovery/${id}', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.delete(apply_path_params('/dna/intent/api/v1/discovery/${id}', path_params), params=params, json=payload)

        return self._object_factory('bpm_4c8cab5f435a80f4', json_data)


    # Start discovery
    def start_discovery(self, rq_cdpLevel = None, rq_discoveryType = None, rq_enablePasswordList = None, rq_globalCredentialIdList = None, rq_httpReadCredential = None, rq_httpWriteCredential = None, rq_ipAddressList = None, rq_ipFilterList = None, rq_lldpLevel = None, rq_name = None, rq_netconfPort = None, rq_noAddNewDevice = None, rq_parentDiscoveryId = None, rq_passwordList = None, rq_preferredMgmtIPMethod = None, rq_protocolOrder = None, rq_reDiscovery = None, rq_retry = None, rq_snmpAuthPassphrase = None, rq_snmpAuthProtocol = None, rq_snmpMode = None, rq_snmpPrivPassphrase = None, rq_snmpPrivProtocol = None, rq_snmpROCommunity = None, rq_snmpROCommunityDesc = None, rq_snmpRWCommunity = None, rq_snmpRWCommunityDesc = None, rq_snmpUserName = None, rq_snmpVersion = None, rq_timeout = None, rq_updateMgmtIp = None, rq_userNameList = None, headers=None,payload=None,**request_parameters):
        if headers is not None:
            check_type( headers.get('Content-Type', self._session.headers.get('Content-Type')), basestring, may_be_none=False)
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = {
        }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        if rq_cdpLevel is not None: payload.update( { 'cdpLevel':  rq_cdpLevel })
        if rq_discoveryType is not None: payload.update( { 'discoveryType':  rq_discoveryType })
        if rq_enablePasswordList is not None: payload.update( { 'enablePasswordList':  rq_enablePasswordList })
        if rq_globalCredentialIdList is not None: payload.update( { 'globalCredentialIdList':  rq_globalCredentialIdList })
        if rq_httpReadCredential is not None: payload.update( { 'httpReadCredential':  rq_httpReadCredential })
        if rq_httpWriteCredential is not None: payload.update( { 'httpWriteCredential':  rq_httpWriteCredential })
        if rq_ipAddressList is not None: payload.update( { 'ipAddressList':  rq_ipAddressList })
        if rq_ipFilterList is not None: payload.update( { 'ipFilterList':  rq_ipFilterList })
        if rq_lldpLevel is not None: payload.update( { 'lldpLevel':  rq_lldpLevel })
        if rq_name is not None: payload.update( { 'name':  rq_name })
        if rq_netconfPort is not None: payload.update( { 'netconfPort':  rq_netconfPort })
        if rq_noAddNewDevice is not None: payload.update( { 'noAddNewDevice':  rq_noAddNewDevice })
        if rq_parentDiscoveryId is not None: payload.update( { 'parentDiscoveryId':  rq_parentDiscoveryId })
        if rq_passwordList is not None: payload.update( { 'passwordList':  rq_passwordList })
        if rq_preferredMgmtIPMethod is not None: payload.update( { 'preferredMgmtIPMethod':  rq_preferredMgmtIPMethod })
        if rq_protocolOrder is not None: payload.update( { 'protocolOrder':  rq_protocolOrder })
        if rq_reDiscovery is not None: payload.update( { 'reDiscovery':  rq_reDiscovery })
        if rq_retry is not None: payload.update( { 'retry':  rq_retry })
        if rq_snmpAuthPassphrase is not None: payload.update( { 'snmpAuthPassphrase':  rq_snmpAuthPassphrase })
        if rq_snmpAuthProtocol is not None: payload.update( { 'snmpAuthProtocol':  rq_snmpAuthProtocol })
        if rq_snmpMode is not None: payload.update( { 'snmpMode':  rq_snmpMode })
        if rq_snmpPrivPassphrase is not None: payload.update( { 'snmpPrivPassphrase':  rq_snmpPrivPassphrase })
        if rq_snmpPrivProtocol is not None: payload.update( { 'snmpPrivProtocol':  rq_snmpPrivProtocol })
        if rq_snmpROCommunity is not None: payload.update( { 'snmpROCommunity':  rq_snmpROCommunity })
        if rq_snmpROCommunityDesc is not None: payload.update( { 'snmpROCommunityDesc':  rq_snmpROCommunityDesc })
        if rq_snmpRWCommunity is not None: payload.update( { 'snmpRWCommunity':  rq_snmpRWCommunity })
        if rq_snmpRWCommunityDesc is not None: payload.update( { 'snmpRWCommunityDesc':  rq_snmpRWCommunityDesc })
        if rq_snmpUserName is not None: payload.update( { 'snmpUserName':  rq_snmpUserName })
        if rq_snmpVersion is not None: payload.update( { 'snmpVersion':  rq_snmpVersion })
        if rq_timeout is not None: payload.update( { 'timeout':  rq_timeout })
        if rq_updateMgmtIp is not None: payload.update( { 'updateMgmtIp':  rq_updateMgmtIp })
        if rq_userNameList is not None: payload.update( { 'userNameList':  rq_userNameList })
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_55b439dc4239b140').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.post(apply_path_params('/dna/intent/api/v1/discovery', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.post(apply_path_params('/dna/intent/api/v1/discovery', path_params), params=params, json=payload)

        return self._object_factory('bpm_55b439dc4239b140', json_data)


    # Create SNMP write community
    def create_snmp_write_community(self, headers=None,payload=None,**request_parameters):
        if headers is not None:
            check_type( headers.get('Content-Type', self._session.headers.get('Content-Type')), basestring, may_be_none=False)
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = {
        }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or []

        self._request_validator('jsd_6bacb8d14639bdc7').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.post(apply_path_params('/dna/intent/api/v1/global-credential/snmpv2-write-community', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.post(apply_path_params('/dna/intent/api/v1/global-credential/snmpv2-write-community', path_params), params=params, json=payload)

        return self._object_factory('bpm_6bacb8d14639bdc7', json_data)


    # Create HTTP write credentials
    def create_http_write_credentials(self, headers=None,payload=None,**request_parameters):
        if headers is not None:
            check_type( headers.get('Content-Type', self._session.headers.get('Content-Type')), basestring, may_be_none=False)
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = {
        }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or []

        self._request_validator('jsd_4d9ca8e2431a8a24').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.post(apply_path_params('/dna/intent/api/v1/global-credential/http-write', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.post(apply_path_params('/dna/intent/api/v1/global-credential/http-write', path_params), params=params, json=payload)

        return self._object_factory('bpm_4d9ca8e2431a8a24', json_data)


    # Get network devices from Discovery
    def get_network_devices_from_discovery(self, path_param_id, param_cli_status = None, param_http_status = None, param_ip_address = None, param_netconf_status = None, param_ping_status = None, param_snmp_status = None, param_sort_by = None, param_sort_order = None, param_task_id = None, headers=None,payload=None,**request_parameters):
        check_type( param_task_id, basestring)
        check_type( param_sort_by, basestring)
        check_type( param_sort_order, basestring)
        check_type( param_ip_address, basestring)
        check_type( param_ping_status, basestring)
        check_type( param_snmp_status, basestring)
        check_type( param_cli_status, basestring)
        check_type( param_netconf_status, basestring)
        check_type( param_http_status, basestring)
        check_type( path_param_id, basestring, may_be_none=False)
        if headers is not None:
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = {
            'taskId': param_task_id,
            'sortBy': param_sort_by,
            'sortOrder': param_sort_order,
            'ipAddress': param_ip_address,
            'pingStatus': param_ping_status,
            'snmpStatus': param_snmp_status,
            'cliStatus': param_cli_status,
            'netconfStatus': param_netconf_status,
            'httpStatus': param_http_status,
        }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
            'id': path_param_id,
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_3d9b99c343398a27').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.get(apply_path_params('/dna/intent/api/v1/discovery/${id}/summary', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.get(apply_path_params('/dna/intent/api/v1/discovery/${id}/summary', path_params), params=params, json=payload)

        return self._object_factory('bpm_3d9b99c343398a27', json_data)


    # Update global credentials
    def update_global_credentials(self, path_param_global_credential_id, rq_siteUuids = None, headers=None,payload=None,**request_parameters):
        check_type( path_param_global_credential_id, basestring, may_be_none=False)
        if headers is not None:
            check_type( headers.get('Content-Type', self._session.headers.get('Content-Type')), basestring, may_be_none=False)
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = {
        }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
            'globalCredentialId': path_param_global_credential_id,
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        if rq_siteUuids is not None: payload.update( { 'siteUuids':  rq_siteUuids })
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_709fda3c42b8877a').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.put(apply_path_params('/dna/intent/api/v1/global-credential/${globalCredentialId}', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.put(apply_path_params('/dna/intent/api/v1/global-credential/${globalCredentialId}', path_params), params=params, json=payload)

        return self._object_factory('bpm_709fda3c42b8877a', json_data)


    # Get Discoveries by range
    def get_discoveries_by_range(self, path_param_records_to_return, path_param_start_index, headers=None,payload=None,**request_parameters):
        check_type( path_param_start_index, int, may_be_none=False)
        check_type( path_param_records_to_return, int, may_be_none=False)
        if headers is not None:
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = {
        }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
            'startIndex': path_param_start_index,
            'recordsToReturn': path_param_records_to_return,
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_33b799d04d0a8907').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.get(apply_path_params('/dna/intent/api/v1/discovery/${startIndex}/${recordsToReturn}', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.get(apply_path_params('/dna/intent/api/v1/discovery/${startIndex}/${recordsToReturn}', path_params), params=params, json=payload)

        return self._object_factory('bpm_33b799d04d0a8907', json_data)


    # Create SNMP read community
    def create_snmp_read_community(self, headers=None,payload=None,**request_parameters):
        if headers is not None:
            check_type( headers.get('Content-Type', self._session.headers.get('Content-Type')), basestring, may_be_none=False)
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = {
        }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or []

        self._request_validator('jsd_7aa3da9d4e098ef2').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.post(apply_path_params('/dna/intent/api/v1/global-credential/snmpv2-read-community', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.post(apply_path_params('/dna/intent/api/v1/global-credential/snmpv2-read-community', path_params), params=params, json=payload)

        return self._object_factory('bpm_7aa3da9d4e098ef2', json_data)


    # Get Discovery by Id
    def get_discovery_by_id(self, path_param_id, headers=None,payload=None,**request_parameters):
        check_type( path_param_id, basestring, may_be_none=False)
        if headers is not None:
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = {
        }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
            'id': path_param_id,
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_63bb88b74f59aa17').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.get(apply_path_params('/dna/intent/api/v1/discovery/${id}', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.get(apply_path_params('/dna/intent/api/v1/discovery/${id}', path_params), params=params, json=payload)

        return self._object_factory('bpm_63bb88b74f59aa17', json_data)


    # Updates an existing discovery by specified Id
    def updates_an_existing_discovery_by_specified_id(self, rq_attributeInfo = None, rq_cdpLevel = None, rq_deviceIds = None, rq_discoveryCondition = None, rq_discoveryStatus = None, rq_discoveryType = None, rq_enablePasswordList = None, rq_globalCredentialIdList = None, rq_httpReadCredential = None, rq_httpWriteCredential = None, rq_id = None, rq_ipAddressList = None, rq_ipFilterList = None, rq_isAutoCdp = None, rq_lldpLevel = None, rq_name = None, rq_netconfPort = None, rq_numDevices = None, rq_parentDiscoveryId = None, rq_passwordList = None, rq_preferredMgmtIPMethod = None, rq_protocolOrder = None, rq_retryCount = None, rq_snmpAuthPassphrase = None, rq_snmpAuthProtocol = None, rq_snmpMode = None, rq_snmpPrivPassphrase = None, rq_snmpPrivProtocol = None, rq_snmpRoCommunity = None, rq_snmpRoCommunityDesc = None, rq_snmpRwCommunity = None, rq_snmpRwCommunityDesc = None, rq_snmpUserName = None, rq_timeOut = None, rq_updateMgmtIp = None, rq_userNameList = None, headers=None,payload=None,**request_parameters):
        if headers is not None:
            check_type( headers.get('Content-Type', self._session.headers.get('Content-Type')), basestring, may_be_none=False)
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = {
        }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        if rq_attributeInfo is not None: payload.update( { 'attributeInfo':  rq_attributeInfo })
        if rq_cdpLevel is not None: payload.update( { 'cdpLevel':  rq_cdpLevel })
        if rq_deviceIds is not None: payload.update( { 'deviceIds':  rq_deviceIds })
        if rq_discoveryCondition is not None: payload.update( { 'discoveryCondition':  rq_discoveryCondition })
        if rq_discoveryStatus is not None: payload.update( { 'discoveryStatus':  rq_discoveryStatus })
        if rq_discoveryType is not None: payload.update( { 'discoveryType':  rq_discoveryType })
        if rq_enablePasswordList is not None: payload.update( { 'enablePasswordList':  rq_enablePasswordList })
        if rq_globalCredentialIdList is not None: payload.update( { 'globalCredentialIdList':  rq_globalCredentialIdList })
        if rq_httpReadCredential is not None: payload.update( { 'httpReadCredential':  rq_httpReadCredential })
        if rq_httpWriteCredential is not None: payload.update( { 'httpWriteCredential':  rq_httpWriteCredential })
        if rq_id is not None: payload.update( { 'id':  rq_id })
        if rq_ipAddressList is not None: payload.update( { 'ipAddressList':  rq_ipAddressList })
        if rq_ipFilterList is not None: payload.update( { 'ipFilterList':  rq_ipFilterList })
        if rq_isAutoCdp is not None: payload.update( { 'isAutoCdp':  rq_isAutoCdp })
        if rq_lldpLevel is not None: payload.update( { 'lldpLevel':  rq_lldpLevel })
        if rq_name is not None: payload.update( { 'name':  rq_name })
        if rq_netconfPort is not None: payload.update( { 'netconfPort':  rq_netconfPort })
        if rq_numDevices is not None: payload.update( { 'numDevices':  rq_numDevices })
        if rq_parentDiscoveryId is not None: payload.update( { 'parentDiscoveryId':  rq_parentDiscoveryId })
        if rq_passwordList is not None: payload.update( { 'passwordList':  rq_passwordList })
        if rq_preferredMgmtIPMethod is not None: payload.update( { 'preferredMgmtIPMethod':  rq_preferredMgmtIPMethod })
        if rq_protocolOrder is not None: payload.update( { 'protocolOrder':  rq_protocolOrder })
        if rq_retryCount is not None: payload.update( { 'retryCount':  rq_retryCount })
        if rq_snmpAuthPassphrase is not None: payload.update( { 'snmpAuthPassphrase':  rq_snmpAuthPassphrase })
        if rq_snmpAuthProtocol is not None: payload.update( { 'snmpAuthProtocol':  rq_snmpAuthProtocol })
        if rq_snmpMode is not None: payload.update( { 'snmpMode':  rq_snmpMode })
        if rq_snmpPrivPassphrase is not None: payload.update( { 'snmpPrivPassphrase':  rq_snmpPrivPassphrase })
        if rq_snmpPrivProtocol is not None: payload.update( { 'snmpPrivProtocol':  rq_snmpPrivProtocol })
        if rq_snmpRoCommunity is not None: payload.update( { 'snmpRoCommunity':  rq_snmpRoCommunity })
        if rq_snmpRoCommunityDesc is not None: payload.update( { 'snmpRoCommunityDesc':  rq_snmpRoCommunityDesc })
        if rq_snmpRwCommunity is not None: payload.update( { 'snmpRwCommunity':  rq_snmpRwCommunity })
        if rq_snmpRwCommunityDesc is not None: payload.update( { 'snmpRwCommunityDesc':  rq_snmpRwCommunityDesc })
        if rq_snmpUserName is not None: payload.update( { 'snmpUserName':  rq_snmpUserName })
        if rq_timeOut is not None: payload.update( { 'timeOut':  rq_timeOut })
        if rq_updateMgmtIp is not None: payload.update( { 'updateMgmtIp':  rq_updateMgmtIp })
        if rq_userNameList is not None: payload.update( { 'userNameList':  rq_userNameList })
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_9788b8fc4418831d').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.put(apply_path_params('/dna/intent/api/v1/discovery', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.put(apply_path_params('/dna/intent/api/v1/discovery', path_params), params=params, json=payload)

        return self._object_factory('bpm_9788b8fc4418831d', json_data)


    # Create CLI credentials
    def create_cli_credentials(self, headers=None,payload=None,**request_parameters):
        if headers is not None:
            check_type( headers.get('Content-Type', self._session.headers.get('Content-Type')), basestring, may_be_none=False)
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = {
        }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or []

        self._request_validator('jsd_948ea8194348bc0b').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.post(apply_path_params('/dna/intent/api/v1/global-credential/cli', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.post(apply_path_params('/dna/intent/api/v1/global-credential/cli', path_params), params=params, json=payload)

        return self._object_factory('bpm_948ea8194348bc0b', json_data)


    # Update SNMP read community
    def update_snmp_read_community(self, rq_comments = None, rq_credentialType = None, rq_description = None, rq_id = None, rq_instanceTenantId = None, rq_instanceUuid = None, rq_readCommunity = None, headers=None,payload=None,**request_parameters):
        if headers is not None:
            check_type( headers.get('Content-Type', self._session.headers.get('Content-Type')), basestring, may_be_none=False)
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = {
        }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        if rq_comments is not None: payload.update( { 'comments':  rq_comments })
        if rq_credentialType is not None: payload.update( { 'credentialType':  rq_credentialType })
        if rq_description is not None: payload.update( { 'description':  rq_description })
        if rq_id is not None: payload.update( { 'id':  rq_id })
        if rq_instanceTenantId is not None: payload.update( { 'instanceTenantId':  rq_instanceTenantId })
        if rq_instanceUuid is not None: payload.update( { 'instanceUuid':  rq_instanceUuid })
        if rq_readCommunity is not None: payload.update( { 'readCommunity':  rq_readCommunity })
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_47a1b84b4e1b8044').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.put(apply_path_params('/dna/intent/api/v1/global-credential/snmpv2-read-community', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.put(apply_path_params('/dna/intent/api/v1/global-credential/snmpv2-read-community', path_params), params=params, json=payload)

        return self._object_factory('bpm_47a1b84b4e1b8044', json_data)


    # Get list of discoveries by discovery Id
    def get_list_of_discoveries_by_discovery_id(self, path_param_id, param_ip_address = None, param_limit = None, param_offset = None, headers=None,payload=None,**request_parameters):
        check_type( param_offset, int)
        check_type( param_limit, int)
        check_type( param_ip_address, basestring)
        check_type( path_param_id, basestring, may_be_none=False)
        if headers is not None:
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = {
            'offset': param_offset,
            'limit': param_limit,
            'ipAddress': param_ip_address,
        }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
            'id': path_param_id,
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_99872a134d0a9fb4').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.get(apply_path_params('/dna/intent/api/v1/discovery/${id}/job', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.get(apply_path_params('/dna/intent/api/v1/discovery/${id}/job', path_params), params=params, json=payload)

        return self._object_factory('bpm_99872a134d0a9fb4', json_data)


    # Create/Update SNMP properties
    def create_update_snmp_properties(self, headers=None,payload=None,**request_parameters):
        if headers is not None:
            check_type( headers.get('Content-Type', self._session.headers.get('Content-Type')), basestring, may_be_none=False)
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = {
        }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or []

        self._request_validator('jsd_a5ac99774c6bb541').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.post(apply_path_params('/dna/intent/api/v1/snmp-property', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.post(apply_path_params('/dna/intent/api/v1/snmp-property', path_params), params=params, json=payload)

        return self._object_factory('bpm_a5ac99774c6bb541', json_data)


    # Get Discovery jobs by IP
    def get_discovery_jobs_by_ip(self, param_ip_address, param_limit = None, param_name = None, param_offset = None, headers=None,payload=None,**request_parameters):
        check_type( param_offset, int)
        check_type( param_limit, int)
        check_type( param_ip_address, basestring, may_be_none=False)
        check_type( param_name, basestring)
        if headers is not None:
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = {
            'offset': param_offset,
            'limit': param_limit,
            'ipAddress': param_ip_address,
            'name': param_name,
        }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_a4967be64dfaaa1a').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.get(apply_path_params('/dna/intent/api/v1/discovery/job', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.get(apply_path_params('/dna/intent/api/v1/discovery/job', path_params), params=params, json=payload)

        return self._object_factory('bpm_a4967be64dfaaa1a', json_data)


    # Get Discovered devices by range
    def get_discovered_devices_by_range(self, path_param_id, path_param_records_to_return, path_param_start_index, param_task_id = None, headers=None,payload=None,**request_parameters):
        check_type( param_task_id, basestring)
        check_type( path_param_id, basestring, may_be_none=False)
        check_type( path_param_start_index, int, may_be_none=False)
        check_type( path_param_records_to_return, int, may_be_none=False)
        if headers is not None:
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = {
            'taskId': param_task_id,
        }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
            'id': path_param_id,
            'startIndex': path_param_start_index,
            'recordsToReturn': path_param_records_to_return,
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_a6b798ab4acaa34e').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.get(apply_path_params('/dna/intent/api/v1/discovery/${id}/network-device/${startIndex}/${recordsToReturn}', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.get(apply_path_params('/dna/intent/api/v1/discovery/${id}/network-device/${startIndex}/${recordsToReturn}', path_params), params=params, json=payload)

        return self._object_factory('bpm_a6b798ab4acaa34e', json_data)


    # Get Credential sub type by credential Id
    def get_credential_sub_type_by_credential_id(self, path_param_id, headers=None,payload=None,**request_parameters):
        check_type( path_param_id, basestring, may_be_none=False)
        if headers is not None:
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = {
        }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
            'id': path_param_id,
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_58a3699e489b9529').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.get(apply_path_params('/dna/intent/api/v1/global-credential/${id}', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.get(apply_path_params('/dna/intent/api/v1/global-credential/${id}', path_params), params=params, json=payload)

        return self._object_factory('bpm_58a3699e489b9529', json_data)


    # Update HTTP write credentials
    def update_http_write_credentials(self, rq_comments = None, rq_credentialType = None, rq_description = None, rq_id = None, rq_instanceTenantId = None, rq_instanceUuid = None, rq_password = None, rq_port = None, rq_secure = None, rq_username = None, headers=None,payload=None,**request_parameters):
        if headers is not None:
            check_type( headers.get('Content-Type', self._session.headers.get('Content-Type')), basestring, may_be_none=False)
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = {
        }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        if rq_comments is not None: payload.update( { 'comments':  rq_comments })
        if rq_credentialType is not None: payload.update( { 'credentialType':  rq_credentialType })
        if rq_description is not None: payload.update( { 'description':  rq_description })
        if rq_id is not None: payload.update( { 'id':  rq_id })
        if rq_instanceTenantId is not None: payload.update( { 'instanceTenantId':  rq_instanceTenantId })
        if rq_instanceUuid is not None: payload.update( { 'instanceUuid':  rq_instanceUuid })
        if rq_password is not None: payload.update( { 'password':  rq_password })
        if rq_port is not None: payload.update( { 'port':  rq_port })
        if rq_secure is not None: payload.update( { 'secure':  rq_secure })
        if rq_username is not None: payload.update( { 'username':  rq_username })
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_b68a6bd8473a9a25').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.put(apply_path_params('/dna/intent/api/v1/global-credential/http-write', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.put(apply_path_params('/dna/intent/api/v1/global-credential/http-write', path_params), params=params, json=payload)

        return self._object_factory('bpm_b68a6bd8473a9a25', json_data)


    # Delete discovery by specified range
    def delete_discovery_by_specified_range(self, path_param_records_to_delete, path_param_start_index, headers=None,payload=None,**request_parameters):
        check_type( path_param_start_index, int, may_be_none=False)
        check_type( path_param_records_to_delete, int, may_be_none=False)
        if headers is not None:
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = {
        }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
            'startIndex': path_param_start_index,
            'recordsToDelete': path_param_records_to_delete,
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_c1ba9a424c08a01b').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.delete(apply_path_params('/dna/intent/api/v1/discovery/${startIndex}/${recordsToDelete}', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.delete(apply_path_params('/dna/intent/api/v1/discovery/${startIndex}/${recordsToDelete}', path_params), params=params, json=payload)

        return self._object_factory('bpm_c1ba9a424c08a01b', json_data)


    # Create HTTP read credentials
    def create_http_read_credentials(self, headers=None,payload=None,**request_parameters):
        if headers is not None:
            check_type( headers.get('Content-Type', self._session.headers.get('Content-Type')), basestring, may_be_none=False)
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = {
        }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or []

        self._request_validator('jsd_bf859ac64a0ba19c').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.post(apply_path_params('/dna/intent/api/v1/global-credential/http-read', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.post(apply_path_params('/dna/intent/api/v1/global-credential/http-read', path_params), params=params, json=payload)

        return self._object_factory('bpm_bf859ac64a0ba19c', json_data)


    # Update Netconf credentials
    def update_netconf_credentials(self, rq_comments = None, rq_credentialType = None, rq_description = None, rq_id = None, rq_instanceTenantId = None, rq_instanceUuid = None, rq_netconfPort = None, headers=None,payload=None,**request_parameters):
        if headers is not None:
            check_type( headers.get('Content-Type', self._session.headers.get('Content-Type')), basestring, may_be_none=False)
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = {
        }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        if rq_comments is not None: payload.update( { 'comments':  rq_comments })
        if rq_credentialType is not None: payload.update( { 'credentialType':  rq_credentialType })
        if rq_description is not None: payload.update( { 'description':  rq_description })
        if rq_id is not None: payload.update( { 'id':  rq_id })
        if rq_instanceTenantId is not None: payload.update( { 'instanceTenantId':  rq_instanceTenantId })
        if rq_instanceUuid is not None: payload.update( { 'instanceUuid':  rq_instanceUuid })
        if rq_netconfPort is not None: payload.update( { 'netconfPort':  rq_netconfPort })
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_c5acd9fa4c1a8abc').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.put(apply_path_params('/dna/intent/api/v1/global-credential/netconf', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.put(apply_path_params('/dna/intent/api/v1/global-credential/netconf', path_params), params=params, json=payload)

        return self._object_factory('bpm_c5acd9fa4c1a8abc', json_data)


    # Delete all discovery
    def delete_all_discovery(self, headers=None,payload=None,**request_parameters):
        if headers is not None:
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = {
        }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_db8e09234a988bab').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.delete(apply_path_params('/dna/intent/api/v1/discovery', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.delete(apply_path_params('/dna/intent/api/v1/discovery', path_params), params=params, json=payload)

        return self._object_factory('bpm_db8e09234a988bab', json_data)


    # Delete global credentials by Id
    def delete_global_credentials_by_id(self, path_param_global_credential_id, headers=None,payload=None,**request_parameters):
        check_type( path_param_global_credential_id, basestring, may_be_none=False)
        if headers is not None:
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = {
        }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
            'globalCredentialId': path_param_global_credential_id,
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_f5ac590c4ca9975a').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.delete(apply_path_params('/dna/intent/api/v1/global-credential/${globalCredentialId}', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.delete(apply_path_params('/dna/intent/api/v1/global-credential/${globalCredentialId}', path_params), params=params, json=payload)

        return self._object_factory('bpm_f5ac590c4ca9975a', json_data)


    # Update HTTP read credential
    def update_http_read_credential(self, rq_comments = None, rq_credentialType = None, rq_description = None, rq_id = None, rq_instanceTenantId = None, rq_instanceUuid = None, rq_password = None, rq_port = None, rq_secure = None, rq_username = None, headers=None,payload=None,**request_parameters):
        if headers is not None:
            check_type( headers.get('Content-Type', self._session.headers.get('Content-Type')), basestring, may_be_none=False)
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = {
        }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        if rq_comments is not None: payload.update( { 'comments':  rq_comments })
        if rq_credentialType is not None: payload.update( { 'credentialType':  rq_credentialType })
        if rq_description is not None: payload.update( { 'description':  rq_description })
        if rq_id is not None: payload.update( { 'id':  rq_id })
        if rq_instanceTenantId is not None: payload.update( { 'instanceTenantId':  rq_instanceTenantId })
        if rq_instanceUuid is not None: payload.update( { 'instanceUuid':  rq_instanceUuid })
        if rq_password is not None: payload.update( { 'password':  rq_password })
        if rq_port is not None: payload.update( { 'port':  rq_port })
        if rq_secure is not None: payload.update( { 'secure':  rq_secure })
        if rq_username is not None: payload.update( { 'username':  rq_username })
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_89b36b4649999d81').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.put(apply_path_params('/dna/intent/api/v1/global-credential/http-read', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.put(apply_path_params('/dna/intent/api/v1/global-credential/http-read', path_params), params=params, json=payload)

        return self._object_factory('bpm_89b36b4649999d81', json_data)


    # Update CLI credentials
    def update_cli_credentials(self, rq_comments = None, rq_credentialType = None, rq_description = None, rq_enablePassword = None, rq_id = None, rq_instanceTenantId = None, rq_instanceUuid = None, rq_password = None, rq_username = None, headers=None,payload=None,**request_parameters):
        if headers is not None:
            check_type( headers.get('Content-Type', self._session.headers.get('Content-Type')), basestring, may_be_none=False)
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = {
        }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        if rq_comments is not None: payload.update( { 'comments':  rq_comments })
        if rq_credentialType is not None: payload.update( { 'credentialType':  rq_credentialType })
        if rq_description is not None: payload.update( { 'description':  rq_description })
        if rq_enablePassword is not None: payload.update( { 'enablePassword':  rq_enablePassword })
        if rq_id is not None: payload.update( { 'id':  rq_id })
        if rq_instanceTenantId is not None: payload.update( { 'instanceTenantId':  rq_instanceTenantId })
        if rq_instanceUuid is not None: payload.update( { 'instanceUuid':  rq_instanceUuid })
        if rq_password is not None: payload.update( { 'password':  rq_password })
        if rq_username is not None: payload.update( { 'username':  rq_username })
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_fba0d80747eb82e8').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.put(apply_path_params('/dna/intent/api/v1/global-credential/cli', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.put(apply_path_params('/dna/intent/api/v1/global-credential/cli', path_params), params=params, json=payload)

        return self._object_factory('bpm_fba0d80747eb82e8', json_data)


    # Create SNMPv3 credentials
    def create_snmpv3_credentials(self, headers=None,payload=None,**request_parameters):
        if headers is not None:
            check_type( headers.get('Content-Type', self._session.headers.get('Content-Type')), basestring, may_be_none=False)
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = {
        }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or []

        self._request_validator('jsd_979688084b7ba60d').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.post(apply_path_params('/dna/intent/api/v1/global-credential/snmpv3', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.post(apply_path_params('/dna/intent/api/v1/global-credential/snmpv3', path_params), params=params, json=payload)

        return self._object_factory('bpm_979688084b7ba60d', json_data)


    # Get Devices discovered by Id
    def get_devices_discovered_by_id(self, path_param_id, param_task_id = None, headers=None,payload=None,**request_parameters):
        check_type( param_task_id, basestring)
        check_type( path_param_id, basestring, may_be_none=False)
        if headers is not None:
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = {
            'taskId': param_task_id,
        }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
            'id': path_param_id,
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_a6965b454c9a8663').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.get(apply_path_params('/dna/intent/api/v1/discovery/${id}/network-device/count', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.get(apply_path_params('/dna/intent/api/v1/discovery/${id}/network-device/count', path_params), params=params, json=payload)

        return self._object_factory('bpm_a6965b454c9a8663', json_data)


    # Get Discovered network devices by discovery Id
    def get_discovered_network_devices_by_discovery_id(self, path_param_id, param_task_id = None, headers=None,payload=None,**request_parameters):
        check_type( param_task_id, basestring)
        check_type( path_param_id, basestring, may_be_none=False)
        if headers is not None:
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = {
            'taskId': param_task_id,
        }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
            'id': path_param_id,
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_f6ac994f451ba011').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.get(apply_path_params('/dna/intent/api/v1/discovery/${id}/network-device', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.get(apply_path_params('/dna/intent/api/v1/discovery/${id}/network-device', path_params), params=params, json=payload)

        return self._object_factory('bpm_f6ac994f451ba011', json_data)


    # Get Global credentials
    def get_global_credentials(self, param_credential_sub_type, param_order = None, param_sort_by = None, headers=None,payload=None,**request_parameters):
        check_type( param_credential_sub_type, basestring, may_be_none=False)
        check_type( param_sort_by, basestring)
        check_type( param_order, basestring)
        if headers is not None:
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = {
            'credentialSubType': param_credential_sub_type,
            'sortBy': param_sort_by,
            'order': param_order,
        }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_ff816b8e435897eb').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.get(apply_path_params('/dna/intent/api/v1/global-credential', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.get(apply_path_params('/dna/intent/api/v1/global-credential', path_params), params=params, json=payload)

        return self._object_factory('bpm_ff816b8e435897eb', json_data)



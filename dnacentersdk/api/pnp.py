# -*- coding: utf-8 -*-
"""DNA Center PnP API wrapper.

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

class Pnp( object ):
    """DNA Center PnP API.

    Wraps the DNA Center PnP API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new Pnp object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the DNA Center service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(Pnp, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator


    # Get Sync Result for Virtual Account
    def get_sync_result_for_virtual_account(self, path_param_domain, path_param_name, headers=None,payload=None,**request_parameters):
        check_type( path_param_domain, basestring, may_be_none=False)
        check_type( path_param_name, basestring, may_be_none=False)
        if headers is not None:
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = {
        }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
            'domain': path_param_domain,
            'name': path_param_name,
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_0a9c988445cb91c8').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.get(apply_path_params('/dna/intent/api/v1/onboarding/pnp-device/sacct/${domain}/vacct/${name}/sync-result', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.get(apply_path_params('/dna/intent/api/v1/onboarding/pnp-device/sacct/${domain}/vacct/${name}/sync-result', path_params), params=params, json=payload)

        return self._object_factory('bpm_0a9c988445cb91c8', json_data)


    # Import Devices in bulk
    def import_devices_in_bulk(self, headers=None,payload=None,**request_parameters):
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

        self._request_validator('jsd_21a6db2540298f55').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.post(apply_path_params('/dna/intent/api/v1/onboarding/pnp-device/import', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.post(apply_path_params('/dna/intent/api/v1/onboarding/pnp-device/import', path_params), params=params, json=payload)

        return self._object_factory('bpm_21a6db2540298f55', json_data)


    # Update Workflow
    def update_workflow(self, path_param_id, rq__id = None, rq_addToInventory = None, rq_addedOn = None, rq_configId = None, rq_currTaskIdx = None, rq_description = None, rq_endTime = None, rq_execTime = None, rq_imageId = None, rq_instanceType = None, rq_lastupdateOn = None, rq_name = None, rq_startTime = None, rq_state = None, rq_tasks = None, rq_tenantId = None, rq_type = None, rq_useState = None, rq_version = None, headers=None,payload=None,**request_parameters):
        check_type( path_param_id, basestring, may_be_none=False)
        if headers is not None:
            check_type( headers.get('Content-Type', self._session.headers.get('Content-Type')), basestring, may_be_none=False)
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = {
        }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
            'id': path_param_id,
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        if rq__id is not None: payload.update( { '_id':  rq__id })
        if rq_addToInventory is not None: payload.update( { 'addToInventory':  rq_addToInventory })
        if rq_addedOn is not None: payload.update( { 'addedOn':  rq_addedOn })
        if rq_configId is not None: payload.update( { 'configId':  rq_configId })
        if rq_currTaskIdx is not None: payload.update( { 'currTaskIdx':  rq_currTaskIdx })
        if rq_description is not None: payload.update( { 'description':  rq_description })
        if rq_endTime is not None: payload.update( { 'endTime':  rq_endTime })
        if rq_execTime is not None: payload.update( { 'execTime':  rq_execTime })
        if rq_imageId is not None: payload.update( { 'imageId':  rq_imageId })
        if rq_instanceType is not None: payload.update( { 'instanceType':  rq_instanceType })
        if rq_lastupdateOn is not None: payload.update( { 'lastupdateOn':  rq_lastupdateOn })
        if rq_name is not None: payload.update( { 'name':  rq_name })
        if rq_startTime is not None: payload.update( { 'startTime':  rq_startTime })
        if rq_state is not None: payload.update( { 'state':  rq_state })
        if rq_tasks is not None: payload.update( { 'tasks':  rq_tasks })
        if rq_tenantId is not None: payload.update( { 'tenantId':  rq_tenantId })
        if rq_type is not None: payload.update( { 'type':  rq_type })
        if rq_useState is not None: payload.update( { 'useState':  rq_useState })
        if rq_version is not None: payload.update( { 'version':  rq_version })
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_3086c9624f498b85').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.put(apply_path_params('/dna/intent/api/v1/onboarding/pnp-workflow/${id}', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.put(apply_path_params('/dna/intent/api/v1/onboarding/pnp-workflow/${id}', path_params), params=params, json=payload)

        return self._object_factory('bpm_3086c9624f498b85', json_data)


    # Un-Claim Device
    def un_claim_device(self, rq_deviceIdList = None, headers=None,payload=None,**request_parameters):
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
        if rq_deviceIdList is not None: payload.update( { 'deviceIdList':  rq_deviceIdList })
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_0b836b7b4b6a9fd5').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.post(apply_path_params('/dna/intent/api/v1/onboarding/pnp-device/unclaim', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.post(apply_path_params('/dna/intent/api/v1/onboarding/pnp-device/unclaim', path_params), params=params, json=payload)

        return self._object_factory('bpm_0b836b7b4b6a9fd5', json_data)


    # Add Virtual Account
    def add_virtual_account(self, rq_autoSyncPeriod = None, rq_ccoUser = None, rq_expiry = None, rq_lastSync = None, rq_profile = None, rq_smartAccountId = None, rq_syncResult = None, rq_syncResultStr = None, rq_syncStartTime = None, rq_syncStatus = None, rq_tenantId = None, rq_token = None, rq_virtualAccountId = None, headers=None,payload=None,**request_parameters):
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
        if rq_autoSyncPeriod is not None: payload.update( { 'autoSyncPeriod':  rq_autoSyncPeriod })
        if rq_ccoUser is not None: payload.update( { 'ccoUser':  rq_ccoUser })
        if rq_expiry is not None: payload.update( { 'expiry':  rq_expiry })
        if rq_lastSync is not None: payload.update( { 'lastSync':  rq_lastSync })
        if rq_profile is not None: payload.update( { 'profile':  rq_profile })
        if rq_smartAccountId is not None: payload.update( { 'smartAccountId':  rq_smartAccountId })
        if rq_syncResult is not None: payload.update( { 'syncResult':  rq_syncResult })
        if rq_syncResultStr is not None: payload.update( { 'syncResultStr':  rq_syncResultStr })
        if rq_syncStartTime is not None: payload.update( { 'syncStartTime':  rq_syncStartTime })
        if rq_syncStatus is not None: payload.update( { 'syncStatus':  rq_syncStatus })
        if rq_tenantId is not None: payload.update( { 'tenantId':  rq_tenantId })
        if rq_token is not None: payload.update( { 'token':  rq_token })
        if rq_virtualAccountId is not None: payload.update( { 'virtualAccountId':  rq_virtualAccountId })
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_1e962af345b8b59f').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.post(apply_path_params('/dna/intent/api/v1/onboarding/pnp-settings/savacct', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.post(apply_path_params('/dna/intent/api/v1/onboarding/pnp-settings/savacct', path_params), params=params, json=payload)

        return self._object_factory('bpm_1e962af345b8b59f', json_data)


    # Update Device
    def update_device(self, path_param_id, rq__id = None, rq_deviceInfo = None, rq_runSummaryList = None, rq_systemResetWorkflow = None, rq_systemWorkflow = None, rq_tenantId = None, rq_version = None, rq_workflow = None, rq_workflowParameters = None, headers=None,payload=None,**request_parameters):
        check_type( path_param_id, basestring, may_be_none=False)
        if headers is not None:
            check_type( headers.get('Content-Type', self._session.headers.get('Content-Type')), basestring, may_be_none=False)
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = {
        }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
            'id': path_param_id,
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        if rq__id is not None: payload.update( { '_id':  rq__id })
        if rq_deviceInfo is not None: payload.update( { 'deviceInfo':  rq_deviceInfo })
        if rq_runSummaryList is not None: payload.update( { 'runSummaryList':  rq_runSummaryList })
        if rq_systemResetWorkflow is not None: payload.update( { 'systemResetWorkflow':  rq_systemResetWorkflow })
        if rq_systemWorkflow is not None: payload.update( { 'systemWorkflow':  rq_systemWorkflow })
        if rq_tenantId is not None: payload.update( { 'tenantId':  rq_tenantId })
        if rq_version is not None: payload.update( { 'version':  rq_version })
        if rq_workflow is not None: payload.update( { 'workflow':  rq_workflow })
        if rq_workflowParameters is not None: payload.update( { 'workflowParameters':  rq_workflowParameters })
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_09b0f9ce4239ae10').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.put(apply_path_params('/dna/intent/api/v1/onboarding/pnp-device/${id}', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.put(apply_path_params('/dna/intent/api/v1/onboarding/pnp-device/${id}', path_params), params=params, json=payload)

        return self._object_factory('bpm_09b0f9ce4239ae10', json_data)


    # Claim a Device to a Site
    def claim_a_device_to_a_site(self, rq_deviceId = None, rq_siteId = None, rq_type = None, headers=None,payload=None,**request_parameters):
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
        if rq_deviceId is not None: payload.update( { 'deviceId':  rq_deviceId })
        if rq_siteId is not None: payload.update( { 'siteId':  rq_siteId })
        if rq_type is not None: payload.update( { 'type':  rq_type })
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_5889fb844939a13b').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.post(apply_path_params('/dna/intent/api/v1/onboarding/pnp-device/site-claim', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.post(apply_path_params('/dna/intent/api/v1/onboarding/pnp-device/site-claim', path_params), params=params, json=payload)

        return self._object_factory('bpm_5889fb844939a13b', json_data)


    # Deregister Virtual Account
    def deregister_virtual_account(self, param_domain, param_name, headers=None,payload=None,**request_parameters):
        check_type( param_domain, basestring, may_be_none=False)
        check_type( param_name, basestring, may_be_none=False)
        if headers is not None:
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = {
            'domain': param_domain,
            'name': param_name,
        }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_2499e9ad42e8ae5b').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.delete(apply_path_params('/dna/intent/api/v1/onboarding/pnp-settings/vacct', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.delete(apply_path_params('/dna/intent/api/v1/onboarding/pnp-settings/vacct', path_params), params=params, json=payload)

        return self._object_factory('bpm_2499e9ad42e8ae5b', json_data)


    # Get Smart Account List
    def get_smart_account_list(self, headers=None,payload=None,**request_parameters):
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

        self._request_validator('jsd_3cb24acb486b89d2').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.get(apply_path_params('/dna/intent/api/v1/onboarding/pnp-settings/sacct', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.get(apply_path_params('/dna/intent/api/v1/onboarding/pnp-settings/sacct', path_params), params=params, json=payload)

        return self._object_factory('bpm_3cb24acb486b89d2', json_data)


    # Get Workflow by Id
    def get_workflow_by_id(self, path_param_id, headers=None,payload=None,**request_parameters):
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

        self._request_validator('jsd_80acb88e4ac9ac6d').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.get(apply_path_params('/dna/intent/api/v1/onboarding/pnp-workflow/${id}', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.get(apply_path_params('/dna/intent/api/v1/onboarding/pnp-workflow/${id}', path_params), params=params, json=payload)

        return self._object_factory('bpm_80acb88e4ac9ac6d', json_data)


    # Update PnP Server Profile
    def update_pnp_server_profile(self, rq_autoSyncPeriod = None, rq_ccoUser = None, rq_expiry = None, rq_lastSync = None, rq_profile = None, rq_smartAccountId = None, rq_syncResult = None, rq_syncResultStr = None, rq_syncStartTime = None, rq_syncStatus = None, rq_tenantId = None, rq_token = None, rq_virtualAccountId = None, headers=None,payload=None,**request_parameters):
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
        if rq_autoSyncPeriod is not None: payload.update( { 'autoSyncPeriod':  rq_autoSyncPeriod })
        if rq_ccoUser is not None: payload.update( { 'ccoUser':  rq_ccoUser })
        if rq_expiry is not None: payload.update( { 'expiry':  rq_expiry })
        if rq_lastSync is not None: payload.update( { 'lastSync':  rq_lastSync })
        if rq_profile is not None: payload.update( { 'profile':  rq_profile })
        if rq_smartAccountId is not None: payload.update( { 'smartAccountId':  rq_smartAccountId })
        if rq_syncResult is not None: payload.update( { 'syncResult':  rq_syncResult })
        if rq_syncResultStr is not None: payload.update( { 'syncResultStr':  rq_syncResultStr })
        if rq_syncStartTime is not None: payload.update( { 'syncStartTime':  rq_syncStartTime })
        if rq_syncStatus is not None: payload.update( { 'syncStatus':  rq_syncStatus })
        if rq_tenantId is not None: payload.update( { 'tenantId':  rq_tenantId })
        if rq_token is not None: payload.update( { 'token':  rq_token })
        if rq_virtualAccountId is not None: payload.update( { 'virtualAccountId':  rq_virtualAccountId })
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_6f9819e84178870c').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.put(apply_path_params('/dna/intent/api/v1/onboarding/pnp-settings/savacct', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.put(apply_path_params('/dna/intent/api/v1/onboarding/pnp-settings/savacct', path_params), params=params, json=payload)

        return self._object_factory('bpm_6f9819e84178870c', json_data)


    # Get Workflow Count
    def get_workflow_count(self, param_name = None, headers=None,payload=None,**request_parameters):
        check_type( param_name, basestring)
        if headers is not None:
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = {
            'name': param_name,
        }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_7989f86846faaf99').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.get(apply_path_params('/dna/intent/api/v1/onboarding/pnp-workflow/count', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.get(apply_path_params('/dna/intent/api/v1/onboarding/pnp-workflow/count', path_params), params=params, json=payload)

        return self._object_factory('bpm_7989f86846faaf99', json_data)


    # Update PnP global settings
    def update_pnp_global_settings(self, rq__id = None, rq_aaaCredentials = None, rq_acceptEula = None, rq_defaultProfile = None, rq_savaMappingList = None, rq_taskTimeOuts = None, rq_tenantId = None, rq_version = None, headers=None,payload=None,**request_parameters):
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
        if rq__id is not None: payload.update( { '_id':  rq__id })
        if rq_aaaCredentials is not None: payload.update( { 'aaaCredentials':  rq_aaaCredentials })
        if rq_acceptEula is not None: payload.update( { 'acceptEula':  rq_acceptEula })
        if rq_defaultProfile is not None: payload.update( { 'defaultProfile':  rq_defaultProfile })
        if rq_savaMappingList is not None: payload.update( { 'savaMappingList':  rq_savaMappingList })
        if rq_taskTimeOuts is not None: payload.update( { 'taskTimeOuts':  rq_taskTimeOuts })
        if rq_tenantId is not None: payload.update( { 'tenantId':  rq_tenantId })
        if rq_version is not None: payload.update( { 'version':  rq_version })
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_8da0391947088a5a').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.put(apply_path_params('/dna/intent/api/v1/onboarding/pnp-settings', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.put(apply_path_params('/dna/intent/api/v1/onboarding/pnp-settings', path_params), params=params, json=payload)

        return self._object_factory('bpm_8da0391947088a5a', json_data)


    # Get PnP global settings
    def get_pnp_global_settings(self, headers=None,payload=None,**request_parameters):
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

        self._request_validator('jsd_7e92f9eb46db8320').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.get(apply_path_params('/dna/intent/api/v1/onboarding/pnp-settings', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.get(apply_path_params('/dna/intent/api/v1/onboarding/pnp-settings', path_params), params=params, json=payload)

        return self._object_factory('bpm_7e92f9eb46db8320', json_data)


    # Reset Device
    def reset_device(self, rq_deviceResetList = None, rq_projectId = None, rq_workflowId = None, headers=None,payload=None,**request_parameters):
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
        if rq_deviceResetList is not None: payload.update( { 'deviceResetList':  rq_deviceResetList })
        if rq_projectId is not None: payload.update( { 'projectId':  rq_projectId })
        if rq_workflowId is not None: payload.update( { 'workflowId':  rq_workflowId })
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_9e857b5a4a0bbcdb').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.post(apply_path_params('/dna/intent/api/v1/onboarding/pnp-device/reset', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.post(apply_path_params('/dna/intent/api/v1/onboarding/pnp-device/reset', path_params), params=params, json=payload)

        return self._object_factory('bpm_9e857b5a4a0bbcdb', json_data)


    # Sync Virtual Account Devices
    def sync_virtual_account_devices(self, rq_autoSyncPeriod = None, rq_ccoUser = None, rq_expiry = None, rq_lastSync = None, rq_profile = None, rq_smartAccountId = None, rq_syncResult = None, rq_syncResultStr = None, rq_syncStartTime = None, rq_syncStatus = None, rq_tenantId = None, rq_token = None, rq_virtualAccountId = None, headers=None,payload=None,**request_parameters):
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
        if rq_autoSyncPeriod is not None: payload.update( { 'autoSyncPeriod':  rq_autoSyncPeriod })
        if rq_ccoUser is not None: payload.update( { 'ccoUser':  rq_ccoUser })
        if rq_expiry is not None: payload.update( { 'expiry':  rq_expiry })
        if rq_lastSync is not None: payload.update( { 'lastSync':  rq_lastSync })
        if rq_profile is not None: payload.update( { 'profile':  rq_profile })
        if rq_smartAccountId is not None: payload.update( { 'smartAccountId':  rq_smartAccountId })
        if rq_syncResult is not None: payload.update( { 'syncResult':  rq_syncResult })
        if rq_syncResultStr is not None: payload.update( { 'syncResultStr':  rq_syncResultStr })
        if rq_syncStartTime is not None: payload.update( { 'syncStartTime':  rq_syncStartTime })
        if rq_syncStatus is not None: payload.update( { 'syncStatus':  rq_syncStatus })
        if rq_tenantId is not None: payload.update( { 'tenantId':  rq_tenantId })
        if rq_token is not None: payload.update( { 'token':  rq_token })
        if rq_virtualAccountId is not None: payload.update( { 'virtualAccountId':  rq_virtualAccountId })
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_a4b6c87a4ffb9efa').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.post(apply_path_params('/dna/intent/api/v1/onboarding/pnp-device/vacct-sync', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.post(apply_path_params('/dna/intent/api/v1/onboarding/pnp-device/vacct-sync', path_params), params=params, json=payload)

        return self._object_factory('bpm_a4b6c87a4ffb9efa', json_data)


    # Get Workflows
    def get_workflows(self, param_limit = None, param_name = None, param_offset = None, param_sort = None, param_sort_order = None, param_type = None, headers=None,payload=None,**request_parameters):
        check_type( param_limit, int)
        check_type( param_offset, int)
        check_type( param_sort, basestring)
        check_type( param_sort_order, basestring)
        check_type( param_type, basestring)
        check_type( param_name, basestring)
        if headers is not None:
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = {
            'limit': param_limit,
            'offset': param_offset,
            'sort': param_sort,
            'sortOrder': param_sort_order,
            'type': param_type,
            'name': param_name,
        }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_aeb4dad04a99bbe3').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.get(apply_path_params('/dna/intent/api/v1/onboarding/pnp-workflow', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.get(apply_path_params('/dna/intent/api/v1/onboarding/pnp-workflow', path_params), params=params, json=payload)

        return self._object_factory('bpm_aeb4dad04a99bbe3', json_data)


    # Delete Workflow By Id
    def delete_workflow_by_id(self, path_param_id, headers=None,payload=None,**request_parameters):
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

        self._request_validator('jsd_af8d7b0e470b8ae2').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.delete(apply_path_params('/dna/intent/api/v1/onboarding/pnp-workflow/${id}', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.delete(apply_path_params('/dna/intent/api/v1/onboarding/pnp-workflow/${id}', path_params), params=params, json=payload)

        return self._object_factory('bpm_af8d7b0e470b8ae2', json_data)


    # Get Device by Id
    def get_device_by_id(self, path_param_id, headers=None,payload=None,**request_parameters):
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

        self._request_validator('jsd_bab6c9e5440885cc').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.get(apply_path_params('/dna/intent/api/v1/onboarding/pnp-device/${id}', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.get(apply_path_params('/dna/intent/api/v1/onboarding/pnp-device/${id}', path_params), params=params, json=payload)

        return self._object_factory('bpm_bab6c9e5440885cc', json_data)


    # Get Virtual Account List
    def get_virtual_account_list(self, path_param_domain, headers=None,payload=None,**request_parameters):
        check_type( path_param_domain, basestring, may_be_none=False)
        if headers is not None:
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = {
        }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
            'domain': path_param_domain,
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_70a479a6462a9496').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.get(apply_path_params('/dna/intent/api/v1/onboarding/pnp-settings/sacct/${domain}/vacct', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.get(apply_path_params('/dna/intent/api/v1/onboarding/pnp-settings/sacct/${domain}/vacct', path_params), params=params, json=payload)

        return self._object_factory('bpm_70a479a6462a9496', json_data)


    # Preview Config
    def preview_config(self, rq_deviceId = None, rq_siteId = None, rq_type = None, headers=None,payload=None,**request_parameters):
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
        if rq_deviceId is not None: payload.update( { 'deviceId':  rq_deviceId })
        if rq_siteId is not None: payload.update( { 'siteId':  rq_siteId })
        if rq_type is not None: payload.update( { 'type':  rq_type })
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_cf9418234d9ab37e').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.post(apply_path_params('/dna/intent/api/v1/onboarding/pnp-device/site-config-preview', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.post(apply_path_params('/dna/intent/api/v1/onboarding/pnp-device/site-config-preview', path_params), params=params, json=payload)

        return self._object_factory('bpm_cf9418234d9ab37e', json_data)


    # Claim Device
    def claim_device(self, rq_configFileUrl = None, rq_configId = None, rq_deviceClaimList = None, rq_fileServiceId = None, rq_imageId = None, rq_imageUrl = None, rq_populateInventory = None, rq_projectId = None, rq_workflowId = None, headers=None,payload=None,**request_parameters):
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
        if rq_configFileUrl is not None: payload.update( { 'configFileUrl':  rq_configFileUrl })
        if rq_configId is not None: payload.update( { 'configId':  rq_configId })
        if rq_deviceClaimList is not None: payload.update( { 'deviceClaimList':  rq_deviceClaimList })
        if rq_fileServiceId is not None: payload.update( { 'fileServiceId':  rq_fileServiceId })
        if rq_imageId is not None: payload.update( { 'imageId':  rq_imageId })
        if rq_imageUrl is not None: payload.update( { 'imageUrl':  rq_imageUrl })
        if rq_populateInventory is not None: payload.update( { 'populateInventory':  rq_populateInventory })
        if rq_projectId is not None: payload.update( { 'projectId':  rq_projectId })
        if rq_workflowId is not None: payload.update( { 'workflowId':  rq_workflowId })
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_d8a619974a8a8c48').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.post(apply_path_params('/dna/intent/api/v1/onboarding/pnp-device/claim', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.post(apply_path_params('/dna/intent/api/v1/onboarding/pnp-device/claim', path_params), params=params, json=payload)

        return self._object_factory('bpm_d8a619974a8a8c48', json_data)


    # Get Device list
    def get_device_list(self, param_cm_state = None, param_last_contact = None, param_limit = None, param_name = None, param_offset = None, param_onb_state = None, param_pid = None, param_project_id = None, param_project_name = None, param_serial_number = None, param_smart_account_id = None, param_sort = None, param_sort_order = None, param_source = None, param_state = None, param_virtual_account_id = None, param_workflow_id = None, param_workflow_name = None, headers=None,payload=None,**request_parameters):
        check_type( param_limit, int)
        check_type( param_offset, int)
        check_type( param_sort, basestring)
        check_type( param_sort_order, basestring)
        check_type( param_serial_number, basestring)
        check_type( param_state, basestring)
        check_type( param_onb_state, basestring)
        check_type( param_cm_state, basestring)
        check_type( param_name, basestring)
        check_type( param_pid, basestring)
        check_type( param_source, basestring)
        check_type( param_project_id, basestring)
        check_type( param_workflow_id, basestring)
        check_type( param_project_name, basestring)
        check_type( param_workflow_name, basestring)
        check_type( param_smart_account_id, basestring)
        check_type( param_virtual_account_id, basestring)
        check_type( param_last_contact, bool)
        if headers is not None:
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = {
            'limit': param_limit,
            'offset': param_offset,
            'sort': param_sort,
            'sortOrder': param_sort_order,
            'serialNumber': param_serial_number,
            'state': param_state,
            'onbState': param_onb_state,
            'cmState': param_cm_state,
            'name': param_name,
            'pid': param_pid,
            'source': param_source,
            'projectId': param_project_id,
            'workflowId': param_workflow_id,
            'projectName': param_project_name,
            'workflowName': param_workflow_name,
            'smartAccountId': param_smart_account_id,
            'virtualAccountId': param_virtual_account_id,
            'lastContact': param_last_contact,
        }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_e6b3db8046c99654').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.get(apply_path_params('/dna/intent/api/v1/onboarding/pnp-device', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.get(apply_path_params('/dna/intent/api/v1/onboarding/pnp-device', path_params), params=params, json=payload)

        return self._object_factory('bpm_e6b3db8046c99654', json_data)


    # Add a Workflow
    def add_a_workflow(self, rq__id = None, rq_addToInventory = None, rq_addedOn = None, rq_configId = None, rq_currTaskIdx = None, rq_description = None, rq_endTime = None, rq_execTime = None, rq_imageId = None, rq_instanceType = None, rq_lastupdateOn = None, rq_name = None, rq_startTime = None, rq_state = None, rq_tasks = None, rq_tenantId = None, rq_type = None, rq_useState = None, rq_version = None, headers=None,payload=None,**request_parameters):
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
        if rq__id is not None: payload.update( { '_id':  rq__id })
        if rq_addToInventory is not None: payload.update( { 'addToInventory':  rq_addToInventory })
        if rq_addedOn is not None: payload.update( { 'addedOn':  rq_addedOn })
        if rq_configId is not None: payload.update( { 'configId':  rq_configId })
        if rq_currTaskIdx is not None: payload.update( { 'currTaskIdx':  rq_currTaskIdx })
        if rq_description is not None: payload.update( { 'description':  rq_description })
        if rq_endTime is not None: payload.update( { 'endTime':  rq_endTime })
        if rq_execTime is not None: payload.update( { 'execTime':  rq_execTime })
        if rq_imageId is not None: payload.update( { 'imageId':  rq_imageId })
        if rq_instanceType is not None: payload.update( { 'instanceType':  rq_instanceType })
        if rq_lastupdateOn is not None: payload.update( { 'lastupdateOn':  rq_lastupdateOn })
        if rq_name is not None: payload.update( { 'name':  rq_name })
        if rq_startTime is not None: payload.update( { 'startTime':  rq_startTime })
        if rq_state is not None: payload.update( { 'state':  rq_state })
        if rq_tasks is not None: payload.update( { 'tasks':  rq_tasks })
        if rq_tenantId is not None: payload.update( { 'tenantId':  rq_tenantId })
        if rq_type is not None: payload.update( { 'type':  rq_type })
        if rq_useState is not None: payload.update( { 'useState':  rq_useState })
        if rq_version is not None: payload.update( { 'version':  rq_version })
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_848b5a7b4f9b8c12').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.post(apply_path_params('/dna/intent/api/v1/onboarding/pnp-workflow', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.post(apply_path_params('/dna/intent/api/v1/onboarding/pnp-workflow', path_params), params=params, json=payload)

        return self._object_factory('bpm_848b5a7b4f9b8c12', json_data)


    # Get Device Count
    def get_device_count(self, param_cm_state = None, param_last_contact = None, param_name = None, param_onb_state = None, param_pid = None, param_project_id = None, param_project_name = None, param_serial_number = None, param_smart_account_id = None, param_source = None, param_state = None, param_virtual_account_id = None, param_workflow_id = None, param_workflow_name = None, headers=None,payload=None,**request_parameters):
        check_type( param_serial_number, basestring)
        check_type( param_state, basestring)
        check_type( param_onb_state, basestring)
        check_type( param_cm_state, basestring)
        check_type( param_name, basestring)
        check_type( param_pid, basestring)
        check_type( param_source, basestring)
        check_type( param_project_id, basestring)
        check_type( param_workflow_id, basestring)
        check_type( param_project_name, basestring)
        check_type( param_workflow_name, basestring)
        check_type( param_smart_account_id, basestring)
        check_type( param_virtual_account_id, basestring)
        check_type( param_last_contact, bool)
        if headers is not None:
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = {
            'serialNumber': param_serial_number,
            'state': param_state,
            'onbState': param_onb_state,
            'cmState': param_cm_state,
            'name': param_name,
            'pid': param_pid,
            'source': param_source,
            'projectId': param_project_id,
            'workflowId': param_workflow_id,
            'projectName': param_project_name,
            'workflowName': param_workflow_name,
            'smartAccountId': param_smart_account_id,
            'virtualAccountId': param_virtual_account_id,
            'lastContact': param_last_contact,
        }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_d9a1fa9c4068b23c').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.get(apply_path_params('/dna/intent/api/v1/onboarding/pnp-device/count', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.get(apply_path_params('/dna/intent/api/v1/onboarding/pnp-device/count', path_params), params=params, json=payload)

        return self._object_factory('bpm_d9a1fa9c4068b23c', json_data)


    # Get Device History
    def get_device_history(self, param_serial_number, param_sort = None, param_sort_order = None, headers=None,payload=None,**request_parameters):
        check_type( param_serial_number, basestring, may_be_none=False)
        check_type( param_sort, basestring)
        check_type( param_sort_order, basestring)
        if headers is not None:
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = {
            'serialNumber': param_serial_number,
            'sort': param_sort,
            'sortOrder': param_sort_order,
        }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_f09319674049a7d4').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.get(apply_path_params('/dna/intent/api/v1/onboarding/pnp-device/history', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.get(apply_path_params('/dna/intent/api/v1/onboarding/pnp-device/history', path_params), params=params, json=payload)

        return self._object_factory('bpm_f09319674049a7d4', json_data)


    # Delete Device by Id from PnP
    def delete_device_by_id_from_pnp(self, path_param_id, headers=None,payload=None,**request_parameters):
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

        self._request_validator('jsd_cdab9b474899ae06').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.delete(apply_path_params('/dna/intent/api/v1/onboarding/pnp-device/${id}', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.delete(apply_path_params('/dna/intent/api/v1/onboarding/pnp-device/${id}', path_params), params=params, json=payload)

        return self._object_factory('bpm_cdab9b474899ae06', json_data)


    # Add Device
    def add_device(self, rq__id = None, rq_deviceInfo = None, rq_runSummaryList = None, rq_systemResetWorkflow = None, rq_systemWorkflow = None, rq_tenantId = None, rq_version = None, rq_workflow = None, rq_workflowParameters = None, headers=None,payload=None,**request_parameters):
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
        if rq__id is not None: payload.update( { '_id':  rq__id })
        if rq_deviceInfo is not None: payload.update( { 'deviceInfo':  rq_deviceInfo })
        if rq_runSummaryList is not None: payload.update( { 'runSummaryList':  rq_runSummaryList })
        if rq_systemResetWorkflow is not None: payload.update( { 'systemResetWorkflow':  rq_systemResetWorkflow })
        if rq_systemWorkflow is not None: payload.update( { 'systemWorkflow':  rq_systemWorkflow })
        if rq_tenantId is not None: payload.update( { 'tenantId':  rq_tenantId })
        if rq_version is not None: payload.update( { 'version':  rq_version })
        if rq_workflow is not None: payload.update( { 'workflow':  rq_workflow })
        if rq_workflowParameters is not None: payload.update( { 'workflowParameters':  rq_workflowParameters })
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_f3b26b5544cabab9').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.post(apply_path_params('/dna/intent/api/v1/onboarding/pnp-device', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.post(apply_path_params('/dna/intent/api/v1/onboarding/pnp-device', path_params), params=params, json=payload)

        return self._object_factory('bpm_f3b26b5544cabab9', json_data)



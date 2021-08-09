# -*- coding: utf-8 -*-
"""Cisco DNA Center Device Onboarding (PnP) API wrapper.

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


class DeviceOnboardingPnp(object):
    """Cisco DNA Center Device Onboarding (PnP) API (version: 1.3.1).

    Wraps the DNA Center Device Onboarding (PnP)
    API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new DeviceOnboardingPnp
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the DNA Center service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(DeviceOnboardingPnp, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def get_sync_result_for_virtual_account(self,
                                            domain,
                                            name,
                                            headers=None,
                                            **request_parameters):
        """Returns the summary of devices synced from the given smart
        account & virtual account with PnP.

        Args:
            domain(basestring): Smart Account Domain.
            name(basestring): Virtual Account Name.
            headers(dict): Dictionary of HTTP Headers to send with the Request
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
        check_type(domain, basestring,
                   may_be_none=False)
        check_type(name, basestring,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        _params = {
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'domain': domain,
            'name': name,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/onboarding/pnp-'
                 + 'device/sacct/${domain}/vacct/${name}/sync-result')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_0a9c988445cb91c8_v1_3_1', json_data)

    def un_claim_device(self,
                        deviceIdList=None,
                        headers=None,
                        payload=None,
                        active_validation=True,
                        **request_parameters):
        """Un-Claims one of more devices with specified workflow.

        Args:
            deviceIdList(list): UnclaimRequest's deviceIdList (list of string, objects).
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

        _params = {
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }

        _payload = {
            'deviceIdList':
                deviceIdList,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_0b836b7b4b6a9fd5_v1_3_1')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/onboarding/pnp-device/unclaim')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_0b836b7b4b6a9fd5_v1_3_1', json_data)

    def update_device(self,
                      id,
                      _id=None,
                      deviceInfo=None,
                      runSummaryList=None,
                      systemResetWorkflow=None,
                      systemWorkflow=None,
                      tenantId=None,
                      version=None,
                      workflow=None,
                      workflowParameters=None,
                      headers=None,
                      payload=None,
                      active_validation=True,
                      **request_parameters):
        """Updates device details specified by device id in PnP database.

        Args:
            _id(string): Device's _id.
            deviceInfo(object): Device's deviceInfo.
            runSummaryList(list): Device's runSummaryList (list of objects).
            systemResetWorkflow(object): Device's systemResetWorkflow.
            systemWorkflow(object): Device's systemWorkflow.
            tenantId(string): Device's tenantId.
            version(number): Device's version.
            workflow(object): Device's workflow.
            workflowParameters(object): Device's workflowParameters.
            id(basestring): id path parameter.
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
        check_type(id, basestring,
                   may_be_none=False)
        if headers is not None:
            if 'Content-Type' in headers:
                check_type(headers.get('Content-Type'),
                           basestring, may_be_none=False)
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        _params = {
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'id': id,
        }

        _payload = {
            '_id':
                _id,
            'deviceInfo':
                deviceInfo,
            'runSummaryList':
                runSummaryList,
            'systemResetWorkflow':
                systemResetWorkflow,
            'systemWorkflow':
                systemWorkflow,
            'tenantId':
                tenantId,
            'version':
                version,
            'workflow':
                workflow,
            'workflowParameters':
                workflowParameters,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_09b0f9ce4239ae10_v1_3_1')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/onboarding/pnp-device/${id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload,
                                          headers=_headers)
        else:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload)

        return self._object_factory('bpm_09b0f9ce4239ae10_v1_3_1', json_data)

    def add_virtual_account(self,
                            autoSyncPeriod=None,
                            ccoUser=None,
                            expiry=None,
                            lastSync=None,
                            profile=None,
                            smartAccountId=None,
                            syncResult=None,
                            syncResultStr=None,
                            syncStartTime=None,
                            syncStatus=None,
                            tenantId=None,
                            token=None,
                            virtualAccountId=None,
                            headers=None,
                            payload=None,
                            active_validation=True,
                            **request_parameters):
        """Registers a Smart Account, Virtual Account and the relevant
        server profile info with the PnP System & database. The
        devices present in the registered virtual account are
        synced with the PnP database as well. The response
        payload returns the new profile.

        Args:
            autoSyncPeriod(number): SAVAMapping's autoSyncPeriod.
            ccoUser(string): SAVAMapping's ccoUser.
            expiry(number): SAVAMapping's expiry.
            lastSync(number): SAVAMapping's lastSync.
            profile(object): SAVAMapping's profile.
            smartAccountId(string): SAVAMapping's smartAccountId.
            syncResult(object): SAVAMapping's syncResult.
            syncResultStr(string): SAVAMapping's syncResultStr.
            syncStartTime(number): SAVAMapping's syncStartTime.
            syncStatus(string): SAVAMapping's syncStatus. Available values are 'NOT_SYNCED', 'SYNCING', 'SUCCESS'
                and 'FAILURE'.
            tenantId(string): SAVAMapping's tenantId.
            token(string): SAVAMapping's token.
            virtualAccountId(string): SAVAMapping's virtualAccountId.
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

        _params = {
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }

        _payload = {
            'autoSyncPeriod':
                autoSyncPeriod,
            'ccoUser':
                ccoUser,
            'expiry':
                expiry,
            'lastSync':
                lastSync,
            'profile':
                profile,
            'smartAccountId':
                smartAccountId,
            'syncResult':
                syncResult,
            'syncResultStr':
                syncResultStr,
            'syncStartTime':
                syncStartTime,
            'syncStatus':
                syncStatus,
            'tenantId':
                tenantId,
            'token':
                token,
            'virtualAccountId':
                virtualAccountId,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_1e962af345b8b59f_v1_3_1')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/onboarding/pnp-settings/savacct')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_1e962af345b8b59f_v1_3_1', json_data)

    def deregister_virtual_account(self,
                                   domain,
                                   name,
                                   headers=None,
                                   **request_parameters):
        """Deregisters the specified smart account & virtual account info
        and the associated device information from the PnP
        System & database. The devices associated with the
        deregistered virtual account are removed from the PnP
        database as well. The response payload contains the
        deregistered smart & virtual account information.

        Args:
            domain(basestring): Smart Account Domain.
            name(basestring): Virtual Account Name.
            headers(dict): Dictionary of HTTP Headers to send with the Request
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
        check_type(domain, basestring,
                   may_be_none=False)
        check_type(name, basestring,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        _params = {
            'domain':
                domain,
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

        e_url = ('/dna/intent/api/v1/onboarding/pnp-settings/vacct')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(endpoint_full_url, params=_params,
                                             headers=_headers)
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_2499e9ad42e8ae5b_v1_3_1', json_data)

    def get_smart_account_list(self,
                               headers=None,
                               **request_parameters):
        """Returns the list of Smart Account domains.

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
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

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

        e_url = ('/dna/intent/api/v1/onboarding/pnp-settings/sacct')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_3cb24acb486b89d2_v1_3_1', json_data)

    def claim_a_device_to_a_site(self,
                                 deviceId=None,
                                 siteId=None,
                                 type=None,
                                 headers=None,
                                 payload=None,
                                 active_validation=True,
                                 **request_parameters):
        """Claim a device based on DNA-C Site based design process.
        Different parameters are required for different device
        platforms.

        Args:
            deviceId(string): SiteProvisionRequest's deviceId.
            siteId(string): SiteProvisionRequest's siteId.
            type(string): SiteProvisionRequest's type. Available values are 'Default', 'AccessPoint', 'StackSwitch',
                'Sensor' and 'MobilityExpress'.
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

        _params = {
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }

        _payload = {
            'deviceId':
                deviceId,
            'siteId':
                siteId,
            'type':
                type,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_5889fb844939a13b_v1_3_1')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/onboarding/pnp-device/site-claim')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_5889fb844939a13b_v1_3_1', json_data)

    def update_pnp_server_profile(self,
                                  autoSyncPeriod=None,
                                  ccoUser=None,
                                  expiry=None,
                                  lastSync=None,
                                  profile=None,
                                  smartAccountId=None,
                                  syncResult=None,
                                  syncResultStr=None,
                                  syncStartTime=None,
                                  syncStatus=None,
                                  tenantId=None,
                                  token=None,
                                  virtualAccountId=None,
                                  headers=None,
                                  payload=None,
                                  active_validation=True,
                                  **request_parameters):
        """Updates the PnP Server profile in a registered Virtual Account
        in the PnP database. The response payload returns the
        updated smart & virtual account info.

        Args:
            autoSyncPeriod(number): SAVAMapping's autoSyncPeriod.
            ccoUser(string): SAVAMapping's ccoUser.
            expiry(number): SAVAMapping's expiry.
            lastSync(number): SAVAMapping's lastSync.
            profile(object): SAVAMapping's profile.
            smartAccountId(string): SAVAMapping's smartAccountId.
            syncResult(object): SAVAMapping's syncResult.
            syncResultStr(string): SAVAMapping's syncResultStr.
            syncStartTime(number): SAVAMapping's syncStartTime.
            syncStatus(string): SAVAMapping's syncStatus. Available values are 'NOT_SYNCED', 'SYNCING', 'SUCCESS'
                and 'FAILURE'.
            tenantId(string): SAVAMapping's tenantId.
            token(string): SAVAMapping's token.
            virtualAccountId(string): SAVAMapping's virtualAccountId.
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

        _params = {
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }

        _payload = {
            'autoSyncPeriod':
                autoSyncPeriod,
            'ccoUser':
                ccoUser,
            'expiry':
                expiry,
            'lastSync':
                lastSync,
            'profile':
                profile,
            'smartAccountId':
                smartAccountId,
            'syncResult':
                syncResult,
            'syncResultStr':
                syncResultStr,
            'syncStartTime':
                syncStartTime,
            'syncStatus':
                syncStatus,
            'tenantId':
                tenantId,
            'token':
                token,
            'virtualAccountId':
                virtualAccountId,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_6f9819e84178870c_v1_3_1')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/onboarding/pnp-settings/savacct')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload,
                                          headers=_headers)
        else:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload)

        return self._object_factory('bpm_6f9819e84178870c_v1_3_1', json_data)

    def get_workflow_count(self,
                           name=None,
                           headers=None,
                           **request_parameters):
        """Returns the workflow count.

        Args:
            name(basestring, list, set, tuple): Workflow Name.
            headers(dict): Dictionary of HTTP Headers to send with the Request
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
        check_type(name, (basestring, list, set, tuple))
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        _params = {
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

        e_url = ('/dna/intent/api/v1/onboarding/pnp-workflow/count')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_7989f86846faaf99_v1_3_1', json_data)

    def get_workflow_by_id(self,
                           id,
                           headers=None,
                           **request_parameters):
        """Returns a workflow specified by id.

        Args:
            id(basestring): id path parameter.
            headers(dict): Dictionary of HTTP Headers to send with the Request
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

        e_url = ('/dna/intent/api/v1/onboarding/pnp-workflow/${id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_80acb88e4ac9ac6d_v1_3_1', json_data)

    def get_virtual_account_list(self,
                                 domain,
                                 headers=None,
                                 **request_parameters):
        """Returns list of virtual accounts associated with the specified
        smart account.

        Args:
            domain(basestring): Smart Account Domain.
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
        check_type(domain, basestring,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        _params = {
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'domain': domain,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/onboarding/pnp-'
                 + 'settings/sacct/${domain}/vacct')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_70a479a6462a9496_v1_3_1', json_data)

    def add_a_workflow(self,
                       _id=None,
                       addToInventory=None,
                       addedOn=None,
                       configId=None,
                       currTaskIdx=None,
                       description=None,
                       endTime=None,
                       execTime=None,
                       imageId=None,
                       instanceType=None,
                       lastupdateOn=None,
                       name=None,
                       startTime=None,
                       state=None,
                       tasks=None,
                       tenantId=None,
                       type=None,
                       useState=None,
                       version=None,
                       headers=None,
                       payload=None,
                       active_validation=True,
                       **request_parameters):
        """Adds a PnP Workflow along with the relevant tasks in the
        workflow into the PnP database.

        Args:
            _id(string): Workflow's _id.
            addToInventory(boolean): Workflow's addToInventory.
            addedOn(number): Workflow's addedOn.
            configId(string): Workflow's configId.
            currTaskIdx(number): Workflow's currTaskIdx.
            description(string): Workflow's description.
            endTime(number): Workflow's endTime.
            execTime(number): Workflow's execTime.
            imageId(string): Workflow's imageId.
            instanceType(string): Workflow's instanceType. Available values are 'SystemWorkflow', 'UserWorkflow' and
                'SystemResetWorkflow'.
            lastupdateOn(number): Workflow's lastupdateOn.
            name(string): Workflow's name.
            startTime(number): Workflow's startTime.
            state(string): Workflow's state.
            tasks(list): Workflow's tasks (list of objects).
            tenantId(string): Workflow's tenantId.
            type(string): Workflow's type.
            useState(string): Workflow's useState.
            version(number): Workflow's version.
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

        _params = {
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }

        _payload = {
            '_id':
                _id,
            'addToInventory':
                addToInventory,
            'addedOn':
                addedOn,
            'configId':
                configId,
            'currTaskIdx':
                currTaskIdx,
            'description':
                description,
            'endTime':
                endTime,
            'execTime':
                execTime,
            'imageId':
                imageId,
            'instanceType':
                instanceType,
            'lastupdateOn':
                lastupdateOn,
            'name':
                name,
            'startTime':
                startTime,
            'state':
                state,
            'tasks':
                tasks,
            'tenantId':
                tenantId,
            'type':
                type,
            'useState':
                useState,
            'version':
                version,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_848b5a7b4f9b8c12_v1_3_1')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/onboarding/pnp-workflow')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_848b5a7b4f9b8c12_v1_3_1', json_data)

    def sync_virtual_account_devices(self,
                                     autoSyncPeriod=None,
                                     ccoUser=None,
                                     expiry=None,
                                     lastSync=None,
                                     profile=None,
                                     smartAccountId=None,
                                     syncResult=None,
                                     syncResultStr=None,
                                     syncStartTime=None,
                                     syncStatus=None,
                                     tenantId=None,
                                     token=None,
                                     virtualAccountId=None,
                                     headers=None,
                                     payload=None,
                                     active_validation=True,
                                     **request_parameters):
        """Synchronizes the device info from the given smart account &
        virtual account with the PnP database. The response
        payload returns a list of synced devices.

        Args:
            autoSyncPeriod(number): SAVAMapping's autoSyncPeriod.
            ccoUser(string): SAVAMapping's ccoUser.
            expiry(number): SAVAMapping's expiry.
            lastSync(number): SAVAMapping's lastSync.
            profile(object): SAVAMapping's profile.
            smartAccountId(string): SAVAMapping's smartAccountId.
            syncResult(object): SAVAMapping's syncResult.
            syncResultStr(string): SAVAMapping's syncResultStr.
            syncStartTime(number): SAVAMapping's syncStartTime.
            syncStatus(string): SAVAMapping's syncStatus. Available values are 'NOT_SYNCED', 'SYNCING', 'SUCCESS'
                and 'FAILURE'.
            tenantId(string): SAVAMapping's tenantId.
            token(string): SAVAMapping's token.
            virtualAccountId(string): SAVAMapping's virtualAccountId.
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

        _params = {
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }

        _payload = {
            'autoSyncPeriod':
                autoSyncPeriod,
            'ccoUser':
                ccoUser,
            'expiry':
                expiry,
            'lastSync':
                lastSync,
            'profile':
                profile,
            'smartAccountId':
                smartAccountId,
            'syncResult':
                syncResult,
            'syncResultStr':
                syncResultStr,
            'syncStartTime':
                syncStartTime,
            'syncStatus':
                syncStatus,
            'tenantId':
                tenantId,
            'token':
                token,
            'virtualAccountId':
                virtualAccountId,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_a4b6c87a4ffb9efa_v1_3_1')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/onboarding/pnp-device/vacct-sync')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_a4b6c87a4ffb9efa_v1_3_1', json_data)

    def reset_device(self,
                     deviceResetList=None,
                     projectId=None,
                     workflowId=None,
                     headers=None,
                     payload=None,
                     active_validation=True,
                     **request_parameters):
        """Recovers a device from a Workflow Execution Error state.

        Args:
            deviceResetList(list): ResetRequest's deviceResetList (list of objects).
            projectId(string): ResetRequest's projectId.
            workflowId(string): ResetRequest's workflowId.
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

        _params = {
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }

        _payload = {
            'deviceResetList':
                deviceResetList,
            'projectId':
                projectId,
            'workflowId':
                workflowId,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_9e857b5a4a0bbcdb_v1_3_1')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/onboarding/pnp-device/reset')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_9e857b5a4a0bbcdb_v1_3_1', json_data)

    def get_workflows(self,
                      limit=None,
                      name=None,
                      offset=None,
                      sort=None,
                      sort_order=None,
                      type=None,
                      headers=None,
                      **request_parameters):
        """Returns the list of workflows based on filter criteria. If a
        limit is not specified, it will default to return 50
        workflows. Pagination and sorting are also supported by
        this endpoint.

        Args:
            limit(int): Limits number of results.
            offset(int): Index of first result.
            sort(basestring, list, set, tuple): Comma seperated lost of fields to sort on.
            sort_order(basestring): Sort Order Ascending (asc) or Descending (des).
            type(basestring, list, set, tuple): Workflow Type.
            name(basestring, list, set, tuple): Workflow Name.
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
        check_type(limit, int)
        check_type(offset, int)
        check_type(sort, (basestring, list, set, tuple))
        check_type(sort_order, basestring)
        check_type(type, (basestring, list, set, tuple))
        check_type(name, (basestring, list, set, tuple))
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        _params = {
            'limit':
                limit,
            'offset':
                offset,
            'sort':
                sort,
            'sortOrder':
                sort_order,
            'type':
                type,
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

        e_url = ('/dna/intent/api/v1/onboarding/pnp-workflow')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_aeb4dad04a99bbe3_v1_3_1', json_data)

    def get_device_by_id(self,
                         id,
                         headers=None,
                         **request_parameters):
        """Returns device details specified by device id.

        Args:
            id(basestring): id path parameter.
            headers(dict): Dictionary of HTTP Headers to send with the Request
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

        e_url = ('/dna/intent/api/v1/onboarding/pnp-device/${id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_bab6c9e5440885cc_v1_3_1', json_data)

    def get_device_count(self,
                         cm_state=None,
                         last_contact=None,
                         name=None,
                         onb_state=None,
                         pid=None,
                         project_id=None,
                         project_name=None,
                         serial_number=None,
                         smart_account_id=None,
                         source=None,
                         state=None,
                         virtual_account_id=None,
                         workflow_id=None,
                         workflow_name=None,
                         headers=None,
                         **request_parameters):
        """Returns the device count based on filter criteria. This is
        useful for pagination.

        Args:
            serial_number(basestring, list, set, tuple): Device Serial Number.
            state(basestring, list, set, tuple): Device State.
            onb_state(basestring, list, set, tuple): Device Onboarding State.
            cm_state(basestring, list, set, tuple): Device Connection Manager State.
            name(basestring, list, set, tuple): Device Name.
            pid(basestring, list, set, tuple): Device ProductId.
            source(basestring, list, set, tuple): Device Source.
            project_id(basestring, list, set, tuple): Device Project Id.
            workflow_id(basestring, list, set, tuple): Device Workflow Id.
            project_name(basestring, list, set, tuple): Device Project Name.
            workflow_name(basestring, list, set, tuple): Device Workflow Name.
            smart_account_id(basestring, list, set, tuple): Device Smart Account.
            virtual_account_id(basestring, list, set, tuple): Device Virtual Account.
            last_contact(bool): Device Has Contacted lastContact > 0.
            headers(dict): Dictionary of HTTP Headers to send with the Request
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
        check_type(serial_number, (basestring, list, set, tuple))
        check_type(state, (basestring, list, set, tuple))
        check_type(onb_state, (basestring, list, set, tuple))
        check_type(cm_state, (basestring, list, set, tuple))
        check_type(name, (basestring, list, set, tuple))
        check_type(pid, (basestring, list, set, tuple))
        check_type(source, (basestring, list, set, tuple))
        check_type(project_id, (basestring, list, set, tuple))
        check_type(workflow_id, (basestring, list, set, tuple))
        check_type(project_name, (basestring, list, set, tuple))
        check_type(workflow_name, (basestring, list, set, tuple))
        check_type(smart_account_id, (basestring, list, set, tuple))
        check_type(virtual_account_id, (basestring, list, set, tuple))
        check_type(last_contact, bool)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        _params = {
            'serialNumber':
                serial_number,
            'state':
                state,
            'onbState':
                onb_state,
            'cmState':
                cm_state,
            'name':
                name,
            'pid':
                pid,
            'source':
                source,
            'projectId':
                project_id,
            'workflowId':
                workflow_id,
            'projectName':
                project_name,
            'workflowName':
                workflow_name,
            'smartAccountId':
                smart_account_id,
            'virtualAccountId':
                virtual_account_id,
            'lastContact':
                last_contact,
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

        e_url = ('/dna/intent/api/v1/onboarding/pnp-device/count')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_d9a1fa9c4068b23c_v1_3_1', json_data)

    def get_device_history(self,
                           serial_number,
                           sort=None,
                           sort_order=None,
                           headers=None,
                           **request_parameters):
        """Returns history for a specific device. Serial number is a
        required parameter.

        Args:
            serial_number(basestring): Device Serial Number.
            sort(basestring, list, set, tuple): Comma seperated list of fields to sort on.
            sort_order(basestring): Sort Order Ascending (asc) or Descending (des).
            headers(dict): Dictionary of HTTP Headers to send with the Request
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
        check_type(sort, (basestring, list, set, tuple))
        check_type(sort_order, basestring)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        _params = {
            'serialNumber':
                serial_number,
            'sort':
                sort,
            'sortOrder':
                sort_order,
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

        e_url = ('/dna/intent/api/v1/onboarding/pnp-device/history')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_f09319674049a7d4_v1_3_1', json_data)

    def delete_device_by_id_from_pnp(self,
                                     id,
                                     headers=None,
                                     **request_parameters):
        """Deletes specified device from PnP database.

        Args:
            id(basestring): id path parameter.
            headers(dict): Dictionary of HTTP Headers to send with the Request
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

        e_url = ('/dna/intent/api/v1/onboarding/pnp-device/${id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(endpoint_full_url, params=_params,
                                             headers=_headers)
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_cdab9b474899ae06_v1_3_1', json_data)

    def import_devices_in_bulk(self,
                               headers=None,
                               payload=None,
                               active_validation=True,
                               **request_parameters):
        """Add devices to PnP in bulk.

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
        """
        check_type(headers, dict)
        check_type(payload, list)
        if headers is not None:
            if 'Content-Type' in headers:
                check_type(headers.get('Content-Type'),
                           basestring, may_be_none=False)
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        _params = {
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }

        _payload = payload or []
        if active_validation:
            self._request_validator('jsd_21a6db2540298f55_v1_3_1')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/onboarding/pnp-device/import')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_21a6db2540298f55_v1_3_1', json_data)

    def update_workflow(self,
                        id,
                        _id=None,
                        addToInventory=None,
                        addedOn=None,
                        configId=None,
                        currTaskIdx=None,
                        description=None,
                        endTime=None,
                        execTime=None,
                        imageId=None,
                        instanceType=None,
                        lastupdateOn=None,
                        name=None,
                        startTime=None,
                        state=None,
                        tasks=None,
                        tenantId=None,
                        type=None,
                        useState=None,
                        version=None,
                        headers=None,
                        payload=None,
                        active_validation=True,
                        **request_parameters):
        """Updates an existing workflow.

        Args:
            _id(string): Workflow's _id.
            addToInventory(boolean): Workflow's addToInventory.
            addedOn(number): Workflow's addedOn.
            configId(string): Workflow's configId.
            currTaskIdx(number): Workflow's currTaskIdx.
            description(string): Workflow's description.
            endTime(number): Workflow's endTime.
            execTime(number): Workflow's execTime.
            imageId(string): Workflow's imageId.
            instanceType(string): Workflow's instanceType. Available values are 'SystemWorkflow', 'UserWorkflow' and
                'SystemResetWorkflow'.
            lastupdateOn(number): Workflow's lastupdateOn.
            name(string): Workflow's name.
            startTime(number): Workflow's startTime.
            state(string): Workflow's state.
            tasks(list): Workflow's tasks (list of objects).
            tenantId(string): Workflow's tenantId.
            type(string): Workflow's type.
            useState(string): Workflow's useState.
            version(number): Workflow's version.
            id(basestring): id path parameter.
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
        check_type(id, basestring,
                   may_be_none=False)
        if headers is not None:
            if 'Content-Type' in headers:
                check_type(headers.get('Content-Type'),
                           basestring, may_be_none=False)
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        _params = {
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'id': id,
        }

        _payload = {
            '_id':
                _id,
            'addToInventory':
                addToInventory,
            'addedOn':
                addedOn,
            'configId':
                configId,
            'currTaskIdx':
                currTaskIdx,
            'description':
                description,
            'endTime':
                endTime,
            'execTime':
                execTime,
            'imageId':
                imageId,
            'instanceType':
                instanceType,
            'lastupdateOn':
                lastupdateOn,
            'name':
                name,
            'startTime':
                startTime,
            'state':
                state,
            'tasks':
                tasks,
            'tenantId':
                tenantId,
            'type':
                type,
            'useState':
                useState,
            'version':
                version,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_3086c9624f498b85_v1_3_1')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/onboarding/pnp-workflow/${id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload,
                                          headers=_headers)
        else:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload)

        return self._object_factory('bpm_3086c9624f498b85_v1_3_1', json_data)

    def get_pnp_global_settings(self,
                                headers=None,
                                **request_parameters):
        """Returns global PnP settings of the user.

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

        e_url = ('/dna/intent/api/v1/onboarding/pnp-settings')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_7e92f9eb46db8320_v1_3_1', json_data)

    def update_pnp_global_settings(self,
                                   _id=None,
                                   aaaCredentials=None,
                                   acceptEula=None,
                                   defaultProfile=None,
                                   savaMappingList=None,
                                   taskTimeOuts=None,
                                   tenantId=None,
                                   version=None,
                                   headers=None,
                                   payload=None,
                                   active_validation=True,
                                   **request_parameters):
        """Updates the user's list of global PnP settings.

        Args:
            _id(string): Settings's _id.
            aaaCredentials(object): Settings's aaaCredentials.
            acceptEula(boolean): Settings's acceptEula.
            defaultProfile(object): Settings's defaultProfile.
            savaMappingList(list): Settings's savaMappingList (list of objects).
            taskTimeOuts(object): Settings's taskTimeOuts.
            tenantId(string): Settings's tenantId.
            version(number): Settings's version.
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

        _params = {
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }

        _payload = {
            '_id':
                _id,
            'aaaCredentials':
                aaaCredentials,
            'acceptEula':
                acceptEula,
            'defaultProfile':
                defaultProfile,
            'savaMappingList':
                savaMappingList,
            'taskTimeOuts':
                taskTimeOuts,
            'tenantId':
                tenantId,
            'version':
                version,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_8da0391947088a5a_v1_3_1')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/onboarding/pnp-settings')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload,
                                          headers=_headers)
        else:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload)

        return self._object_factory('bpm_8da0391947088a5a_v1_3_1', json_data)

    def delete_workflow_by_id(self,
                              id,
                              headers=None,
                              **request_parameters):
        """Deletes a workflow specified by id.

        Args:
            id(basestring): id path parameter.
            headers(dict): Dictionary of HTTP Headers to send with the Request
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

        e_url = ('/dna/intent/api/v1/onboarding/pnp-workflow/${id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(endpoint_full_url, params=_params,
                                             headers=_headers)
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_af8d7b0e470b8ae2_v1_3_1', json_data)

    def add_device(self,
                   _id=None,
                   deviceInfo=None,
                   runSummaryList=None,
                   systemResetWorkflow=None,
                   systemWorkflow=None,
                   tenantId=None,
                   version=None,
                   workflow=None,
                   workflowParameters=None,
                   headers=None,
                   payload=None,
                   active_validation=True,
                   **request_parameters):
        """Adds a device to the PnP database.

        Args:
            _id(string): Device's _id.
            deviceInfo(object): Device's deviceInfo.
            runSummaryList(list): Device's runSummaryList (list of objects).
            systemResetWorkflow(object): Device's systemResetWorkflow.
            systemWorkflow(object): Device's systemWorkflow.
            tenantId(string): Device's tenantId.
            version(number): Device's version.
            workflow(object): Device's workflow.
            workflowParameters(object): Device's workflowParameters.
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

        _params = {
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }

        _payload = {
            '_id':
                _id,
            'deviceInfo':
                deviceInfo,
            'runSummaryList':
                runSummaryList,
            'systemResetWorkflow':
                systemResetWorkflow,
            'systemWorkflow':
                systemWorkflow,
            'tenantId':
                tenantId,
            'version':
                version,
            'workflow':
                workflow,
            'workflowParameters':
                workflowParameters,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_f3b26b5544cabab9_v1_3_1')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/onboarding/pnp-device')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_f3b26b5544cabab9_v1_3_1', json_data)

    def preview_config(self,
                       deviceId=None,
                       siteId=None,
                       type=None,
                       headers=None,
                       payload=None,
                       active_validation=True,
                       **request_parameters):
        """Triggers a preview for site-based Day 0 Configuration.

        Args:
            deviceId(string): SiteProvisionRequest's deviceId.
            siteId(string): SiteProvisionRequest's siteId.
            type(string): SiteProvisionRequest's type. Available values are 'Default', 'AccessPoint', 'StackSwitch',
                'Sensor' and 'MobilityExpress'.
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

        _params = {
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }

        _payload = {
            'deviceId':
                deviceId,
            'siteId':
                siteId,
            'type':
                type,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_cf9418234d9ab37e_v1_3_1')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/onboarding/pnp-device/site-config-'
                 + 'preview')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_cf9418234d9ab37e_v1_3_1', json_data)

    def claim_device(self,
                     configFileUrl=None,
                     configId=None,
                     deviceClaimList=None,
                     fileServiceId=None,
                     imageId=None,
                     imageUrl=None,
                     populateInventory=None,
                     projectId=None,
                     workflowId=None,
                     headers=None,
                     payload=None,
                     active_validation=True,
                     **request_parameters):
        """Claims one of more devices with specified workflow.

        Args:
            configFileUrl(string): ClaimDeviceRequest's configFileUrl.
            configId(string): ClaimDeviceRequest's configId.
            deviceClaimList(list): ClaimDeviceRequest's deviceClaimList (list of objects).
            fileServiceId(string): ClaimDeviceRequest's fileServiceId.
            imageId(string): ClaimDeviceRequest's imageId.
            imageUrl(string): ClaimDeviceRequest's imageUrl.
            populateInventory(boolean): ClaimDeviceRequest's populateInventory.
            projectId(string): ClaimDeviceRequest's projectId.
            workflowId(string): ClaimDeviceRequest's workflowId.
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

        _params = {
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }

        _payload = {
            'configFileUrl':
                configFileUrl,
            'configId':
                configId,
            'deviceClaimList':
                deviceClaimList,
            'fileServiceId':
                fileServiceId,
            'imageId':
                imageId,
            'imageUrl':
                imageUrl,
            'populateInventory':
                populateInventory,
            'projectId':
                projectId,
            'workflowId':
                workflowId,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_d8a619974a8a8c48_v1_3_1')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/onboarding/pnp-device/claim')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_d8a619974a8a8c48_v1_3_1', json_data)

    def get_device_list(self,
                        cm_state=None,
                        last_contact=None,
                        limit=None,
                        name=None,
                        offset=None,
                        onb_state=None,
                        pid=None,
                        project_id=None,
                        project_name=None,
                        serial_number=None,
                        smart_account_id=None,
                        sort=None,
                        sort_order=None,
                        source=None,
                        state=None,
                        virtual_account_id=None,
                        workflow_id=None,
                        workflow_name=None,
                        headers=None,
                        **request_parameters):
        """Returns list of devices based on filter crieteria. If a limit is
        not specified, it will default to return 50 devices.
        Pagination and sorting are also supported by this
        endpoint.

        Args:
            limit(int): Limits number of results.
            offset(int): Index of first result.
            sort(basestring, list, set, tuple): Comma seperated list of fields to sort on.
            sort_order(basestring): Sort Order Ascending (asc) or Descending (des).
            serial_number(basestring, list, set, tuple): Device Serial Number.
            state(basestring, list, set, tuple): Device State.
            onb_state(basestring, list, set, tuple): Device Onboarding State.
            cm_state(basestring, list, set, tuple): Device Connection Manager State.
            name(basestring, list, set, tuple): Device Name.
            pid(basestring, list, set, tuple): Device ProductId.
            source(basestring, list, set, tuple): Device Source.
            project_id(basestring, list, set, tuple): Device Project Id.
            workflow_id(basestring, list, set, tuple): Device Workflow Id.
            project_name(basestring, list, set, tuple): Device Project Name.
            workflow_name(basestring, list, set, tuple): Device Workflow Name.
            smart_account_id(basestring, list, set, tuple): Device Smart Account.
            virtual_account_id(basestring, list, set, tuple): Device Virtual Account.
            last_contact(bool): Device Has Contacted lastContact > 0.
            headers(dict): Dictionary of HTTP Headers to send with the Request
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
        check_type(limit, int)
        check_type(offset, int)
        check_type(sort, (basestring, list, set, tuple))
        check_type(sort_order, basestring)
        check_type(serial_number, (basestring, list, set, tuple))
        check_type(state, (basestring, list, set, tuple))
        check_type(onb_state, (basestring, list, set, tuple))
        check_type(cm_state, (basestring, list, set, tuple))
        check_type(name, (basestring, list, set, tuple))
        check_type(pid, (basestring, list, set, tuple))
        check_type(source, (basestring, list, set, tuple))
        check_type(project_id, (basestring, list, set, tuple))
        check_type(workflow_id, (basestring, list, set, tuple))
        check_type(project_name, (basestring, list, set, tuple))
        check_type(workflow_name, (basestring, list, set, tuple))
        check_type(smart_account_id, (basestring, list, set, tuple))
        check_type(virtual_account_id, (basestring, list, set, tuple))
        check_type(last_contact, bool)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        _params = {
            'limit':
                limit,
            'offset':
                offset,
            'sort':
                sort,
            'sortOrder':
                sort_order,
            'serialNumber':
                serial_number,
            'state':
                state,
            'onbState':
                onb_state,
            'cmState':
                cm_state,
            'name':
                name,
            'pid':
                pid,
            'source':
                source,
            'projectId':
                project_id,
            'workflowId':
                workflow_id,
            'projectName':
                project_name,
            'workflowName':
                workflow_name,
            'smartAccountId':
                smart_account_id,
            'virtualAccountId':
                virtual_account_id,
            'lastContact':
                last_contact,
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

        e_url = ('/dna/intent/api/v1/onboarding/pnp-device')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_e6b3db8046c99654_v1_3_1', json_data)

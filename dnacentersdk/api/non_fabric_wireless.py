# -*- coding: utf-8 -*-
"""DNA Center Non-Fabric Wireless API wrapper.

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

class NonFabricWireless( object ):
    """DNA Center Non-Fabric Wireless API.

    Wraps the DNA Center Non-Fabric Wireless API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new NonFabricWireless object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the DNA Center service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(NonFabricWireless, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator


    # Provision
    def provision(self, headers=None,payload=None,**request_parameters):
        if headers is not None:
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = { }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or []

        self._request_validator('jsd_07913b7f4e1880de').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.post(apply_path_params('/dna/intent/api/v1/provision', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.post(apply_path_params('/dna/intent/api/v1/provision', path_params), params=params, json=payload)

        return self._object_factory('bpm_07913b7f4e1880de', json_data)


    # Update Wireless Profile
    def update_wireless_profile(self, rq_profileDetails = None, headers=None,payload=None,**request_parameters):
        if headers is not None:
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = { }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        if rq_profileDetails is not None: payload.update( { 'profileDetails':  rq_profileDetails })
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_20872aec43b9bf50').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.put(apply_path_params('/dna/intent/api/v1/wireless-profile', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.put(apply_path_params('/dna/intent/api/v1/wireless-profile', path_params), params=params, json=payload)

        return self._object_factory('bpm_20872aec43b9bf50', json_data)


    # Get Wireless Profile
    def get_wireless_profile(self, param_profile_name = None, headers=None,payload=None,**request_parameters):
        check_type( param_profile_name, basestring)
        if headers is not None:
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = { }
        if param_profile_name is not None: params.update( { 'profileName': param_profile_name })
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_6896993e41b8bd7a').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.get(apply_path_params('/dna/intent/api/v1/wireless-profile', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.get(apply_path_params('/dna/intent/api/v1/wireless-profile', path_params), params=params, json=payload)

        return self._object_factory('bpm_6896993e41b8bd7a', json_data)


    # Provision
    def provision(self, headers=None,payload=None,**request_parameters):
        if headers is not None:
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = { }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or []

        self._request_validator('jsd_a0be3a2f47ab9f3c').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.put(apply_path_params('/dna/intent/api/v1/reprovision', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.put(apply_path_params('/dna/intent/api/v1/reprovision', path_params), params=params, json=payload)

        return self._object_factory('bpm_a0be3a2f47ab9f3c', json_data)


    # Delete Wireless Profile
    def delete_wireless_profile(self, path_param_wireless_profile_name, headers=None,payload=None,**request_parameters):
        check_type( path_param_wireless_profile_name, basestring, may_be_none=False)
        if headers is not None:
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = { }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
            'wirelessProfileName': path_param_wireless_profile_name,
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_ae86a8c14b5980b7').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.delete(apply_path_params('/dna/intent/api/v1/wireless-profile/${wirelessProfileName}', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.delete(apply_path_params('/dna/intent/api/v1/wireless-profile/${wirelessProfileName}', path_params), params=params, json=payload)

        return self._object_factory('bpm_ae86a8c14b5980b7', json_data)


    # Create Wireless Profile
    def create_wireless_profile(self, rq_profileDetails = None, headers=None,payload=None,**request_parameters):
        if headers is not None:
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = { }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        if rq_profileDetails is not None: payload.update( { 'profileDetails':  rq_profileDetails })
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_47ba59204e0ab742').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.post(apply_path_params('/dna/intent/api/v1/wireless-profile', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.post(apply_path_params('/dna/intent/api/v1/wireless-profile', path_params), params=params, json=payload)

        return self._object_factory('bpm_47ba59204e0ab742', json_data)


    # Create and Provision SSID
    def create_and_provision_ssid(self, rq_enableFabric = None, rq_flexConnect = None, rq_managedAPLocations = None, rq_ssidDetails = None, rq_ssidType = None, headers=None,payload=None,**request_parameters):
        if headers is not None:
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = { }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        if rq_managedAPLocations is not None: payload.update( { 'managedAPLocations':  rq_managedAPLocations })
        if rq_ssidDetails is not None: payload.update( { 'ssidDetails':  rq_ssidDetails })
        if rq_ssidType is not None: payload.update( { 'ssidType':  rq_ssidType })
        if rq_enableFabric is not None: payload.update( { 'enableFabric':  rq_enableFabric })
        if rq_flexConnect is not None: payload.update( { 'flexConnect':  rq_flexConnect })
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_db9f997f4e59aec1').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.post(apply_path_params('/dna/intent/api/v1/provision-ssid', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.post(apply_path_params('/dna/intent/api/v1/provision-ssid', path_params), params=params, json=payload)

        return self._object_factory('bpm_db9f997f4e59aec1', json_data)


    # Delete Enterprise SSID
    def delete_enterprise_ssid(self, path_param_ssid_name, headers=None,payload=None,**request_parameters):
        check_type( path_param_ssid_name, basestring, may_be_none=False)
        if headers is not None:
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = { }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
            'ssidName': path_param_ssid_name,
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_c7a6592b4b98a369').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.delete(apply_path_params('/dna/intent/api/v1/enterprise-ssid/${ssidName}', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.delete(apply_path_params('/dna/intent/api/v1/enterprise-ssid/${ssidName}', path_params), params=params, json=payload)

        return self._object_factory('bpm_c7a6592b4b98a369', json_data)


    # Delete and provision SSID
    def delete_and_provision_ssid(self, path_param_managed_aplocations, path_param_ssid_name, headers=None,payload=None,**request_parameters):
        check_type( path_param_ssid_name, basestring, may_be_none=False)
        check_type( path_param_managed_aplocations, basestring, may_be_none=False)
        if headers is not None:
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = { }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
            'ssidName': path_param_ssid_name,
            'managedAPLocations': path_param_managed_aplocations,
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_cca098344a489dfa').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.delete(apply_path_params('/dna/intent/api/v1/provision-ssid/${ssidName}/${managedAPLocations}', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.delete(apply_path_params('/dna/intent/api/v1/provision-ssid/${ssidName}/${managedAPLocations}', path_params), params=params, json=payload)

        return self._object_factory('bpm_cca098344a489dfa', json_data)


    # Get Enterprise SSID
    def get_enterprise_ssid(self, param_ssid_name = None, headers=None,payload=None,**request_parameters):
        check_type( param_ssid_name, basestring)
        if headers is not None:
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = { }
        if param_ssid_name is not None: params.update( { 'ssidName': param_ssid_name })
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_cca519ba45ebb423').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.get(apply_path_params('/dna/intent/api/v1/enterprise-ssid', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.get(apply_path_params('/dna/intent/api/v1/enterprise-ssid', path_params), params=params, json=payload)

        return self._object_factory('bpm_cca519ba45ebb423', json_data)


    # Create Enterprise SSID
    def create_enterprise_ssid(self, rq_enableBroadcastSSID = None, rq_enableFastLane = None, rq_enableMACFiltering = None, rq_fastTransition = None, rq_name = None, rq_passphrase = None, rq_radioPolicy = None, rq_securityLevel = None, rq_trafficType = None, headers=None,payload=None,**request_parameters):
        if headers is not None:
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = { }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        if rq_name is not None: payload.update( { 'name':  rq_name })
        if rq_securityLevel is not None: payload.update( { 'securityLevel':  rq_securityLevel })
        if rq_passphrase is not None: payload.update( { 'passphrase':  rq_passphrase })
        if rq_enableFastLane is not None: payload.update( { 'enableFastLane':  rq_enableFastLane })
        if rq_enableMACFiltering is not None: payload.update( { 'enableMACFiltering':  rq_enableMACFiltering })
        if rq_trafficType is not None: payload.update( { 'trafficType':  rq_trafficType })
        if rq_radioPolicy is not None: payload.update( { 'radioPolicy':  rq_radioPolicy })
        if rq_enableBroadcastSSID is not None: payload.update( { 'enableBroadcastSSID':  rq_enableBroadcastSSID })
        if rq_fastTransition is not None: payload.update( { 'fastTransition':  rq_fastTransition })
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_8a96fb954d09a349').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.post(apply_path_params('/dna/intent/api/v1/enterprise-ssid', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.post(apply_path_params('/dna/intent/api/v1/enterprise-ssid', path_params), params=params, json=payload)

        return self._object_factory('bpm_8a96fb954d09a349', json_data)



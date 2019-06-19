# -*- coding: utf-8 -*-
"""DNA Center Fabric Wired API wrapper.

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

class FabricWired( object ):
    """DNA Center Fabric Wired API.

    Wraps the DNA Center Fabric Wired API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new FabricWired object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the DNA Center service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(FabricWired, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator


    # Gets border device details from SDA Fabric
    def gets_border_device_details_from_sda_fabric(self, path_param_device_ip_address, path_param_sda_border_device, headers=None,payload=None,**request_parameters):
        check_type( path_param_sda_border_device, basestring, may_be_none=False)
        check_type( path_param_device_ip_address, basestring, may_be_none=False)
        if headers is not None:
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = { }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
            'sda/border-device': path_param_sda_border_device,
            'device-ip-address': path_param_device_ip_address,
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_98a39bf4485a9871').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.get(apply_path_params('/dna/intent/api/v1/business/sda/border-device/${device-ip-address}', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.get(apply_path_params('/dna/intent/api/v1/business/sda/border-device/${device-ip-address}', path_params), params=params, json=payload)

        return self._object_factory('bpm_98a39bf4485a9871', json_data)


    # Adds border device in SDA Fabric
    def adds_border_device_in_sda_fabric(self, path_param_sda_border_device, headers=None,payload=None,**request_parameters):
        check_type( path_param_sda_border_device, basestring, may_be_none=False)
        if headers is not None:
            check_type( headers.get('__runsync', self._session.headers.get('__runsync')), bool)
            check_type( headers.get('__runsynctimeout', self._session.headers.get('__runsynctimeout')), int)
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = { }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
            'sda/border-device': path_param_sda_border_device,
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or []

        self._request_validator('jsd_bead7b3443b996a7').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.post(apply_path_params('/dna/intent/api/v1/business/sda/border-device', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.post(apply_path_params('/dna/intent/api/v1/business/sda/border-device', path_params), params=params, json=payload)

        return self._object_factory('bpm_bead7b3443b996a7', json_data)


    # Deletes border device from SDA Fabric
    def deletes_border_device_from_sda_fabric(self, path_param_device_ip_address, path_param_sda_border_device, headers=None,payload=None,**request_parameters):
        check_type( path_param_sda_border_device, basestring, may_be_none=False)
        check_type( path_param_device_ip_address, basestring, may_be_none=False)
        if headers is not None:
            check_type( headers.get('__runsync', self._session.headers.get('__runsync')), bool)
            check_type( headers.get('__runsynctimeout', self._session.headers.get('__runsynctimeout')), int)
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = { }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
            'sda/border-device': path_param_sda_border_device,
            'device-ip-address': path_param_device_ip_address,
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_cb81b93540baaab0').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.delete(apply_path_params('/dna/intent/api/v1/business/sda/border-device/${device-ip-address}', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.delete(apply_path_params('/dna/intent/api/v1/business/sda/border-device/${device-ip-address}', path_params), params=params, json=payload)

        return self._object_factory('bpm_cb81b93540baaab0', json_data)



# -*- coding: utf-8 -*-
"""DNA Center SWIM API wrapper.

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

class Swim( object ):
    """DNA Center SWIM API.

    Wraps the DNA Center SWIM API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new Swim object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the DNA Center service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(Swim, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator


    # Get software image details
    def get_software_image_details(self, param_application_type = None, param_created_time = None, param_family = None, param_image_integrity_status = None, param_image_name = None, param_image_series = None, param_image_size_greater_than = None, param_image_size_lesser_than = None, param_image_uuid = None, param_is_cco_latest = None, param_is_cco_recommended = None, param_is_tagged_golden = None, param_limit = None, param_name = None, param_offset = None, param_sort_by = None, param_sort_order = 'asc', param_version = None, headers=None,payload=None,**request_parameters):
        check_type( param_image_uuid, basestring)
        check_type( param_name, basestring)
        check_type( param_family, basestring)
        check_type( param_application_type, basestring)
        check_type( param_image_integrity_status, basestring)
        check_type( param_version, basestring)
        check_type( param_image_series, basestring)
        check_type( param_image_name, basestring)
        check_type( param_is_tagged_golden, bool)
        check_type( param_is_cco_recommended, bool)
        check_type( param_is_cco_latest, bool)
        check_type( param_created_time, int)
        check_type( param_image_size_greater_than, int)
        check_type( param_image_size_lesser_than, int)
        check_type( param_sort_by, basestring)
        check_type( param_sort_order, basestring)
        check_type( param_limit, int)
        check_type( param_offset, int)
        if headers is not None:
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = { }
        if param_image_uuid is not None: params.update( { 'imageUuid': param_image_uuid })
        if param_name is not None: params.update( { 'name': param_name })
        if param_family is not None: params.update( { 'family': param_family })
        if param_application_type is not None: params.update( { 'applicationType': param_application_type })
        if param_image_integrity_status is not None: params.update( { 'imageIntegrityStatus': param_image_integrity_status })
        if param_version is not None: params.update( { 'version': param_version })
        if param_image_series is not None: params.update( { 'imageSeries': param_image_series })
        if param_image_name is not None: params.update( { 'imageName': param_image_name })
        if param_is_tagged_golden is not None: params.update( { 'isTaggedGolden': param_is_tagged_golden })
        if param_is_cco_recommended is not None: params.update( { 'isCCORecommended': param_is_cco_recommended })
        if param_is_cco_latest is not None: params.update( { 'isCCOLatest': param_is_cco_latest })
        if param_created_time is not None: params.update( { 'createdTime': param_created_time })
        if param_image_size_greater_than is not None: params.update( { 'imageSizeGreaterThan': param_image_size_greater_than })
        if param_image_size_lesser_than is not None: params.update( { 'imageSizeLesserThan': param_image_size_lesser_than })
        if param_sort_by is not None: params.update( { 'sortBy': param_sort_by })
        if param_sort_order is not None: params.update( { 'sortOrder': param_sort_order })
        if param_limit is not None: params.update( { 'limit': param_limit })
        if param_offset is not None: params.update( { 'offset': param_offset })
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_0c8f7a0b49b9aedd').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.get(apply_path_params('/api/v1/image/importation', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.get(apply_path_params('/api/v1/image/importation', path_params), params=params, json=payload)

        return self._object_factory('bpm_0c8f7a0b49b9aedd', json_data)


    # Trigger software image distribution
    def trigger_software_image_distribution(self, headers=None,payload=None,**request_parameters):
        if headers is not None:
            check_type( headers.get('Content-Type', self._session.headers.get('Content-Type')), basestring, may_be_none=False)
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = { }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or []

        self._request_validator('jsd_8cb6783b4faba1f4').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.post(apply_path_params('/api/v1/image/distribution', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.post(apply_path_params('/api/v1/image/distribution', path_params), params=params, json=payload)

        return self._object_factory('bpm_8cb6783b4faba1f4', json_data)


    # Import local software image
    def import_local_software_image(self, param_is_third_party = None, param_third_party_application_type = None, param_third_party_image_family = None, param_third_party_vendor = None, headers=None,payload=None,**request_parameters):
        check_type( param_is_third_party, bool)
        check_type( param_third_party_vendor, basestring)
        check_type( param_third_party_image_family, basestring)
        check_type( param_third_party_application_type, basestring)
        if headers is not None:
            check_type( headers.get('Content-Type', self._session.headers.get('Content-Type')), basestring, may_be_none=False)
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = { }
        if param_is_third_party is not None: params.update( { 'isThirdParty': param_is_third_party })
        if param_third_party_vendor is not None: params.update( { 'thirdPartyVendor': param_third_party_vendor })
        if param_third_party_image_family is not None: params.update( { 'thirdPartyImageFamily': param_third_party_image_family })
        if param_third_party_application_type is not None: params.update( { 'thirdPartyApplicationType': param_third_party_application_type })
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_4dbe3bc743a891bc').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.post(apply_path_params('/api/v1/image/importation/source/file', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.post(apply_path_params('/api/v1/image/importation/source/file', path_params), params=params, json=payload)

        return self._object_factory('bpm_4dbe3bc743a891bc', json_data)


    # Import software image via URL
    def import_software_image_via_url(self, param_schedule_at = None, param_schedule_desc = None, param_schedule_origin = None, headers=None,payload=None,**request_parameters):
        check_type( param_schedule_at, basestring)
        check_type( param_schedule_desc, basestring)
        check_type( param_schedule_origin, basestring)
        if headers is not None:
            check_type( headers.get('Content-Type', self._session.headers.get('Content-Type')), basestring, may_be_none=False)
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = { }
        if param_schedule_at is not None: params.update( { 'scheduleAt': param_schedule_at })
        if param_schedule_desc is not None: params.update( { 'scheduleDesc': param_schedule_desc })
        if param_schedule_origin is not None: params.update( { 'scheduleOrigin': param_schedule_origin })
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or []

        self._request_validator('jsd_bc8aab4746ca883d').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.post(apply_path_params('/api/v1/image/importation/source/url', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.post(apply_path_params('/api/v1/image/importation/source/url', path_params), params=params, json=payload)

        return self._object_factory('bpm_bc8aab4746ca883d', json_data)


    # Trigger software image activation
    def trigger_software_image_activation(self, param_schedule_validate = None, headers=None,payload=None,**request_parameters):
        check_type( param_schedule_validate, bool)
        if headers is not None:
            check_type( headers.get('Content-Type', self._session.headers.get('Content-Type')), basestring, may_be_none=False)
            check_type( headers.get('Client-Type', self._session.headers.get('Client-Type')), basestring)
            check_type( headers.get('Client-Url', self._session.headers.get('Client-Url')), basestring)
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = { }
        if param_schedule_validate is not None: params.update( { 'scheduleValidate': param_schedule_validate })
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or []

        self._request_validator('jsd_fb9beb664f2aba4c').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.post(apply_path_params('/api/v1/image/activation/device', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.post(apply_path_params('/api/v1/image/activation/device', path_params), params=params, json=payload)

        return self._object_factory('bpm_fb9beb664f2aba4c', json_data)



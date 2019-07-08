# -*- coding: utf-8 -*-
"""DNA Center Tag API wrapper.

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

class Tag( object ):
    """DNA Center Tag API.

    Wraps the DNA Center Tag API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new Tag object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the DNA Center service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(Tag, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator


    # Add members to the tag
    def add_members_to_the_tag(self, path_param_id, headers=None,payload=None,**request_parameters):
        check_type( path_param_id, basestring, may_be_none=False)
        if headers is not None:
            check_type( headers.get('Content-Type', self._session.headers.get('Content-Type')), basestring, may_be_none=False)
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = { }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
            'id': path_param_id,
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_00a2fa6146089317').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.post(apply_path_params('/api/v2/tag/${id}/member', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.post(apply_path_params('/api/v2/tag/${id}/member', path_params), params=params, json=payload)

        return self._object_factory('bpm_00a2fa6146089317', json_data)


    # Create Tag
    def create_tag(self, rq_description = None, rq_dynamicRules = None, rq_id = None, rq_instanceTenantId = None, rq_name = None, rq_systemTag = None, headers=None,payload=None,**request_parameters):
        if headers is not None:
            check_type( headers.get('Content-Type', self._session.headers.get('Content-Type')), basestring, may_be_none=False)
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = { }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        if rq_systemTag is not None: payload.update( { 'systemTag':  rq_systemTag })
        if rq_description is not None: payload.update( { 'description':  rq_description })
        if rq_dynamicRules is not None: payload.update( { 'dynamicRules':  rq_dynamicRules })
        if rq_name is not None: payload.update( { 'name':  rq_name })
        if rq_id is not None: payload.update( { 'id':  rq_id })
        if rq_instanceTenantId is not None: payload.update( { 'instanceTenantId':  rq_instanceTenantId })
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_1399891c42a8be64').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.post(apply_path_params('/api/v2/tag', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.post(apply_path_params('/api/v2/tag', path_params), params=params, json=payload)

        return self._object_factory('bpm_1399891c42a8be64', json_data)


    # Delete Tag
    def delete_tag(self, path_param_id, headers=None,payload=None,**request_parameters):
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

        self._request_validator('jsd_429c28154bdaa13d').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.delete(apply_path_params('/api/v2/tag/${id}', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.delete(apply_path_params('/api/v2/tag/${id}', path_params), params=params, json=payload)

        return self._object_factory('bpm_429c28154bdaa13d', json_data)


    # Get Tag Member count
    def get_tag_member_count(self, param_member_type, path_param_id, param_level = '0', param_member_association_type = None, headers=None,payload=None,**request_parameters):
        check_type( param_member_type, basestring, may_be_none=False)
        check_type( param_member_association_type, basestring)
        check_type( param_level, basestring)
        check_type( path_param_id, basestring, may_be_none=False)
        if headers is not None:
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = { }
        if param_member_type is not None: params.update( { 'memberType': param_member_type })
        if param_member_association_type is not None: params.update( { 'memberAssociationType': param_member_association_type })
        if param_level is not None: params.update( { 'level': param_level })
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
            'id': path_param_id,
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_2e9db85840fbb1cf').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.get(apply_path_params('/api/v2/tag/${id}/member/count', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.get(apply_path_params('/api/v2/tag/${id}/member/count', path_params), params=params, json=payload)

        return self._object_factory('bpm_2e9db85840fbb1cf', json_data)


    # Get Tag resource types
    def get_tag_resource_types(self, headers=None,payload=None,**request_parameters):
        if headers is not None:
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = { }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_4695090d403b8eaa').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.get(apply_path_params('/api/v2/tag/member/type', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.get(apply_path_params('/api/v2/tag/member/type', path_params), params=params, json=payload)

        return self._object_factory('bpm_4695090d403b8eaa', json_data)


    # Updates tag membership
    def updates_tag_membership(self, rq_memberToTags = None, rq_memberType = None, headers=None,payload=None,**request_parameters):
        if headers is not None:
            check_type( headers.get('Content-Type', self._session.headers.get('Content-Type')), basestring, may_be_none=False)
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = { }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        if rq_memberToTags is not None: payload.update( { 'memberToTags':  rq_memberToTags })
        if rq_memberType is not None: payload.update( { 'memberType':  rq_memberType })
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_45bc7a8344a8bc1e').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.put(apply_path_params('/api/v2/tag/member', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.put(apply_path_params('/api/v2/tag/member', path_params), params=params, json=payload)

        return self._object_factory('bpm_45bc7a8344a8bc1e', json_data)


    # Update Tag
    def update_tag(self, rq_description = None, rq_dynamicRules = None, rq_id = None, rq_instanceTenantId = None, rq_name = None, rq_systemTag = None, headers=None,payload=None,**request_parameters):
        if headers is not None:
            check_type( headers.get('Content-Type', self._session.headers.get('Content-Type')), basestring, may_be_none=False)
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = { }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        if rq_systemTag is not None: payload.update( { 'systemTag':  rq_systemTag })
        if rq_description is not None: payload.update( { 'description':  rq_description })
        if rq_dynamicRules is not None: payload.update( { 'dynamicRules':  rq_dynamicRules })
        if rq_name is not None: payload.update( { 'name':  rq_name })
        if rq_id is not None: payload.update( { 'id':  rq_id })
        if rq_instanceTenantId is not None: payload.update( { 'instanceTenantId':  rq_instanceTenantId })
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_4d86a993469a9da9').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.put(apply_path_params('/api/v2/tag', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.put(apply_path_params('/api/v2/tag', path_params), params=params, json=payload)

        return self._object_factory('bpm_4d86a993469a9da9', json_data)


    # Get Tag Count
    def get_tag_count(self, param_attribute_name = None, param_level = None, param_name = None, param_name_space = None, param_size = None, param_system_tag = None, headers=None,payload=None,**request_parameters):
        check_type( param_name, basestring)
        check_type( param_name_space, basestring)
        check_type( param_attribute_name, basestring)
        check_type( param_level, basestring)
        check_type( param_size, basestring)
        check_type( param_system_tag, basestring)
        if headers is not None:
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = { }
        if param_name is not None: params.update( { 'name': param_name })
        if param_name_space is not None: params.update( { 'nameSpace': param_name_space })
        if param_attribute_name is not None: params.update( { 'attributeName': param_attribute_name })
        if param_level is not None: params.update( { 'level': param_level })
        if param_size is not None: params.update( { 'size': param_size })
        if param_system_tag is not None: params.update( { 'systemTag': param_system_tag })
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_8091a9b84bfba53b').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.get(apply_path_params('/api/v2/tag/count', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.get(apply_path_params('/api/v2/tag/count', path_params), params=params, json=payload)

        return self._object_factory('bpm_8091a9b84bfba53b', json_data)


    # Get Tag by Id
    def get_tag_by_id(self, path_param_id, headers=None,payload=None,**request_parameters):
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

        self._request_validator('jsd_c1a359b14c89b573').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.get(apply_path_params('/api/v2/tag/${id}', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.get(apply_path_params('/api/v2/tag/${id}', path_params), params=params, json=payload)

        return self._object_factory('bpm_c1a359b14c89b573', json_data)


    # Get Tag members by Id
    def get_tag_members_by_id(self, param_member_type, path_param_id, param_level = '0', param_limit = None, param_member_association_type = None, param_offset = None, headers=None,payload=None,**request_parameters):
        check_type( param_member_type, basestring, may_be_none=False)
        check_type( param_offset, basestring)
        check_type( param_limit, basestring)
        check_type( param_member_association_type, basestring)
        check_type( param_level, basestring)
        check_type( path_param_id, basestring, may_be_none=False)
        if headers is not None:
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = { }
        if param_member_type is not None: params.update( { 'memberType': param_member_type })
        if param_offset is not None: params.update( { 'offset': param_offset })
        if param_limit is not None: params.update( { 'limit': param_limit })
        if param_member_association_type is not None: params.update( { 'memberAssociationType': param_member_association_type })
        if param_level is not None: params.update( { 'level': param_level })
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
            'id': path_param_id,
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_eab7abe048fb99ad').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.get(apply_path_params('/api/v2/tag/${id}/member', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.get(apply_path_params('/api/v2/tag/${id}/member', path_params), params=params, json=payload)

        return self._object_factory('bpm_eab7abe048fb99ad', json_data)


    # Remove Tag member
    def remove_tag_member(self, path_param_id, path_param_member_id, headers=None,payload=None,**request_parameters):
        check_type( path_param_id, basestring, may_be_none=False)
        check_type( path_param_member_id, basestring, may_be_none=False)
        if headers is not None:
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = { }
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
            'id': path_param_id,
            'memberId': path_param_member_id,
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_caa3ea704d78b37e').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.delete(apply_path_params('/api/v2/tag/${id}/member/${memberId}', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.delete(apply_path_params('/api/v2/tag/${id}/member/${memberId}', path_params), params=params, json=payload)

        return self._object_factory('bpm_caa3ea704d78b37e', json_data)


    # Get Tag
    def get_tag(self, param_additional_info_attributes = None, param_additional_info_name_space = None, param_field = None, param_level = None, param_limit = None, param_name = None, param_offset = None, param_order = None, param_size = None, param_sort_by = None, param_system_tag = None, headers=None,payload=None,**request_parameters):
        check_type( param_name, basestring)
        check_type( param_additional_info_name_space, basestring)
        check_type( param_additional_info_attributes, basestring)
        check_type( param_level, basestring)
        check_type( param_offset, basestring)
        check_type( param_limit, basestring)
        check_type( param_size, basestring)
        check_type( param_field, basestring)
        check_type( param_sort_by, basestring)
        check_type( param_order, basestring)
        check_type( param_system_tag, basestring)
        if headers is not None:
            check_type( headers.get('X-Auth-Token', self._session.headers.get('X-Auth-Token')), basestring, may_be_none=False)

        params = { }
        if param_name is not None: params.update( { 'name': param_name })
        if param_additional_info_name_space is not None: params.update( { 'additionalInfo.nameSpace': param_additional_info_name_space })
        if param_additional_info_attributes is not None: params.update( { 'additionalInfo.attributes': param_additional_info_attributes })
        if param_level is not None: params.update( { 'level': param_level })
        if param_offset is not None: params.update( { 'offset': param_offset })
        if param_limit is not None: params.update( { 'limit': param_limit })
        if param_size is not None: params.update( { 'size': param_size })
        if param_field is not None: params.update( { 'field': param_field })
        if param_sort_by is not None: params.update( { 'sortBy': param_sort_by })
        if param_order is not None: params.update( { 'order': param_order })
        if param_system_tag is not None: params.update( { 'systemTag': param_system_tag })
        params.update(dict_filt(request_parameters, 'params'))

        path_params = {
        }
        path_params.update(dict_filt(request_parameters, 'path_params'))

        payload = payload or {}
        payload.update( dict_filt(request_parameters, 'payload') )

        self._request_validator('jsd_ee9aab01487a8896').validate(payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
                _headers.update(headers)
                with_custom_headers = True
        if dict_filt(request_parameters, 'headers'):
                _headers.update(dict_filt(request_parameters, 'headers'))
                with_custom_headers = True


        # API request
        json_data = self._session.get(apply_path_params('/api/v2/tag', path_params), params=params, json=payload, headers=_headers) if with_custom_headers \
        else self._session.get(apply_path_params('/api/v2/tag', path_params), params=params, json=payload)

        return self._object_factory('bpm_ee9aab01487a8896', json_data)



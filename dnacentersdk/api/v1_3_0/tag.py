# -*- coding: utf-8 -*-
"""Cisco DNA Center Tag API wrapper.

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


class Tag(object):
    """Cisco DNA Center Tag API (version: 1.3.0).

    Wraps the DNA Center Tag
    API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new Tag
        object with the provided RestSession.

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

    def add_members_to_the_tag(self,
                               id,
                               headers=None,
                               payload=None,
                               active_validation=True,
                               **request_parameters):
        """Adds members to the tag specified by id.

        Args:
            id(basestring): Tag ID.
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
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_00a2fa6146089317_v1_3_0')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/tag/${id}/member')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_00a2fa6146089317_v1_3_0', json_data)

    def create_tag(self,
                   description=None,
                   dynamicRules=None,
                   id=None,
                   instanceTenantId=None,
                   name=None,
                   systemTag=None,
                   headers=None,
                   payload=None,
                   active_validation=True,
                   **request_parameters):
        """Creates tag with specified tag attributes.

        Args:
            description(string): TagDTO's description.
            dynamicRules(list): TagDTO's dynamicRules (list of objects).
            id(string): TagDTO's id.
            instanceTenantId(string): TagDTO's instanceTenantId.
            name(string): TagDTO's name.
            systemTag(boolean): TagDTO's systemTag.
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
            'systemTag':
                systemTag,
            'description':
                description,
            'dynamicRules':
                dynamicRules,
            'name':
                name,
            'id':
                id,
            'instanceTenantId':
                instanceTenantId,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_1399891c42a8be64_v1_3_0')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/tag')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_1399891c42a8be64_v1_3_0', json_data)

    def delete_tag(self,
                   id,
                   headers=None,
                   **request_parameters):
        """Deletes a tag specified by id.

        Args:
            id(basestring): Tag ID.
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

        e_url = ('/dna/intent/api/v1/tag/${id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(endpoint_full_url, params=_params,
                                             headers=_headers)
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_429c28154bdaa13d_v1_3_0', json_data)

    def get_tag_member_count(self,
                             id,
                             member_type,
                             level='0',
                             member_association_type=None,
                             headers=None,
                             **request_parameters):
        """Returns the number of members in a given tag.

        Args:
            id(basestring): Tag ID.
            member_type(basestring): memberType query parameter.
            member_association_type(basestring): memberAssociationType query parameter.
            level(basestring): level query parameter.
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
        check_type(member_type, basestring,
                   may_be_none=False)
        check_type(member_association_type, basestring)
        check_type(level, basestring)
        check_type(id, basestring,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        _params = {
            'memberType':
                member_type,
            'memberAssociationType':
                member_association_type,
            'level':
                level,
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

        e_url = ('/dna/intent/api/v1/tag/${id}/member/count')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_2e9db85840fbb1cf_v1_3_0', json_data)

    def get_tag_resource_types(self,
                               headers=None,
                               **request_parameters):
        """Returns list of supported resource types.

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

        e_url = ('/dna/intent/api/v1/tag/member/type')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_4695090d403b8eaa_v1_3_0', json_data)

    def updates_tag_membership(self,
                               memberToTags=None,
                               memberType=None,
                               headers=None,
                               payload=None,
                               active_validation=True,
                               **request_parameters):
        """Updates tag membership. As part of the request payload through
        this API, only the specified members are added /
        retained to the given input tags. Possible values of
        memberType attribute in the request payload can be
        queried by using the /tag/member/type API.

        Args:
            memberToTags(array, object): TagMemberDTO's memberToTags.
            memberType(string): TagMemberDTO's memberType.
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
            'memberToTags':
                memberToTags,
            'memberType':
                memberType,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_45bc7a8344a8bc1e_v1_3_0')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/tag/member')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload,
                                          headers=_headers)
        else:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload)

        return self._object_factory('bpm_45bc7a8344a8bc1e_v1_3_0', json_data)

    def update_tag(self,
                   description=None,
                   dynamicRules=None,
                   id=None,
                   instanceTenantId=None,
                   name=None,
                   systemTag=None,
                   headers=None,
                   payload=None,
                   active_validation=True,
                   **request_parameters):
        """Updates a tag specified by id.

        Args:
            description(string): TagDTO's description.
            dynamicRules(list): TagDTO's dynamicRules (list of objects).
            id(string): TagDTO's id.
            instanceTenantId(string): TagDTO's instanceTenantId.
            name(string): TagDTO's name.
            systemTag(boolean): TagDTO's systemTag.
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
            'systemTag':
                systemTag,
            'description':
                description,
            'dynamicRules':
                dynamicRules,
            'name':
                name,
            'id':
                id,
            'instanceTenantId':
                instanceTenantId,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_4d86a993469a9da9_v1_3_0')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/tag')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload,
                                          headers=_headers)
        else:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload)

        return self._object_factory('bpm_4d86a993469a9da9_v1_3_0', json_data)

    def get_tag_count(self,
                      attribute_name=None,
                      level=None,
                      name=None,
                      name_space=None,
                      size=None,
                      system_tag=None,
                      headers=None,
                      **request_parameters):
        """Returns tag count.

        Args:
            name(basestring): name query parameter.
            name_space(basestring): nameSpace query parameter.
            attribute_name(basestring): attributeName query parameter.
            level(basestring): level query parameter.
            size(basestring): size in kilobytes(KB).
            system_tag(basestring): systemTag query parameter.
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
        check_type(name, basestring)
        check_type(name_space, basestring)
        check_type(attribute_name, basestring)
        check_type(level, basestring)
        check_type(size, basestring)
        check_type(system_tag, basestring)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        _params = {
            'name':
                name,
            'nameSpace':
                name_space,
            'attributeName':
                attribute_name,
            'level':
                level,
            'size':
                size,
            'systemTag':
                system_tag,
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

        e_url = ('/dna/intent/api/v1/tag/count')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_8091a9b84bfba53b_v1_3_0', json_data)

    def get_tag_by_id(self,
                      id,
                      headers=None,
                      **request_parameters):
        """Returns tag specified by Id.

        Args:
            id(basestring): Tag ID.
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

        e_url = ('/dna/intent/api/v1/tag/${id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_c1a359b14c89b573_v1_3_0', json_data)

    def get_tag_members_by_id(self,
                              id,
                              member_type,
                              level='0',
                              limit=None,
                              member_association_type=None,
                              offset=None,
                              headers=None,
                              **request_parameters):
        """Returns tag members specified by id.

        Args:
            id(basestring): Tag ID.
            member_type(basestring): Entity type of the member. Possible values can be retrieved by using
                /tag/member/type API.
            offset(basestring): Used for pagination. It indicates the starting row number out of available member
                records.
            limit(basestring): Used to Number of maximum members to return in the result.
            member_association_type(basestring): Indicates how the member is associated with the tag. Possible
                values and description. 1) DYNAMIC : The member is associated to the tag through rules.
                2) STATIC – The member is associated to the tag manually. 3) MIXED – The member is
                associated manually and also satisfies the rule defined for the tag.
            level(basestring): level query parameter.
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
        check_type(member_type, basestring,
                   may_be_none=False)
        check_type(offset, basestring)
        check_type(limit, basestring)
        check_type(member_association_type, basestring)
        check_type(level, basestring)
        check_type(id, basestring,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        _params = {
            'memberType':
                member_type,
            'offset':
                offset,
            'limit':
                limit,
            'memberAssociationType':
                member_association_type,
            'level':
                level,
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

        e_url = ('/dna/intent/api/v1/tag/${id}/member')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_eab7abe048fb99ad_v1_3_0', json_data)

    def remove_tag_member(self,
                          id,
                          member_id,
                          headers=None,
                          **request_parameters):
        """Removes Tag member from the tag specified by id.

        Args:
            id(basestring): Tag ID.
            member_id(basestring): TagMember id to be removed from tag.
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
        check_type(member_id, basestring,
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
            'memberId': member_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/tag/${id}/member/${memberId}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(endpoint_full_url, params=_params,
                                             headers=_headers)
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_caa3ea704d78b37e_v1_3_0', json_data)

    def get_tag(self,
                additional_info_attributes=None,
                additional_info_name_space=None,
                field=None,
                level=None,
                limit=None,
                name=None,
                offset=None,
                order=None,
                size=None,
                sort_by=None,
                system_tag=None,
                headers=None,
                **request_parameters):
        """Returns the tags for given filter criteria.

        Args:
            name(basestring): Tag name is mandatory when filter operation is used.
            additional_info_name_space(basestring): additionalInfo.nameSpace query parameter.
            additional_info_attributes(basestring): additionalInfo.attributes query parameter.
            level(basestring): level query parameter.
            offset(basestring): offset query parameter.
            limit(basestring): limit query parameter.
            size(basestring): size in kilobytes(KB).
            field(basestring): Available field names are
                :'name,id,parentId,type,additionalInfo.nameSpace,additionalInfo.attributes'.
            sort_by(basestring): Only supported attribute is name. SortyBy is mandatory when order is used.
            order(basestring): Available values are asc and des.
            system_tag(basestring): systemTag query parameter.
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
        check_type(name, basestring)
        check_type(additional_info_name_space, basestring)
        check_type(additional_info_attributes, basestring)
        check_type(level, basestring)
        check_type(offset, basestring)
        check_type(limit, basestring)
        check_type(size, basestring)
        check_type(field, basestring)
        check_type(sort_by, basestring)
        check_type(order, basestring)
        check_type(system_tag, basestring)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

        _params = {
            'name':
                name,
            'additionalInfo.nameSpace':
                additional_info_name_space,
            'additionalInfo.attributes':
                additional_info_attributes,
            'level':
                level,
            'offset':
                offset,
            'limit':
                limit,
            'size':
                size,
            'field':
                field,
            'sortBy':
                sort_by,
            'order':
                order,
            'systemTag':
                system_tag,
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

        e_url = ('/dna/intent/api/v1/tag')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_ee9aab01487a8896_v1_3_0', json_data)

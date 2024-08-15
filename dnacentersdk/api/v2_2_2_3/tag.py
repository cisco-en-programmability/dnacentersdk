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


from builtins import *


from ...restsession import RestSession
from ...utils import (
    apply_path_params,
    check_type,
    dict_from_items_with_values,
    dict_of_str,
)


class Tag(object):
    """Cisco DNA Center Tag API (version: 2.2.2.3).

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
        """Updates a tag specified by id .

        Args:
            description(string): Tag's description.
            dynamicRules(list): Tag's dynamicRules (list of objects).
            id(string): Tag's id.
            instanceTenantId(string): Tag's instanceTenantId.
            name(string): Tag's name.
            systemTag(boolean): Tag's systemTag.
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
                           str, may_be_none=False)
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

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
            self._request_validator('jsd_c9f995abc21b54e7860f66aef2ffbc85_v2_2_2_3')\
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

        return self._object_factory('bpm_c9f995abc21b54e7860f66aef2ffbc85_v2_2_2_3', json_data)

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
        """Returns the tags for given filter criteria .

        Args:
            name(str): name query parameter. Tag name is mandatory when filter operation is used. .
            additional_info_name_space(str): additionalInfo.nameSpace query parameter.
            additional_info_attributes(str): additionalInfo.attributes query parameter.
            level(str): level query parameter.
            offset(str,int): offset query parameter.
            limit(str,int): limit query parameter.
            size(str): size query parameter. size in kilobytes(KB) .
            field(str): field query parameter. Available field names are
                :'name,id,parentId,type,additionalInfo.nameSpace,additionalInfo.attributes' .
            sort_by(str): sortBy query parameter. Only supported attribute is name. SortyBy is mandatory when
                order is used. .
            order(str): order query parameter. Available values are asc and des .
            system_tag(str): systemTag query parameter.
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
        check_type(name, str)
        check_type(additional_info_name_space, str)
        check_type(additional_info_attributes, str)
        check_type(level, str)
        check_type(offset, (int, str))
        check_type(limit, (int, str))
        check_type(size, str)
        check_type(field, str)
        check_type(sort_by, str)
        check_type(order, str)
        check_type(system_tag, str)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

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

        return self._object_factory('bpm_a4185f5b40aabe991f8cdb2816_v2_2_2_3', json_data)

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
        """Creates tag with specified tag attributes .

        Args:
            description(string): Tag's description.
            dynamicRules(list): Tag's dynamicRules (list of objects).
            id(string): Tag's id.
            instanceTenantId(string): Tag's instanceTenantId.
            name(string): Tag's name.
            systemTag(boolean): Tag's systemTag.
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
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

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
            self._request_validator('jsd_e8271b05b62c54609f74b4f2f373ad5a_v2_2_2_3')\
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

        return self._object_factory('bpm_e8271b05b62c54609f74b4f2f373ad5a_v2_2_2_3', json_data)

    def get_tag_count(self,
                      attribute_name=None,
                      level=None,
                      name=None,
                      name_space=None,
                      size=None,
                      system_tag=None,
                      headers=None,
                      **request_parameters):
        """Returns tag count .

        Args:
            name(str): name query parameter.
            name_space(str): nameSpace query parameter.
            attribute_name(str): attributeName query parameter.
            level(str): level query parameter.
            size(str): size query parameter. size in kilobytes(KB) .
            system_tag(str): systemTag query parameter.
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
        check_type(name, str)
        check_type(name_space, str)
        check_type(attribute_name, str)
        check_type(level, str)
        check_type(size, str)
        check_type(system_tag, str)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

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

        return self._object_factory('bpm_afb52259f7c3501ca4d8ccd277828658_v2_2_2_3', json_data)

    def updates_tag_membership(self,
                               memberToTags=None,
                               memberType=None,
                               headers=None,
                               payload=None,
                               active_validation=True,
                               **request_parameters):
        """Updates tag membership. As part of the request payload through this API, only the specified members are added /
        retained to the given input tags. Possible values of memberType attribute in the request payload can be
        queried by using the /tag/member/type API .

        Args:
            memberToTags(object): Tag's memberToTags.
            memberType(string): Tag's memberType.
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
                           str, may_be_none=False)
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

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
            self._request_validator('jsd_e3934b0fb68a5ff787e65e9b7c8e6296_v2_2_2_3')\
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

        return self._object_factory('bpm_e3934b0fb68a5ff787e65e9b7c8e6296_v2_2_2_3', json_data)

    def get_tag_resource_types(self,
                               headers=None,
                               **request_parameters):
        """Returns list of supported resource types .

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
                           str, may_be_none=False)

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

        return self._object_factory('bpm_baf47897d525e5899f62e4d5bdd260b_v2_2_2_3', json_data)

    def delete_tag(self,
                   id,
                   headers=None,
                   **request_parameters):
        """Deletes a tag specified by id .

        Args:
            id(str): id path parameter. Tag ID .
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
        check_type(id, str,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

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

        e_url = ('/dna/intent/api/v1/tag/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(endpoint_full_url, params=_params,
                                             headers=_headers)
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_ed48fc373506cb1688cff36c2cb0f_v2_2_2_3', json_data)

    def get_tag_by_id(self,
                      id,
                      headers=None,
                      **request_parameters):
        """Returns tag specified by Id .

        Args:
            id(str): id path parameter. Tag ID .
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
        check_type(id, str,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

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

        e_url = ('/dna/intent/api/v1/tag/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_d65f9b9d8ad5426bdf7e55461fcf761_v2_2_2_3', json_data)

    def get_tag_members_by_id(self,
                              id,
                              member_type,
                              level=None,
                              limit=None,
                              member_association_type=None,
                              offset=None,
                              headers=None,
                              **request_parameters):
        """Returns tag members specified by id .

        Args:
            id(str): id path parameter. Tag ID .
            member_type(str): memberType query parameter. Entity type of the member. Possible values can be
                retrieved by using /tag/member/type API .
            offset(str,int): offset query parameter. Used for pagination. It indicates the starting row number
                out of available member records .
            limit(str,int): limit query parameter. Used to Number of maximum members to return in the result .
            member_association_type(str): memberAssociationType query parameter. Indicates how the member is
                associated with the tag. Possible values and description. 1) DYNAMIC : The member is
                associated to the tag through rules. 2) STATIC – The member is associated to the tag
                manually. 3) MIXED – The member is associated manually and also satisfies the rule
                defined for the tag .
            level(str): level query parameter.
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
        check_type(member_type, str,
                   may_be_none=False)
        check_type(offset, (int, str))
        check_type(limit, (int, str))
        check_type(member_association_type, str)
        check_type(level, str)
        check_type(id, str,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

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

        e_url = ('/dna/intent/api/v1/tag/{id}/member')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_ff12c50ea3fb53c9a53f9c9e2c595d44_v2_2_2_3', json_data)

    def add_members_to_the_tag(self,
                               id,
                               headers=None,
                               payload=None,
                               active_validation=True,
                               **request_parameters):
        """Adds members to the tag specified by id .

        Args:
            id(str): id path parameter. Tag ID .
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
        check_type(id, str,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

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
            self._request_validator('jsd_dcc43be0514e50fea80cfa827f13ee5c_v2_2_2_3')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/tag/{id}/member')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_dcc43be0514e50fea80cfa827f13ee5c_v2_2_2_3', json_data)

    def get_tag_member_count(self,
                             id,
                             member_type,
                             level=None,
                             member_association_type=None,
                             headers=None,
                             **request_parameters):
        """Returns the number of members in a given tag .

        Args:
            id(str): id path parameter. Tag ID .
            member_type(str): memberType query parameter.
            member_association_type(str): memberAssociationType query parameter.
            level(str): level query parameter.
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
        check_type(member_type, str,
                   may_be_none=False)
        check_type(member_association_type, str)
        check_type(level, str)
        check_type(id, str,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

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

        e_url = ('/dna/intent/api/v1/tag/{id}/member/count')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_ffacb52f745c15b40b9b352754e2e1_v2_2_2_3', json_data)

    def remove_tag_member(self,
                          id,
                          member_id,
                          headers=None,
                          **request_parameters):
        """Removes Tag member from the tag specified by id .

        Args:
            id(str): id path parameter. Tag ID .
            member_id(str): memberId path parameter. TagMember id to be removed from tag .
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
        check_type(id, str,
                   may_be_none=False)
        check_type(member_id, str,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

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

        e_url = ('/dna/intent/api/v1/tag/{id}/member/{memberId}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(endpoint_full_url, params=_params,
                                             headers=_headers)
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_cc9883be5c1cad1959347babb342_v2_2_2_3', json_data)

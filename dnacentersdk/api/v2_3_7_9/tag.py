# -*- coding: utf-8 -*-
"""Cisco Catalyst Center Tag API wrapper.

Copyright (c) 2024 Cisco Systems.

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
    """Cisco Catalyst Center Tag API (version: 2.3.7.9).

    Wraps the Catalyst Center Tag
    API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new Tag
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Catalyst Center service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(Tag, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def update_tag_v1(self,
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
            description(string): Tag's description of the tag. .
            dynamicRules(list): Tag's dynamicRules (list of objects).
            id(string): Tag's mandatory instanceUuid of the tag that needs to be updated. .
            instanceTenantId(string): Tag's instanceTenantId generated for the tag. .
            name(string): Tag's name of the tag. .
            systemTag(boolean): Tag's true for system created tags, false for user defined tags .
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!update-tag
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
            self._request_validator('jsd_c9f995abc21b54e7860f66aef2ffbc85_v2_3_7_9')\
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

        return self._object_factory('bpm_c9f995abc21b54e7860f66aef2ffbc85_v2_3_7_9', json_data)

    def get_tag_v1(self,
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
            offset(int): offset query parameter.
            limit(int): limit query parameter. The number of tags to be retrieved. If not specified, the default is
                500. The maximum allowed limit is 500. .
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-tag
        """
        check_type(headers, dict)
        check_type(name, str)
        check_type(additional_info_name_space, str)
        check_type(additional_info_attributes, str)
        check_type(level, str)
        check_type(offset, int)
        check_type(limit, int)
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

        return self._object_factory('bpm_a4185f5b40aabe991f8cdb2816_v2_3_7_9', json_data)

    def create_tag_v1(self,
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
            description(string): Tag's description of the tag. .
            dynamicRules(list): Tag's dynamicRules (list of objects).
            id(string): Tag's instanceUuid generated for the tag. .
            instanceTenantId(string): Tag's instanceTenantId generated for the tag. .
            name(string): Tag's name of the tag. .
            systemTag(boolean): Tag's true for system created tags, false for user defined tags .
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!create-tag
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
            self._request_validator('jsd_e8271b05b62c54609f74b4f2f373ad5a_v2_3_7_9')\
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

        return self._object_factory('bpm_e8271b05b62c54609f74b4f2f373ad5a_v2_3_7_9', json_data)

    def get_tag_count_v1(self,
                         attribute_name=None,
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-tag-count
        """
        check_type(headers, dict)
        check_type(name, str)
        check_type(name_space, str)
        check_type(attribute_name, str)
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

        return self._object_factory('bpm_afb52259f7c3501ca4d8ccd277828658_v2_3_7_9', json_data)

    def update_tag_membership_v1(self,
                                 memberToTags=None,
                                 memberType=None,
                                 headers=None,
                                 payload=None,
                                 active_validation=True,
                                 **request_parameters):
        """Update tag membership. As part of the request payload through this API, only the specified members are added /
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!update-tag-membership
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
            self._request_validator('jsd_e3934b0fb68a5ff787e65e9b7c8e6296_v2_3_7_9')\
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

        return self._object_factory('bpm_e3934b0fb68a5ff787e65e9b7c8e6296_v2_3_7_9', json_data)

    def get_tag_resource_types_v1(self,
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-tag-resource-types
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

        return self._object_factory('bpm_baf47897d525e5899f62e4d5bdd260b_v2_3_7_9', json_data)

    def delete_tag_v1(self,
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!delete-tag
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

        return self._object_factory('bpm_ed48fc373506cb1688cff36c2cb0f_v2_3_7_9', json_data)

    def get_tag_by_id_v1(self,
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-tag-by-id
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

        return self._object_factory('bpm_d65f9b9d8ad5426bdf7e55461fcf761_v2_3_7_9', json_data)

    def get_tag_members_by_id_v1(self,
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
            offset(int): offset query parameter. Used for pagination. It indicates the starting row number out of
                available member records .
            limit(int): limit query parameter. The number of members to be retrieved. If not specified, the default
                is 500. The maximum allowed limit is 500. .
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-tag-members-by-id
        """
        check_type(headers, dict)
        check_type(member_type, str,
                   may_be_none=False)
        check_type(offset, int)
        check_type(limit, int)
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

        return self._object_factory('bpm_ff12c50ea3fb53c9a53f9c9e2c595d44_v2_3_7_9', json_data)

    def add_members_to_the_tag_v1(self,
                                  id,
                                  memberType=None,
                                  headers=None,
                                  payload=None,
                                  active_validation=True,
                                  **request_parameters):
        """Adds members to the tag specified by id .

        Args:
            memberType(list): Tag's memberType (list of strings).
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!add-members-to-the-tag
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
            'memberType':
                memberType,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_dcc43be0514e50fea80cfa827f13ee5c_v2_3_7_9')\
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

        return self._object_factory('bpm_dcc43be0514e50fea80cfa827f13ee5c_v2_3_7_9', json_data)

    def get_tag_member_count_v1(self,
                                id,
                                member_type,
                                member_association_type=None,
                                headers=None,
                                **request_parameters):
        """Returns the number of members in a given tag .

        Args:
            id(str): id path parameter. Tag ID .
            member_type(str): memberType query parameter.
            member_association_type(str): memberAssociationType query parameter.
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-tag-member-count
        """
        check_type(headers, dict)
        check_type(member_type, str,
                   may_be_none=False)
        check_type(member_association_type, str)
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

        return self._object_factory('bpm_ffacb52f745c15b40b9b352754e2e1_v2_3_7_9', json_data)

    def remove_tag_member_v1(self,
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!remove-tag-member
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

        return self._object_factory('bpm_cc9883be5c1cad1959347babb342_v2_3_7_9', json_data)

    def retrieve_tags_associated_with_the_interfaces_v1(self,
                                                        limit=None,
                                                        offset=None,
                                                        headers=None,
                                                        **request_parameters):
        """Fetches the tags associated with the interfaces. Interfaces that don't have any tags associated will not be
        included in the response. A tag is a user-defined or system-defined construct to group resources. When
        an interface is tagged, it is called a member of the tag. .

        Args:
            offset(int): offset query parameter. The first record to show for this page; the first record is
                numbered 1. minimum: 1 .
            limit(int): limit query parameter. The number of records to show for this page. minimum: 1, maximum: 500
                .
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!retrieve-tags-associated-with-the-interfaces
        """
        check_type(headers, dict)
        check_type(offset, int)
        check_type(limit, int)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'offset':
                offset,
            'limit':
                limit,
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

        e_url = ('/dna/intent/api/v1/tags/interfaces/membersAssociations')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_c07bbbe75f63913bd83b34277d12_v2_3_7_9', json_data)

    def update_tags_associated_with_the_interfaces_v1(self,
                                                      headers=None,
                                                      payload=None,
                                                      active_validation=True,
                                                      **request_parameters):
        """Updates the tags associated with the interfaces. A tag is a user-defined or system-defined construct to group
        resources. When an interface is tagged, it is called a member of the tag. A tag can be created by using
        this POST `/dna/intent/api/v1/tag` API. .

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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!update-tags-associated-with-the-interfaces
        """
        check_type(headers, dict)
        check_type(payload, list)
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
        _payload = payload or []
        if active_validation:
            self._request_validator('jsd_ea4363569a9d58779c2bfc05b6e45423_v2_3_7_9')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/tags/interfaces/membersAssociations/b'
                 + 'ulk')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload,
                                          headers=_headers)
        else:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload)

        return self._object_factory('bpm_ea4363569a9d58779c2bfc05b6e45423_v2_3_7_9', json_data)

    def retrieve_the_count_of_interfaces_that_are_associated_with_at_least_one_tag_v1(self,
                                                                                      headers=None,
                                                                                      **request_parameters):
        """Fetches the count of interfaces that are associated with at least one tag. A tag is a user-defined or system-
        defined construct to group resources. When an interface is tagged, it is called a member of the tag. .

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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!retrieve-the-count-of-interfaces-that-are-associated-with-at-least-one-tag
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

        e_url = ('/dna/intent/api/v1/tags/interfaces/membersAssociations/c'
                 + 'ount')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_f55ae4d0c6f65207a7630fa556ba2774_v2_3_7_9', json_data)

    def query_the_tags_associated_with_interfaces_v1(self,
                                                     ids=None,
                                                     headers=None,
                                                     payload=None,
                                                     active_validation=True,
                                                     **request_parameters):
        """Fetches the tags associated with the given interface `ids`. Interfaces that don't have any tags associated will
        not be included in the response. A tag is a user-defined or system-defined construct to group resources.
        When an interface is tagged, it is called a member of the tag. `ids` can be fetched via
        `/dna/intent/api/v1/interface` API. .

        Args:
            ids(list): Tag's List of member ids (network device or interface), maximum 500 ids can be passed.  (list
                of strings).
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!query-the-tags-associated-with-interfaces
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
            'ids':
                ids,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_f751cc2f55767b34e4c890b3fd36e_v2_3_7_9')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/tags/interfaces/membersAssociations/q'
                 + 'uery')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_f751cc2f55767b34e4c890b3fd36e_v2_3_7_9', json_data)

    def retrieve_tags_associated_with_network_devices_v1(self,
                                                         limit=None,
                                                         offset=None,
                                                         headers=None,
                                                         **request_parameters):
        """Fetches the tags associated with network devices. Devices that don't have any tags associated will not be
        included in the response. A tag is a user-defined or system-defined construct to group resources. When a
        device is tagged, it is called a member of the tag. .

        Args:
            offset(int): offset query parameter. The first record to show for this page; the first record is
                numbered 1. minimum: 1 .
            limit(int): limit query parameter. The number of records to show for this page. minimum: 1, maximum: 500
                .
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!retrieve-tags-associated-with-network-devices
        """
        check_type(headers, dict)
        check_type(offset, int)
        check_type(limit, int)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'offset':
                offset,
            'limit':
                limit,
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

        e_url = ('/dna/intent/api/v1/tags/networkDevices/membersAssociatio'
                 + 'ns')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_da9595ad2c4d51eaa0d2740d18c97d3a_v2_3_7_9', json_data)

    def update_tags_associated_with_the_network_devices_v1(self,
                                                           headers=None,
                                                           payload=None,
                                                           active_validation=True,
                                                           **request_parameters):
        """Updates the tags associated with the devices. A tag is a user-defined or system-defined construct to group
        resources. When a device is tagged, it is called a member of the tag. A tag can be created by using this
        POST `/dna/intent/api/v1/tag` API. .

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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!update-tags-associated-with-the-network-devices
        """
        check_type(headers, dict)
        check_type(payload, list)
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
        _payload = payload or []
        if active_validation:
            self._request_validator('jsd_bc1f37a9f2571fa4d7bc85b9e8a583_v2_3_7_9')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/tags/networkDevices/membersAssociatio'
                 + 'ns/bulk')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload,
                                          headers=_headers)
        else:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload)

        return self._object_factory('bpm_bc1f37a9f2571fa4d7bc85b9e8a583_v2_3_7_9', json_data)

    def retrieve_the_count_of_network_devices_that_are_associated_with_at_least_one_tag_v1(self,
                                                                                           headers=None,
                                                                                           **request_parameters):
        """Fetches the count of network devices that are associated with at least one tag. A tag is a user-defined or
        system-defined construct to group resources. When a device is tagged, it is called a member of the tag.
        .

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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!retrieve-the-count-of-network-devices-that-are-associated-with-at-least-one-tag
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

        e_url = ('/dna/intent/api/v1/tags/networkDevices/membersAssociatio'
                 + 'ns/count')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_edcdc3299250419200cea088186337_v2_3_7_9', json_data)

    def query_the_tags_associated_with_network_devices_v1(self,
                                                          ids=None,
                                                          headers=None,
                                                          payload=None,
                                                          active_validation=True,
                                                          **request_parameters):
        """Fetches the tags associated with the given network device `ids`. Devices that don't have any tags associated
        will not be included in the response. A tag is a user-defined or system-defined construct to group
        resources. When a device is tagged, it is called a member of the tag. `ids` can be fetched via
        `/dna/intent/api/v1/network-device` API. .

        Args:
            ids(list): Tag's List of member ids (network device or interface), maximum 500 ids can be passed.  (list
                of strings).
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!query-the-tags-associated-with-network-devices
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
            'ids':
                ids,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_e4d083d956805f63b970be543c34eb0e_v2_3_7_9')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/tags/networkDevices/membersAssociatio'
                 + 'ns/query')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_e4d083d956805f63b970be543c34eb0e_v2_3_7_9', json_data)



    # Alias Function
    def get_tag_members_by_id(self,
                                 id,
                                 member_type,
                                 level=None,
                                 limit=None,
                                 member_association_type=None,
                                 offset=None,
                                 headers=None,
                                 **request_parameters):
        """ This function is an alias of get_tag_members_by_id_v1 .
        Args:
            id(str): id path parameter. Tag ID .
            member_type(str): memberType query parameter. Entity type of the member. Possible values can be
                retrieved by using /tag/member/type API .
            offset(int): offset query parameter. Used for pagination. It indicates the starting row number out of
                available member records .
            limit(int): limit query parameter. The number of members to be retrieved. If not specified, the default
                is 500. The maximum allowed limit is 500. .
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
            This function returns the output of get_tag_members_by_id_v1 .
        """
        return self.get_tag_members_by_id_v1(
                    id=id,
                    member_type=member_type,
                    level=level,
                    limit=limit,
                    member_association_type=member_association_type,
                    offset=offset,
                    headers=headers,
                    **request_parameters
        )


    # Alias Function
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
        """ This function is an alias of update_tag_v1 .
        Args:
            description(string): Tag's description of the tag. .
            dynamicRules(list): Tag's dynamicRules (list of objects).
            id(string): Tag's mandatory instanceUuid of the tag that needs to be updated. .
            instanceTenantId(string): Tag's instanceTenantId generated for the tag. .
            name(string): Tag's name of the tag. .
            systemTag(boolean): Tag's true for system created tags, false for user defined tags .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of update_tag_v1 .
        """
        return self.update_tag_v1(
                    description=description,
                    dynamicRules=dynamicRules,
                    id=id,
                    instanceTenantId=instanceTenantId,
                    name=name,
                    systemTag=systemTag,
                    headers=headers,
                    payload=payload,
                    active_validation=active_validation,
                    **request_parameters
        )


    # Alias Function
    def delete_tag(self,
                      id,
                      headers=None,
                      **request_parameters):
        """ This function is an alias of delete_tag_v1 .
        Args:
            id(str): id path parameter. Tag ID .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of delete_tag_v1 .
        """
        return self.delete_tag_v1(
                    id=id,
                    headers=headers,
                    **request_parameters
        )


    # Alias Function
    def update_tags_associated_with_the_network_devices(self,
                                                           headers=None,
                                                           payload=None,
                                                           active_validation=True,
                                                           **request_parameters):
        """ This function is an alias of update_tags_associated_with_the_network_devices_v1 .
        Args:
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of update_tags_associated_with_the_network_devices_v1 .
        """
        return self.update_tags_associated_with_the_network_devices_v1(
                    headers=headers,
                    payload=payload,
                    active_validation=active_validation,
                    **request_parameters
        )


    # Alias Function
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
        """ This function is an alias of get_tag_v1 .
        Args:
            name(str): name query parameter. Tag name is mandatory when filter operation is used. .
            additional_info_name_space(str): additionalInfo.nameSpace query parameter.
            additional_info_attributes(str): additionalInfo.attributes query parameter.
            level(str): level query parameter.
            offset(int): offset query parameter.
            limit(int): limit query parameter. The number of tags to be retrieved. If not specified, the default is
                500. The maximum allowed limit is 500. .
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
            This function returns the output of get_tag_v1 .
        """
        return self.get_tag_v1(
                    additional_info_attributes=additional_info_attributes,
                    additional_info_name_space=additional_info_name_space,
                    field=field,
                    level=level,
                    limit=limit,
                    name=name,
                    offset=offset,
                    order=order,
                    size=size,
                    sort_by=sort_by,
                    system_tag=system_tag,
                    headers=headers,
                    **request_parameters
        )


    # Alias Function
    def remove_tag_member(self,
                             id,
                             member_id,
                             headers=None,
                             **request_parameters):
        """ This function is an alias of remove_tag_member_v1 .
        Args:
            id(str): id path parameter. Tag ID .
            member_id(str): memberId path parameter. TagMember id to be removed from tag .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of remove_tag_member_v1 .
        """
        return self.remove_tag_member_v1(
                    id=id,
                    member_id=member_id,
                    headers=headers,
                    **request_parameters
        )


    # Alias Function
    def retrieve_tags_associated_with_the_interfaces(self,
                                                        limit=None,
                                                        offset=None,
                                                        headers=None,
                                                        **request_parameters):
        """ This function is an alias of retrieve_tags_associated_with_the_interfaces_v1 .
        Args:
            offset(int): offset query parameter. The first record to show for this page; the first record is
                numbered 1. minimum: 1 .
            limit(int): limit query parameter. The number of records to show for this page. minimum: 1, maximum: 500
                .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of retrieve_tags_associated_with_the_interfaces_v1 .
        """
        return self.retrieve_tags_associated_with_the_interfaces_v1(
                    limit=limit,
                    offset=offset,
                    headers=headers,
                    **request_parameters
        )


    # Alias Function
    def get_tag_resource_types(self,
                                  headers=None,
                                  **request_parameters):
        """ This function is an alias of get_tag_resource_types_v1 .
        Args:
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_tag_resource_types_v1 .
        """
        return self.get_tag_resource_types_v1(
                    headers=headers,
                    **request_parameters
        )


    # Alias Function
    def retrieve_the_count_of_network_devices_that_are_associated_with_at_least_one_tag(self,
                                                                                           headers=None,
                                                                                           **request_parameters):
        """ This function is an alias of retrieve_the_count_of_network_devices_that_are_associated_with_at_least_one_tag_v1 .
        Args:
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of retrieve_the_count_of_network_devices_that_are_associated_with_at_least_one_tag_v1 .
        """
        return self.retrieve_the_count_of_network_devices_that_are_associated_with_at_least_one_tag_v1(
                    headers=headers,
                    **request_parameters
        )


    # Alias Function
    def query_the_tags_associated_with_network_devices(self,
                                                          ids=None,
                                                          headers=None,
                                                          payload=None,
                                                          active_validation=True,
                                                          **request_parameters):
        """ This function is an alias of query_the_tags_associated_with_network_devices_v1 .
        Args:
            ids(list): Tag's List of member ids (network device or interface), maximum 500 ids can be passed.  (list
                of strings).
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of query_the_tags_associated_with_network_devices_v1 .
        """
        return self.query_the_tags_associated_with_network_devices_v1(
                    ids=ids,
                    headers=headers,
                    payload=payload,
                    active_validation=active_validation,
                    **request_parameters
        )


    # Alias Function
    def retrieve_the_count_of_interfaces_that_are_associated_with_at_least_one_tag(self,
                                                                                      headers=None,
                                                                                      **request_parameters):
        """ This function is an alias of retrieve_the_count_of_interfaces_that_are_associated_with_at_least_one_tag_v1 .
        Args:
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of retrieve_the_count_of_interfaces_that_are_associated_with_at_least_one_tag_v1 .
        """
        return self.retrieve_the_count_of_interfaces_that_are_associated_with_at_least_one_tag_v1(
                    headers=headers,
                    **request_parameters
        )


    # Alias Function
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
        """ This function is an alias of create_tag_v1 .
        Args:
            description(string): Tag's description of the tag. .
            dynamicRules(list): Tag's dynamicRules (list of objects).
            id(string): Tag's instanceUuid generated for the tag. .
            instanceTenantId(string): Tag's instanceTenantId generated for the tag. .
            name(string): Tag's name of the tag. .
            systemTag(boolean): Tag's true for system created tags, false for user defined tags .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of create_tag_v1 .
        """
        return self.create_tag_v1(
                    description=description,
                    dynamicRules=dynamicRules,
                    id=id,
                    instanceTenantId=instanceTenantId,
                    name=name,
                    systemTag=systemTag,
                    headers=headers,
                    payload=payload,
                    active_validation=active_validation,
                    **request_parameters
        )


    # Alias Function
    def retrieve_tags_associated_with_network_devices(self,
                                                         limit=None,
                                                         offset=None,
                                                         headers=None,
                                                         **request_parameters):
        """ This function is an alias of retrieve_tags_associated_with_network_devices_v1 .
        Args:
            offset(int): offset query parameter. The first record to show for this page; the first record is
                numbered 1. minimum: 1 .
            limit(int): limit query parameter. The number of records to show for this page. minimum: 1, maximum: 500
                .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of retrieve_tags_associated_with_network_devices_v1 .
        """
        return self.retrieve_tags_associated_with_network_devices_v1(
                    limit=limit,
                    offset=offset,
                    headers=headers,
                    **request_parameters
        )


    # Alias Function
    def get_tag_member_count(self,
                                id,
                                member_type,
                                member_association_type=None,
                                headers=None,
                                **request_parameters):
        """ This function is an alias of get_tag_member_count_v1 .
        Args:
            id(str): id path parameter. Tag ID .
            member_type(str): memberType query parameter.
            member_association_type(str): memberAssociationType query parameter.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_tag_member_count_v1 .
        """
        return self.get_tag_member_count_v1(
                    id=id,
                    member_type=member_type,
                    member_association_type=member_association_type,
                    headers=headers,
                    **request_parameters
        )


    # Alias Function
    def query_the_tags_associated_with_interfaces(self,
                                                     ids=None,
                                                     headers=None,
                                                     payload=None,
                                                     active_validation=True,
                                                     **request_parameters):
        """ This function is an alias of query_the_tags_associated_with_interfaces_v1 .
        Args:
            ids(list): Tag's List of member ids (network device or interface), maximum 500 ids can be passed.  (list
                of strings).
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of query_the_tags_associated_with_interfaces_v1 .
        """
        return self.query_the_tags_associated_with_interfaces_v1(
                    ids=ids,
                    headers=headers,
                    payload=payload,
                    active_validation=active_validation,
                    **request_parameters
        )


    # Alias Function
    def update_tag_membership(self,
                                 memberToTags=None,
                                 memberType=None,
                                 headers=None,
                                 payload=None,
                                 active_validation=True,
                                 **request_parameters):
        """ This function is an alias of update_tag_membership_v1 .
        Args:
            memberToTags(object): Tag's memberToTags.
            memberType(string): Tag's memberType.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of update_tag_membership_v1 .
        """
        return self.update_tag_membership_v1(
                    memberToTags=memberToTags,
                    memberType=memberType,
                    headers=headers,
                    payload=payload,
                    active_validation=active_validation,
                    **request_parameters
        )


    # Alias Function
    def get_tag_count(self,
                         attribute_name=None,
                         name=None,
                         name_space=None,
                         size=None,
                         system_tag=None,
                         headers=None,
                         **request_parameters):
        """ This function is an alias of get_tag_count_v1 .
        Args:
            name(str): name query parameter.
            name_space(str): nameSpace query parameter.
            attribute_name(str): attributeName query parameter.
            size(str): size query parameter. size in kilobytes(KB) .
            system_tag(str): systemTag query parameter.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_tag_count_v1 .
        """
        return self.get_tag_count_v1(
                    attribute_name=attribute_name,
                    name=name,
                    name_space=name_space,
                    size=size,
                    system_tag=system_tag,
                    headers=headers,
                    **request_parameters
        )


    # Alias Function
    def update_tags_associated_with_the_interfaces(self,
                                                      headers=None,
                                                      payload=None,
                                                      active_validation=True,
                                                      **request_parameters):
        """ This function is an alias of update_tags_associated_with_the_interfaces_v1 .
        Args:
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of update_tags_associated_with_the_interfaces_v1 .
        """
        return self.update_tags_associated_with_the_interfaces_v1(
                    headers=headers,
                    payload=payload,
                    active_validation=active_validation,
                    **request_parameters
        )


    # Alias Function
    def add_members_to_the_tag(self,
                                  id,
                                  memberType=None,
                                  headers=None,
                                  payload=None,
                                  active_validation=True,
                                  **request_parameters):
        """ This function is an alias of add_members_to_the_tag_v1 .
        Args:
            memberType(list): Tag's memberType (list of strings).
            id(str): id path parameter. Tag ID .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of add_members_to_the_tag_v1 .
        """
        return self.add_members_to_the_tag_v1(
                    id=id,
                    memberType=memberType,
                    headers=headers,
                    payload=payload,
                    active_validation=active_validation,
                    **request_parameters
        )


    # Alias Function
    def get_tag_by_id(self,
                         id,
                         headers=None,
                         **request_parameters):
        """ This function is an alias of get_tag_by_id_v1 .
        Args:
            id(str): id path parameter. Tag ID .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_tag_by_id_v1 .
        """
        return self.get_tag_by_id_v1(
                    id=id,
                    headers=headers,
                    **request_parameters
        )



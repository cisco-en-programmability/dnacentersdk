# -*- coding: utf-8 -*-
"""Cisco Catalyst Center Cisco IMC API wrapper.

Copyright (c) 2025 Cisco Systems.

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


class CiscoIMC(object):
    """Cisco Catalyst Center Cisco IMC API (version: 3.1.3.0).

    Wraps the Catalyst Center Cisco IMC
    API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new CiscoIMC
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Catalyst Center service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(CiscoIMC, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def adds_cisco_i_m_c_configuration_to_a_catalyst_center_node(
        self,
        ipAddress=None,
        nodeId=None,
        password=None,
        username=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This API adds a Cisco Integrated Management Controller (IMC) configuration to a Cisco Catalyst Center node,
        identified by its `nodeId`. Obtain the `nodeId` from the `id` attribute in the response of the
        `/dna/intent/api/v1/nodes-config` API. The Cisco IMC configuration APIs enable the management of
        connections between Cisco IMC and Cisco Catalyst Center. By providing the Cisco IMC IP address and
        credentials to Catalyst Center, Catalyst Center can access and report the health status of hardware
        components within the Cisco appliance. More data about the Cisco IMC can be retrieved using the APIs
        exposed directly by Cisco IMC. Details are available in the Cisco IMC documentation
        https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-c-series-integrated-management-
        controller/series.html#~tab-documents The Cisco IMC configuration is relevant only for Catalyst Center
        deployments based on UCS appliances. In cases where Cisco IMC configuration is not supported by the
        deployment, these APIs will respond with a `404 Not Found` status code. When Cisco IMC configuration is
        supported, this API responds with the URL of a diagnostic task. .

        Args:
            ipAddress(string): Cisco IMC's IP address of the Cisco IMC .
            nodeId(string): Cisco IMC's The UUID that represents the Catalyst Center node. Its value can be obtained
                from the `id` attribute of the response of the `/dna/intent/api/v1/nodes-config` API. .
            password(string): Cisco IMC's Password of the Cisco IMC .
            username(string): Cisco IMC's Username of the Cisco IMC .
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
            https://developer.cisco.com/docs/dna-center/#!adds-cisco-i-m-c-configuration-to-a-catalyst-center-node
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = {
            "nodeId": nodeId,
            "ipAddress": ipAddress,
            "username": username,
            "password": password,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_d5f8cf25475dc5be53f35357aca5a4_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/system/api/v1/ciscoImcs"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(
                endpoint_full_url, params=_params, json=_payload, headers=_headers
            )
        else:
            json_data = self._session.post(
                endpoint_full_url, params=_params, json=_payload
            )

        return self._object_factory(
            "bpm_d5f8cf25475dc5be53f35357aca5a4_v3_1_3_0", json_data
        )

    def retrieves_cisco_i_m_c_configurations_for_catalyst_center_nodes(
        self, headers=None, **request_parameters
    ):
        """This API retrieves the configurations of the Cisco Integrated Management Controller (IMC) that have been added
        to the Catalyst Center nodes. The Cisco IMC configuration APIs enable the management of connections
        between Cisco IMC and Cisco Catalyst Center. By providing the Cisco IMC IP address and credentials to
        Catalyst Center, Catalyst Center can access and report the health status of hardware components within
        the Cisco appliance. More data about the Cisco IMC can be retrieved using the APIs exposed directly by
        Cisco IMC. Details are available in the Cisco IMC documentation
        https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-c-series-integrated-management-
        controller/series.html#~tab-documents The Cisco IMC configuration is relevant only for Catalyst Center
        deployments based on UCS appliances. In cases where Cisco IMC configuration is not supported by the
        deployment, these APIs will respond with a `404 Not Found` status code. .

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
            https://developer.cisco.com/docs/dna-center/#!retrieves-cisco-i-m-c-configurations-for-catalyst-center-nodes
        """
        check_type(headers, dict)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/system/api/v1/ciscoImcs"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_b7ed1910345a8b9b9ad88aeee4f109_v3_1_3_0", json_data
        )

    def deletes_the_cisco_i_m_c_configuration_for_a_catalyst_center_node(
        self, id, headers=None, **request_parameters
    ):
        """This API removes a specific Cisco Integrated Management Controller (IMC) configuration from a Catalyst Center
        node using the provided identifier. The Cisco IMC configuration APIs enable the management of
        connections between Cisco IMC and Cisco Catalyst Center. By providing the Cisco IMC IP address and
        credentials to Catalyst Center, Catalyst Center can access and report the health status of hardware
        components within the Cisco appliance. More data about the Cisco IMC can be retrieved using the APIs
        exposed directly by Cisco IMC. Details are available in the Cisco IMC documentation
        https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-c-series-integrated-management-
        controller/series.html#~tab-documents The Cisco IMC configuration is relevant only for Catalyst Center
        deployments based on UCS appliances. In cases where Cisco IMC configuration is not supported by the
        deployment, these APIs will respond with a `404 Not Found` status code. .

        Args:
            id(str): id path parameter. The unique identifier for this Cisco IMC configuration .
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
            https://developer.cisco.com/docs/dna-center/#!deletes-the-cisco-i-m-c-configuration-for-a-catalyst-center-node
        """
        check_type(headers, dict)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/system/api/v1/ciscoImcs/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_baa237a3253535e875c62928443888b_v3_1_3_0", json_data
        )

    def updates_the_cisco_i_m_c_configuration_for_a_catalyst_center_node(
        self,
        id,
        ipAddress=None,
        password=None,
        username=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This API updates the Cisco Integrated Management Controller (IMC) configuration for a Catalyst Center node,
        identified by the specified ID. The Cisco IMC configuration APIs enable the management of connections
        between Cisco IMC and Cisco Catalyst Center. By providing the Cisco IMC IP address and credentials to
        Catalyst Center, Catalyst Center can access and report the health status of hardware components within
        the Cisco appliance. More data about the Cisco IMC can be retrieved using the APIs exposed directly by
        Cisco IMC. Details are available in the Cisco IMC documentation
        https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-c-series-integrated-management-
        controller/series.html#~tab-documents The Cisco IMC configuration is relevant only for Catalyst Center
        deployments based on UCS appliances. In cases where Cisco IMC configuration is not supported by the
        deployment, these APIs will respond with a `404 Not Found` status code. When Cisco IMC configuration is
        supported, this API responds with the URL of a diagnostic task. .

        Args:
            ipAddress(string): Cisco IMC's IP address of the Cisco IMC .
            password(string): Cisco IMC's Password of the Cisco IMC .
            username(string): Cisco IMC's Username of the Cisco IMC .
            id(str): id path parameter. The unique identifier for this Cisco IMC configuration .
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
            https://developer.cisco.com/docs/dna-center/#!updates-the-cisco-i-m-c-configuration-for-a-catalyst-center-node
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }
        _payload = {
            "ipAddress": ipAddress,
            "username": username,
            "password": password,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_f2562a2d8e5ec287738032961762ed_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/system/api/v1/ciscoImcs/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(
                endpoint_full_url, params=_params, json=_payload, headers=_headers
            )
        else:
            json_data = self._session.put(
                endpoint_full_url, params=_params, json=_payload
            )

        return self._object_factory(
            "bpm_f2562a2d8e5ec287738032961762ed_v3_1_3_0", json_data
        )

    def retrieves_the_cisco_i_m_c_configuration_for_a_catalyst_center_node(
        self, id, headers=None, **request_parameters
    ):
        """This API retrieves the Cisco Integrated Management Controller (IMC) configuration for a Catalyst Center node,
        identified by the specified ID. The Cisco IMC configuration APIs enable the management of connections
        between Cisco IMC and Cisco Catalyst Center. By providing the Cisco IMC IP address and credentials to
        Catalyst Center, Catalyst Center can access and report the health status of hardware components within
        the Cisco appliance. More data about the Cisco IMC can be retrieved using the APIs exposed directly by
        Cisco IMC. Details are available in the Cisco IMC documentation
        https://www.cisco.com/c/en/us/support/servers-unified-computing/ucs-c-series-integrated-management-
        controller/series.html#~tab-documents The Cisco IMC configuration is relevant only for Catalyst Center
        deployments based on UCS appliances. In cases where Cisco IMC configuration is not supported by the
        deployment, these APIs will respond with a `404 Not Found` status code. .

        Args:
            id(str): id path parameter. The unique identifier for this Cisco IMC configuration .
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-the-cisco-i-m-c-configuration-for-a-catalyst-center-node
        """
        check_type(headers, dict)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/system/api/v1/ciscoImcs/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_afae98de597f918fe9d08045026c_v3_1_3_0", json_data
        )


# Alias Functions

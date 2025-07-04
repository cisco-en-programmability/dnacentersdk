# -*- coding: utf-8 -*-
"""Cisco Catalyst Center Industrial Configuration API wrapper.

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


class IndustrialConfiguration(object):
    """Cisco Catalyst Center Industrial Configuration API (version: 2.3.7.9).

    Wraps the Catalyst Center Industrial Configuration
    API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new IndustrialConfiguration
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Catalyst Center service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(IndustrialConfiguration, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def configure_are_p_ring_on_fabric_deployment(
        self,
        deploymentMode=None,
        ringName=None,
        rootNeighbourNetworkDeviceIds=None,
        rootNetworkDeviceId=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This API configures a REP ring on FABRIC deployment. The input payload contains the following fields ringName
        (unique ring name) , rootNetworkDeviceId (Network device ID of the root node of the REP Ring) and
        rootNeighbourNetworkDeviceIds (Network device IDs of the two immediate neighbour devices of the root
        node of the REP Ring). The networkDeviceId is the instanceUuid attribute in the response of API
        /dna/intent/api/v1/networkDevices. .

        Args:
            deploymentMode(string): Industrial Configuration's Deployment mode of the configured REP ring. .
                Available values are 'FABRIC' and 'NON_FABRIC'.
            ringName(string): Industrial Configuration's Unique name of REP ring to be configured. .
            rootNeighbourNetworkDeviceIds(list): Industrial Configuration's It contains the network device IDs of
                the immediate neighboring ring members of the root node. API
                `/dna/intent/api/v1/networkDevices` can be used to get the list of networkDeviceIds of
                the neighbors , `instanceUuid` attribute in the response contains
                rootNeighbourNetworkDeviceIds.  (list of strings).
            rootNetworkDeviceId(string): Industrial Configuration's rootNetworkDeviceId  is the network device ID of
                the root node in the REP ring. API `/dna/intent/api/v1/networkDevices` can be used to
                get the rootNetworkDeviceId , `instanceUuid` attribute in the response contains
                rootNetworkDeviceId. .
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
            https://developer.cisco.com/docs/dna-center/#!configure-a-r-e-p-ring-on-f-a-b-r-i-c-deployment
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
            "ringName": ringName,
            "rootNetworkDeviceId": rootNetworkDeviceId,
            "rootNeighbourNetworkDeviceIds": rootNeighbourNetworkDeviceIds,
            "deploymentMode": deploymentMode,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_f200dc9a10d25beab1243a5b29f99c7d_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/iot/fabric/repRings"
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
            "bpm_f200dc9a10d25beab1243a5b29f99c7d_v2_3_7_9", json_data
        )

    def delete_are_p_ring_configured_in_the_fabric_deployment(
        self, id, headers=None, **request_parameters
    ):
        """This API deletes the REP ring configured in the FABRIC deployment for the given id. The id of configured REP
        ring can be retrieved using the API /dna/intent/api/v1/iot/repRings/query.The taskid returned can be
        used to monitor the status of delete operation using following API -/intent/api/v1/task/{taskId}. .

        Args:
            id(str): id path parameter. Ring ID of configured REP ring can be fetched using the API
                `/dna/intent/api/v1/iot/repRings/query`. .
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
            https://developer.cisco.com/docs/dna-center/#!delete-r-e-p-ring-configured-in-the-f-a-b-r-i-c-deployment
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

        e_url = "/dna/intent/api/v1/iot/fabric/repRings/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_aca1b387f556ca0c87d563b3df8f2_v2_3_7_9", json_data
        )

    def retrieves_the_list_of_mrp_rings(
        self,
        network_device_id,
        id=None,
        limit=None,
        offset=None,
        headers=None,
        **request_parameters
    ):
        """This API returns the list of all the MRP rings configured on the Network device when Ring ID is not specified
        and returns the details of a single MRP ring when Ring ID is specified based on the given fields
        networkDeviceId (Network device ID of the MRP ring member. The networkDeviceId is the instanceUuid
        attribute in the response of API /dna/intent/api/v1/networkDevices) and id (ID of the MRP ring. The id
        of the configured MRP Ring can be retrieved using the API
        /dna/intent/api/v1/iot/networkDevices/${networkDeviceId}/mrpRings). .

        Args:
            network_device_id(str): networkDeviceId path parameter. Network device ID of the MRP ring member. .
            id(int): id query parameter. ID of the MRP ring. .
            offset(int): offset query parameter. The first record to show for this page; the first record is
                numbered 1. .
            limit(int): limit query parameter. The number of records to show for this page. .
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!retrieves-the-list-of-m-r-p-rings
        """
        check_type(headers, dict)
        check_type(id, int)
        check_type(offset, int)
        check_type(limit, int)
        check_type(network_device_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "id": id,
            "offset": offset,
            "limit": limit,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "networkDeviceId": network_device_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/iot/networkDevices/{networkDeviceId}/" + "mrpRings"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ef907f6fb75c9187c6377b24549af5_v2_3_7_9", json_data
        )

    def retrieves_the_count_of_mrp_rings(
        self, network_device_id, headers=None, **request_parameters
    ):
        """This API returns the count of MRP rings for the given fields networkDeviceId (Network device ID of the MRP ring
        member. The networkDeviceId is the instanceUuid attribute in the response of API
        /dna/intent/api/v1/networkDevices). .

        Args:
            network_device_id(str): networkDeviceId path parameter. Network device ID of the MRP ring member. .
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!retrieves-the-count-of-m-r-p-rings
        """
        check_type(headers, dict)
        check_type(network_device_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "networkDeviceId": network_device_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/iot/networkDevices/{networkDeviceId}/"
            + "mrpRings/count"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_f4d2ca417d50d7912fb8ea4a31662d_v2_3_7_9", json_data
        )

    def retrieves_the_list_of_network_devices_part_of_mrp_ring(
        self,
        id,
        network_device_id,
        limit=None,
        offset=None,
        headers=None,
        **request_parameters
    ):
        """This API returns the list of MRP ring members for the given fields networkDeviceId (Network device ID of the MRP
        ring member. The networkDeviceId is the instanceUuid attribute in the response of API
        /dna/intent/api/v1/networkDevices) and id (ID of the MRP ring. The id of the configured MRP Ring can be
        retrieved using the API /dna/intent/api/v1/iot/networkDevices/${networkDeviceId}/mrpRings). .

        Args:
            network_device_id(str): networkDeviceId path parameter. Network device ID of the MRP ring member. .
            id(int): id path parameter. ID of the MRP ring. .
            offset(int): offset query parameter. The first record to show for this page; the first record is
                numbered 1. .
            limit(int): limit query parameter. The number of records to show for this page. .
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!retrieves-the-list-of-network-devices-part-of-m-r-p-ring
        """
        check_type(headers, dict)
        check_type(offset, int)
        check_type(limit, int)
        check_type(network_device_id, str, may_be_none=False)
        check_type(id, int, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "offset": offset,
            "limit": limit,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "networkDeviceId": network_device_id,
            "id": id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/iot/networkDevices/{networkDeviceId}/"
            + "mrpRings/{id}/members"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_bf87f6cb9efb5451b84253593e548f98_v2_3_7_9", json_data
        )

    def retrieves_the_count_of_mrp_ring_members(
        self, id, network_device_id, headers=None, **request_parameters
    ):
        """This API returns the count of MRP ring members for the given fields networkDeviceId (Network device ID of the
        MRP ring member. The networkDeviceId is the instanceUuid attribute in the response of API
        /dna/intent/api/v1/networkDevices) and id (ID of the MRP ring. The id of the configured MRP Ring can be
        retrieved using the API /dna/intent/api/v1/iot/networkDevices/${networkDeviceId}/mrpRings). .

        Args:
            network_device_id(str): networkDeviceId path parameter. Network device ID of the MRP ring member. .
            id(int): id path parameter. ID of the MRP ring. .
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!retrieves-the-count-of-m-r-p-ring-members
        """
        check_type(headers, dict)
        check_type(network_device_id, str, may_be_none=False)
        check_type(id, int, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "networkDeviceId": network_device_id,
            "id": id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/iot/networkDevices/{networkDeviceId}/"
            + "mrpRings/{id}/members/count"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_bc1b3345f259e9859ac21a1ec694fe_v2_3_7_9", json_data
        )

    def configure_are_p_ring_on_non_fabric_deployment(
        self,
        deploymentMode=None,
        ringName=None,
        rootNeighbourNetworkDeviceIds=None,
        rootNetworkDeviceId=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This API configures a REP ring on NON-FABRIC deployment. The input payload contains the following fields
        ringName (unique ring name) , rootNetworkDeviceId (Network device ID of the root node of the REP Ring)
        and rootNeighbourNetworkDeviceIds (Network device IDs of the two immediate neighbour devices of the root
        node of the REP Ring). The networkDeviceId is the instanceUuid attribute in the response of API
        /dna/intent/api/v1/networkDevices. .

        Args:
            deploymentMode(string): Industrial Configuration's Deployment mode of the configured REP ring. .
                Available values are 'FABRIC' and 'NON_FABRIC'.
            ringName(string): Industrial Configuration's Unique name of REP ring to be configured. .
            rootNeighbourNetworkDeviceIds(list): Industrial Configuration's It contains the network device IDs of
                the immediate neighboring ring members of the root node. API
                `/dna/intent/api/v1/networkDevices` can be used to get the list of networkDeviceIds of
                the neighbors , `instanceUuid` attribute in the response contains
                rootNeighbourNetworkDeviceIds.  (list of strings).
            rootNetworkDeviceId(string): Industrial Configuration's rootNetworkDeviceId  is the network device ID of
                the root node in the REP ring. API `/dna/intent/api/v1/networkDevices` can be used to
                get the rootNetworkDeviceId , `instanceUuid` attribute in the response contains
                rootNetworkDeviceId. .
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
            https://developer.cisco.com/docs/dna-center/#!configure-a-r-e-p-ring-on-n-o-n-f-a-b-r-i-c-deployment
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
            "ringName": ringName,
            "rootNetworkDeviceId": rootNetworkDeviceId,
            "rootNeighbourNetworkDeviceIds": rootNeighbourNetworkDeviceIds,
            "deploymentMode": deploymentMode,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_bbc4dab8193c546ab116e19863dff621_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/iot/nonFabric/repRings"
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
            "bpm_bbc4dab8193c546ab116e19863dff621_v2_3_7_9", json_data
        )

    def delete_are_p_ring_configured_in_the_non_fabric_deployment(
        self, id, headers=None, **request_parameters
    ):
        """This API deletes the REP ring configured in the NON-FABRIC deployment for the given id. The id of configured REP
        ring can be retrieved using the API /dna/intent/api/v1/iot/repRings/query.The taskid returned can be
        used to monitor the status of delete operation using following API -/intent/api/v1/task/{taskId}. .

        Args:
            id(str): id path parameter. Ring ID of configured REP ring can be fetched using the API
                `/dna/intent/api/v1/iot/repRings/query`. .
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
            https://developer.cisco.com/docs/dna-center/#!delete-r-e-p-ring-configured-in-the-n-o-n-f-a-b-r-i-c-deployment
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

        e_url = "/dna/intent/api/v1/iot/nonFabric/repRings/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_dcf9b8fecdd57f0bb7a33d358e6be37_v2_3_7_9", json_data
        )

    def retrieves_the_list_of_are_p_rings(
        self,
        deploymentMode=None,
        limit=None,
        networkDeviceId=None,
        offset=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This API returns the list of REP rings for the given fields networkDeviceId (Network device ID of the REP ring
        member. In case of successful REP ring creation, any of the REP ring member networkDeviceId can be
        provided. In case of failed REP ring creation, provide only root node networkDeviceId. The
        networkDeviceId is the instanceUuid attribute in the response of API /dna/intent/api/v1/networkDevice)
        and deploymentMode (FABRIC/NON_FABRIC). .

        Args:
            deploymentMode(string): Industrial Configuration's Deployment mode of the configured REP ring. .
                Available values are 'FABRIC' and 'NON_FABRIC'.
            limit(integer): Industrial Configuration's The number of records to show for this page. .
            networkDeviceId(string): Industrial Configuration's Network device id of the REP ring member. API
                `/dna/intent/api/v1/networkDevices` can be used to get the list of networkDeviceIds of
                the neighbors , `instanceUuid` attribute in the response contains networkDeviceId. .
            offset(integer): Industrial Configuration's The first record to show for this page; the first record is
                numbered 1. .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(dict): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            list: JSON response. A list of MyDict objects.
            Access the object's properties by using the dot notation
            or the bracket notation.

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!retrieves-the-list-of-r-e-p-rings
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
            "networkDeviceId": networkDeviceId,
            "deploymentMode": deploymentMode,
            "limit": limit,
            "offset": offset,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_fa2127b55124a3a00b2991b77db6_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/iot/repRings/query"
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
            "bpm_fa2127b55124a3a00b2991b77db6_v2_3_7_9", json_data
        )

    def retrieves_the_count_of_are_p_rings(
        self,
        deploymentMode=None,
        networkDeviceId=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This API returns the count of REP rings for the given fields networkDeviceId (Network device ID of the REP ring
        member. The networkDeviceId is the instanceUuid attribute in the response of API
        /dna/intent/api/v1/networkDevices) and deploymentMode (FABRIC/NON_FABRIC). .

        Args:
            deploymentMode(string): Industrial Configuration's Deployment mode of the configured REP ring. .
                Available values are 'FABRIC' and 'NON_FABRIC'.
            networkDeviceId(string): Industrial Configuration's Network device id of the REP ring member. API
                `/dna/intent/api/v1/networkDevices` can be used to get the list of networkDeviceIds of
                the neighbors , `instanceUuid` attribute in the response contains networkDeviceId. .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(dict): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            list: JSON response. A list of MyDict objects.
            Access the object's properties by using the dot notation
            or the bracket notation.

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!retrieves-the-count-of-r-e-p-rings
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
            "networkDeviceId": networkDeviceId,
            "deploymentMode": deploymentMode,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_d9f276a532e5eeb86bb591f8537fcc7_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/iot/repRings/query/count"
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
            "bpm_d9f276a532e5eeb86bb591f8537fcc7_v2_3_7_9", json_data
        )

    def get_the_are_p_ring_based_on_the_ring_id(
        self, id, headers=None, **request_parameters
    ):
        """This API returns REP ring for the given id (The id of configured REP ring can be retrieved using the API
        /dna/intent/api/v1/iot/repRings/query). .

        Args:
            id(str): id path parameter. Ring ID of configured REP ring can be fetched using the API
                `/dna/intent/api/v1/iot/repRings/query`. .
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
            ApiError: If the Catalyst Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!get-the-r-e-p-ring-based-on-the-ring-id
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

        e_url = "/dna/intent/api/v1/iot/repRings/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ce1469c515d8a72455779e3a484_v2_3_7_9", json_data
        )


# Alias Functions

# -*- coding: utf-8 -*-
"""Cisco Catalyst Center Configuration Archive API wrapper.

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


class ConfigurationArchive(object):
    """Cisco Catalyst Center Configuration Archive API (version: 3.1.3.0).

    Wraps the Catalyst Center Configuration Archive
    API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new ConfigurationArchive
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Catalyst Center service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(ConfigurationArchive, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def export_device_configurations(
        self,
        deviceId=None,
        password=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Export Device configuration for every device that is provided will be included in an encrypted zip file. .

        Args:
            deviceId(list): Configuration Archive's UUIDs of the devices for which configurations need to be
                exported.  (list of strings).
            password(string): Configuration Archive's Password for the zip file to protect exported configurations.
                Must contain, at minimum 8 characters, one lowercase letter, one uppercase letter, one
                number, one special character(-=[];,./~!@#$%^&*()_+{}|:?). It may not contain white
                space or the characters <>. .
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
            https://developer.cisco.com/docs/dna-center/#!export-device-configurations
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
            "deviceId": deviceId,
            "password": password,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_e85b40c5ca055f4c82281617a8f95644_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/network-device-archive/cleartext"
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
            "bpm_e85b40c5ca055f4c82281617a8f95644_v3_1_3_0", json_data
        )

    def get_configuration_archive_details(
        self,
        created_by=None,
        created_time=None,
        device_id=None,
        file_type=None,
        limit=None,
        offset=None,
        headers=None,
        **request_parameters
    ):
        """Returns the historical device configurations (running configuration , startup configuration , vlan if
        applicable) by specified criteria .

        Args:
            device_id(str): deviceId query parameter. comma separated device id for example
                cf35b0a1-407f-412f-b2f4-f0c3156695f9,aaa38191-0c22-4158-befd-779a09d7cec1 . if device id
                is not provided it will fetch for all devices .
            file_type(str): fileType query parameter. Config File Type can be RUNNINGCONFIG or STARTUPCONFIG .
            created_time(str): createdTime query parameter. Supported with logical filters GT,GTE,LT,LTE & BT : time
                in milliseconds (epoc format) .
            created_by(str): createdBy query parameter. Comma separated values for createdBy SCHEDULED, USER,
                CONFIG_CHANGE_EVENT, SCHEDULED_FIRST_TIME, DR_CALL_BACK, PRE_DEPLOY .
            offset(int): offset query parameter.
            limit(int): limit query parameter. The number of records to be retrieved defaults to 500 if not
                specified, with a maximum allowed limit of 500. .
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
            https://developer.cisco.com/docs/dna-center/#!get-configuration-archive-details
        """
        check_type(headers, dict)
        check_type(device_id, str)
        check_type(file_type, str)
        check_type(created_time, str)
        check_type(created_by, str)
        check_type(offset, int)
        check_type(limit, int)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "deviceId": device_id,
            "fileType": file_type,
            "createdTime": created_time,
            "createdBy": created_by,
            "offset": offset,
            "limit": limit,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/network-device-config"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ff699112d3854d99557dc1f48987f09_v3_1_3_0", json_data
        )

    def get_network_device_configuration_file_details(
        self,
        file_type=None,
        id=None,
        limit=None,
        network_device_id=None,
        offset=None,
        headers=None,
        **request_parameters
    ):
        """Retrieves the list of network device configuration file details, sorted by createdTime in descending order. Use
        /intent/api/v1/networkDeviceConfigFiles/{id}/downloadMasked to download masked configurations, or
        /intent/api/v1/networkDeviceConfigFiles/{id}/downloadUnmasked for unmasked configurations. .

        Args:
            id(str): id query parameter. Unique identifier (UUID) of the configuration file. .
            network_device_id(str): networkDeviceId query parameter. Unique identifier (UUID) of the network
                devices. The number of networkDeviceId(s) must not exceed 5. .
            file_type(str): fileType query parameter. Type of device configuration file.Available values :
                'RUNNINGCONFIG', 'STARTUPCONFIG', 'VLAN' .
            offset(int): offset query parameter. The first record to show for this page; the first record is
                numbered 1. .
            limit(int): limit query parameter. The number of records to be retrieved defaults to 500 if not
                specified, with a maximum allowed limit of 500. .
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
            https://developer.cisco.com/docs/dna-center/#!get-network-device-configuration-file-details
        """
        check_type(headers, dict)
        check_type(id, str)
        check_type(network_device_id, str)
        check_type(file_type, str)
        check_type(offset, int)
        check_type(limit, int)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "id": id,
            "networkDeviceId": network_device_id,
            "fileType": file_type,
            "offset": offset,
            "limit": limit,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/networkDeviceConfigFiles"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c07ca5c25f5084ae4148ce8b1ce940_v3_1_3_0", json_data
        )

    def count_of_network_device_configuration_files(
        self,
        file_type=None,
        id=None,
        network_device_id=None,
        headers=None,
        **request_parameters
    ):
        """Retrieves count the details of the network device configuration files. .

        Args:
            id(str): id query parameter. Unique identifier (UUID) of the configuration file. .
            network_device_id(str): networkDeviceId query parameter. Unique identifier (UUID) of the network
                devices. The number of networkDeviceId(s) must not exceed 5. .
            file_type(str): fileType query parameter. Type of device configuration file. Available values :
                'RUNNINGCONFIG', 'STARTUPCONFIG', 'VLAN' .
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
            https://developer.cisco.com/docs/dna-center/#!count-of-network-device-configuration-files
        """
        check_type(headers, dict)
        check_type(id, str)
        check_type(network_device_id, str)
        check_type(file_type, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "id": id,
            "networkDeviceId": network_device_id,
            "fileType": file_type,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/networkDeviceConfigFiles/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_af5e273c15f6abc150e9328e4d070_v3_1_3_0", json_data
        )

    def get_configuration_file_details_by_id(
        self, id, headers=None, **request_parameters
    ):
        """Retrieves the details of a specific network device configuration file using the `id`. .

        Args:
            id(str): id path parameter. The value of `id` can be obtained from the response of API
                `/dna/intent/api/v1/networkDeviceConfigFiles` .
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
            https://developer.cisco.com/docs/dna-center/#!get-configuration-file-details-by-i-d
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

        e_url = "/dna/intent/api/v1/networkDeviceConfigFiles/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_e8878000b5e5810be1b2630e70a5118_v3_1_3_0", json_data
        )

    def download_masked_device_configuration(
        self, id, headers=None, **request_parameters
    ):
        """Download the masked (sanitized) device configuration by providing the file `id`. .

        Args:
            id(str): id path parameter. The value of `id` can be obtained from the response of API
                `/dna/intent/api/v1/networkDeviceConfigFiles` .
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
            https://developer.cisco.com/docs/dna-center/#!download-masked-device-configuration
        """
        check_type(headers, dict)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
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

        e_url = "/dna/intent/api/v1/networkDeviceConfigFiles/{id}/downloa" + "dMasked"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.post(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_fe0e28b3465084b5ee60a43602be1c_v3_1_3_0", json_data
        )

    def download_unmaskedraw_device_configuration_as_zip(
        self,
        id,
        password=None,
        dirpath=None,
        save_file=None,
        filename=None,
        headers=None,
        payload=None,
        **request_parameters
    ):
        """Download the unmasked (raw) device configuration by providing the file `id` and a `password`. The response will
        be a password-protected zip file containing the unmasked configuration. Password must contain a minimum
        of 8 characters, one lowercase letter, one uppercase letter, one number, one special character
        (`-=[];,./~!@#$%^&*()_+{}|:?`). It may not contain white space or the characters `<>`. .

        Args:
            password(string): Configuration Archive's Password for the zip file to protect exported configurations.
                Must contain, at minimum 8 characters, one lowercase letter, one uppercase letter, one
                number, one special character(-=[];,./~!@#$%^&*()_+{}|:?). It may not contain white
                space or the characters <>. .
            id(str): id path parameter. The value of `id` can be obtained from the response of API
                `/dna/intent/api/v1/networkDeviceConfigFiles` .
            dirpath(str): Directory absolute path. Defaults to os.getcwd().
            save_file(bool): Enable or disable automatic file creation of
                raw response.
            filename(str): The filename used to save the download file.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(dict): A JSON serializable Python object to send in the
                body of the Request.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            DownloadResponse: The DownloadResponse wrapper. Wraps the urllib3.response.HTTPResponse. For more
            information check the `urlib3 documentation <https://urllib3.readthedocs.io/en/latest/reference/urllib3.response.html>`_

        Raises:
            TypeError: If the parameter types are incorrect.
            MalformedRequest: If the request body created is invalid.
            ApiError: If the Catalyst Center cloud returns an error.
            DownloadFailure: If was not able to download the raw
            response to a file.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!download-unmaskedraw-device-configuration-as-z-i-p
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
        }
        _payload = {
            "password": password,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/networkDeviceConfigFiles/{id}/downloa" + "dUnmasked"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(
                endpoint_full_url,
                params=_params,
                json=_payload,
                headers=_headers,
                stream=True,
                dirpath=dirpath,
                save_file=save_file,
                filename=filename,
            )
        else:
            json_data = self._session.post(
                endpoint_full_url,
                params=_params,
                json=_payload,
                stream=True,
                dirpath=dirpath,
                save_file=save_file,
                filename=filename,
            )

        return self._object_factory(
            "bpm_d8fcd6dbb7ff53b58f7398c49b27ded2_v3_1_3_0", json_data
        )

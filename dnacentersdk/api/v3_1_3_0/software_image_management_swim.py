# -*- coding: utf-8 -*-
"""Cisco Catalyst Center Software Image Management (SWIM) API wrapper.

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


class SoftwareImageManagementSwim(object):
    """Cisco Catalyst Center Software Image Management (SWIM) API (version: 3.1.3.0).

    Wraps the Catalyst Center Software Image Management (SWIM)
    API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new SoftwareImageManagementSwim
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Catalyst Center service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(SoftwareImageManagementSwim, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def trigger_software_image_activation(
        self,
        schedule_validate=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Activates a software image on a given device. Software image must be present in the device flash .

        Args:
            schedule_validate(bool): scheduleValidate query parameter. scheduleValidate, validates data before
                schedule (Optional) .
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
            https://developer.cisco.com/docs/dna-center/#!trigger-software-image-activation
        """
        check_type(headers, dict)
        check_type(payload, list)
        check_type(schedule_validate, bool)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "Client-Type" in headers:
                check_type(headers.get("Client-Type"), str)
            if "Client-Url" in headers:
                check_type(headers.get("Client-Url"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "scheduleValidate": schedule_validate,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = payload or []
        if active_validation:
            self._request_validator(
                "jsd_a9136d5513985f15e91a19da66c_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/image/activation/device"
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
            "bpm_a9136d5513985f15e91a19da66c_v3_1_3_0", json_data
        )

    def trigger_software_image_distribution(
        self, headers=None, payload=None, active_validation=True, **request_parameters
    ):
        """Distributes a software image on a given device. Software image must be imported successfully into Catalyst Center
        before it can be distributed .

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
            https://developer.cisco.com/docs/dna-center/#!trigger-software-image-distribution
        """
        check_type(headers, dict)
        check_type(payload, list)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = payload or []
        if active_validation:
            self._request_validator(
                "jsd_c8d11fb9fc752ab8bb8e2b1413ccc92_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/image/distribution"
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
            "bpm_c8d11fb9fc752ab8bb8e2b1413ccc92_v3_1_3_0", json_data
        )

    def get_software_image_details(
        self,
        application_type=None,
        created_time=None,
        family=None,
        image_integrity_status=None,
        image_name=None,
        image_series=None,
        image_size_greater_than=None,
        image_size_lesser_than=None,
        image_uuid=None,
        is_cco_latest=None,
        is_cco_recommended=None,
        is_tagged_golden=None,
        limit=None,
        name=None,
        offset=None,
        sort_by=None,
        sort_order=None,
        version=None,
        headers=None,
        **request_parameters
    ):
        """Returns software image list based on a filter criteria. For example: "filterbyName = cat3k%" .

        Args:
            image_uuid(str): imageUuid query parameter.
            name(str): name query parameter.
            family(str): family query parameter.
            application_type(str): applicationType query parameter.
            image_integrity_status(str): imageIntegrityStatus query parameter. imageIntegrityStatus FAILURE,
                UNKNOWN, VERIFIED .
            version(str): version query parameter. software Image Version .
            image_series(str): imageSeries query parameter. image Series .
            image_name(str): imageName query parameter. image Name .
            is_tagged_golden(bool): isTaggedGolden query parameter. is Tagged Golden .
            is_cco_recommended(bool): isCCORecommended query parameter. is recommended from cisco.com .
            is_cco_latest(bool): isCCOLatest query parameter. is latest from cisco.com .
            created_time(int): createdTime query parameter. time in milliseconds (epoch format) .
            image_size_greater_than(int): imageSizeGreaterThan query parameter. size in bytes .
            image_size_lesser_than(int): imageSizeLesserThan query parameter. size in bytes .
            sort_by(str): sortBy query parameter. sort results by this field .
            sort_order(str): sortOrder query parameter. sort order 'asc' or 'des'. Default is asc .
            limit(int): limit query parameter.
            offset(int): offset query parameter.
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
            https://developer.cisco.com/docs/dna-center/#!get-software-image-details
        """
        check_type(headers, dict)
        check_type(image_uuid, str)
        check_type(name, str)
        check_type(family, str)
        check_type(application_type, str)
        check_type(image_integrity_status, str)
        check_type(version, str)
        check_type(image_series, str)
        check_type(image_name, str)
        check_type(is_tagged_golden, bool)
        check_type(is_cco_recommended, bool)
        check_type(is_cco_latest, bool)
        check_type(created_time, int)
        check_type(image_size_greater_than, int)
        check_type(image_size_lesser_than, int)
        check_type(sort_by, str)
        check_type(sort_order, str)
        check_type(limit, int)
        check_type(offset, int)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "imageUuid": image_uuid,
            "name": name,
            "family": family,
            "applicationType": application_type,
            "imageIntegrityStatus": image_integrity_status,
            "version": version,
            "imageSeries": image_series,
            "imageName": image_name,
            "isTaggedGolden": is_tagged_golden,
            "isCCORecommended": is_cco_recommended,
            "isCCOLatest": is_cco_latest,
            "createdTime": created_time,
            "imageSizeGreaterThan": image_size_greater_than,
            "imageSizeLesserThan": image_size_lesser_than,
            "sortBy": sort_by,
            "sortOrder": sort_order,
            "limit": limit,
            "offset": offset,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/image/importation"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_f73101d5d5e409f571084ab4c6049_v3_1_3_0", json_data
        )

    def get_device_family_identifiers(self, headers=None, **request_parameters):
        """API to get Device Family Identifiers for all Device Families that can be used for tagging an image golden. .

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
            https://developer.cisco.com/docs/dna-center/#!get-device-family-identifiers
        """
        check_type(headers, dict)
        if headers is not None:
            if "Accept" in headers:
                check_type(headers.get("Accept"), str)
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

        e_url = "/dna/intent/api/v1/image/importation/device-family-" + "identifiers"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_b5c47f316ff058eb979bdea047f9d5b5_v3_1_3_0", json_data
        )

    def tag_as_golden_image(
        self,
        deviceFamilyIdentifier=None,
        deviceRole=None,
        imageId=None,
        siteId=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Golden Tag image. Set siteId as -1 for Global site. .

        Args:
            deviceFamilyIdentifier(string): Software Image Management (SWIM)'s Device Family Identifier e.g. :
                277696480-283933147, 277696480 .
            deviceRole(string): Software Image Management (SWIM)'s Device Role. Permissible Values : ALL, UNKNOWN,
                ACCESS, BORDER ROUTER, DISTRIBUTION and CORE. .
            imageId(string): Software Image Management (SWIM)'s imageId in uuid format. .
            siteId(string): Software Image Management (SWIM)'s SiteId in uuid format. For Global Site "-1" to be
                used. .
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
            https://developer.cisco.com/docs/dna-center/#!tag-as-golden-image
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if "Accept" in headers:
                check_type(headers.get("Accept"), str)
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = {
            "imageId": imageId,
            "siteId": siteId,
            "deviceRole": deviceRole,
            "deviceFamilyIdentifier": deviceFamilyIdentifier,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_a9b864257b965fe4bd8b0293f41f1537_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/image/importation/golden"
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
            "bpm_a9b864257b965fe4bd8b0293f41f1537_v3_1_3_0", json_data
        )

    def remove_golden_tag_for_image(
        self,
        device_family_identifier,
        device_role,
        image_id,
        site_id,
        headers=None,
        **request_parameters
    ):
        """Remove golden tag. Set siteId as -1 for Global site. .

        Args:
            site_id(str): siteId path parameter. Site Id in uuid format. Set siteId as -1 for Global site. .
            device_family_identifier(str): deviceFamilyIdentifier path parameter. Device family identifier e.g. :
                277696480-283933147, e.g. : 277696480 .
            device_role(str): deviceRole path parameter. Device Role. Permissible Values : ALL, UNKNOWN, ACCESS,
                BORDER ROUTER, DISTRIBUTION and CORE. .
            image_id(str): imageId path parameter. Image Id in uuid format. .
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
            https://developer.cisco.com/docs/dna-center/#!remove-golden-tag-for-image
        """
        check_type(headers, dict)
        check_type(site_id, str, may_be_none=False)
        check_type(device_family_identifier, str, may_be_none=False)
        check_type(device_role, str, may_be_none=False)
        check_type(image_id, str, may_be_none=False)
        if headers is not None:
            if "Accept" in headers:
                check_type(headers.get("Accept"), str)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "siteId": site_id,
            "deviceFamilyIdentifier": device_family_identifier,
            "deviceRole": device_role,
            "imageId": image_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/image/importation/golden/site/{siteId"
            + "}/family/{deviceFamilyIdentifier}/role/{deviceRole}/imag"
            + "e/{imageId}"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_e9dd960c5378ab442f235c8135d0_v3_1_3_0", json_data
        )

    def get_golden_tag_status_of_an_image(
        self,
        device_family_identifier,
        device_role,
        image_id,
        site_id,
        headers=None,
        **request_parameters
    ):
        """Get golden tag status of an image. Set siteId as -1 for Global site. .

        Args:
            site_id(str): siteId path parameter. Site Id in uuid format. Set siteId as -1 for Global site. .
            device_family_identifier(str): deviceFamilyIdentifier path parameter. Device family identifier e.g. :
                277696480-283933147, e.g. : 277696480 .
            device_role(str): deviceRole path parameter. Device Role. Permissible Values : ALL, UNKNOWN, ACCESS,
                BORDER ROUTER, DISTRIBUTION and CORE. .
            image_id(str): imageId path parameter. Image Id in uuid format. .
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
            https://developer.cisco.com/docs/dna-center/#!get-golden-tag-status-of-an-image
        """
        check_type(headers, dict)
        check_type(site_id, str, may_be_none=False)
        check_type(device_family_identifier, str, may_be_none=False)
        check_type(device_role, str, may_be_none=False)
        check_type(image_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "siteId": site_id,
            "deviceFamilyIdentifier": device_family_identifier,
            "deviceRole": device_role,
            "imageId": image_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/image/importation/golden/site/{siteId"
            + "}/family/{deviceFamilyIdentifier}/role/{deviceRole}/imag"
            + "e/{imageId}"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ab6266cac654d394cf943a161fcc7b_v3_1_3_0", json_data
        )

    def import_local_software_image(
        self,
        multipart_fields,
        multipart_monitor_callback,
        is_third_party=None,
        third_party_application_type=None,
        third_party_image_family=None,
        third_party_vendor=None,
        headers=None,
        **request_parameters
    ):
        """Fetches a software image from local file system and uploads to Catalyst Center. Supported software image files
        extensions are bin, img, tar, smu, pie, aes, iso, ova, tar_gz and qcow2 .

        The following code gives an example of the multipart_fields.

        .. code-block:: python

            multipart_fields={'file': ('file.zip', open('file.zip', 'rb')}
            multipart_fields={'file': ('file.txt', open('file.txt', 'rb'),
                'text/plain',
                {'X-My-Header': 'my-value'})}
            multipart_fields=[('images', ('foo.png', open('foo.png', 'rb'),
                'image/png')),
                ('images', ('bar.png', open('bar.png', 'rb'), 'image/png'))]

        The following example demonstrates how to use
        `multipart_monitor_callback=create_callback` to create a progress bar
        using clint.

        .. code-block:: python

            from clint.textui.progress import Bar
            def create_callback(encoder):
                encoder_len = encoder.len
                bar = Bar(expected_size=encoder_len,
                          filled_char="=")
                def callback(monitor):
                    bar.show(monitor.bytes_read)
                return callback

        Args:
            is_third_party(bool): isThirdParty query parameter. Third party Image check .
            third_party_vendor(str): thirdPartyVendor query parameter. Third Party Vendor .
            third_party_image_family(str): thirdPartyImageFamily query parameter. Third Party image family .
            third_party_application_type(str): thirdPartyApplicationType query parameter. Third Party Application
                Type .
            multipart_fields(dict): Fields from which to create a
                multipart/form-data body.
            multipart_monitor_callback(function): function used to monitor
                the progress of the upload.
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
            https://developer.cisco.com/docs/dna-center/#!import-local-software-image
        """
        check_type(headers, dict)
        check_type(is_third_party, bool)
        check_type(third_party_vendor, str)
        check_type(third_party_image_family, str)
        check_type(third_party_application_type, str)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "isThirdParty": is_third_party,
            "thirdPartyVendor": third_party_vendor,
            "thirdPartyImageFamily": third_party_image_family,
            "thirdPartyApplicationType": third_party_application_type,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/image/importation/source/file"
        endpoint_full_url = apply_path_params(e_url, path_params)
        m_data = self._session.multipart_data(
            multipart_fields, multipart_monitor_callback
        )
        _headers.update(
            {
                "Content-Type": m_data.content_type,
                "Content-Length": str(m_data.len),
                "Connection": "keep-alive",
            }
        )
        with_custom_headers = True
        if with_custom_headers:
            json_data = self._session.post(
                endpoint_full_url, params=_params, data=m_data, headers=_headers
            )
        else:
            json_data = self._session.post(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c1cf6d5d5f0fa2e92539134b6c1d_v3_1_3_0", json_data
        )

    def import_software_image_via_url(
        self,
        schedule_at=None,
        schedule_desc=None,
        schedule_origin=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Fetches a software image from remote file system (using URL for HTTP/FTP) and uploads to Catalyst Center. Supported
        image files extensions are bin, img, tar, smu, pie, aes, iso, ova, tar_gz and qcow2 .

        Args:
            schedule_at(str): scheduleAt query parameter. Epoch Time (The number of milli-seconds since January 1
                1970 UTC) at which the distribution should be scheduled (Optional) .
            schedule_desc(str): scheduleDesc query parameter. Custom Description (Optional) .
            schedule_origin(str): scheduleOrigin query parameter. Originator of this call (Optional) .
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
            https://developer.cisco.com/docs/dna-center/#!import-software-image-via-u-r-l
        """
        check_type(headers, dict)
        check_type(payload, list)
        check_type(schedule_at, str)
        check_type(schedule_desc, str)
        check_type(schedule_origin, str)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "scheduleAt": schedule_at,
            "scheduleDesc": schedule_desc,
            "scheduleOrigin": schedule_origin,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = payload or []
        if active_validation:
            self._request_validator(
                "jsd_be8cdb967555fcca03a4c1f796eee56_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/image/importation/source/url"
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
            "bpm_be8cdb967555fcca03a4c1f796eee56_v3_1_3_0", json_data
        )

    def returns_list_of_software_images(
        self,
        golden=None,
        has_addon_images=None,
        imported=None,
        integrity=None,
        is_addon_images=None,
        limit=None,
        name=None,
        offset=None,
        product_name_ordinal=None,
        site_id=None,
        supervisor_product_name_ordinal=None,
        version=None,
        headers=None,
        **request_parameters
    ):
        """A list of available images for the specified site is provided. The default value of the site is set to global.
        The list includes images that have been imported onto the disk, as well as the latest and suggested
        images from Cisco.com. .

        Args:
            site_id(str): siteId query parameter. Site identifier to get the list of all available products under
                the site. The default value is the global site.  See
                https://developer.cisco.com/docs/dna-center/get-site for `siteId` .
            product_name_ordinal(int): productNameOrdinal query parameter. The product name ordinal is a unique
                value for each network device product. The productNameOrdinal can be obtained from the
                response of API `/dna/intent/api/v1/siteWiseProductNames` .
            supervisor_product_name_ordinal(int): supervisorProductNameOrdinal query parameter. The supervisor
                engine module ordinal is a unique value for each supervisor module. The
                `supervisorProductNameOrdinal` can be obtained from the response of API
                `/dna/intent/api/v1/siteWiseProductNames` .
            imported(bool): imported query parameter. When the value is set to `true`, it will include physically
                imported images. Conversely, when the value is set to `false`, it will include image
                records from the cloud. The identifier for cloud images can be utilized to download
                images from Cisco.com to the disk. .
            name(str): name query parameter. Filter with software image or add-on name. Supports partial case-
                insensitive search. A minimum of 3 characters is required for the search. .
            version(str): version query parameter. Filter with image version. Supports partial case-insensitive
                search. A minimum of 3 characters is required for the search. .
            golden(bool): golden query parameter. When set to `true`, it will retrieve the images marked as tagged
                golden. When set to `false`, it will retrieve the images marked as not tagged golden. .
            integrity(str): integrity query parameter. Filter with verified images using Integrity Verification
                Available values: UNKNOWN, VERIFIED .
            has_addon_images(bool): hasAddonImages query parameter. When set to `true`, it will retrieve the images
                which have add-on images. When set to `false`, it will retrieve the images which do not
                have add-on images. .
            is_addon_images(bool): isAddonImages query parameter. When set to `true`, it will retrieve the images
                that an add-on image.  When set to `false`, it will retrieve the images that are not
                add-on images .
            offset(int): offset query parameter. The first record to show for this page; the first record is
                numbered 1. The minimum value is 1. .
            limit(int): limit query parameter. The number of records to show for this page. The minimum and maximum
                values are 1 and 500, respectively. .
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
            https://developer.cisco.com/docs/dna-center/#!returns-list-of-software-images
        """
        check_type(headers, dict)
        check_type(site_id, str)
        check_type(product_name_ordinal, int)
        check_type(supervisor_product_name_ordinal, int)
        check_type(imported, bool)
        check_type(name, str)
        check_type(version, str)
        check_type(golden, bool)
        check_type(integrity, str)
        check_type(has_addon_images, bool)
        check_type(is_addon_images, bool)
        check_type(offset, int)
        check_type(limit, int)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "siteId": site_id,
            "productNameOrdinal": product_name_ordinal,
            "supervisorProductNameOrdinal": supervisor_product_name_ordinal,
            "imported": imported,
            "name": name,
            "version": version,
            "golden": golden,
            "integrity": integrity,
            "hasAddonImages": has_addon_images,
            "isAddonImages": is_addon_images,
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

        e_url = "/dna/intent/api/v1/images"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_eb239c565c57d59cd6d6f7d193a993_v3_1_3_0", json_data
        )

    def initiates_sync_of_software_images_from_cisco_com(
        self, headers=None, **request_parameters
    ):
        """Initiating the synchronization of the software images from Cisco.com. The latest and suggested images will be
        retrieved, along with the corresponding product name and PIDs for imported and retrieved images from
        Cisco.com. Once the task is completed, the API `/intent/api/v1/images?imported=false` will display all
        the images fetched from Cisco.com. .

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
            https://developer.cisco.com/docs/dna-center/#!initiates-sync-of-software-images-from-cisco-com
        """
        check_type(headers, dict)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
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

        e_url = "/dna/intent/api/v1/images/ccoSync"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.post(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_febee79ae42f5ae481d85e3e5ad6fac8_v3_1_3_0", json_data
        )

    def returns_count_of_software_images(
        self,
        golden=None,
        has_addon_images=None,
        imported=None,
        integrity=None,
        is_addon_images=None,
        name=None,
        product_name_ordinal=None,
        site_id=None,
        supervisor_product_name_ordinal=None,
        version=None,
        headers=None,
        **request_parameters
    ):
        """Returns the count of software images for given `siteId`. The default value of siteId is global .

        Args:
            site_id(str): siteId query parameter. Site identifier to get the list of all available products under
                the site. The default value is the global site.  See
                https://developer.cisco.com/docs/dna-center/get-site for siteId .
            product_name_ordinal(int): productNameOrdinal query parameter. The product name ordinal is a unique
                value for each network device product. The productNameOrdinal can be obtained from the
                response of the API `/dna/intent/api/v1/siteWiseProductNames`. .
            supervisor_product_name_ordinal(int): supervisorProductNameOrdinal query parameter. The supervisor
                engine module ordinal is a unique value for each supervisor module. The
                `supervisorProductNameOrdinal` can be obtained from the response of API
                `/dna/intent/api/v1/siteWiseProductNames` .
            imported(bool): imported query parameter. When the value is set to `true`, it will include physically
                imported images. Conversely, when the value is set to `false`, it will include image
                records from the cloud. The identifier for cloud images can be utilised to download
                images from Cisco.com to the disk. .
            name(str): name query parameter. Filter with software image or add-on name. Supports partial case-
                insensitive search. A minimum of 3 characters is required for the search .
            version(str): version query parameter. Filter with image version. Supports partial case-insensitive
                search. A minimum of 3 characters is required for the search .
            golden(str): golden query parameter. When set to `true`, it will retrieve the images marked tagged
                golden. When set to `false`, it will retrieve the images marked not tagged golden. .
            integrity(str): integrity query parameter. Filter with verified images using Integrity Verification
                Available values: UNKNOWN, VERIFIED .
            has_addon_images(bool): hasAddonImages query parameter. When set to `true`, it will retrieve the images
                which have add-on images. When set to `false`, it will retrieve the images which do not
                have add-on images. .
            is_addon_images(bool): isAddonImages query parameter. When set to `true`, it will retrieve the images
                that an add-on image.  When set to `false`, it will retrieve the images that are not
                add-on images .
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
            https://developer.cisco.com/docs/dna-center/#!returns-count-of-software-images
        """
        check_type(headers, dict)
        check_type(site_id, str)
        check_type(product_name_ordinal, int)
        check_type(supervisor_product_name_ordinal, int)
        check_type(imported, bool)
        check_type(name, str)
        check_type(version, str)
        check_type(golden, str)
        check_type(integrity, str)
        check_type(has_addon_images, bool)
        check_type(is_addon_images, bool)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "siteId": site_id,
            "productNameOrdinal": product_name_ordinal,
            "supervisorProductNameOrdinal": supervisor_product_name_ordinal,
            "imported": imported,
            "name": name,
            "version": version,
            "golden": golden,
            "integrity": integrity,
            "hasAddonImages": has_addon_images,
            "isAddonImages": is_addon_images,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/images/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_bdcd5a6fab705566a60c7885a18bf1ac_v3_1_3_0", json_data
        )

    def add_image_distribution_server(
        self,
        password=None,
        portNumber=None,
        rootLocation=None,
        serverAddress=None,
        username=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Add remote server for distributing software images. Upto two such distribution servers are supported. .

        Args:
            password(string): Software Image Management (SWIM)'s Server password .
            portNumber(number): Software Image Management (SWIM)'s Port number .
            rootLocation(string): Software Image Management (SWIM)'s Server root location .
            serverAddress(string): Software Image Management (SWIM)'s FQDN or IP address of the server .
            username(string): Software Image Management (SWIM)'s Server username .
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
            https://developer.cisco.com/docs/dna-center/#!add-image-distribution-server
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
            "serverAddress": serverAddress,
            "username": username,
            "portNumber": portNumber,
            "rootLocation": rootLocation,
            "password": password,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_db0f8e07ae0d5ecc83e34d29e5e57b41_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/images/distributionServerSettings"
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
            "bpm_db0f8e07ae0d5ecc83e34d29e5e57b41_v3_1_3_0", json_data
        )

    def retrieve_image_distribution_servers(self, headers=None, **request_parameters):
        """Retrieve the list of remote image distribution servers. There can be up to two remote servers.Product always
        acts as local distribution server, and it is not part of this API response. .

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
            https://developer.cisco.com/docs/dna-center/#!retrieve-image-distribution-servers
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

        e_url = "/dna/intent/api/v1/images/distributionServerSettings"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_e2c81db557e753178af3bec81caa7a02_v3_1_3_0", json_data
        )

    def update_remote_image_distribution_server(
        self,
        id,
        password=None,
        portNumber=None,
        username=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Update remote image distribution server details. .

        Args:
            password(string): Software Image Management (SWIM)'s Server password .
            portNumber(number): Software Image Management (SWIM)'s Port number .
            username(string): Software Image Management (SWIM)'s Server username .
            id(str): id path parameter. Remote server identifier. .
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
            https://developer.cisco.com/docs/dna-center/#!update-remote-image-distribution-server
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
            "username": username,
            "portNumber": portNumber,
            "password": password,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_c49a8488cd52158790aac513e7184a_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/images/distributionServerSettings/{id" + "}"
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
            "bpm_c49a8488cd52158790aac513e7184a_v3_1_3_0", json_data
        )

    def retrieve_specific_image_distribution_server(
        self, id, headers=None, **request_parameters
    ):
        """Retrieve image distribution server for the given server identifier .

        Args:
            id(str): id path parameter. Server identifier .
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
            https://developer.cisco.com/docs/dna-center/#!retrieve-specific-image-distribution-server
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

        e_url = "/dna/intent/api/v1/images/distributionServerSettings/{id" + "}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_fe1411fc463c506591c20a0d6fbabca9_v3_1_3_0", json_data
        )

    def remove_image_distribution_server(self, id, headers=None, **request_parameters):
        """Delete remote image distribution server. .

        Args:
            id(str): id path parameter. Remote server identifier. .
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
            https://developer.cisco.com/docs/dna-center/#!remove-image-distribution-server
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

        e_url = "/dna/intent/api/v1/images/distributionServerSettings/{id" + "}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ba08e3af5db79aaef9e2909aa312_v3_1_3_0", json_data
        )

    def delete_image(self, id, headers=None, **request_parameters):
        """Delete the image from image repository .

        Args:
            id(str): id path parameter. The software image identifier that needs to be deleted can be obtained from
                the API `/dna/intent/api/v1/images?imported=true`. Use this API to obtain the `id` of
                the image. .
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
            https://developer.cisco.com/docs/dna-center/#!delete-image
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

        e_url = "/dna/intent/api/v1/images/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_af3d9db14c855d1a863625d4a33eb9ac_v3_1_3_0", json_data
        )

    def retrieve_applicable_add_on_images_for_the_given_software_image(
        self, id, headers=None, **request_parameters
    ):
        """Retrieves the list of applicable add-on images if available for the given software image. `id` can be obtained
        from the response of API [ /dna/intent/api/v1/images?hasAddonImages=true ]. .

        Args:
            id(str): id path parameter. Software image identifier. Check
                `/dna/intent/api/v1/images?hasAddonImages=true` API to get the same. .
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
            https://developer.cisco.com/docs/dna-center/#!retrieve-applicable-add-on-images-for-the-given-software-image
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

        e_url = "/dna/intent/api/v1/images/{id}/addonImages"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_f6787ea025b02b69de4030f36cc5c_v3_1_3_0", json_data
        )

    def returns_count_of_add_on_images(self, id, headers=None, **request_parameters):
        """Count of add-on images available for the given software image identifier, `id` can be obtained from the response
        of API [ /dna/intent/api/v1/images?hasAddonImages=true ]. .

        Args:
            id(str): id path parameter. Software image identifier. Check API `/dna/intent/api/v1/images` for id from
                response. .
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
            https://developer.cisco.com/docs/dna-center/#!returns-count-of-add-on-images
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

        e_url = "/dna/intent/api/v1/images/{id}/addonImages/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_d86809df17513dbe211ec7c5591a5f_v3_1_3_0", json_data
        )

    def download_the_software_image(self, id, headers=None, **request_parameters):
        """Initiates download of the software image from Cisco.com on the disk for the given `id`. Refer to
        `/dna/intent/api/v1/images` for obtaining `id`. .

        Args:
            id(str): id path parameter. Software image identifier. Check API `/dna/intent/api/v1/images` for `id`
                from response. .
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
            https://developer.cisco.com/docs/dna-center/#!download-the-software-image
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

        e_url = "/dna/intent/api/v1/images/{id}/download"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.post(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_cd82233a8af55e49ba9a202607561de9_v3_1_3_0", json_data
        )

    def tagging_golden_image(
        self,
        id,
        site_id,
        deviceRoles=None,
        deviceTags=None,
        productNameOrdinal=None,
        supervisorProductNameOrdinal=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Creates golden image tagging specifically for a particular device type or supervisor engine module. Conditions
        for tagging the golden image: 1) The golden tagging of SMU, PISRT_SMU, APSP, and APDP image type depends
        on the golden tagged applied on the base image. If any discrepancies are identified in the request
        payload, the golden tagging process will fail. For example:       a) If the base image is tagged with
        Device Role: ACCESS, then add-ons can only be done ACCESS role only and the same is applied if any
        device tag is used. Any other request will fail.      b) If the base image is tagged at global or any
        site level then add-ons also need to be tagged at site level.  2) Tagging of SUBPACKAGE and ROMMON image
        type is not supported. .

        Args:
            deviceRoles(list): Software Image Management (SWIM)'s Device Roles. Available value will be [ CORE,
                DISTRIBUTION, UNKNOWN, ACCESS, BORDER ROUTER ]  (list of strings).
            deviceTags(list): Software Image Management (SWIM)'s Device tags can be fetched fom API
                https://developer.cisco.com/docs/dna-center/#!get-tag  (list of strings).
            productNameOrdinal(number): Software Image Management (SWIM)'s The product name ordinal is a unique
                value for each network device product. `productNameOrdinal` can be obtained from the
                response of API `/dna/intent/api/v1/siteWiseProductNames?siteId= ` .
            supervisorProductNameOrdinal(number): Software Image Management (SWIM)'s The supervisor engine module
                ordinal is a unique value for each supervisor module. `supervisorProductNameOrdinal` can
                be obtained from the response of API `/dna/intent/api/v1/siteWiseProductNames?siteId= `
                .
            id(str): id path parameter. Software image identifier is used for golden tagging or intent to tag it.
                The value of `id` can be obtained from the response of the API
                `/dna/intent/api/v1/images?imported=true&isAddonImages=false` for the base image and
                `/dna/images/{id}/addonImages` where `id` will be the software image identifier of the
                base image. .
            site_id(str): siteId path parameter. Site identifier for tagged image or intent to tag it. The default
                value is global site id. See [https://developer.cisco.com/docs/dna-center](#!get-site)
                for `siteId` .
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
            https://developer.cisco.com/docs/dna-center/#!tagging-golden-image
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(id, str, may_be_none=False)
        check_type(site_id, str, may_be_none=False)
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
            "siteId": site_id,
        }
        _payload = {
            "productNameOrdinal": productNameOrdinal,
            "supervisorProductNameOrdinal": supervisorProductNameOrdinal,
            "deviceRoles": deviceRoles,
            "deviceTags": deviceTags,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_febb2149ac5f8ba25dbf4d9a862d94_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/images/{id}/sites/{siteId}/tagGolden"
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
            "bpm_febb2149ac5f8ba25dbf4d9a862d94_v3_1_3_0", json_data
        )

    def untagging_golden_image(
        self,
        id,
        site_id,
        deviceRoles=None,
        deviceTags=None,
        productNameOrdinal=None,
        supervisorProductNameOrdinal=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Untag the golden images specifically designed for a particular device type or supervisor engine module.
        Conditions for untagging the golden image: 1) Untagging the golden image can only be done where the
        golden tagged is applied.    For example, if golden tagging is applied to a global site, then untagging
        can only be done on a global site. Even though the same setting will be inherited on native, attempting
        to untag will fail. 2) Untagging of SUBPACKAGE and ROMMON image type is not supported. .

        Args:
            deviceRoles(list): Software Image Management (SWIM)'s Device Roles. Available value will be [ CORE,
                DISTRIBUTION, UNKNOWN, ACCESS, BORDER ROUTER ]  (list of strings).
            deviceTags(list): Software Image Management (SWIM)'s Device tags can be fetched fom API
                https://developer.cisco.com/docs/dna-center/#!get-tag  (list of strings).
            productNameOrdinal(number): Software Image Management (SWIM)'s The product name ordinal is a unique
                value for each network device product. `productNameOrdinal` can be obtained from the
                response of API `/dna/intent/api/v1/siteWiseProductNames?siteId= ` .
            supervisorProductNameOrdinal(number): Software Image Management (SWIM)'s The supervisor engine module
                ordinal is a unique value for each supervisor module. `supervisorProductNameOrdinal` can
                be obtained from the response of API `/dna/intent/api/v1/siteWiseProductNames?siteId= `
                .
            id(str): id path parameter. Software image identifier is used for golden tagging or intent to tag it.
                The value of `id` can be obtained from the response of the API
                `/dna/intent/api/v1/images?imported=true&isAddonImages=false` for the base image and
                `/dna/images/{id}/addonImages` where `id` will be the software image identifier of the
                base image. .
            site_id(str): siteId path parameter. Site identifier for tagged image or intent to tag it. The default
                value is global site id. See [https://developer.cisco.com/docs/dna-center](#!get-site)
                for `siteId` .
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
            https://developer.cisco.com/docs/dna-center/#!untagging-golden-image
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(id, str, may_be_none=False)
        check_type(site_id, str, may_be_none=False)
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
            "siteId": site_id,
        }
        _payload = {
            "productNameOrdinal": productNameOrdinal,
            "supervisorProductNameOrdinal": supervisorProductNameOrdinal,
            "deviceRoles": deviceRoles,
            "deviceTags": deviceTags,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_b3ff5f865f1c8122a0ec8ca73921_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/images/{id}/sites/{siteId}/untagGolde" + "n"
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
            "bpm_b3ff5f865f1c8122a0ec8ca73921_v3_1_3_0", json_data
        )

    def assign_network_device_product_name_to_the_given_software_image(
        self,
        image_id,
        productNameOrdinal=None,
        siteIds=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Assign network device product name and sites for the given image identifier. Refer `/dna/intent/api/v1/images`
        API for obtaining imageId .

        Args:
            productNameOrdinal(number): Software Image Management (SWIM)'s Product name ordinal is unique value for
                each network device product .
            siteIds(list): Software Image Management (SWIM)'s Sites where this image needs to be assigned. Ref
                https://developer.cisco.com/docs/dna-center/#!sites  (list of strings).
            image_id(str): imageId path parameter. Software image identifier. Refer `/dna/intent/api/v1/images` API
                for obtaining `imageId` .
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
            https://developer.cisco.com/docs/dna-center/#!assign-network-device-product-name-to-the-given-software-image
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(image_id, str, may_be_none=False)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "imageId": image_id,
        }
        _payload = {
            "productNameOrdinal": productNameOrdinal,
            "siteIds": siteIds,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_eb4a05f61e475ad0b9e74f963f27ea1d_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/images/{imageId}/siteWiseProductNames"
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
            "bpm_eb4a05f61e475ad0b9e74f963f27ea1d_v3_1_3_0", json_data
        )

    def retrieves_network_device_product_names_assigned_to_a_software_image(
        self,
        image_id,
        assigned=None,
        limit=None,
        offset=None,
        product_id=None,
        product_name=None,
        recommended=None,
        headers=None,
        **request_parameters
    ):
        """Returns a list of network device product names and associated sites for a given image identifier. Refer
        `/dna/intent/api/v1/images` API for obtaining `imageId`. .

        Args:
            image_id(str): imageId path parameter. Software image identifier. Refer `/dna/intent/api/v1/images` API
                for obtaining `imageId` .
            product_name(str): productName query parameter. Filter with network device product name. Supports
                partial case-insensitive search. A minimum of 3 characters is required for the search. .
            product_id(str): productId query parameter. Filter with product ID (PID) .
            recommended(str): recommended query parameter. Filter with recommended source. If `CISCO` then the
                network device product assigned was recommended by Cisco and `USER` then the user has
                manually assigned. Available values: CISCO, USER .
            assigned(str): assigned query parameter. Filter with the assigned/unassigned, `ASSIGNED` option will
                filter network device products that are associated with the given image. The
                `NOT_ASSIGNED` option will filter network device products that have not yet been
                associated with the given image but apply to it. Available values: ASSIGNED,
                NOT_ASSIGNED .
            offset(int): offset query parameter. The first record to show for this page; the first record is
                numbered 1. The minimum value is 1 .
            limit(int): limit query parameter. The number of records to show for this page. The minimum and maximum
                values are 1 and 500, respectively .
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-network-device-product-names-assigned-to-a-software-image
        """
        check_type(headers, dict)
        check_type(product_name, str)
        check_type(product_id, str)
        check_type(recommended, str)
        check_type(assigned, str)
        check_type(offset, int)
        check_type(limit, int)
        check_type(image_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "productName": product_name,
            "productId": product_id,
            "recommended": recommended,
            "assigned": assigned,
            "offset": offset,
            "limit": limit,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "imageId": image_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/images/{imageId}/siteWiseProductNames"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_fb538ce59b945302bfaf521c6794691e_v3_1_3_0", json_data
        )

    def retrieves_the_count_of_assigned_network_device_products(
        self,
        image_id,
        assigned=None,
        product_id=None,
        product_name=None,
        recommended=None,
        headers=None,
        **request_parameters
    ):
        """Returns count of assigned network device product for a given image identifier. Refer `/dna/intent/api/v1/images`
        API for obtaining `imageId` .

        Args:
            image_id(str): imageId path parameter. Software image identifier. Refer `/dna/intent/api/v/images` API
                for obtaining `imageId` .
            product_name(str): productName query parameter. Filter with network device product name. Supports
                partial case-insensitive search. A minimum of 3 characters are required for search. .
            product_id(str): productId query parameter. Filter with product ID (PID) .
            recommended(str): recommended query parameter. Filter with recommended source. If `CISCO` then the
                network device product assigned was recommended by Cisco and `USER` then the user has
                manually assigned. Available values : CISCO, USER .
            assigned(str): assigned query parameter. Filter with the assigned/unassigned, `ASSIGNED` option will
                filter network device products that are associated with the given image. The
                `NOT_ASSIGNED` option will filter network device products that have not yet been
                associated with the given image but apply to it. Available values: ASSIGNED,
                NOT_ASSIGNED .
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-the-count-of-assigned-network-device-products
        """
        check_type(headers, dict)
        check_type(product_name, str)
        check_type(product_id, str)
        check_type(recommended, str)
        check_type(assigned, str)
        check_type(image_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "productName": product_name,
            "productId": product_id,
            "recommended": recommended,
            "assigned": assigned,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "imageId": image_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/images/{imageId}/siteWiseProductNames" + "/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_febd252a9e4d5411bfbb98d538210ea3_v3_1_3_0", json_data
        )

    def unassign_network_device_product_name_from_the_given_software_image(
        self, image_id, product_name_ordinal, headers=None, **request_parameters
    ):
        """This API unassigns the network device product name from all the sites for the given software image.
        Refer to `/dna/intent/api/v1/images` and `/dna/intent/api/v1/images/{imageId}/siteWiseProductNames` GET
        APIs for obtaining  `imageId` and `productNameOrdinal` respectively. .

        Args:
            image_id(str): imageId path parameter. Software image identifier. Refer `/dna/intent/api/v1/images` API
                for obtaining `imageId` .
            product_name_ordinal(int): productNameOrdinal path parameter. The product name ordinal is a unique value
                for each network device product. Refer
                `/dna/intent/api/v1/images/{imageId}/siteWiseProductNames` GET API for obtaining
                `productNameOrdinal` .
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
            https://developer.cisco.com/docs/dna-center/#!unassign-network-device-product-name-from-the-given-software-image
        """
        check_type(headers, dict)
        check_type(image_id, str, may_be_none=False)
        check_type(product_name_ordinal, int, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "imageId": image_id,
            "productNameOrdinal": product_name_ordinal,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/images/{imageId}/siteWiseProductNames"
            + "/{productNameOrdinal}"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ecf7c4398475f279abe95abdf5500f2_v3_1_3_0", json_data
        )

    def update_the_list_of_sites_for_the_network_device_product_name_assigned_to_the_software_image(
        self,
        image_id,
        product_name_ordinal,
        siteIds=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Update the list of sites for the network device product name assigned to the software image. Refer to
        `/dna/intent/api/v1/images` and `/dna/intent/api/v1/images/{imageId}/siteWiseProductNames` GET APIs for
        obtaining  `imageId` and `productNameOrdinal` respectively. .

        Args:
            siteIds(list): Software Image Management (SWIM)'s Sites where all this image need to be assigned  (list
                of strings).
            image_id(str): imageId path parameter. Software image identifier. Refer `/dna/intent/api/v1/images` API
                for obtaining `imageId` .
            product_name_ordinal(int): productNameOrdinal path parameter. Product name ordinal is unique value for
                each network device product. Refer
                `/dna/intent/api/v1/images/{imageId}/siteWiseProductNames` GET API for obtaining
                `productNameOrdinal`. .
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
            https://developer.cisco.com/docs/dna-center/#!update-the-list-of-sites-for-the-network-device-product-name-assigned-to-the-software-image
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(image_id, str, may_be_none=False)
        check_type(product_name_ordinal, int, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "imageId": image_id,
            "productNameOrdinal": product_name_ordinal,
        }
        _payload = {
            "siteIds": siteIds,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_c224ae3007d5486bbc5abb1f88e95e6_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/images/{imageId}/siteWiseProductNames"
            + "/{productNameOrdinal}"
        )
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
            "bpm_c224ae3007d5486bbc5abb1f88e95e6_v3_1_3_0", json_data
        )

    def get_network_device_image_updates(
        self,
        end_time=None,
        host_name=None,
        id=None,
        image_name=None,
        limit=None,
        management_address=None,
        network_device_id=None,
        offset=None,
        order=None,
        parent_id=None,
        sort_by=None,
        start_time=None,
        status=None,
        headers=None,
        **request_parameters
    ):
        """Returns the list of network device image updates based on the given filter criteria .

        Args:
            id(str): id query parameter. Update id which is unique for each network device under the parentId .
            parent_id(str): parentId query parameter. Updates that have this parent id .
            network_device_id(str): networkDeviceId query parameter. Network device id .
            status(str): status query parameter. Status of the image update. Available values : FAILURE, SUCCESS,
                IN_PROGRESS, PENDING .
            image_name(str): imageName query parameter. Software image name for the update .
            host_name(str): hostName query parameter. Host name of the network device for the image update. Supports
                case-insensitive partial search .
            management_address(str): managementAddress query parameter. Management address of the network device .
            start_time(int): startTime query parameter. Image update started after the given time (as milliseconds
                since UNIX epoch) .
            end_time(int): endTime query parameter. Image update started before the given time (as milliseconds
                since UNIX epoch) .
            sort_by(str): sortBy query parameter. A property within the response to sort by. .
            order(str): order query parameter. Whether ascending or descending order should be used to sort the
                response. .
            offset(int): offset query parameter. The first record to show for this page; the first record is
                numbered 1. .
            limit(int): limit query parameter. The number of records to show for this page. The minimum and maximum
                values are 1 and 500, respectively .
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
            https://developer.cisco.com/docs/dna-center/#!get-network-device-image-updates
        """
        check_type(headers, dict)
        check_type(id, str)
        check_type(parent_id, str)
        check_type(network_device_id, str)
        check_type(status, str)
        check_type(image_name, str)
        check_type(host_name, str)
        check_type(management_address, str)
        check_type(start_time, int)
        check_type(end_time, int)
        check_type(sort_by, str)
        check_type(order, str)
        check_type(offset, int)
        check_type(limit, int)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "id": id,
            "parentId": parent_id,
            "networkDeviceId": network_device_id,
            "status": status,
            "imageName": image_name,
            "hostName": host_name,
            "managementAddress": management_address,
            "startTime": start_time,
            "endTime": end_time,
            "sortBy": sort_by,
            "order": order,
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

        e_url = "/dna/intent/api/v1/networkDeviceImageUpdates"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ab118a78541c9b7e3f3857d6d1f5_v3_1_3_0", json_data
        )

    def count_of_network_device_image_updates(
        self,
        end_time=None,
        host_name=None,
        id=None,
        image_name=None,
        management_address=None,
        network_device_id=None,
        parent_id=None,
        start_time=None,
        status=None,
        headers=None,
        **request_parameters
    ):
        """Returns the count of network device image updates based on the given filter criteria .

        Args:
            id(str): id query parameter. Update id which is unique for each network device under the parentId .
            parent_id(str): parentId query parameter. Updates that have this parent id .
            network_device_id(str): networkDeviceId query parameter. Network device id .
            status(str): status query parameter. Status of the image update. Available values: FAILURE, SUCCESS,
                IN_PROGRESS, PENDING .
            image_name(str): imageName query parameter. Software image name for the update .
            host_name(str): hostName query parameter. Host name of the network device for the image update. Supports
                case-insensitive partial search. .
            management_address(str): managementAddress query parameter. Management address of the network device .
            start_time(int): startTime query parameter. Image update started after the given time (as milliseconds
                since UNIX epoch). .
            end_time(int): endTime query parameter. Image update started before the given time (as milliseconds
                since UNIX epoch). .
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
            https://developer.cisco.com/docs/dna-center/#!count-of-network-device-image-updates
        """
        check_type(headers, dict)
        check_type(id, str)
        check_type(parent_id, str)
        check_type(network_device_id, str)
        check_type(status, str)
        check_type(image_name, str)
        check_type(host_name, str)
        check_type(management_address, str)
        check_type(start_time, int)
        check_type(end_time, int)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "id": id,
            "parentId": parent_id,
            "networkDeviceId": network_device_id,
            "status": status,
            "imageName": image_name,
            "hostName": host_name,
            "managementAddress": management_address,
            "startTime": start_time,
            "endTime": end_time,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/networkDeviceImageUpdates/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory("bpm_de19e56c5aab0f9d10589871d_v3_1_3_0", json_data)

    def get_the_list_of_network_devices_with_image_details(
        self,
        limit=None,
        management_address=None,
        network_device_image_status=None,
        network_device_update_status=None,
        offset=None,
        order=None,
        sort_by=None,
        headers=None,
        **request_parameters
    ):
        """This API retrieves information about running images and golden image bundle, if they are available for network
        devices. It also provides network device update status and image update status related to the golden
        image bundle and the compatible features supported by the network devices. Network devices with
        `networkDeviceImageStatus` set as `OUTDATED` are considered ready for update based on the golden bundle.
        .

        Args:
            management_address(str): managementAddress query parameter. IP address or DNS name used to access and
                manage network devices. .
            network_device_image_status(str): networkDeviceImageStatus query parameter. Network device image status
                with respect to golden images. Available values : OUTDATED, UP_TO_DATE, UNKNOWN,
                CONFLICTED, UNSUPPORTED. .
            network_device_update_status(str): networkDeviceUpdateStatus query parameter. Network device current
                update status with respect to golden images. Available values : DISTRIBUTION_PENDING,
                DISTRIBUTION_IN_PROGRESS, DISTRIBUTION_FAILED, ACTIVATION_PENDING,
                ACTIVATION_IN_PROGRESS, ACTIVATION_FAILED, DEVICE_UP_TO_DATE,UNKNOWN. .
            sort_by(str): sortBy query parameter. Sort the response by a specified attribute. Available attributes
                for sorting are: `id`,`networkDeviceUpdateStatus`,`networkDeviceImageStatus`,
                `goldenImages.name`, `goldenImages.version`, `installedImages.name`,
                `installedImages.version`. .
            order(str): order query parameter. Whether ascending or descending order should be used to sort the
                response. Available values : asc, desc. .
            offset(int): offset query parameter. The first record to show for this page; the first record is
                numbered 1. The minimum value is 1. .
            limit(int): limit query parameter. The number of records to show for this page. The minimum and maximum
                values are 1 and 500, respectively. .
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
            https://developer.cisco.com/docs/dna-center/#!get-the-list-of-network-devices-with-image-details
        """
        check_type(headers, dict)
        check_type(management_address, str)
        check_type(network_device_image_status, str)
        check_type(network_device_update_status, str)
        check_type(sort_by, str)
        check_type(order, str)
        check_type(offset, int)
        check_type(limit, int)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "managementAddress": management_address,
            "networkDeviceImageStatus": network_device_image_status,
            "networkDeviceUpdateStatus": network_device_update_status,
            "sortBy": sort_by,
            "order": order,
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

        e_url = "/dna/intent/api/v1/networkDeviceImages"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_e39b6621058569039ee9a6e935145_v3_1_3_0", json_data
        )

    def bulk_update_images_on_network_devices(
        self, headers=None, payload=None, active_validation=True, **request_parameters
    ):
        """This API initiates the process of updating the software image on the given network devices. Providing value for
        the `installedImages` in request payload will initiate both distribution and activation of the images.
        At the end of this process, only the images which are part of `installedImages` will be running on the
        network devices. To monitor the progress and completion of the update task, call the GET API
        `/dna/intent/api/v1/networkDeviceImageUpdates?parentId={taskId}`, where `taskId` is from the response of
        the current endpoint. .

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
            https://developer.cisco.com/docs/dna-center/#!bulk-update-images-on-network-devices
        """
        check_type(headers, dict)
        check_type(payload, list)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = payload or []
        if active_validation:
            self._request_validator(
                "jsd_f21b7552158e889b51d0c109c15db_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/networkDeviceImages/activate/bulk"
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
            "bpm_f21b7552158e889b51d0c109c15db_v3_1_3_0", json_data
        )

    def count_of_network_devices_for_the_given_status_filters(
        self,
        management_address=None,
        network_device_image_status=None,
        network_device_update_status=None,
        headers=None,
        **request_parameters
    ):
        """Returns the count of network devices based on the given filters .

        Args:
            management_address(str): managementAddress query parameter. IP address or DNS name used to access and
                manage network devices. .
            network_device_image_status(str): networkDeviceImageStatus query parameter. Network device image status
                with respect to golden images. Available values : OUTDATED, UP_TO_DATE, UNKNOWN,
                CONFLICTED, UNSUPPORTED. .
            network_device_update_status(str): networkDeviceUpdateStatus query parameter. Network device current
                update status with respect to golden images. Available values : DISTRIBUTION_PENDING,
                DISTRIBUTION_IN_PROGRESS, DISTRIBUTION_FAILED, ACTIVATION_PENDING,
                ACTIVATION_IN_PROGRESS, ACTIVATION_FAILED, DEVICE_UP_TO_DATE,UNKNOWN. .
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
            https://developer.cisco.com/docs/dna-center/#!count-of-network-devices-for-the-given-status-filters
        """
        check_type(headers, dict)
        check_type(management_address, str)
        check_type(network_device_image_status, str)
        check_type(network_device_update_status, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "managementAddress": management_address,
            "networkDeviceImageStatus": network_device_image_status,
            "networkDeviceUpdateStatus": network_device_update_status,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/networkDeviceImages/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_eb5a6c6193a58ed9624f466a3e90bc4_v3_1_3_0", json_data
        )

    def bulk_distribute_images_on_network_devices(
        self, headers=None, payload=None, active_validation=True, **request_parameters
    ):
        """This API initiates the process of distributing the software image on the given network devices. Providing value
        for the `distributedImages` will only trigger the distribution process. To monitor the progress and
        completion of the update task, please call the GET API
        `/dna/intent/api/v1/networkDeviceImageUpdates?parentId={taskId}`, where `taskId` is from the response of
        the current endpoint. .

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
            https://developer.cisco.com/docs/dna-center/#!bulk-distribute-images-on-network-devices
        """
        check_type(headers, dict)
        check_type(payload, list)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = payload or []
        if active_validation:
            self._request_validator(
                "jsd_c1fa19f9295c50018132c6c9ebc3fc35_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/networkDeviceImages/distribute/bulk"
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
            "bpm_c1fa19f9295c50018132c6c9ebc3fc35_v3_1_3_0", json_data
        )

    def network_device_image_update_validation_results(
        self,
        id=None,
        limit=None,
        network_device_id=None,
        offset=None,
        operation_type=None,
        order=None,
        sort_by=None,
        status=None,
        type=None,
        headers=None,
        **request_parameters
    ):
        """This API provides a comprehensive overview of the outcomes from various tests and assessments defined by system
        and custom validations related to network device images. These results are essential for identifying
        potential issues, verifying configurations, and ensuring that the network meets the requirement for
        image update. .

        Args:
            network_device_id(str): networkDeviceId query parameter. Network device identifier. .
            id(str): id query parameter. Unique identifier of network device validation task. .
            operation_type(str): operationType query parameter. The operation type, as part of which this validation
                will get triggered. Available values : DISTRIBUTION, ACTIVATION, READINESS_CHECK. .
            status(str): status query parameter. Status of the validation result. SUCCESS, FAILED, IN_PROGRESS,
                WARNING. .
            type(str): type query parameter. Type of the validation. Available values : PRE_VALIDATION,
                POST_VALIDATION. .
            sort_by(str): sortBy query parameter. A property within the response to sort by. .
            order(str): order query parameter. Whether ascending or descending order should be used to sort the
                response. Available values : asc, desc .
            limit(int): limit query parameter. The number of records to show for this page. The minimum and maximum
                values are 1 and 500, respectively. .
            offset(int): offset query parameter. The first record to show for this page; the first record is
                numbered 1. The minimum value is 1. .
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
            https://developer.cisco.com/docs/dna-center/#!network-device-image-update-validation-results
        """
        check_type(headers, dict)
        check_type(network_device_id, str)
        check_type(id, str)
        check_type(operation_type, str)
        check_type(status, str)
        check_type(type, str)
        check_type(sort_by, str)
        check_type(order, str)
        check_type(limit, int)
        check_type(offset, int)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "networkDeviceId": network_device_id,
            "id": id,
            "operationType": operation_type,
            "status": status,
            "type": type,
            "sortBy": sort_by,
            "order": order,
            "limit": limit,
            "offset": offset,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/networkDeviceImages/validationResults"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ef43a0018635536f9208b408a799c844_v3_1_3_0", json_data
        )

    def count_of_network_device_image_update_validation_results(
        self,
        network_device_id=None,
        operation_type=None,
        status=None,
        type=None,
        headers=None,
        **request_parameters
    ):
        """The count of network device validation results. .

        Args:
            network_device_id(str): networkDeviceId query parameter. Network device identifier. .
            operation_type(str): operationType query parameter. The operation type, as part of which this validation
                will get triggered. Available values : DISTRIBUTION, ACTIVATION, READINESS_CHECK. .
            status(str): status query parameter. Status of the validation result. Available values : SUCCESS,
                FAILED, IN_PROGRESS, WARNING. .
            type(str): type query parameter. Type of the validation. Available values : PRE_VALIDATION,
                POST_VALIDATION. .
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
            https://developer.cisco.com/docs/dna-center/#!count-of-network-device-image-update-validation-results
        """
        check_type(headers, dict)
        check_type(network_device_id, str)
        check_type(operation_type, str)
        check_type(status, str)
        check_type(type, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "networkDeviceId": network_device_id,
            "operationType": operation_type,
            "status": status,
            "type": type,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/networkDeviceImages/validationResults" + "/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_daeb0e5e463d553fa456fe8500a132ba_v3_1_3_0", json_data
        )

    def create_custom_network_device_validation(
        self,
        cli=None,
        description=None,
        name=None,
        operationType=None,
        productSeriesOrdinals=None,
        type=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Custom network device validation refers to the tailored process of verifying and assessing the configurations of
        network devices based on specific organizational requirements and unique network environments. Unlike
        standard validations, custom network device validations are designed to address the distinctive needs
        and challenges of a particular network infrastructure, ensuring that devices operate optimally within
        the defined parameters. Upon task completion, the task API response's `resultLocation` attribute will
        provide the URL to retrieve the validation id. .

        Args:
            cli(string): Software Image Management (SWIM)'s Show commands that will be executed. Validate the CLI
                Cisco DevNet [ https://developer.cisco.com/docs/dna-center/2-3-7/run-read-only-commands-
                on-devices-to-get-their-real-time-configuration/ ] .
            description(string): Software Image Management (SWIM)'s Details of the network device validation. .
            name(string): Software Image Management (SWIM)'s Name of the network device validation. .
            operationType(string): Software Image Management (SWIM)'s The operation type, as part of which this
                validation will get triggered. . Available values are 'DISTRIBUTION' and 'ACTIVATION'.
            productSeriesOrdinals(list): Software Image Management (SWIM)'s The custom check will be mapped to the
                product series and devices that belong to this series. These devices will consume this
                check when triggered. Fetch productSeriesOrdinal from API
                `/dna/intent/api/v1/productSeries`.  (list of numbers).
            type(string): Software Image Management (SWIM)'s The type of network device validation determines
                whether this validation runs before or after the operation. . Available values are
                'PRE_VALIDATION' and 'POST_VALIDATION'.
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
            https://developer.cisco.com/docs/dna-center/#!create-custom-network-device-validation
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
            "name": name,
            "type": type,
            "operationType": operationType,
            "description": description,
            "cli": cli,
            "productSeriesOrdinals": productSeriesOrdinals,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_ca519342eb25dfcaf15f8f44baf0ee0_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/networkDeviceImages/validations"
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
            "bpm_ca519342eb25dfcaf15f8f44baf0ee0_v3_1_3_0", json_data
        )

    def get_the_list_of_custom_network_device_validations(
        self,
        limit=None,
        offset=None,
        operation_type=None,
        order=None,
        product_series_ordinal=None,
        type=None,
        headers=None,
        **request_parameters
    ):
        """Fetches custom network device validations that run on the network device as part of the update workflow. This
        process verifies and assesses the configuration of the network devices. .

        Args:
            product_series_ordinal(int): productSeriesOrdinal query parameter. Unique identifier of product series.
                .
            operation_type(str): operationType query parameter. The operation type, as part of which this validation
                will get triggered. Available values : DISTRIBUTION, ACTIVATION. .
            type(str): type query parameter. Type of the validation. Available values : PRE_VALIDATION,
                POST_VALIDATION. .
            order(str): order query parameter. Whether ascending or descending order should be used to sort the
                response. Available values : asc, desc. .
            offset(int): offset query parameter. The first record to show for this page; the first record is
                numbered 1. The minimum value is 1. .
            limit(int): limit query parameter. The number of records to show for this page. The minimum and maximum
                values are 1 and 500, respectively. .
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
            https://developer.cisco.com/docs/dna-center/#!get-the-list-of-custom-network-device-validations
        """
        check_type(headers, dict)
        check_type(product_series_ordinal, int)
        check_type(operation_type, str)
        check_type(type, str)
        check_type(order, str)
        check_type(offset, int)
        check_type(limit, int)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "productSeriesOrdinal": product_series_ordinal,
            "operationType": operation_type,
            "type": type,
            "order": order,
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

        e_url = "/dna/intent/api/v1/networkDeviceImages/validations"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c38b9dd078265df3a306553baf0e064c_v3_1_3_0", json_data
        )

    def count_of_custom_network_device_validations(
        self,
        operation_type=None,
        product_series_ordinal=None,
        type=None,
        headers=None,
        **request_parameters
    ):
        """Count the number of network device validations. .

        Args:
            product_series_ordinal(int): productSeriesOrdinal query parameter. Unique identifier of product series.
                .
            operation_type(str): operationType query parameter. The operation type, as part of which this validation
                will get triggered. Available values : DISTRIBUTION, ACTIVATION, READINESS_CHECK. .
            type(str): type query parameter. Type of the validation. Available values : PRE_VALIDATION,
                POST_VALIDATION. .
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
            https://developer.cisco.com/docs/dna-center/#!count-of-custom-network-device-validations
        """
        check_type(headers, dict)
        check_type(product_series_ordinal, int)
        check_type(operation_type, str)
        check_type(type, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "productSeriesOrdinal": product_series_ordinal,
            "operationType": operation_type,
            "type": type,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/networkDeviceImages/validations/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_b2a0b2686505a9148599e9c52837f_v3_1_3_0", json_data
        )

    def update_custom_network_device_validation(
        self,
        id,
        cli=None,
        description=None,
        productSeriesOrdinals=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Update the custom network device validation details. .

        Args:
            cli(string): Software Image Management (SWIM)'s Edit the Command line interface (CLI). Validate the CLI
                Cisco DevNet [ https://developer.cisco.com/docs/dna-center/2-3-7/run-read-only-commands-
                on-devices-to-get-their-real-time-configuration/ ] .
            description(string): Software Image Management (SWIM)'s Details of the network device validation. .
            productSeriesOrdinals(list): Software Image Management (SWIM)'s The custom check will be mapped to the
                product series and devices that belong to this series. These devices will consume this
                check when triggered.  (list of numbers).
            id(str): id path parameter. Unique identifier of network device validation. .
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
            https://developer.cisco.com/docs/dna-center/#!update-custom-network-device-validation
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
            "description": description,
            "cli": cli,
            "productSeriesOrdinals": productSeriesOrdinals,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_cf0f416ef5c25a159f4c3e376741a_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/networkDeviceImages/validations/{id}"
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
            "bpm_cf0f416ef5c25a159f4c3e376741a_v3_1_3_0", json_data
        )

    def get_custom_network_device_validation_details(
        self, id, headers=None, **request_parameters
    ):
        """This API fetches the details for the given network device validation. .

        Args:
            id(str): id path parameter. Unique identifier of network device validation. .
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
            https://developer.cisco.com/docs/dna-center/#!get-custom-network-device-validation-details
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

        e_url = "/dna/intent/api/v1/networkDeviceImages/validations/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_d0a1ee8bf91f567d863552a06fb37885_v3_1_3_0", json_data
        )

    def delete_custom_network_device_validation(
        self, id, headers=None, **request_parameters
    ):
        """Delete the custom network device validation. .

        Args:
            id(str): id path parameter. Unique identifier of network device validation. .
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
            https://developer.cisco.com/docs/dna-center/#!delete-custom-network-device-validation
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

        e_url = "/dna/intent/api/v1/networkDeviceImages/validations/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_f3847fd15d8d5299ada781bab2e084f9_v3_1_3_0", json_data
        )

    def fetch_network_device_with_image_details(
        self, id, headers=None, **request_parameters
    ):
        """The API retrieves information about running images and golden image bundle, if they are available for the
        network device. It also provides network device update status and image update status related to the
        golden image bundle and the compatible features supported by the network device. Network device with
        `networkDeviceImageStatus` set as `OUTDATED` is considered ready for update based on the golden image
        bundle. .

        Args:
            id(str): id path parameter. Network device identifier .
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
            https://developer.cisco.com/docs/dna-center/#!fetch-network-device-with-image-details
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

        e_url = "/dna/intent/api/v1/networkDeviceImages/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_f34cbcb416c95e4bbc7898768716a018_v3_1_3_0", json_data
        )

    def update_images_on_the_network_device(
        self,
        id,
        compatibleFeatures=None,
        installedImages=None,
        networkValidationIds=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This API initiates the process of updating the software image on the network device. Providing value for the
        `installedImages` in request payload will initiate both distribution and activation of the images. At
        the end of this process, only the images which are part of `installedImages` will be running on the
        network device. To monitor the progress and completion of the update task, call the GET API
        `/dna/intent/api/v1/networkDeviceImageUpdates?parentId={taskId}`, where `taskId` is from the response of
        the current endpoint. .

        Args:
            compatibleFeatures(list): Software Image Management (SWIM)'s compatibleFeatures (list of objects).
            installedImages(list): Software Image Management (SWIM)'s installedImages (list of objects).
            networkValidationIds(list): Software Image Management (SWIM)'s List of unique identifiers of custom
                network device validations.  (list of strings).
            id(str): id path parameter. Network device identifier. .
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
            https://developer.cisco.com/docs/dna-center/#!update-images-on-the-network-device
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
            "installedImages": installedImages,
            "compatibleFeatures": compatibleFeatures,
            "networkValidationIds": networkValidationIds,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_cd9d7d858f094469abf9464431f_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/networkDeviceImages/{id}/activate"
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
            "bpm_cd9d7d858f094469abf9464431f_v3_1_3_0", json_data
        )

    def distribute_images_on_the_network_device(
        self,
        id,
        distributedImages=None,
        networkValidationIds=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This API initiates the process of distributing the software image on the network device. Providing value for the
        `distributedImages` will only trigger the distribution process. To monitor the progress and completion
        of the update task, please call the GET API
        `/dna/intent/api/v1/networkDeviceImageUpdates?parentId={taskId}`, where `taskId` is from the response of
        the current endpoint. .

        Args:
            distributedImages(list): Software Image Management (SWIM)'s distributedImages (list of objects).
            networkValidationIds(list): Software Image Management (SWIM)'s List of unique identifiers of custom
                network device validations.  (list of strings).
            id(str): id path parameter. Network device identifier. .
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
            https://developer.cisco.com/docs/dna-center/#!distribute-images-on-the-network-device
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
            "distributedImages": distributedImages,
            "networkValidationIds": networkValidationIds,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_a914cc0c96a35a06a54856e778742a8c_v3_1_3_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/networkDeviceImages/{id}/distribute"
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
            "bpm_a914cc0c96a35a06a54856e778742a8c_v3_1_3_0", json_data
        )

    def trigger_update_readiness_for_network_device(
        self, id, headers=None, **request_parameters
    ):
        """Triggers an on-demand network device update readiness check, where system-defined pre-checks will be performed.
        Upon task completion, the task API response's `resultLocation` attribute will contain the URL for
        fetching the validation result. .

        Args:
            id(str): id path parameter. Network device identifier. .
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
            https://developer.cisco.com/docs/dna-center/#!trigger-update-readiness-for-network-device
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

        e_url = "/dna/intent/api/v1/networkDeviceImages/{id}/readinessChe" + "cks"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.post(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a6ad169a14d54c6b6d0111c7b38e69d_v3_1_3_0", json_data
        )

    def retrieves_the_list_of_network_device_product_names(
        self,
        limit=None,
        offset=None,
        product_id=None,
        product_name=None,
        headers=None,
        **request_parameters
    ):
        """Get the list of network device product names, their ordinal, and the support PIDs based on filter criteria. .

        Args:
            product_name(str): productName query parameter. Filter with network device product name. Supports
                partial case-insensitive search. A minimum of 3 characters are required for search .
            product_id(str): productId query parameter. Filter with product ID (PID) .
            offset(int): offset query parameter. The first record to show for this page; the first record is
                numbered 1. The minimum value is 1. .
            limit(int): limit query parameter. The number of records to show for this page. The minimum and maximum
                values are 1 and 500, respectively. .
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-the-list-of-network-device-product-names
        """
        check_type(headers, dict)
        check_type(product_name, str)
        check_type(product_id, str)
        check_type(offset, int)
        check_type(limit, int)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "productName": product_name,
            "productId": product_id,
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

        e_url = "/dna/intent/api/v1/productNames"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_b13b416b145acba7f74764f49364cd_v3_1_3_0", json_data
        )

    def count_of_network_product_names(
        self, product_id=None, product_name=None, headers=None, **request_parameters
    ):
        """Count of product names based on filter criteria .

        Args:
            product_name(str): productName query parameter. Filter with network device product name. Supports
                partial case-insensitive search. A minimum of 3 characters are required for search .
            product_id(str): productId query parameter. Filter with product ID (PID) .
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
            https://developer.cisco.com/docs/dna-center/#!count-of-network-product-names
        """
        check_type(headers, dict)
        check_type(product_name, str)
        check_type(product_id, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "productName": product_name,
            "productId": product_id,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/productNames/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_f933fdff7c5744a163227040d0367b_v3_1_3_0", json_data
        )

    def retrieve_network_device_product_name(
        self, product_name_ordinal, headers=None, **request_parameters
    ):
        """Get the network device product name, its ordinal, and supported PIDs. .

        Args:
            product_name_ordinal(int): productNameOrdinal path parameter. Product name ordinal is unique value for
                each network device product. .
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
            https://developer.cisco.com/docs/dna-center/#!retrieve-network-device-product-name
        """
        check_type(headers, dict)
        check_type(product_name_ordinal, int, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "productNameOrdinal": product_name_ordinal,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/productNames/{productNameOrdinal}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a6c00bdb02675408b8f0fb0107dcb7ed_v3_1_3_0", json_data
        )

    def retrieves_the_list_of_network_device_product_series(
        self, limit=None, name=None, offset=None, headers=None, **request_parameters
    ):
        """Get the list of network device product series and  their ordinal on filter criteria. .

        Args:
            name(str): name query parameter. Product series name. Supports partial case-insensitive search. A
                minimum of 3 characters is required for the search. .
            offset(int): offset query parameter. The first record to show for this page; the first record is
                numbered 1. The minimum value is 1. .
            limit(int): limit query parameter. The number of records to show for this page. The minimum and maximum
                values are 1 and 500, respectively. .
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
            https://developer.cisco.com/docs/dna-center/#!retrieves-the-list-of-network-device-product-series
        """
        check_type(headers, dict)
        check_type(name, str)
        check_type(offset, int)
        check_type(limit, int)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "name": name,
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

        e_url = "/dna/intent/api/v1/productSeries"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a5801264fcc15304be778491a0d356f9_v3_1_3_0", json_data
        )

    def count_of_network_product_series(
        self, name=None, headers=None, **request_parameters
    ):
        """Count of product series based on filter criteria .

        Args:
            name(str): name query parameter. Product series name. Supports partial case-insensitive search. A
                minimum of 3 characters is required for the search. .
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
            https://developer.cisco.com/docs/dna-center/#!count-of-network-product-series
        """
        check_type(headers, dict)
        check_type(name, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "name": name,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/productSeries/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ae3f664755d35cbfa22f54ab07fda9e8_v3_1_3_0", json_data
        )

    def retrieve_network_device_product_series(
        self, product_series_ordinal, headers=None, **request_parameters
    ):
        """Get the network device product series, its ordinal .

        Args:
            product_series_ordinal(int): productSeriesOrdinal path parameter. Unique identifier of product series. .
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
            https://developer.cisco.com/docs/dna-center/#!retrieve-network-device-product-series
        """
        check_type(headers, dict)
        check_type(product_series_ordinal, int, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "productSeriesOrdinal": product_series_ordinal,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/productSeries/{productSeriesOrdinal}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_e96f4748798d55d2a9257675107b7d7d_v3_1_3_0", json_data
        )

    def returns_the_image_summary_for_the_given_site(
        self, site_id=None, headers=None, **request_parameters
    ):
        """Returns aggregate counts of network device product names, golden and non-golden tagged products, imported
        images, golden images tagged, and advisor for a specific site provide, the default value of `siteId` is
        set to global. .

        Args:
            site_id(str): siteId query parameter. Site identifier to get the aggreagte counts products under the
                site. The default value is global site id. See [https://developer.cisco.com/docs/dna-
                center](#!get-site) for `siteId` .
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
            https://developer.cisco.com/docs/dna-center/#!returns-the-image-summary-for-the-given-site
        """
        check_type(headers, dict)
        check_type(site_id, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "siteId": site_id,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/siteWiseImagesSummary"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a2a643a99f01589ca0e12920ac5b257d_v3_1_3_0", json_data
        )

    def returns_network_device_product_names_for_a_site(
        self,
        limit=None,
        offset=None,
        product_name=None,
        site_id=None,
        headers=None,
        **request_parameters
    ):
        """Provides network device product names for a site. The default value of `siteId` is global. The response will
        include the network device count and image summary. .

        Args:
            site_id(str): siteId query parameter. Site identifier to get the list of all available products under
                the site. The default value is the global site.  See
                https://developer.cisco.com/docs/dna-center/get-site for siteId .
            product_name(str): productName query parameter. Filter with network device product name. Supports
                partial case-insensitive search. A minimum of 3 characters are required for search .
            offset(int): offset query parameter. The first record to show for this page; the first record is
                numbered 1. The minimum value is 1 .
            limit(int): limit query parameter. The number of records to show for this page. The minimum and maximum
                values are 1 and 500, respectively .
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
            https://developer.cisco.com/docs/dna-center/#!returns-network-device-product-names-for-a-site
        """
        check_type(headers, dict)
        check_type(site_id, str)
        check_type(product_name, str)
        check_type(offset, int)
        check_type(limit, int)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "siteId": site_id,
            "productName": product_name,
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

        e_url = "/dna/intent/api/v1/siteWiseProductNames"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a2ca9a4f55d0b44d7041186b9bab_v3_1_3_0", json_data
        )

    def returns_the_count_of_network_device_product_names_for_a_site(
        self, product_name=None, site_id=None, headers=None, **request_parameters
    ):
        """Returns the count of network device product names for given filters. The default value of `siteId` is global. .

        Args:
            site_id(str): siteId query parameter. Site identifier to get the list of all available products under
                the site. The default value is global site id. See https://developer.cisco.com/docs/dna-
                center/get-site/ for siteId .
            product_name(str): productName query parameter. Filter with network device product name. Supports
                partial case-insensitive search. A minimum of 3 characters are required for search .
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
            https://developer.cisco.com/docs/dna-center/#!returns-the-count-of-network-device-product-names-for-a-site
        """
        check_type(headers, dict)
        check_type(site_id, str)
        check_type(product_name, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "siteId": site_id,
            "productName": product_name,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/siteWiseProductNames/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ade3fee0a5a8eb0a7ced03126d560_v3_1_3_0", json_data
        )


# Alias Functions

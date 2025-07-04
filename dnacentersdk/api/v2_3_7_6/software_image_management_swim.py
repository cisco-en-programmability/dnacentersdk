# -*- coding: utf-8 -*-
"""Cisco DNA Center Software Image Management (SWIM) API wrapper.

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


class SoftwareImageManagementSwim(object):
    """Cisco DNA Center Software Image Management (SWIM) API (version: 2.3.7.6).

    Wraps the DNA Center Software Image Management (SWIM)
    API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new SoftwareImageManagementSwim
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the DNA Center service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(SoftwareImageManagementSwim, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def trigger_software_image_activation_v1(
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
            ApiError: If the DNA Center cloud returns an error.
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
                "jsd_a9136d5513985f15e91a19da66c_v2_3_7_6"
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
            "bpm_a9136d5513985f15e91a19da66c_v2_3_7_6", json_data
        )

    def trigger_software_image_distribution_v1(
        self, headers=None, payload=None, active_validation=True, **request_parameters
    ):
        """Distributes a software image on a given device. Software image must be imported successfully into DNACenter
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
            ApiError: If the DNA Center cloud returns an error.
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
                "jsd_c8d11fb9fc752ab8bb8e2b1413ccc92_v2_3_7_6"
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
            "bpm_c8d11fb9fc752ab8bb8e2b1413ccc92_v2_3_7_6", json_data
        )

    def get_software_image_details_v1(
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
            ApiError: If the DNA Center cloud returns an error.
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
            "bpm_f73101d5d5e409f571084ab4c6049_v2_3_7_6", json_data
        )

    def get_device_family_identifiers_v1(self, headers=None, **request_parameters):
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
            ApiError: If the DNA Center cloud returns an error.
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
            "bpm_b5c47f316ff058eb979bdea047f9d5b5_v2_3_7_6", json_data
        )

    def tag_as_golden_image_v1(
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
            ApiError: If the DNA Center cloud returns an error.
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
                "jsd_a9b864257b965fe4bd8b0293f41f1537_v2_3_7_6"
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
            "bpm_a9b864257b965fe4bd8b0293f41f1537_v2_3_7_6", json_data
        )

    def remove_golden_tag_for_image_v1(
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
            device_family_identifier(str): deviceFamilyIdentifier path parameter. Device family identifier
                e.g. : 277696480-283933147, e.g. : 277696480 .
            device_role(str): deviceRole path parameter. Device Role. Permissible Values : ALL, UNKNOWN,
                ACCESS, BORDER ROUTER, DISTRIBUTION and CORE. .
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
            ApiError: If the DNA Center cloud returns an error.
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
            "bpm_e9dd960c5378ab442f235c8135d0_v2_3_7_6", json_data
        )

    def get_golden_tag_status_of_an_image_v1(
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
            device_family_identifier(str): deviceFamilyIdentifier path parameter. Device family identifier
                e.g. : 277696480-283933147, e.g. : 277696480 .
            device_role(str): deviceRole path parameter. Device Role. Permissible Values : ALL, UNKNOWN,
                ACCESS, BORDER ROUTER, DISTRIBUTION and CORE. .
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
            ApiError: If the DNA Center cloud returns an error.
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
            "bpm_ab6266cac654d394cf943a161fcc7b_v2_3_7_6", json_data
        )

    def import_local_software_image_v1(
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
        """Fetches a software image from local file system and uploads to DNA Center. Supported software image files
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
            third_party_application_type(str): thirdPartyApplicationType query parameter. Third Party
                Application Type .
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
            ApiError: If the DNA Center cloud returns an error.
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
            "bpm_c1cf6d5d5f0fa2e92539134b6c1d_v2_3_7_6", json_data
        )

    def import_software_image_via_url_v1(
        self,
        schedule_at=None,
        schedule_desc=None,
        schedule_origin=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Fetches a software image from remote file system (using URL for HTTP/FTP) and uploads to DNACenter. Supported
        image files extensions are bin, img, tar, smu, pie, aes, iso, ova, tar_gz and qcow2 .

        Args:
            schedule_at(str): scheduleAt query parameter. Epoch Time (The number of milli-seconds since
                January 1 1970 UTC) at which the distribution should be scheduled (Optional)  .
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
            ApiError: If the DNA Center cloud returns an error.
        Documentation Link:
            https://developer.cisco.com/docs/dna-center/#!import-software-image-via-url
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
                "jsd_be8cdb967555fcca03a4c1f796eee56_v2_3_7_6"
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
            "bpm_be8cdb967555fcca03a4c1f796eee56_v2_3_7_6", json_data
        )

    def returns_list_of_software_images_v1(
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
        images from Cisco.com.  .

        Args:
            site_id(str): siteId query parameter. Site identifier to get the list of all available products
                under the site. The default value is the global site.  See
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
            name(str): name query parameter. Filter with software image or add-on name. Supports partial
                case-insensitive search. A minimum of 3 characters is required for the search. .
            version(str): version query parameter. Filter with image version. Supports partial case-
                insensitive search. A minimum of 3 characters is required for the search. .
            golden(bool): golden query parameter. When set to `true`, it will retrieve the images marked as tagged
                golden. When set to `false`, it will retrieve the images marked as not tagged golden. .
            integrity(str): integrity query parameter. Filter with verified images using Integrity
                Verification Available values: UNKNOWN, VERIFIED .
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
            ApiError: If the DNA Center cloud returns an error.
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
            "bpm_eb239c565c57d59cd6d6f7d193a993_v2_3_7_6", json_data
        )

    def returns_count_of_software_images_v1(
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
            site_id(str): siteId query parameter. Site identifier to get the list of all available products
                under the site. The default value is the global site.  See
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
            name(str): name query parameter. Filter with software image or add-on name. Supports partial
                case-insensitive search. A minimum of 3 characters is required for the search .
            version(str): version query parameter. Filter with image version. Supports partial case-
                insensitive search. A minimum of 3 characters is required for the search .
            golden(str): golden query parameter. When set to `true`, it will retrieve the images marked
                tagged golden. When set to `false`, it will retrieve the images marked not tagged
                golden. .
            integrity(str): integrity query parameter. Filter with verified images using Integrity
                Verification Available values: UNKNOWN, VERIFIED .
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
            ApiError: If the DNA Center cloud returns an error.
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
            "bpm_bdcd5a6fab705566a60c7885a18bf1ac_v2_3_7_6", json_data
        )

    def add_image_distribution_server_v1(
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
            ApiError: If the DNA Center cloud returns an error.
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
                "jsd_db0f8e07ae0d5ecc83e34d29e5e57b41_v2_3_7_6"
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
            "bpm_db0f8e07ae0d5ecc83e34d29e5e57b41_v2_3_7_6", json_data
        )

    def retrieve_image_distribution_servers_v1(
        self, headers=None, **request_parameters
    ):
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
            ApiError: If the DNA Center cloud returns an error.
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
            "bpm_e2c81db557e753178af3bec81caa7a02_v2_3_7_6", json_data
        )

    def update_remote_image_distribution_server_v1(
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
            ApiError: If the DNA Center cloud returns an error.
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
                "jsd_c49a8488cd52158790aac513e7184a_v2_3_7_6"
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
            "bpm_c49a8488cd52158790aac513e7184a_v2_3_7_6", json_data
        )

    def retrieve_specific_image_distribution_server_v1(
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
            ApiError: If the DNA Center cloud returns an error.
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
            "bpm_fe1411fc463c506591c20a0d6fbabca9_v2_3_7_6", json_data
        )

    def remove_image_distribution_server_v1(
        self, id, headers=None, **request_parameters
    ):
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
            ApiError: If the DNA Center cloud returns an error.
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
            "bpm_ba08e3af5db79aaef9e2909aa312_v2_3_7_6", json_data
        )

    def retrieve_applicable_add_on_images_for_the_given_software_image_v1(
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
            ApiError: If the DNA Center cloud returns an error.
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
            "bpm_f6787ea025b02b69de4030f36cc5c_v2_3_7_6", json_data
        )

    def returns_count_of_add_on_images_v1(self, id, headers=None, **request_parameters):
        """Count of add-on images available for the given software image identifier, `id` can be obtained from the response
        of API [ /dna/intent/api/v1/images?hasAddonImages=true ]. .

        Args:
            id(str): id path parameter. Software image identifier. Check API `/dna/intent/api/v1/images` for
                id from response. .
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
            "bpm_d86809df17513dbe211ec7c5591a5f_v2_3_7_6", json_data
        )

    def download_the_software_image_v1(self, id, headers=None, **request_parameters):
        """Initiates download of the software image from Cisco.com on the disk for the given `id`. Refer to
        `/dna/intent/api/v1/images` for obtaining `id`. .

        Args:
            id(str): id path parameter. Software image identifier. Check API `/dna/intent/api/v1/images` for
                `id` from response. .
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
            "bpm_cd82233a8af55e49ba9a202607561de9_v2_3_7_6", json_data
        )

    def assign_network_device_product_name_to_the_given_software_image_v1(
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
            image_id(str): imageId path parameter. Software image identifier. Refer
                `/dna/intent/api/v1/images` API for obtaining `imageId` .
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
                "jsd_eb4a05f61e475ad0b9e74f963f27ea1d_v2_3_7_6"
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
            "bpm_eb4a05f61e475ad0b9e74f963f27ea1d_v2_3_7_6", json_data
        )

    def retrieves_network_device_product_names_assigned_to_a_software_image_v1(
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
            image_id(str): imageId path parameter. Software image identifier. Refer
                `/dna/intent/api/v1/images` API for obtaining `imageId` .
            product_name(str): productName query parameter. Filter with network device product name. Supports
                partial case-insensitive search. A minimum of 3 characters is required for the search. .
            product_id(str): productId query parameter. Filter with product ID (PID) .
            recommended(str): recommended query parameter. Filter with recommended source. If `CISCO` then
                the network device product assigned was recommended by Cisco and `USER` then the user
                has manually assigned. Available values: CISCO, USER .
            assigned(str): assigned query parameter. Filter with the assigned/unassigned, `ASSIGNED` option
                will filter network device products that are associated with the given image. The
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
            ApiError: If the DNA Center cloud returns an error.
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
            "bpm_fb538ce59b945302bfaf521c6794691e_v2_3_7_6", json_data
        )

    def retrieves_the_count_of_assigned_network_device_products_v1(
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
            image_id(str): imageId path parameter. Software image identifier. Refer
                `/dna/intent/api/v/images` API for obtaining `imageId` .
            product_name(str): productName query parameter. Filter with network device product name. Supports
                partial case-insensitive search. A minimum of 3 characters are required for search. .
            product_id(str): productId query parameter. Filter with product ID (PID) .
            recommended(str): recommended query parameter. Filter with recommended source. If `CISCO` then
                the network device product assigned was recommended by Cisco and `USER` then the user
                has manually assigned. Available values : CISCO, USER .
            assigned(str): assigned query parameter. Filter with the assigned/unassigned, `ASSIGNED` option
                will filter network device products that are associated with the given image. The
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
            ApiError: If the DNA Center cloud returns an error.
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
            "bpm_febd252a9e4d5411bfbb98d538210ea3_v2_3_7_6", json_data
        )

    def unassign_network_device_product_name_from_the_given_software_image_v1(
        self, image_id, product_name_ordinal, headers=None, **request_parameters
    ):
        """This API unassigns the network device product name from all the sites for the given software image.
        Refer to `/dna/intent/api/v1/images` and `/dna/intent/api/v1/images/{imageId}/siteWiseProductNames` GET
        APIs for obtaining  `imageId` and `productNameOrdinal` respectively. .

        Args:
            image_id(str): imageId path parameter. Software image identifier. Refer
                `/dna/intent/api/v1/images` API for obtaining `imageId` .
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
            ApiError: If the DNA Center cloud returns an error.
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
            "bpm_ecf7c4398475f279abe95abdf5500f2_v2_3_7_6", json_data
        )

    def update_the_list_of_sites_for_the_network_device_product_name_assigned_to_the_software_image_v1(
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
            image_id(str): imageId path parameter. Software image identifier. Refer
                `/dna/intent/api/v1/images` API for obtaining `imageId` .
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
            ApiError: If the DNA Center cloud returns an error.
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
                "jsd_c224ae3007d5486bbc5abb1f88e95e6_v2_3_7_6"
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
            "bpm_c224ae3007d5486bbc5abb1f88e95e6_v2_3_7_6", json_data
        )

    def get_network_device_image_updates_v1(
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
            id(str): id query parameter. Update id which is unique for each network device under the parentId
                .
            parent_id(str): parentId query parameter. Updates that have this parent id .
            network_device_id(str): networkDeviceId query parameter. Network device id .
            status(str): status query parameter. Status of the image update. Available values : FAILURE,
                SUCCESS, IN_PROGRESS, PENDING .
            image_name(str): imageName query parameter. Software image name for the update .
            host_name(str): hostName query parameter. Host name of the network device for the image update.
                Supports case-insensitive partial search .
            management_address(str): managementAddress query parameter. Management address of the network
                device .
            start_time(int): startTime query parameter. Image update started after the given time (as milliseconds
                since UNIX epoch) .
            end_time(int): endTime query parameter. Image update started before the given time (as milliseconds
                since UNIX epoch) .
            sort_by(str): sortBy query parameter. A property within the response to sort by. .
            order(str): order query parameter. Whether ascending or descending order should be used to sort
                the response. .
            offset(int): offset query parameter. The first record to show for this page; the first record is
                numbered 1. .
            limit(int): limit query parameter. The number of records to show for this page. .
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
            "bpm_ab118a78541c9b7e3f3857d6d1f5_v2_3_7_6", json_data
        )

    def count_of_network_device_image_updates_v1(
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
            id(str): id query parameter. Update id which is unique for each network device under the parentId
                .
            parent_id(str): parentId query parameter. Updates that have this parent id .
            network_device_id(str): networkDeviceId query parameter. Network device id .
            status(str): status query parameter. Status of the image update. Available values: FAILURE,
                SUCCESS, IN_PROGRESS, PENDING .
            image_name(str): imageName query parameter. Software image name for the update .
            host_name(str): hostName query parameter. Host name of the network device for the image update.
                Supports case-insensitive partial search. .
            management_address(str): managementAddress query parameter. Management address of the network
                device .
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
            ApiError: If the DNA Center cloud returns an error.
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

        return self._object_factory("bpm_de19e56c5aab0f9d10589871d_v2_3_7_6", json_data)

    def retrieves_the_list_of_network_device_product_names_v1(
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
            ApiError: If the DNA Center cloud returns an error.
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
            "bpm_b13b416b145acba7f74764f49364cd_v2_3_7_6", json_data
        )

    def count_of_network_product_names_v1(
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
            ApiError: If the DNA Center cloud returns an error.
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
            "bpm_f933fdff7c5744a163227040d0367b_v2_3_7_6", json_data
        )

    def retrieve_network_device_product_name_v1(
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
            ApiError: If the DNA Center cloud returns an error.
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
            "bpm_a6c00bdb02675408b8f0fb0107dcb7ed_v2_3_7_6", json_data
        )

    def returns_network_device_product_names_for_a_site_v1(
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
            site_id(str): siteId query parameter. Site identifier to get the list of all available products
                under the site. The default value is the global site.  See
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
            ApiError: If the DNA Center cloud returns an error.
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
            "bpm_a2ca9a4f55d0b44d7041186b9bab_v2_3_7_6", json_data
        )

    def returns_the_count_of_network_device_product_names_for_a_site_v1(
        self, product_name=None, site_id=None, headers=None, **request_parameters
    ):
        """Returns the count of network device product names for given filters. The default value of `siteId` is global. .

        Args:
            site_id(str): siteId query parameter. Site identifier to get the list of all available products
                under the site. The default value is global site id. See
                https://developer.cisco.com/docs/dna-center/get-site/ for siteId .
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
            ApiError: If the DNA Center cloud returns an error.
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
            "bpm_ade3fee0a5a8eb0a7ced03126d560_v2_3_7_6", json_data
        )

    # Alias Function
    def get_device_family_identifiers(self, headers=None, **request_parameters):
        """This function is an alias of get_device_family_identifiers_v1 .
        Args:
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_device_family_identifiers_v1 .
        """
        return self.get_device_family_identifiers_v1(
            headers=headers, **request_parameters
        )

    # Alias Function
    def trigger_software_image_distribution(
        self, headers=None, payload=None, active_validation=True, **request_parameters
    ):
        """This function is an alias of trigger_software_image_distribution_v1 .
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
            This function returns the output of trigger_software_image_distribution_v1 .
        """
        return self.trigger_software_image_distribution_v1(
            headers=headers,
            payload=payload,
            active_validation=active_validation,
            **request_parameters
        )

    # Alias Function
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
        """This function is an alias of get_network_device_image_updates_v1 .
        Args:
            id(basestring): id query parameter. Update id which is unique for each network device under the parentId
                .
            parent_id(basestring): parentId query parameter. Updates that have this parent id .
            network_device_id(basestring): networkDeviceId query parameter. Network device id .
            status(basestring): status query parameter. Status of the image update. Available values : FAILURE,
                SUCCESS, IN_PROGRESS, PENDING .
            image_name(basestring): imageName query parameter. Software image name for the update .
            host_name(basestring): hostName query parameter. Host name of the network device for the image update.
                Supports case-insensitive partial search .
            management_address(basestring): managementAddress query parameter. Management address of the network
                device .
            start_time(int): startTime query parameter. Image update started after the given time (as milliseconds
                since UNIX epoch) .
            end_time(int): endTime query parameter. Image update started before the given time (as milliseconds
                since UNIX epoch) .
            sort_by(basestring): sortBy query parameter. A property within the response to sort by. .
            order(basestring): order query parameter. Whether ascending or descending order should be used to sort
                the response. .
            offset(int): offset query parameter. The first record to show for this page; the first record is
                numbered 1. .
            limit(int): limit query parameter. The number of records to show for this page. .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_network_device_image_updates_v1 .
        """
        return self.get_network_device_image_updates_v1(
            end_time=end_time,
            host_name=host_name,
            id=id,
            image_name=image_name,
            limit=limit,
            management_address=management_address,
            network_device_id=network_device_id,
            offset=offset,
            order=order,
            parent_id=parent_id,
            sort_by=sort_by,
            start_time=start_time,
            status=status,
            headers=headers,
            **request_parameters
        )

    # Alias Function
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
        """This function is an alias of update_remote_image_distribution_server_v1 .
        Args:
            password(string): Software Image Management (SWIM)'s Server password .
            portNumber(number): Software Image Management (SWIM)'s Port number .
            username(string): Software Image Management (SWIM)'s Server username .
            id(basestring): id path parameter. Remote server identifier. .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of update_remote_image_distribution_server_v1 .
        """
        return self.update_remote_image_distribution_server_v1(
            id=id,
            password=password,
            portNumber=portNumber,
            username=username,
            headers=headers,
            payload=payload,
            active_validation=active_validation,
            **request_parameters
        )

    # Alias Function
    def retrieves_the_list_of_network_device_product_names(
        self,
        limit=None,
        offset=None,
        product_id=None,
        product_name=None,
        headers=None,
        **request_parameters
    ):
        """This function is an alias of retrieves_the_list_of_network_device_product_names_v1 .
        Args:
            product_name(basestring): productName query parameter. Filter with network device product name. Supports
                partial case-insensitive search. A minimum of 3 characters are required for search .
            product_id(basestring): productId query parameter. Filter with product ID (PID) .
            offset(int): offset query parameter. The first record to show for this page; the first record is
                numbered 1. The minimum value is 1. .
            limit(int): limit query parameter. The number of records to show for this page. The minimum and maximum
                values are 1 and 500, respectively. .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of retrieves_the_list_of_network_device_product_names_v1 .
        """
        return self.retrieves_the_list_of_network_device_product_names_v1(
            limit=limit,
            offset=offset,
            product_id=product_id,
            product_name=product_name,
            headers=headers,
            **request_parameters
        )

    # Alias Function
    def download_the_software_image(self, id, headers=None, **request_parameters):
        """This function is an alias of download_the_software_image_v1 .
        Args:
            id(basestring): id path parameter. Software image identifier. Check API `/dna/intent/api/v1/images` for
                `id` from response. .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of download_the_software_image_v1 .
        """
        return self.download_the_software_image_v1(
            id=id, headers=headers, **request_parameters
        )

    # Alias Function
    def trigger_software_image_activation(
        self,
        schedule_validate=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This function is an alias of trigger_software_image_activation_v1 .
        Args:
            schedule_validate(bool): scheduleValidate query parameter. scheduleValidate, validates data before
                schedule (Optional) .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of trigger_software_image_activation_v1 .
        """
        return self.trigger_software_image_activation_v1(
            schedule_validate=schedule_validate,
            headers=headers,
            payload=payload,
            active_validation=active_validation,
            **request_parameters
        )

    # Alias Function
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
        """This function is an alias of assign_network_device_product_name_to_the_given_software_image_v1 .
        Args:
            productNameOrdinal(number): Software Image Management (SWIM)'s Product name ordinal is unique value for
                each network device product .
            siteIds(list): Software Image Management (SWIM)'s Sites where this image needs to be assigned. Ref
                https://developer.cisco.com/docs/dna-center/#!sites  (list of strings).
            image_id(basestring): imageId path parameter. Software image identifier. Refer
                `/dna/intent/api/v1/images` API for obtaining `imageId` .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of assign_network_device_product_name_to_the_given_software_image_v1 .
        """
        return self.assign_network_device_product_name_to_the_given_software_image_v1(
            image_id=image_id,
            productNameOrdinal=productNameOrdinal,
            siteIds=siteIds,
            headers=headers,
            payload=payload,
            active_validation=active_validation,
            **request_parameters
        )

    # Alias Function
    def retrieve_network_device_product_name(
        self, product_name_ordinal, headers=None, **request_parameters
    ):
        """This function is an alias of retrieve_network_device_product_name_v1 .
        Args:
            product_name_ordinal(int): productNameOrdinal path parameter. Product name ordinal is unique value for
                each network device product. .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of retrieve_network_device_product_name_v1 .
        """
        return self.retrieve_network_device_product_name_v1(
            product_name_ordinal=product_name_ordinal,
            headers=headers,
            **request_parameters
        )

    # Alias Function
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
        """This function is an alias of get_software_image_details_v1 .
        Args:
            image_uuid(basestring): imageUuid query parameter.
            name(basestring): name query parameter.
            family(basestring): family query parameter.
            application_type(basestring): applicationType query parameter.
            image_integrity_status(basestring): imageIntegrityStatus query parameter. imageIntegrityStatus FAILURE,
                UNKNOWN, VERIFIED .
            version(basestring): version query parameter. software Image Version .
            image_series(basestring): imageSeries query parameter. image Series .
            image_name(basestring): imageName query parameter. image Name .
            is_tagged_golden(bool): isTaggedGolden query parameter. is Tagged Golden .
            is_cco_recommended(bool): isCCORecommended query parameter. is recommended from cisco.com .
            is_cco_latest(bool): isCCOLatest query parameter. is latest from cisco.com .
            created_time(int): createdTime query parameter. time in milliseconds (epoch format) .
            image_size_greater_than(int): imageSizeGreaterThan query parameter. size in bytes .
            image_size_lesser_than(int): imageSizeLesserThan query parameter. size in bytes .
            sort_by(basestring): sortBy query parameter. sort results by this field .
            sort_order(basestring): sortOrder query parameter. sort order 'asc' or 'des'. Default is asc .
            limit(int): limit query parameter.
            offset(int): offset query parameter.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_software_image_details_v1 .
        """
        return self.get_software_image_details_v1(
            application_type=application_type,
            created_time=created_time,
            family=family,
            image_integrity_status=image_integrity_status,
            image_name=image_name,
            image_series=image_series,
            image_size_greater_than=image_size_greater_than,
            image_size_lesser_than=image_size_lesser_than,
            image_uuid=image_uuid,
            is_cco_latest=is_cco_latest,
            is_cco_recommended=is_cco_recommended,
            is_tagged_golden=is_tagged_golden,
            limit=limit,
            name=name,
            offset=offset,
            sort_by=sort_by,
            sort_order=sort_order,
            version=version,
            headers=headers,
            **request_parameters
        )

    # Alias Function
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
        """This function is an alias of returns_list_of_software_images_v1 .
        Args:
            site_id(basestring): siteId query parameter. Site identifier to get the list of all available products
                under the site. The default value is the global site.  See
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
            name(basestring): name query parameter. Filter with software image or add-on name. Supports partial
                case-insensitive search. A minimum of 3 characters is required for the search. .
            version(basestring): version query parameter. Filter with image version. Supports partial case-
                insensitive search. A minimum of 3 characters is required for the search. .
            golden(bool): golden query parameter. When set to `true`, it will retrieve the images marked as tagged
                golden. When set to `false`, it will retrieve the images marked as not tagged golden. .
            integrity(basestring): integrity query parameter. Filter with verified images using Integrity
                Verification Available values: UNKNOWN, VERIFIED .
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
            This function returns the output of returns_list_of_software_images_v1 .
        """
        return self.returns_list_of_software_images_v1(
            golden=golden,
            has_addon_images=has_addon_images,
            imported=imported,
            integrity=integrity,
            is_addon_images=is_addon_images,
            limit=limit,
            name=name,
            offset=offset,
            product_name_ordinal=product_name_ordinal,
            site_id=site_id,
            supervisor_product_name_ordinal=supervisor_product_name_ordinal,
            version=version,
            headers=headers,
            **request_parameters
        )

    # Alias Function
    def returns_count_of_add_on_images(self, id, headers=None, **request_parameters):
        """This function is an alias of returns_count_of_add_on_images_v1 .
        Args:
            id(basestring): id path parameter. Software image identifier. Check API `/dna/intent/api/v1/images` for
                id from response. .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of returns_count_of_add_on_images_v1 .
        """
        return self.returns_count_of_add_on_images_v1(
            id=id, headers=headers, **request_parameters
        )

    # Alias Function
    def count_of_network_product_names(
        self, product_id=None, product_name=None, headers=None, **request_parameters
    ):
        """This function is an alias of count_of_network_product_names_v1 .
        Args:
            product_name(basestring): productName query parameter. Filter with network device product name. Supports
                partial case-insensitive search. A minimum of 3 characters are required for search .
            product_id(basestring): productId query parameter. Filter with product ID (PID) .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of count_of_network_product_names_v1 .
        """
        return self.count_of_network_product_names_v1(
            product_id=product_id,
            product_name=product_name,
            headers=headers,
            **request_parameters
        )

    # Alias Function
    def retrieve_specific_image_distribution_server(
        self, id, headers=None, **request_parameters
    ):
        """This function is an alias of retrieve_specific_image_distribution_server_v1 .
        Args:
            id(basestring): id path parameter. Server identifier .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of retrieve_specific_image_distribution_server_v1 .
        """
        return self.retrieve_specific_image_distribution_server_v1(
            id=id, headers=headers, **request_parameters
        )

    # Alias Function
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
        """This function is an alias of import_software_image_via_url_v1 .
        Args:
            schedule_at(basestring): scheduleAt query parameter. Epoch Time (The number of milli-seconds since
                January 1 1970 UTC) at which the distribution should be scheduled (Optional)  .
            schedule_desc(basestring): scheduleDesc query parameter. Custom Description (Optional) .
            schedule_origin(basestring): scheduleOrigin query parameter. Originator of this call (Optional) .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of import_software_image_via_url_v1 .
        """
        return self.import_software_image_via_url_v1(
            schedule_at=schedule_at,
            schedule_desc=schedule_desc,
            schedule_origin=schedule_origin,
            headers=headers,
            payload=payload,
            active_validation=active_validation,
            **request_parameters
        )

    # Alias Function
    def returns_network_device_product_names_for_a_site(
        self,
        limit=None,
        offset=None,
        product_name=None,
        site_id=None,
        headers=None,
        **request_parameters
    ):
        """This function is an alias of returns_network_device_product_names_for_a_site_v1 .
        Args:
            site_id(basestring): siteId query parameter. Site identifier to get the list of all available products
                under the site. The default value is the global site.  See
                https://developer.cisco.com/docs/dna-center/get-site for siteId .
            product_name(basestring): productName query parameter. Filter with network device product name. Supports
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
            This function returns the output of returns_network_device_product_names_for_a_site_v1 .
        """
        return self.returns_network_device_product_names_for_a_site_v1(
            limit=limit,
            offset=offset,
            product_name=product_name,
            site_id=site_id,
            headers=headers,
            **request_parameters
        )

    # Alias Function
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
        """This function is an alias of returns_count_of_software_images_v1 .
        Args:
            site_id(basestring): siteId query parameter. Site identifier to get the list of all available products
                under the site. The default value is the global site.  See
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
            name(basestring): name query parameter. Filter with software image or add-on name. Supports partial
                case-insensitive search. A minimum of 3 characters is required for the search .
            version(basestring): version query parameter. Filter with image version. Supports partial case-
                insensitive search. A minimum of 3 characters is required for the search .
            golden(basestring): golden query parameter. When set to `true`, it will retrieve the images marked
                tagged golden. When set to `false`, it will retrieve the images marked not tagged
                golden. .
            integrity(basestring): integrity query parameter. Filter with verified images using Integrity
                Verification Available values: UNKNOWN, VERIFIED .
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
            This function returns the output of returns_count_of_software_images_v1 .
        """
        return self.returns_count_of_software_images_v1(
            golden=golden,
            has_addon_images=has_addon_images,
            imported=imported,
            integrity=integrity,
            is_addon_images=is_addon_images,
            name=name,
            product_name_ordinal=product_name_ordinal,
            site_id=site_id,
            supervisor_product_name_ordinal=supervisor_product_name_ordinal,
            version=version,
            headers=headers,
            **request_parameters
        )

    # Alias Function
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
        """This function is an alias of count_of_network_device_image_updates_v1 .
        Args:
            id(basestring): id query parameter. Update id which is unique for each network device under the parentId
                .
            parent_id(basestring): parentId query parameter. Updates that have this parent id .
            network_device_id(basestring): networkDeviceId query parameter. Network device id .
            status(basestring): status query parameter. Status of the image update. Available values: FAILURE,
                SUCCESS, IN_PROGRESS, PENDING .
            image_name(basestring): imageName query parameter. Software image name for the update .
            host_name(basestring): hostName query parameter. Host name of the network device for the image update.
                Supports case-insensitive partial search. .
            management_address(basestring): managementAddress query parameter. Management address of the network
                device .
            start_time(int): startTime query parameter. Image update started after the given time (as milliseconds
                since UNIX epoch). .
            end_time(int): endTime query parameter. Image update started before the given time (as milliseconds
                since UNIX epoch). .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of count_of_network_device_image_updates_v1 .
        """
        return self.count_of_network_device_image_updates_v1(
            end_time=end_time,
            host_name=host_name,
            id=id,
            image_name=image_name,
            management_address=management_address,
            network_device_id=network_device_id,
            parent_id=parent_id,
            start_time=start_time,
            status=status,
            headers=headers,
            **request_parameters
        )

    # Alias Function
    def unassign_network_device_product_name_from_the_given_software_image(
        self, image_id, product_name_ordinal, headers=None, **request_parameters
    ):
        """This function is an alias of unassign_network_device_product_name_from_the_given_software_image_v1 .
        Args:
            image_id(basestring): imageId path parameter. Software image identifier. Refer
                `/dna/intent/api/v1/images` API for obtaining `imageId` .
            product_name_ordinal(int): productNameOrdinal path parameter. The product name ordinal is a unique value
                for each network device product. Refer
                `/dna/intent/api/v1/images/{imageId}/siteWiseProductNames` GET API for obtaining
                `productNameOrdinal` .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of unassign_network_device_product_name_from_the_given_software_image_v1 .
        """
        return (
            self.unassign_network_device_product_name_from_the_given_software_image_v1(
                image_id=image_id,
                product_name_ordinal=product_name_ordinal,
                headers=headers,
                **request_parameters
            )
        )

    # Alias Function
    def remove_image_distribution_server(self, id, headers=None, **request_parameters):
        """This function is an alias of remove_image_distribution_server_v1 .
        Args:
            id(basestring): id path parameter. Remote server identifier. .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of remove_image_distribution_server_v1 .
        """
        return self.remove_image_distribution_server_v1(
            id=id, headers=headers, **request_parameters
        )

    # Alias Function
    def retrieve_applicable_add_on_images_for_the_given_software_image(
        self, id, headers=None, **request_parameters
    ):
        """This function is an alias of retrieve_applicable_add_on_images_for_the_given_software_image_v1 .
        Args:
            id(basestring): id path parameter. Software image identifier. Check
                `/dna/intent/api/v1/images?hasAddonImages=true` API to get the same. .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of retrieve_applicable_add_on_images_for_the_given_software_image_v1 .
        """
        return self.retrieve_applicable_add_on_images_for_the_given_software_image_v1(
            id=id, headers=headers, **request_parameters
        )

    # Alias Function
    def remove_golden_tag_for_image(
        self,
        device_family_identifier,
        device_role,
        image_id,
        site_id,
        headers=None,
        **request_parameters
    ):
        """This function is an alias of remove_golden_tag_for_image_v1 .
        Args:
            site_id(basestring): siteId path parameter. Site Id in uuid format. Set siteId as -1 for Global site. .
            device_family_identifier(basestring): deviceFamilyIdentifier path parameter. Device family identifier
                e.g. : 277696480-283933147, e.g. : 277696480 .
            device_role(basestring): deviceRole path parameter. Device Role. Permissible Values : ALL, UNKNOWN,
                ACCESS, BORDER ROUTER, DISTRIBUTION and CORE. .
            image_id(basestring): imageId path parameter. Image Id in uuid format. .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of remove_golden_tag_for_image_v1 .
        """
        return self.remove_golden_tag_for_image_v1(
            device_family_identifier=device_family_identifier,
            device_role=device_role,
            image_id=image_id,
            site_id=site_id,
            headers=headers,
            **request_parameters
        )

    # Alias Function
    def returns_the_count_of_network_device_product_names_for_a_site(
        self, product_name=None, site_id=None, headers=None, **request_parameters
    ):
        """This function is an alias of returns_the_count_of_network_device_product_names_for_a_site_v1 .
        Args:
            site_id(basestring): siteId query parameter. Site identifier to get the list of all available products
                under the site. The default value is global site id. See
                https://developer.cisco.com/docs/dna-center/get-site/ for siteId .
            product_name(basestring): productName query parameter. Filter with network device product name. Supports
                partial case-insensitive search. A minimum of 3 characters are required for search .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of returns_the_count_of_network_device_product_names_for_a_site_v1 .
        """
        return self.returns_the_count_of_network_device_product_names_for_a_site_v1(
            product_name=product_name,
            site_id=site_id,
            headers=headers,
            **request_parameters
        )

    # Alias Function
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
        """This function is an alias of retrieves_the_count_of_assigned_network_device_products_v1 .
        Args:
            image_id(basestring): imageId path parameter. Software image identifier. Refer
                `/dna/intent/api/v/images` API for obtaining `imageId` .
            product_name(basestring): productName query parameter. Filter with network device product name. Supports
                partial case-insensitive search. A minimum of 3 characters are required for search. .
            product_id(basestring): productId query parameter. Filter with product ID (PID) .
            recommended(basestring): recommended query parameter. Filter with recommended source. If `CISCO` then
                the network device product assigned was recommended by Cisco and `USER` then the user
                has manually assigned. Available values : CISCO, USER .
            assigned(basestring): assigned query parameter. Filter with the assigned/unassigned, `ASSIGNED` option
                will filter network device products that are associated with the given image. The
                `NOT_ASSIGNED` option will filter network device products that have not yet been
                associated with the given image but apply to it. Available values: ASSIGNED,
                NOT_ASSIGNED .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of retrieves_the_count_of_assigned_network_device_products_v1 .
        """
        return self.retrieves_the_count_of_assigned_network_device_products_v1(
            image_id=image_id,
            assigned=assigned,
            product_id=product_id,
            product_name=product_name,
            recommended=recommended,
            headers=headers,
            **request_parameters
        )

    # Alias Function
    def get_golden_tag_status_of_an_image(
        self,
        device_family_identifier,
        device_role,
        image_id,
        site_id,
        headers=None,
        **request_parameters
    ):
        """This function is an alias of get_golden_tag_status_of_an_image_v1 .
        Args:
            site_id(basestring): siteId path parameter. Site Id in uuid format. Set siteId as -1 for Global site. .
            device_family_identifier(basestring): deviceFamilyIdentifier path parameter. Device family identifier
                e.g. : 277696480-283933147, e.g. : 277696480 .
            device_role(basestring): deviceRole path parameter. Device Role. Permissible Values : ALL, UNKNOWN,
                ACCESS, BORDER ROUTER, DISTRIBUTION and CORE. .
            image_id(basestring): imageId path parameter. Image Id in uuid format. .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of get_golden_tag_status_of_an_image_v1 .
        """
        return self.get_golden_tag_status_of_an_image_v1(
            device_family_identifier=device_family_identifier,
            device_role=device_role,
            image_id=image_id,
            site_id=site_id,
            headers=headers,
            **request_parameters
        )

    # Alias Function
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
        """This function is an alias of add_image_distribution_server_v1 .
        Args:
            password(string): Software Image Management (SWIM)'s Server password .
            portNumber(number): Software Image Management (SWIM)'s Port number .
            rootLocation(string): Software Image Management (SWIM)'s Server root location .
            serverAddress(string): Software Image Management (SWIM)'s FQDN or IP address of the server .
            username(string): Software Image Management (SWIM)'s Server username .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of add_image_distribution_server_v1 .
        """
        return self.add_image_distribution_server_v1(
            password=password,
            portNumber=portNumber,
            rootLocation=rootLocation,
            serverAddress=serverAddress,
            username=username,
            headers=headers,
            payload=payload,
            active_validation=active_validation,
            **request_parameters
        )

    # Alias Function
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
        """This function is an alias of update_the_list_of_sites_for_the_network_device_product_name_assigned_to_the_software_image_v1 .
        Args:
            siteIds(list): Software Image Management (SWIM)'s Sites where all this image need to be assigned  (list
                of strings).
            image_id(basestring): imageId path parameter. Software image identifier. Refer
                `/dna/intent/api/v1/images` API for obtaining `imageId` .
            product_name_ordinal(int): productNameOrdinal path parameter. Product name ordinal is unique value for
                each network device product. Refer
                `/dna/intent/api/v1/images/{imageId}/siteWiseProductNames` GET API for obtaining
                `productNameOrdinal`. .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of update_the_list_of_sites_for_the_network_device_product_name_assigned_to_the_software_image_v1 .
        """
        return self.update_the_list_of_sites_for_the_network_device_product_name_assigned_to_the_software_image_v1(
            image_id=image_id,
            product_name_ordinal=product_name_ordinal,
            siteIds=siteIds,
            headers=headers,
            payload=payload,
            active_validation=active_validation,
            **request_parameters
        )

    # Alias Function
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
        """This function is an alias of import_local_software_image_v1 .
        Args:
            is_third_party(bool): isThirdParty query parameter. Third party Image check .
            third_party_vendor(basestring): thirdPartyVendor query parameter. Third Party Vendor .
            third_party_image_family(basestring): thirdPartyImageFamily query parameter. Third Party image family .
            third_party_application_type(basestring): thirdPartyApplicationType query parameter. Third Party
                Application Type .
            multipart_fields(dict): Fields from which to create a
                multipart/form-data body.
            multipart_monitor_callback(function): function used to monitor
                the progress of the upload.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of import_local_software_image_v1 .
        """
        return self.import_local_software_image_v1(
            multipart_fields=multipart_fields,
            multipart_monitor_callback=multipart_monitor_callback,
            is_third_party=is_third_party,
            third_party_application_type=third_party_application_type,
            third_party_image_family=third_party_image_family,
            third_party_vendor=third_party_vendor,
            headers=headers,
            **request_parameters
        )

    # Alias Function
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
        """This function is an alias of tag_as_golden_image_v1 .
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
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of tag_as_golden_image_v1 .
        """
        return self.tag_as_golden_image_v1(
            deviceFamilyIdentifier=deviceFamilyIdentifier,
            deviceRole=deviceRole,
            imageId=imageId,
            siteId=siteId,
            headers=headers,
            payload=payload,
            active_validation=active_validation,
            **request_parameters
        )

    # Alias Function
    def retrieve_image_distribution_servers(self, headers=None, **request_parameters):
        """This function is an alias of retrieve_image_distribution_servers_v1 .
        Args:
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of retrieve_image_distribution_servers_v1 .
        """
        return self.retrieve_image_distribution_servers_v1(
            headers=headers, **request_parameters
        )

    # Alias Function
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
        """This function is an alias of retrieves_network_device_product_names_assigned_to_a_software_image_v1 .
        Args:
            image_id(basestring): imageId path parameter. Software image identifier. Refer
                `/dna/intent/api/v1/images` API for obtaining `imageId` .
            product_name(basestring): productName query parameter. Filter with network device product name. Supports
                partial case-insensitive search. A minimum of 3 characters is required for the search. .
            product_id(basestring): productId query parameter. Filter with product ID (PID) .
            recommended(basestring): recommended query parameter. Filter with recommended source. If `CISCO` then
                the network device product assigned was recommended by Cisco and `USER` then the user
                has manually assigned. Available values: CISCO, USER .
            assigned(basestring): assigned query parameter. Filter with the assigned/unassigned, `ASSIGNED` option
                will filter network device products that are associated with the given image. The
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
            This function returns the output of retrieves_network_device_product_names_assigned_to_a_software_image_v1 .
        """
        return (
            self.retrieves_network_device_product_names_assigned_to_a_software_image_v1(
                image_id=image_id,
                assigned=assigned,
                limit=limit,
                offset=offset,
                product_id=product_id,
                product_name=product_name,
                recommended=recommended,
                headers=headers,
                **request_parameters
            )
        )

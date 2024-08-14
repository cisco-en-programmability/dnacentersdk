# -*- coding: utf-8 -*-
"""Cisco DNA Center Software Image Management (SWIM) API wrapper.

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


class SoftwareImageManagementSwim(object):
    """Cisco DNA Center Software Image Management (SWIM) API (version: 2.3.3.0).

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

    def trigger_software_image_activation(self,
                                          schedule_validate=None,
                                          headers=None,
                                          payload=None,
                                          active_validation=True,
                                          **request_parameters):
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
        """
        check_type(headers, dict)
        check_type(payload, list)
        check_type(schedule_validate, bool)
        if headers is not None:
            if 'Content-Type' in headers:
                check_type(headers.get('Content-Type'),
                           str, may_be_none=False)
            if 'Client-Type' in headers:
                check_type(headers.get('Client-Type'),
                           str)
            if 'Client-Url' in headers:
                check_type(headers.get('Client-Url'),
                           str)
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'scheduleValidate':
                schedule_validate,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }
        _payload = payload or []
        if active_validation:
            self._request_validator('jsd_a9136d5513985f15e91a19da66c_v2_3_3_0')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/image/activation/device')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_a9136d5513985f15e91a19da66c_v2_3_3_0', json_data)

    def trigger_software_image_distribution(self,
                                            headers=None,
                                            payload=None,
                                            active_validation=True,
                                            **request_parameters):
        """Distributes a software image on a given device. Software image must be imported successfully into DNA Center
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
            self._request_validator('jsd_c8d11fb9fc752ab8bb8e2b1413ccc92_v2_3_3_0')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/image/distribution')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_c8d11fb9fc752ab8bb8e2b1413ccc92_v2_3_3_0', json_data)

    def get_software_image_details(self,
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
                                   **request_parameters):
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
            limit(str, int): limit query parameter.
            offset(str, int): offset query parameter.
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
        check_type(limit, (str, int))
        check_type(offset, (str, int))
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'imageUuid':
                image_uuid,
            'name':
                name,
            'family':
                family,
            'applicationType':
                application_type,
            'imageIntegrityStatus':
                image_integrity_status,
            'version':
                version,
            'imageSeries':
                image_series,
            'imageName':
                image_name,
            'isTaggedGolden':
                is_tagged_golden,
            'isCCORecommended':
                is_cco_recommended,
            'isCCOLatest':
                is_cco_latest,
            'createdTime':
                created_time,
            'imageSizeGreaterThan':
                image_size_greater_than,
            'imageSizeLesserThan':
                image_size_lesser_than,
            'sortBy':
                sort_by,
            'sortOrder':
                sort_order,
            'limit':
                limit,
            'offset':
                offset,
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

        e_url = ('/dna/intent/api/v1/image/importation')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_f73101d5d5e409f571084ab4c6049_v2_3_3_0', json_data)

    def get_device_family_identifiers(self,
                                      headers=None,
                                      **request_parameters):
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
        """
        check_type(headers, dict)
        if headers is not None:
            if 'Accept' in headers:
                check_type(headers.get('Accept'),
                           str)
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

        e_url = ('/dna/intent/api/v1/image/importation/device-family-'
                 + 'identifiers')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_b5c47f316ff058eb979bdea047f9d5b5_v2_3_3_0', json_data)

    def tag_as_golden_image(self,
                            deviceFamilyIdentifier=None,
                            deviceRole=None,
                            imageId=None,
                            siteId=None,
                            headers=None,
                            payload=None,
                            active_validation=True,
                            **request_parameters):
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
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if 'Accept' in headers:
                check_type(headers.get('Accept'),
                           str)
            if 'Content-Type' in headers:
                check_type(headers.get('Content-Type'),
                           str)
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
            'imageId':
                imageId,
            'siteId':
                siteId,
            'deviceRole':
                deviceRole,
            'deviceFamilyIdentifier':
                deviceFamilyIdentifier,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_a9b864257b965fe4bd8b0293f41f1537_v2_3_3_0')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/image/importation/golden')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_a9b864257b965fe4bd8b0293f41f1537_v2_3_3_0', json_data)

    def remove_golden_tag_for_image(self,
                                    device_family_identifier,
                                    device_role,
                                    image_id,
                                    site_id,
                                    headers=None,
                                    **request_parameters):
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
        """
        check_type(headers, dict)
        check_type(site_id, str,
                   may_be_none=False)
        check_type(device_family_identifier, str,
                   may_be_none=False)
        check_type(device_role, str,
                   may_be_none=False)
        check_type(image_id, str,
                   may_be_none=False)
        if headers is not None:
            if 'Accept' in headers:
                check_type(headers.get('Accept'),
                           str)
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'siteId': site_id,
            'deviceFamilyIdentifier': device_family_identifier,
            'deviceRole': device_role,
            'imageId': image_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/image/importation/golden/site/{siteId'
                 + '}/family/{deviceFamilyIdentifier}/role/{deviceRole}/imag'
                 + 'e/{imageId}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(endpoint_full_url, params=_params,
                                             headers=_headers)
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_e9dd960c5378ab442f235c8135d0_v2_3_3_0', json_data)

    def get_golden_tag_status_of_an_image(self,
                                          device_family_identifier,
                                          device_role,
                                          image_id,
                                          site_id,
                                          headers=None,
                                          **request_parameters):
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
        """
        check_type(headers, dict)
        check_type(site_id, str,
                   may_be_none=False)
        check_type(device_family_identifier, str,
                   may_be_none=False)
        check_type(device_role, str,
                   may_be_none=False)
        check_type(image_id, str,
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
            'siteId': site_id,
            'deviceFamilyIdentifier': device_family_identifier,
            'deviceRole': device_role,
            'imageId': image_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/image/importation/golden/site/{siteId'
                 + '}/family/{deviceFamilyIdentifier}/role/{deviceRole}/imag'
                 + 'e/{imageId}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_ab6266cac654d394cf943a161fcc7b_v2_3_3_0', json_data)

    def import_local_software_image(self,
                                    multipart_fields,
                                    multipart_monitor_callback,
                                    is_third_party=None,
                                    third_party_application_type=None,
                                    third_party_image_family=None,
                                    third_party_vendor=None,
                                    headers=None,
                                    **request_parameters):
        """Fetches a software image from local file system and uploads to DNA Center. Supported software image files
        extensions are bin, img, tar, smu, pie, aes, iso, ova, tar_gz and qcow2. Upload the file to the **file**
        form data field .

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
        """
        check_type(headers, dict)
        check_type(is_third_party, bool)
        check_type(third_party_vendor, str)
        check_type(third_party_image_family, str)
        check_type(third_party_application_type, str)
        if headers is not None:
            if 'Content-Type' in headers:
                check_type(headers.get('Content-Type'),
                           str, may_be_none=False)
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'isThirdParty':
                is_third_party,
            'thirdPartyVendor':
                third_party_vendor,
            'thirdPartyImageFamily':
                third_party_image_family,
            'thirdPartyApplicationType':
                third_party_application_type,
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

        e_url = ('/dna/intent/api/v1/image/importation/source/file')
        endpoint_full_url = apply_path_params(e_url, path_params)
        m_data = self._session.multipart_data(multipart_fields,
                                              multipart_monitor_callback)
        _headers.update({'Content-Type': m_data.content_type,
                         'Content-Length': str(m_data.len),
                         'Connection': 'keep-alive'})
        with_custom_headers = True
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           data=m_data,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params)

        return self._object_factory('bpm_c1cf6d5d5f0fa2e92539134b6c1d_v2_3_3_0', json_data)

    def import_software_image_via_url(self,
                                      schedule_at=None,
                                      schedule_desc=None,
                                      schedule_origin=None,
                                      headers=None,
                                      payload=None,
                                      active_validation=True,
                                      **request_parameters):
        """Fetches a software image from remote file system (using URL for HTTP/FTP) and uploads to DNA Center. Supported
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
        """
        check_type(headers, dict)
        check_type(payload, list)
        check_type(schedule_at, str)
        check_type(schedule_desc, str)
        check_type(schedule_origin, str)
        if headers is not None:
            if 'Content-Type' in headers:
                check_type(headers.get('Content-Type'),
                           str, may_be_none=False)
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'scheduleAt':
                schedule_at,
            'scheduleDesc':
                schedule_desc,
            'scheduleOrigin':
                schedule_origin,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
        }
        _payload = payload or []
        if active_validation:
            self._request_validator('jsd_be8cdb967555fcca03a4c1f796eee56_v2_3_3_0')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/image/importation/source/url')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_be8cdb967555fcca03a4c1f796eee56_v2_3_3_0', json_data)

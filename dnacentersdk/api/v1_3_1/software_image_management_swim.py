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


class SoftwareImageManagementSwim(object):
    """Cisco DNA Center Software Image Management (SWIM) API (version: 1.3.1).

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
                                   sort_order='asc',
                                   version=None,
                                   headers=None,
                                   **request_parameters):
        """Returns software image list based on a filter criteria. For
        example: "filterbyName = cat3k%".

        Args:
            image_uuid(basestring): imageUuid query parameter.
            name(basestring): name query parameter.
            family(basestring): family query parameter.
            application_type(basestring): applicationType query parameter.
            image_integrity_status(basestring): imageIntegrityStatus FAILURE, UNKNOWN, VERIFIED.
            version(basestring): software Image Version.
            image_series(basestring): image Series.
            image_name(basestring): image Name.
            is_tagged_golden(bool): is Tagged Golden.
            is_cco_recommended(bool): is recommended from cisco.com.
            is_cco_latest(bool): is latest from cisco.com.
            created_time(int): time in milliseconds (epoch format).
            image_size_greater_than(int): size in bytes.
            image_size_lesser_than(int): size in bytes.
            sort_by(basestring): sort results by this field.
            sort_order(basestring): sort order 'asc' or 'des'. Default is asc.
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
        """
        check_type(headers, dict)
        check_type(image_uuid, basestring)
        check_type(name, basestring)
        check_type(family, basestring)
        check_type(application_type, basestring)
        check_type(image_integrity_status, basestring)
        check_type(version, basestring)
        check_type(image_series, basestring)
        check_type(image_name, basestring)
        check_type(is_tagged_golden, bool)
        check_type(is_cco_recommended, bool)
        check_type(is_cco_latest, bool)
        check_type(created_time, int)
        check_type(image_size_greater_than, int)
        check_type(image_size_lesser_than, int)
        check_type(sort_by, basestring)
        check_type(sort_order, basestring)
        check_type(limit, int)
        check_type(offset, int)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

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

        return self._object_factory('bpm_0c8f7a0b49b9aedd_v1_3_1', json_data)

    def import_local_software_image(self,
                                    multipart_fields,
                                    multipart_monitor_callback,
                                    is_third_party=None,
                                    third_party_application_type=None,
                                    third_party_image_family=None,
                                    third_party_vendor=None,
                                    headers=None,
                                    **request_parameters):
        """Fetches a software image from local file system and uploads to
        DNA Center. Supported software image files extensions
        are bin, img, tar, smu, pie, aes, iso, ova, tar_gz and
        qcow2.

        The following code gives an **example** of the multipart_fields,
        using `file` and `images` as form data field.

        Use the appropiate form data field for the function.

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
            is_third_party(bool): Third party Image check.
            third_party_vendor(basestring): Third Party Vendor.
            third_party_image_family(basestring): Third Party image family.
            third_party_application_type(basestring): Third Party Application Type.
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
        check_type(third_party_vendor, basestring)
        check_type(third_party_image_family, basestring)
        check_type(third_party_application_type, basestring)
        if headers is not None:
            if 'Content-Type' in headers:
                check_type(headers.get('Content-Type'),
                           basestring, may_be_none=False)
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

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

        return self._object_factory('bpm_4dbe3bc743a891bc_v1_3_1', json_data)

    def trigger_software_image_distribution(self,
                                            headers=None,
                                            payload=None,
                                            active_validation=True,
                                            **request_parameters):
        """Distributes a software image on a given device. Software image
        must be imported successfully into DNA Center before it
        can be distributed.

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

        _payload = payload or []
        if active_validation:
            self._request_validator('jsd_8cb6783b4faba1f4_v1_3_1')\
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

        return self._object_factory('bpm_8cb6783b4faba1f4_v1_3_1', json_data)

    def import_software_image_via_url(self,
                                      schedule_at=None,
                                      schedule_desc=None,
                                      schedule_origin=None,
                                      headers=None,
                                      payload=None,
                                      active_validation=True,
                                      **request_parameters):
        """Fetches a software image from remote file system (using URL for
        HTTP/FTP) and uploads to DNA Center. Supported image
        files extensions are bin, img, tar, smu, pie, aes, iso,
        ova, tar_gz and qcow2.

        Args:
            schedule_at(basestring): Epoch Time (The number of milli-seconds since January 1 1970 UTC) at which the
                distribution should be scheduled (Optional) .
            schedule_desc(basestring): Custom Description (Optional).
            schedule_origin(basestring): Originator of this call (Optional).
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
        check_type(schedule_at, basestring)
        check_type(schedule_desc, basestring)
        check_type(schedule_origin, basestring)
        if headers is not None:
            if 'Content-Type' in headers:
                check_type(headers.get('Content-Type'),
                           basestring, may_be_none=False)
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

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
            self._request_validator('jsd_bc8aab4746ca883d_v1_3_1')\
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

        return self._object_factory('bpm_bc8aab4746ca883d_v1_3_1', json_data)

    def trigger_software_image_activation(self,
                                          schedule_validate=None,
                                          headers=None,
                                          payload=None,
                                          active_validation=True,
                                          **request_parameters):
        """Activates a software image on a given device. Software image
        must be present in the device flash.

        Args:
            schedule_validate(bool): scheduleValidate, validates data before schedule (Optional).
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
                           basestring, may_be_none=False)
            if 'Client-Type' in headers:
                check_type(headers.get('Client-Type'),
                           basestring)
            if 'Client-Url' in headers:
                check_type(headers.get('Client-Url'),
                           basestring)
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           basestring, may_be_none=False)

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
            self._request_validator('jsd_fb9beb664f2aba4c_v1_3_1')\
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

        return self._object_factory('bpm_fb9beb664f2aba4c_v1_3_1', json_data)

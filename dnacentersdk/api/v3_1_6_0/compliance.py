# -*- coding: utf-8 -*-
"""Cisco Catalyst Center Compliance API wrapper.

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
    deprecated,
)


class Compliance(object):
    """Cisco Catalyst Center Compliance API (version: 3.1.6.0).

    Wraps the Catalyst Center Compliance
    API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new Compliance
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Catalyst Center service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(Compliance, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def get_compliance_status_(
        self,
        compliance_status=None,
        device_uuid=None,
        limit=None,
        offset=None,
        headers=None,
        **request_parameters
    ):
        """Return compliance status of device(s).

        Args:
            compliance_status(str): complianceStatus query parameter. Specify "Compliance status(es)" separated by
                commas. The Compliance status can be 'COMPLIANT', 'NON_COMPLIANT', 'IN_PROGRESS',
                'NOT_AVAILABLE', 'NOT_APPLICABLE', 'ERROR'.
            device_uuid(str): deviceUuid query parameter. Comma separated 'Device Ids'.
            offset(int): offset query parameter. offset/starting row        number.
            limit(int): limit query parameter. The number of records to be retrieved defaults to 500 if not
                specified, with a maximum allowed limit of 500.
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
        https://developer.cisco.com/docs/dna-center/#!get-compliance-status
        """
        return self.get_compliance_status(
            compliance_status=compliance_status,
            device_uuid=device_uuid,
            limit=limit,
            offset=offset,
            headers=headers,
            **request_parameters
        )

    def get_compliance_status(
        self,
        compliance_status=None,
        device_uuid=None,
        limit=None,
        offset=None,
        headers=None,
        **request_parameters
    ):
        """Return compliance status of device(s).

        Args:
            compliance_status(str): complianceStatus query parameter. Specify "Compliance status(es)" separated by
                commas. The Compliance status can be 'COMPLIANT', 'NON_COMPLIANT', 'IN_PROGRESS',
                'NOT_AVAILABLE', 'NOT_APPLICABLE', 'ERROR'.
            device_uuid(str): deviceUuid query parameter. Comma separated 'Device Ids'.
            offset(int): offset query parameter. offset/starting row        number.
            limit(int): limit query parameter. The number of records to be retrieved defaults to 500 if not
                specified, with a maximum allowed limit of 500.
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
            https://developer.cisco.com/docs/dna-center/#!get-compliance-status
        """
        check_type(headers, dict)
        check_type(compliance_status, str)
        check_type(device_uuid, str)
        check_type(offset, int)
        check_type(limit, int)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "complianceStatus": compliance_status,
            "deviceUuid": device_uuid,
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

        e_url = "/dna/intent/api/v1/compliance"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a1de7ff46fa5da09c5051c06ad07f2c_v3_1_6_0", json_data
        )

    def run_compliance(
        self,
        categories=None,
        deviceUuids=None,
        triggerFull=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Run compliance check for device(s).

        Args:
            categories(list): Compliance's Category can have any value among 'INTENT'(mapped to compliance types:
                NETWORK_SETTINGS,NETWORK_PROFILE,WORKFLOW,FABRIC,APPLICATION_VISIBILITY),
                'RUNNING_CONFIG' , 'IMAGE' , 'PSIRT' , 'EOX' (list of strings).
            deviceUuids(list): Compliance's UUID of the device. (list of strings).
            triggerFull(boolean): Compliance's if it is true then compliance will be triggered for all categories.
                If it is false then compliance will be triggered for categories mentioned in categories
                section .
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
            https://developer.cisco.com/docs/dna-center/#!run-compliance
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
            "triggerFull": triggerFull,
            "categories": categories,
            "deviceUuids": deviceUuids,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator("jsd_a0a8d545698d1d59a9be90e51_v3_1_6_0").validate(
                _payload
            )

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/compliance/"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(
                endpoint_full_url, params=_params, json=_payload, headers=_headers
            )
        else:
            json_data = self._session.post(
                endpoint_full_url, params=_params, json=_payload
            )

        return self._object_factory("bpm_a0a8d545698d1d59a9be90e51_v3_1_6_0", json_data)

    def get_compliance_status_count(
        self, compliance_status=None, headers=None, **request_parameters
    ):
        """Return Compliance Status Count.

        Args:
            compliance_status(str): complianceStatus query parameter. Specify "Compliance status(es)" separated by
                commas. The Compliance status can be 'COMPLIANT', 'NON_COMPLIANT', 'IN_PROGRESS',
                'NOT_AVAILABLE', 'NOT_APPLICABLE', 'ERROR'.
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
            https://developer.cisco.com/docs/dna-center/#!get-compliance-status-count
        """
        check_type(headers, dict)
        check_type(compliance_status, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "complianceStatus": compliance_status,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/compliance/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c37ce8136584f9e2ed471fc896ef9_v3_1_6_0", json_data
        )

    def get_compliance_detail(
        self,
        compliance_status=None,
        compliance_type=None,
        device_uuid=None,
        limit=None,
        offset=None,
        headers=None,
        **request_parameters
    ):
        """Return Compliance Detail.

        Args:
            compliance_type(str): complianceType query parameter. Specify "Compliance type(s)" in commas. The
                Compliance type can be 'NETWORK_PROFILE', 'IMAGE', 'FABRIC', 'APPLICATION_VISIBILITY',
                'FABRIC', RUNNING_CONFIG', 'NETWORK_SETTINGS', 'WORKFLOW' , 'EOX'.
            compliance_status(str): complianceStatus query parameter. Specify "Compliance status(es)" in commas. The
                Compliance status can be 'COMPLIANT', 'NON_COMPLIANT', 'IN_PROGRESS', 'NOT_AVAILABLE',
                'NOT_APPLICABLE', 'ERROR'.
            device_uuid(str): deviceUuid query parameter. Comma separated "Device Id(s)".
            offset(int): offset query parameter. offset/starting row.
            limit(int): limit query parameter. The number of records to be retrieved defaults to 500 if not
                specified, with a maximum allowed limit of 500.
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
            https://developer.cisco.com/docs/dna-center/#!get-compliance-detail
        """
        check_type(headers, dict)
        check_type(compliance_type, str)
        check_type(compliance_status, str)
        check_type(device_uuid, str)
        check_type(offset, int)
        check_type(limit, int)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "complianceType": compliance_type,
            "complianceStatus": compliance_status,
            "deviceUuid": device_uuid,
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

        e_url = "/dna/intent/api/v1/compliance/detail"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_adeaeb8157da972efb7b91e1e2cb_v3_1_6_0", json_data
        )

    def get_compliance_detail_count(
        self,
        compliance_status=None,
        compliance_type=None,
        headers=None,
        **request_parameters
    ):
        """Return  Compliance Count Detail.

        Args:
            compliance_type(str): complianceType query parameter. Specify "Compliance type(s)" separated by commas.
                The Compliance type can be 'APPLICATION_VISIBILITY', 'EOX', 'FABRIC', 'IMAGE',
                'NETWORK_PROFILE', 'NETWORK_SETTINGS', 'PSIRT', 'RUNNING_CONFIG', 'WORKFLOW'.
            compliance_status(str): complianceStatus query parameter. Specify "Compliance status(es)" separated by
                commas. The Compliance status can be 'COMPLIANT', 'NON_COMPLIANT', 'IN_PROGRESS',
                'NOT_AVAILABLE', 'NOT_APPLICABLE', 'ERROR'.
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
            https://developer.cisco.com/docs/dna-center/#!get-compliance-detail-count
        """
        check_type(headers, dict)
        check_type(compliance_type, str)
        check_type(compliance_status, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "complianceType": compliance_type,
            "complianceStatus": compliance_status,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/compliance/detail/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_d3d38fed534f5aeaa80f5a8c63694708_v3_1_6_0", json_data
        )

    def compliance_remediation(self, id, headers=None, **request_parameters):
        """Remediates configuration compliance issues. Compliance issues related to 'Routing', 'HA Remediation', 'Software
        Image', 'Securities Advisories', 'SD-Access Unsupported Configuration', 'Workflow', etc. will not be
        addressed by this API.  Warning: Fixing compliance mismatches could result in a possible network flap.

        Args:
            id(str): id path parameter. Network device identifier.
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
            https://developer.cisco.com/docs/dna-center/#!compliance-remediation
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

        e_url = (
            "/dna/intent/api/v1/compliance/networkDevices/{id}/issues"
            + "/remediation/provision"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.post(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a233477d86a459eab3c5e9352c1c9d3e_v3_1_6_0", json_data
        )

    def retrieve_the_violating_policies(
        self,
        network_device_id,
        limit=None,
        offset=None,
        headers=None,
        **request_parameters
    ):
        """Retrieve the details of violating compliance policies for the network device.

        Args:
            network_device_id(str): networkDeviceId path parameter. The `id` of the network device.
            offset(int): offset query parameter. The first record to show for this page; the first record is
                numbered 1.
            limit(int): limit query parameter. The number of records to show for this page. Default is 500 if not
                specified. Maximum allowed limit is 500.
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
            https://developer.cisco.com/docs/dna-center/#!retrieve-the-violating-policies
        """
        check_type(headers, dict)
        check_type(offset, int)
        check_type(limit, int)
        check_type(network_device_id, str, may_be_none=False)
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
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/compliance/networkDevices/{networkDev"
            + "iceId}/detail/policys"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory("bpm_b12c05818915b94f985d903f8_v3_1_6_0", json_data)

    def retrieve_the_policy_violations(
        self,
        network_device_id,
        policy_id,
        limit=None,
        offset=None,
        headers=None,
        **request_parameters
    ):
        """Retrieve the violation details of the compliance policy for the network device.

        Args:
            network_device_id(str): networkDeviceId path parameter. The `id` of the network device.
            policy_id(str): policyId path parameter. The `id` of the compliance policy.
            offset(int): offset query parameter. The first record to show for this page; the first record is
                numbered 1.
            limit(int): limit query parameter. The number of records to show for this page. Default is 500 if not
                specified. Maximum allowed limit is 500.
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
            https://developer.cisco.com/docs/dna-center/#!retrieve-the-policy-violations
        """
        check_type(headers, dict)
        check_type(offset, int)
        check_type(limit, int)
        check_type(network_device_id, str, may_be_none=False)
        check_type(policy_id, str, may_be_none=False)
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
            "policyId": policy_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/compliance/networkDevices/{networkDev"
            + "iceId}/detail/policys/{policyId}/violations"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_f77405fe5d3f59b2b05445d36358adaf_v3_1_6_0", json_data
        )

    def device_compliance_status(self, device_uuid, headers=None, **request_parameters):
        """Return compliance status of a device.

        Args:
            device_uuid(str): deviceUuid path parameter. Device Id.
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
            https://developer.cisco.com/docs/dna-center/#!device-compliance-status
        """
        check_type(headers, dict)
        check_type(device_uuid, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "deviceUuid": device_uuid,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/compliance/{deviceUuid}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_da8e5cdd435db0b1da1684be8f15b8_v3_1_6_0", json_data
        )

    def compliance_details_of_device(
        self,
        device_uuid,
        category=None,
        compliance_type=None,
        diff_list=None,
        remediation_supported=None,
        status=None,
        headers=None,
        **request_parameters
    ):
        """Return compliance detailed report for a device.

        Args:
            device_uuid(str): deviceUuid path parameter. Device Id.
            category(str): category query parameter. category can have any value among 'INTENT', 'RUNNING_CONFIG' ,
                'IMAGE' , 'PSIRT' , 'DESIGN_OOD' , 'EOX' , 'NETWORK_SETTINGS'.
            compliance_type(str): complianceType query parameter. Specify "Compliance type(s)" separated by commas.
                The Compliance type can be 'APPLICATION_VISIBILITY', 'EOX', 'FABRIC', 'IMAGE',
                'NETWORK_PROFILE', 'NETWORK_SETTINGS', 'PSIRT', 'RUNNING_CONFIG', 'WORKFLOW'.
            diff_list(bool): diffList query parameter. diff list [ pass true to fetch the diff list ].
            status(str): status query parameter. 'COMPLIANT', 'NON_COMPLIANT', 'ERROR', 'IN_PROGRESS',
                'NOT_APPLICABLE', 'NOT_AVAILABLE', 'WARNING', 'REMEDIATION_IN_PROGRESS' can be the value
                of the compliance 'status' parameter. [COMPLIANT: Device currently meets the compliance
                requirements.  NON_COMPLIANT: One of the compliance requirements like Software Image,
                PSIRT, Network Profile, Startup vs Running, etc. are not met. ERROR: Compliance is
                unable to compute status due to underlying errors. IN_PROGRESS: Compliance check is in
                progress for the device. NOT_APPLICABLE: Device is not supported for compliance, or
                minimum license requirement is not met. NOT_AVAILABLE: Compliance is not available for
                the device. COMPLIANT_WARNING: The device is compliant with warning if the last date of
                support is nearing. REMEDIATION_IN_PROGRESS: Compliance remediation is in progress for
                the device.].
            remediation_supported(bool): remediationSupported query parameter. The 'remediationSupported' parameter
                can be set to 'true' or 'false'. The result will be a combination of both values if it
                is not provided.
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
            https://developer.cisco.com/docs/dna-center/#!compliance-details-of-device
        """
        check_type(headers, dict)
        check_type(category, str)
        check_type(compliance_type, str)
        check_type(diff_list, bool)
        check_type(status, str)
        check_type(remediation_supported, bool)
        check_type(device_uuid, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "category": category,
            "complianceType": compliance_type,
            "diffList": diff_list,
            "status": status,
            "remediationSupported": remediation_supported,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "deviceUuid": device_uuid,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/compliance/{deviceUuid}/detail"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_b70e1b6a2f51a59690669a4b2fd3f0_v3_1_6_0", json_data
        )

    def retrieve_the_policies(
        self,
        limit=None,
        name=None,
        offset=None,
        policy_id=None,
        headers=None,
        **request_parameters
    ):
        """Retrieves the list of compliance policies.

        Args:
            policy_id(str): policyId query parameter. The IDs of the compliance policies. The number of policyId(s)
                must not exceed 25.
            name(str): name query parameter. Filter with policy name. Supports partial case-insensitive search.
            offset(int): offset query parameter. The first record to show for this page; the first record is
                numbered 1.
            limit(int): limit query parameter. The number of records to show for this page. Default is 500 if not
                specified. Maximum allowed limit is 500.
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
            https://developer.cisco.com/docs/dna-center/#!retrieve-the-policies
        """
        check_type(headers, dict)
        check_type(policy_id, str)
        check_type(name, str)
        check_type(offset, int)
        check_type(limit, int)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "policyId": policy_id,
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

        e_url = "/dna/intent/api/v1/compliancePolicys"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_e4d1fc1b50b5b7a976f7b918453aaf8_v3_1_6_0", json_data
        )

    def create_a_new_policy(
        self,
        description=None,
        name=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This API operation creates a new compliance policy. It is recommended to have no more than 500 policies in the
        system.

        Args:
            description(string): Compliance's An optional field for providing a detailed description of the
                compliance policy.
            name(string): Compliance's The unique name of the compliance policy.
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
            https://developer.cisco.com/docs/dna-center/#!create-a-new-policy
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
            "description": description,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator("jsd_fdfba50738387ab89bede6252_v3_1_6_0").validate(
                _payload
            )

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/compliancePolicys"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(
                endpoint_full_url, params=_params, json=_payload, headers=_headers
            )
        else:
            json_data = self._session.post(
                endpoint_full_url, params=_params, json=_payload
            )

        return self._object_factory("bpm_fdfba50738387ab89bede6252_v3_1_6_0", json_data)

    def retrieve_the_count_of_policies(
        self,
        name=None,
        policy_id=None,
        site_id=None,
        headers=None,
        **request_parameters
    ):
        """Retrieves the count of compliance policies.

        Args:
            policy_id(str): policyId query parameter. The IDs of the compliance policies.The number of policyId(s)
                must not exceed 25.
            name(str): name query parameter. Filter with policy name. Supports partial case-insensitive search.
            site_id(str): siteId query parameter. The `id` of the site to which compliance policies are associated.
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
            https://developer.cisco.com/docs/dna-center/#!retrieve-the-count-of-policies
        """
        check_type(headers, dict)
        check_type(policy_id, str)
        check_type(name, str)
        check_type(site_id, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "policyId": policy_id,
            "name": name,
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

        e_url = "/dna/intent/api/v1/compliancePolicys/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_f7125969fcf0572597a99c8b8ce071c8_v3_1_6_0", json_data
        )

    def delete_a_specific_policy(self, id, headers=None, **request_parameters):
        """Deletes a specific compliance policy. This operation also removes the rules, conditions, and variables within
        the policy.

        Args:
            id(str): id path parameter. The `id` of the compliance policy.
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
            https://developer.cisco.com/docs/dna-center/#!delete-a-specific-policy
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

        e_url = "/dna/intent/api/v1/compliancePolicys/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ecbcd3aa7abb552d9123b8c8c6b194a0_v3_1_6_0", json_data
        )

    def retrieve_a_specific_policy(self, id, headers=None, **request_parameters):
        """Retrieves the details of a specific compliance policy.

        Args:
            id(str): id path parameter. The `id` of the compliance policy.
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
            https://developer.cisco.com/docs/dna-center/#!retrieve-a-specific-policy
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

        e_url = "/dna/intent/api/v1/compliancePolicys/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ca810854e3285927bd7fa0b36d0b2322_v3_1_6_0", json_data
        )

    def update_an_existing_policy(
        self,
        id,
        description=None,
        name=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Updates the details of an existing compliance policy.

        Args:
            description(string): Compliance's An optional field for providing a detailed description of the
                compliance policy.
            name(string): Compliance's The unique name of the compliance policy.
            id(str): id path parameter. The `id` of the compliance policy.
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
            https://developer.cisco.com/docs/dna-center/#!update-an-existing-policy
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
            "name": name,
            "description": description,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_f50ab34f58526bb0ed8aa910f47f24_v3_1_6_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/compliancePolicys/{id}"
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
            "bpm_f50ab34f58526bb0ed8aa910f47f24_v3_1_6_0", json_data
        )

    def retrieve_the_rules(
        self, policy_id, limit=None, offset=None, headers=None, **request_parameters
    ):
        """Retrieves the list of rules under the specified compliance policy.

        Args:
            policy_id(str): policyId path parameter. The `id` of the compliance policy.
            offset(int): offset query parameter. The first record to show for this page; the first record is
                numbered 1.
            limit(int): limit query parameter. The number of records to show for this page. Default is 500 if not
                specified. Maximum allowed limit is 500.
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
            https://developer.cisco.com/docs/dna-center/#!retrieve-the-rules
        """
        check_type(headers, dict)
        check_type(offset, int)
        check_type(limit, int)
        check_type(policy_id, str, may_be_none=False)
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
            "policyId": policy_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/compliancePolicys/{policyId}/rules"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a17e315a6e8af213a81d5c97c1_v3_1_6_0", json_data
        )

    def create_a_new_rule(
        self,
        policy_id,
        description=None,
        deviceTypes=None,
        impact=None,
        name=None,
        softwareType=None,
        suggestedFix=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This API operation creates a new rule within the specified compliance policy. A rule acts as a container for
        conditions that are specific to a software type and one or more device families. Additional filtering
        can be applied within the selected device families, such as by device series and models. It is
        recommended to have no more than 20 rules within a policy.

        Args:
            description(string): Compliance's A comprehensive description of the rule. This should provide detailed
                information about what the rule does, its scope, and any other pertinent details that
                explain its function and purpose.
            deviceTypes(list): Compliance's deviceTypes (list of objects).
            impact(string): Compliance's This describes the potential impact when the conditions of this rule are
                violated.
            name(string): Compliance's This is the name of the rule. It should be a concise and descriptive title
                that clearly identifies the rule's purpose or function. The name must be unique within
                the specified policy.
            softwareType(string): Compliance's Specifies the software type applicable to the rule. For detailed enum
                descriptions, refer to the `Features` tab.. Available values are 'IOS, IOS_XE,
                CISCO_CONTROLLER'.
            suggestedFix(string): Compliance's Suggestions on how to fix the issues detected by this rule.
            policy_id(str): policyId path parameter. The `id` of the compliance policy.
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
            https://developer.cisco.com/docs/dna-center/#!create-a-new-rule
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(policy_id, str, may_be_none=False)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "policyId": policy_id,
        }
        _payload = {
            "name": name,
            "description": description,
            "impact": impact,
            "suggestedFix": suggestedFix,
            "softwareType": softwareType,
            "deviceTypes": deviceTypes,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_f7a0cdee493d597e816e012afbcc928d_v3_1_6_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/compliancePolicys/{policyId}/rules"
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
            "bpm_f7a0cdee493d597e816e012afbcc928d_v3_1_6_0", json_data
        )

    def retrieve_the_count_of_rules(
        self, policy_id, headers=None, **request_parameters
    ):
        """Retrieves the count of rules under the specified compliance policy.

        Args:
            policy_id(str): policyId path parameter. The `id` of the compliance policy.
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
            https://developer.cisco.com/docs/dna-center/#!retrieve-the-count-of-rules
        """
        check_type(headers, dict)
        check_type(policy_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "policyId": policy_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/compliancePolicys/{policyId}/rules/co" + "unt"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_d0cf3341d554ccb0dab6a6444ad747_v3_1_6_0", json_data
        )

    def delete_a_specific_rule(self, id, policy_id, headers=None, **request_parameters):
        """Deletes the rule within the specified compliance policy.  This operation also removes the conditions and
        variables associated with the rule.

        Args:
            policy_id(str): policyId path parameter. The `id` of the compliance policy.
            id(str): id path parameter. The `id` of the rule within the compliance policy.
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
            https://developer.cisco.com/docs/dna-center/#!delete-a-specific-rule
        """
        check_type(headers, dict)
        check_type(policy_id, str, may_be_none=False)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "policyId": policy_id,
            "id": id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/compliancePolicys/{policyId}/rules/{i" + "d}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ae58a079ac705cba94b721c4f964871b_v3_1_6_0", json_data
        )

    def retrieve_a_specific_rule(
        self, id, policy_id, headers=None, **request_parameters
    ):
        """Retrieves the details of a rule under the specified compliance policy.

        Args:
            policy_id(str): policyId path parameter. The `id` of the compliance policy.
            id(str): id path parameter. The `id` of the rule within the compliance policy.
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
            https://developer.cisco.com/docs/dna-center/#!retrieve-a-specific-rule
        """
        check_type(headers, dict)
        check_type(policy_id, str, may_be_none=False)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "policyId": policy_id,
            "id": id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/compliancePolicys/{policyId}/rules/{i" + "d}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_e67ac393f9f55c93b7911cf4053be19d_v3_1_6_0", json_data
        )

    def update_an_existing_rule(
        self,
        id,
        policy_id,
        description=None,
        deviceTypes=None,
        impact=None,
        name=None,
        softwareType=None,
        suggestedFix=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Updates the details of an existing rule within the specified compliance policy.

        Args:
            description(string): Compliance's A comprehensive description of the rule. This should provide detailed
                information about what the rule does, its scope, and any other pertinent details that
                explain its function and purpose.
            deviceTypes(list): Compliance's deviceTypes (list of objects).
            impact(string): Compliance's This describes the potential impact when the conditions of this rule are
                violated.
            name(string): Compliance's This is the name of the rule. It should be a concise and descriptive title
                that clearly identifies the rule's purpose or function. The name must be unique within
                the specified policy.
            softwareType(string): Compliance's Specifies the software type applicable to the rule. For detailed enum
                descriptions, refer to the `Features` tab.. Available values are 'IOS, IOS_XE,
                CISCO_CONTROLLER'.
            suggestedFix(string): Compliance's Suggestions on how to fix the issues detected by this rule.
            policy_id(str): policyId path parameter. The `id` of the compliance policy.
            id(str): id path parameter. The `id` of the rule within the compliance policy.
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
            https://developer.cisco.com/docs/dna-center/#!update-an-existing-rule
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(policy_id, str, may_be_none=False)
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
            "policyId": policy_id,
            "id": id,
        }
        _payload = {
            "name": name,
            "description": description,
            "impact": impact,
            "suggestedFix": suggestedFix,
            "softwareType": softwareType,
            "deviceTypes": deviceTypes,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_feb78fec3e454e1bd9dd531a6a29100_v3_1_6_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/compliancePolicys/{policyId}/rules/{i" + "d}"
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
            "bpm_feb78fec3e454e1bd9dd531a6a29100_v3_1_6_0", json_data
        )

    def retrieve_the_conditions(
        self,
        policy_id,
        rule_id,
        limit=None,
        offset=None,
        headers=None,
        **request_parameters
    ):
        """Retrieves the list of all conditions within the specified compliance policy and rule.  Use this to review
        conditions that are applied to ensure device compliance, such as checking for specific software versions
        or command outputs.

        Args:
            policy_id(str): policyId path parameter. The `id` of the compliance policy.
            rule_id(str): ruleId path parameter. The `id` of the rule within the compliance policy.
            offset(int): offset query parameter. The first record to show for this page; the first record is
                numbered 1.
            limit(int): limit query parameter. The number of records to show for this page. Default is 500 if not
                specified. Maximum allowed limit is 500.
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
            https://developer.cisco.com/docs/dna-center/#!retrieve-the-conditions
        """
        check_type(headers, dict)
        check_type(offset, int)
        check_type(limit, int)
        check_type(policy_id, str, may_be_none=False)
        check_type(rule_id, str, may_be_none=False)
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
            "policyId": policy_id,
            "ruleId": rule_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/compliancePolicys/{policyId}/rules/{r"
            + "uleId}/conditions"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_f73ad38bbbe15d65ba9526018bb4d03b_v3_1_6_0", json_data
        )

    def create_a_new_condition(
        self,
        policy_id,
        rule_id,
        action=None,
        blockEndExpression=None,
        blockStartExpression=None,
        blockViolationCriteria=None,
        deviceProperty=None,
        operator=None,
        parseAsBlocks=None,
        regexViolationCriteria=None,
        scope=None,
        showCommand=None,
        value=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This API operation creates a new condition within the specified compliance policy and rule. The condition
        defines specific checks for compliance based on device configurations and properties. For example, you
        can specify conditions that check for unauthorized SNMP community strings or ensure a minimum number of
        NTP servers are configured. New conditions get the sequence number assigned in the order of creation. It
        is recommended to have no more than 10 conditions within a rule.

        Args:
            action(object): Compliance's action.
            blockEndExpression(string): Compliance's The regular expression defining the end of a block. If not
                specified, block parsing will continue until new section starts in the configuration.
                This is applicable only when `parseAsBlocks` is set. This is an optional field.  The
                value, when provided, must be a valid regular expression.
            blockStartExpression(string): Compliance's The regular expression defining the start of a block. This is
                used to identify the beginning of relevant configuration sections.  This is applicable
                and required only when `parseAsBlocks` is set.  The value must be a valid regular
                expression.
            blockViolationCriteria(string): Compliance's Criteria determining when a violation is raised based on
                block evaluation results. This allows for flexible compliance checks depending on
                whether a single failure or all failures should trigger a violation.  For detailed enum
                descriptions, refer to the `Features` tab.. Available values are
                'RAISE_FOR_EACH_VIOLATION, RAISE_SINGLE_FOR_ANY_VIOLATION, RAISE_IF_ALL_VIOLATED'.
            deviceProperty(string): Compliance's The specific device property to consider as source for the
                condition. For detailed enum descriptions, refer to the `Features` tab.. Available
                values are 'DEVICE_NAME, IP_ADDRESS, OS_NAME, OS_VERSION'.
            operator(string): Compliance's The operation used to evaluate the condition. String, regular expression,
                and expressions required for the operator to work are provided in `value` attribute. For
                detailed enum descriptions, refer to the `Features` tab.. Available values are
                'CONTAINS_STRING, DOES_NOT_CONTAIN_STRING, MATCHES_EXPRESSION,
                DOES_NOT_MATCH_EXPRESSION, EVALUATE_EXPRESSION'.
            parseAsBlocks(boolean): Compliance's An optional param that indicates whether to parse the configuration
                as discrete blocks for evaluation. Useful for conditions that apply to specific sections
                of a configuration file.  This is applicable for all condition scopes except
                `DEVICE_PROPERTIES`. When scope is `PREVIOUSLY_MATCHED_BLOCKS`, this helps extract sub-
                blocks or portion of the blocks.  When this is set, `blockStartExpression` must be
                provided. Optionally, `blockEndExpression` can be provided to customise blocks further.
            regexViolationCriteria(string): Compliance's Criteria determining when a violation is raised based on
                regular expression evaluation results. This allows for flexible compliance checks
                depending on whether a single failure or all failures should trigger a violation. For
                detailed enum descriptions, refer to the `Features` tab.. Available values are
                'RAISE_FOR_EACH_VIOLATION, RAISE_SINGLE_FOR_ANY_VIOLATION, RAISE_IF_ALL_VIOLATED'.
            scope(string): Compliance's The source of data for the evaluation of the condition. For detailed enum
                descriptions, refer to the `Features` tab.. Available values are 'CONFIGURATION,
                DEVICE_PROPERTIES, DEVICE_COMMAND_OUTPUT, PREVIOUSLY_MATCHED_BLOCKS'.
            showCommand(string): Compliance's The command executed on the device to retrieve output for evaluation.
                Pattern: ^((S|s)(H|h)(O|o)(W|w))\\s+.+$ — The string must start with `show` (case-
                insensitive), followed by at least one space, and then any sequence of characters. For
                detailed information on using `show` command, refer to the `Features` tab.
            value(string): Compliance's The value or pattern used in the condition evaluation.  Custom variables and
                automatically generated regular expression group variables can both be used in this
                field. For detailed information on using variables, refer to the `Features` tab.
            policy_id(str): policyId path parameter. The `id` of the compliance policy.
            rule_id(str): ruleId path parameter. The `id` of the rule within the compliance policy.
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
            https://developer.cisco.com/docs/dna-center/#!create-a-new-condition
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(policy_id, str, may_be_none=False)
        check_type(rule_id, str, may_be_none=False)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "policyId": policy_id,
            "ruleId": rule_id,
        }
        _payload = {
            "scope": scope,
            "deviceProperty": deviceProperty,
            "showCommand": showCommand,
            "parseAsBlocks": parseAsBlocks,
            "blockStartExpression": blockStartExpression,
            "blockEndExpression": blockEndExpression,
            "blockViolationCriteria": blockViolationCriteria,
            "operator": operator,
            "regexViolationCriteria": regexViolationCriteria,
            "value": value,
            "action": action,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_ecb990ad7f24519397dd8d6c88de0067_v3_1_6_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/compliancePolicys/{policyId}/rules/{r"
            + "uleId}/conditions"
        )
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
            "bpm_ecb990ad7f24519397dd8d6c88de0067_v3_1_6_0", json_data
        )

    def retrieve_the_count_of_conditions(
        self, policy_id, rule_id, headers=None, **request_parameters
    ):
        """Retrieves the count of conditions under the specified compliance policy and rule.

        Args:
            policy_id(str): policyId path parameter. The `id` of the compliance policy.
            rule_id(str): ruleId path parameter.
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
            https://developer.cisco.com/docs/dna-center/#!retrieve-the-count-of-conditions
        """
        check_type(headers, dict)
        check_type(policy_id, str, may_be_none=False)
        check_type(rule_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "policyId": policy_id,
            "ruleId": rule_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/compliancePolicys/{policyId}/rules/{r"
            + "uleId}/conditions/count"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_bff7821a975285a23ccae23d08ebd1_v3_1_6_0", json_data
        )

    def delete_a_specific_condition(
        self, id, policy_id, rule_id, headers=None, **request_parameters
    ):
        """Deletes a specific condition within the specified compliance policy and rule.

        Args:
            policy_id(str): policyId path parameter. The `id` of the compliance policy.
            rule_id(str): ruleId path parameter. The `id` of the rule within the compliance policy.
            id(str): id path parameter. The `id` of the condition.
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
            https://developer.cisco.com/docs/dna-center/#!delete-a-specific-condition
        """
        check_type(headers, dict)
        check_type(policy_id, str, may_be_none=False)
        check_type(rule_id, str, may_be_none=False)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "policyId": policy_id,
            "ruleId": rule_id,
            "id": id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/compliancePolicys/{policyId}/rules/{r"
            + "uleId}/conditions/{id}"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c2eef5f8f6d5598866cd9da47a77842_v3_1_6_0", json_data
        )

    def retrieve_a_specific_condition(
        self, id, policy_id, rule_id, headers=None, **request_parameters
    ):
        """Retrieves a specific condition within the specified compliance policy and rule.  Use this to review a single
        condition that is applied to ensure device compliance.

        Args:
            policy_id(str): policyId path parameter. The `id` of the compliance policy.
            rule_id(str): ruleId path parameter. The `id` of the rule within the compliance policy.
            id(str): id path parameter. The `id` of the condition.
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
            https://developer.cisco.com/docs/dna-center/#!retrieve-a-specific-condition
        """
        check_type(headers, dict)
        check_type(policy_id, str, may_be_none=False)
        check_type(rule_id, str, may_be_none=False)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "policyId": policy_id,
            "ruleId": rule_id,
            "id": id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/compliancePolicys/{policyId}/rules/{r"
            + "uleId}/conditions/{id}"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_b254b9b8f2d059088f2bcad712ed4277_v3_1_6_0", json_data
        )

    def update_an_existing_condition(
        self,
        id,
        policy_id,
        rule_id,
        action=None,
        blockEndExpression=None,
        blockStartExpression=None,
        blockViolationCriteria=None,
        deviceProperty=None,
        operator=None,
        parseAsBlocks=None,
        regexViolationCriteria=None,
        scope=None,
        showCommand=None,
        value=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Updates an existing compliance condition within the specified compliance policy and rule. This operation cannot
        be used to change the sequence number or reorder the conditions. Note that the reorder conditions API
        will be provided in upcoming releases.

        Args:
            action(object): Compliance's action.
            blockEndExpression(string): Compliance's The regular expression defining the end of a block. If not
                specified, block parsing will continue until new section starts in the configuration.
                This is applicable only when `parseAsBlocks` is set. This is an optional field.  The
                value, when provided, must be a valid regular expression.
            blockStartExpression(string): Compliance's The regular expression defining the start of a block. This is
                used to identify the beginning of relevant configuration sections.  This is applicable
                and required only when `parseAsBlocks` is set.  The value must be a valid regular
                expression.
            blockViolationCriteria(string): Compliance's Criteria determining when a violation is raised based on
                block evaluation results. This allows for flexible compliance checks depending on
                whether a single failure or all failures should trigger a violation.  For detailed enum
                descriptions, refer to the `Features` tab.. Available values are
                'RAISE_FOR_EACH_VIOLATION, RAISE_SINGLE_FOR_ANY_VIOLATION, RAISE_IF_ALL_VIOLATED'.
            deviceProperty(string): Compliance's The specific device property to consider as source for the
                condition. For detailed enum descriptions, refer to the `Features` tab.. Available
                values are 'DEVICE_NAME, IP_ADDRESS, OS_NAME, OS_VERSION'.
            operator(string): Compliance's The operation used to evaluate the condition. String, regular expression,
                and expressions required for the operator to work are provided in `value` attribute. For
                detailed enum descriptions, refer to the `Features` tab.. Available values are
                'CONTAINS_STRING, DOES_NOT_CONTAIN_STRING, MATCHES_EXPRESSION,
                DOES_NOT_MATCH_EXPRESSION, EVALUATE_EXPRESSION'.
            parseAsBlocks(boolean): Compliance's An optional param that indicates whether to parse the configuration
                as discrete blocks for evaluation. Useful for conditions that apply to specific sections
                of a configuration file.  This is applicable for all condition scopes except
                `DEVICE_PROPERTIES`. When scope is `PREVIOUSLY_MATCHED_BLOCKS`, this helps extract sub-
                blocks or portion of the blocks.  When this is set, `blockStartExpression` must be
                provided. Optionally, `blockEndExpression` can be provided to customise blocks further.
            regexViolationCriteria(string): Compliance's Criteria determining when a violation is raised based on
                regular expression evaluation results. This allows for flexible compliance checks
                depending on whether a single failure or all failures should trigger a violation. For
                detailed enum descriptions, refer to the `Features` tab.. Available values are
                'RAISE_FOR_EACH_VIOLATION, RAISE_SINGLE_FOR_ANY_VIOLATION, RAISE_IF_ALL_VIOLATED'.
            scope(string): Compliance's The source of data for the evaluation of the condition. For detailed enum
                descriptions, refer to the `Features` tab.. Available values are 'CONFIGURATION,
                DEVICE_PROPERTIES, DEVICE_COMMAND_OUTPUT, PREVIOUSLY_MATCHED_BLOCKS'.
            showCommand(string): Compliance's The command executed on the device to retrieve output for evaluation.
                Pattern: ^((S|s)(H|h)(O|o)(W|w))\\s+.+$ — The string must start with `show` (case-
                insensitive), followed by at least one space, and then any sequence of characters. For
                detailed information on using `show` command, refer to the `Features` tab.
            value(string): Compliance's The value or pattern used in the condition evaluation.  Custom variables and
                automatically generated regular expression group variables can both be used in this
                field. For detailed information on using variables, refer to the `Features` tab.
            policy_id(str): policyId path parameter. The `id` of the compliance policy.
            rule_id(str): ruleId path parameter. The `id` of the rule within the compliance policy.
            id(str): id path parameter. The `id` of the condition.
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
            https://developer.cisco.com/docs/dna-center/#!update-an-existing-condition
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(policy_id, str, may_be_none=False)
        check_type(rule_id, str, may_be_none=False)
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
            "policyId": policy_id,
            "ruleId": rule_id,
            "id": id,
        }
        _payload = {
            "scope": scope,
            "deviceProperty": deviceProperty,
            "showCommand": showCommand,
            "parseAsBlocks": parseAsBlocks,
            "blockStartExpression": blockStartExpression,
            "blockEndExpression": blockEndExpression,
            "blockViolationCriteria": blockViolationCriteria,
            "operator": operator,
            "regexViolationCriteria": regexViolationCriteria,
            "value": value,
            "action": action,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_c024bb00458248144753c93dd8215_v3_1_6_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/compliancePolicys/{policyId}/rules/{r"
            + "uleId}/conditions/{id}"
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
            "bpm_c024bb00458248144753c93dd8215_v3_1_6_0", json_data
        )

    def retrieve_the_variables(
        self,
        policy_id,
        rule_id,
        limit=None,
        offset=None,
        headers=None,
        **request_parameters
    ):
        """Retrieves the list of all variables within the specified compliance policy and rule.

        Args:
            policy_id(str): policyId path parameter. The `id` of the compliance policy.
            rule_id(str): ruleId path parameter. The `id` of the rule within the compliance policy.
            offset(int): offset query parameter. The first record to show for this page; the first record is
                numbered 1.
            limit(int): limit query parameter. The number of records to show for this page. Default is 500 if not
                specified. Maximum allowed limit is 500.
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
            https://developer.cisco.com/docs/dna-center/#!retrieve-the-variables
        """
        check_type(headers, dict)
        check_type(offset, int)
        check_type(limit, int)
        check_type(policy_id, str, may_be_none=False)
        check_type(rule_id, str, may_be_none=False)
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
            "policyId": policy_id,
            "ruleId": rule_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/compliancePolicys/{policyId}/rules/{r"
            + "uleId}/variables"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_f0883863a905d0b9e14aee6936c3586_v3_1_6_0", json_data
        )

    def create_a_new_variable(
        self,
        policy_id,
        rule_id,
        dataType=None,
        defaultValue=None,
        description=None,
        identifier=None,
        inputType=None,
        mandatory=None,
        maxLength=None,
        maxValue=None,
        minValue=None,
        name=None,
        selectionList=None,
        validationRegex=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This API operation creates a new variable within the specified compliance policy and rule. New variables get the
        sequence number assigned in the order of creation. It is recommended to have no more than 10 variables
        within a rule. To understand how variable values are assigned and how inheritance works, please refer to
        the "Set site variables" API
        `/dna/intent/api/v1/compliancePolicys/{policyId}/sites/{siteId}/rules/{id}/variables`.

        Args:
            dataType(string): Compliance's The data type of the variable. IP mask is supported in IP address form
                (e.g., 255.255.255.0) only. Interface names must be provided in their full form, such as
                GigabitEthernet1/0/1.. Available values are 'STRING, INTEGER, BOOLEAN, IP_ADDRESS,
                INTERFACE_NAME, IP_MASK'.
            defaultValue(string): Compliance's The default value for the variable. This is applicable when
                `inputType` is `SINGLE_TEXT` or `MULTI_TEXT`.  Ensure that any type of data is formatted
                as a string, but it must match the required format for the data type and adhere to any
                provided constraints.
            description(string): Compliance's A brief description of the variable.
            identifier(string): Compliance's This is the identifier of the variable. Variables are referenced using
                the identifier enclosed in angle brackets.  Update operation cannot be used to change
                the identifier.
            inputType(string): Compliance's The input type of the variable. For detailed enum descriptions, refer to
                the `Features` tab.. Available values are 'SINGLE_SELECT, MULTI_SELECT, SINGLE_TEXT,
                MULTI_TEXT '.
            mandatory(boolean): Compliance's Indicates if the variable is mandatory.
            maxLength(integer): Compliance's The maximum length constraint for the `STRING` values. This is only
                applicable when the `inputType` is `SINGLE_TEXT` or `MULTI_TEXT`. Max length must be
                between 1 and 255, both inclusive.
            maxValue(integer): Compliance's The maximum value constraint for the `INTEGER` variable. This is only
                applicable when the `inputType` is `SINGLE_TEXT` or `MULTI_TEXT`.
            minValue(integer): Compliance's The minimum value constraint for the `INTEGER` variable. This is only
                applicable when the `inputType` is `SINGLE_TEXT` or `MULTI_TEXT`.
            name(string): Compliance's This is the name of the variable. It should be a concise and descriptive
                title that clearly identifies the variable. The name must be unique within the specified
                rule. pattern: ^[\\w\\ \\-\\(\\)]+$.
            selectionList(list): Compliance's selectionList (list of objects).
            validationRegex(string): Compliance's A regular expression pattern for constraining `STRING` values.
                This is only applicable when the `inputType` is `SINGLE_TEXT` or `MULTI_TEXT`.
            policy_id(str): policyId path parameter. The `id` of the compliance policy.
            rule_id(str): ruleId path parameter. The `id` of the rule within the compliance policy.
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
            https://developer.cisco.com/docs/dna-center/#!create-a-new-variable
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(policy_id, str, may_be_none=False)
        check_type(rule_id, str, may_be_none=False)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "policyId": policy_id,
            "ruleId": rule_id,
        }
        _payload = {
            "name": name,
            "description": description,
            "dataType": dataType,
            "mandatory": mandatory,
            "inputType": inputType,
            "selectionList": selectionList,
            "defaultValue": defaultValue,
            "maxLength": maxLength,
            "validationRegex": validationRegex,
            "minValue": minValue,
            "maxValue": maxValue,
            "identifier": identifier,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_b1ded5eaafa25e6b8814fa1cc0f9829a_v3_1_6_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/compliancePolicys/{policyId}/rules/{r"
            + "uleId}/variables"
        )
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
            "bpm_b1ded5eaafa25e6b8814fa1cc0f9829a_v3_1_6_0", json_data
        )

    def retrieve_the_count_of_variables(
        self, policy_id, rule_id, headers=None, **request_parameters
    ):
        """Retrieves the count of variables under the specified compliance policy and rule.

        Args:
            policy_id(str): policyId path parameter. The `id` of the compliance policy.
            rule_id(str): ruleId path parameter. The `id` of the rule within the compliance policy.
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
            https://developer.cisco.com/docs/dna-center/#!retrieve-the-count-of-variables
        """
        check_type(headers, dict)
        check_type(policy_id, str, may_be_none=False)
        check_type(rule_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "policyId": policy_id,
            "ruleId": rule_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/compliancePolicys/{policyId}/rules/{r"
            + "uleId}/variables/count"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a2a2ac82e53aeba856542a343a6d7_v3_1_6_0", json_data
        )

    def delete_a_specific_variable(
        self, id, policy_id, rule_id, headers=None, **request_parameters
    ):
        """Deletes a specific variable within the specified compliance policy and rule.  Note that a variable cannot be
        deleted if it is being used in a condition. Ensure that the variable is not referenced in any conditions
        before attempting deletion.

        Args:
            policy_id(str): policyId path parameter. The `id` of the compliance policy.
            rule_id(str): ruleId path parameter. The `id` of the rule within the compliance policy.
            id(str): id path parameter. The `id` of the variable.
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
            https://developer.cisco.com/docs/dna-center/#!delete-a-specific-variable
        """
        check_type(headers, dict)
        check_type(policy_id, str, may_be_none=False)
        check_type(rule_id, str, may_be_none=False)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "policyId": policy_id,
            "ruleId": rule_id,
            "id": id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/compliancePolicys/{policyId}/rules/{r"
            + "uleId}/variables/{id}"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a1be1aa4cd8c58e3aeefef124501c19b_v3_1_6_0", json_data
        )

    def retrieve_a_specific_variable(
        self, id, policy_id, rule_id, headers=None, **request_parameters
    ):
        """Retrieves a specific variable within the specified compliance policy and rule.

        Args:
            policy_id(str): policyId path parameter. The `id` of the compliance policy.
            rule_id(str): ruleId path parameter. The `id` of the rule within the compliance policy.
            id(str): id path parameter. The `id` of the variable.
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
            https://developer.cisco.com/docs/dna-center/#!retrieve-a-specific-variable
        """
        check_type(headers, dict)
        check_type(policy_id, str, may_be_none=False)
        check_type(rule_id, str, may_be_none=False)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "policyId": policy_id,
            "ruleId": rule_id,
            "id": id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/compliancePolicys/{policyId}/rules/{r"
            + "uleId}/variables/{id}"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_e6bad3aeee1356e89796eea887f1e03e_v3_1_6_0", json_data
        )

    def update_an_existing_variable(
        self,
        id,
        policy_id,
        rule_id,
        dataType=None,
        defaultValue=None,
        description=None,
        inputType=None,
        mandatory=None,
        maxLength=None,
        maxValue=None,
        minValue=None,
        name=None,
        selectionList=None,
        validationRegex=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Updates an existing compliance variable within the specified compliance policy and rule.  This operation cannot
        be used to change the sequence number or identifier of the variable. Note that the reorder variables API
        will be provided in upcoming releases.

        Args:
            dataType(string): Compliance's The data type of the variable. IP mask is supported in IP address form
                (e.g., 255.255.255.0) only. Interface names must be provided in their full form, such as
                GigabitEthernet1/0/1.. Available values are 'STRING, INTEGER, BOOLEAN, IP_ADDRESS,
                INTERFACE_NAME, IP_MASK'.
            defaultValue(string): Compliance's The default value for the variable. This is applicable when
                `inputType` is `SINGLE_TEXT` or `MULTI_TEXT`.  Ensure that any type of data is formatted
                as a string, but it must match the required format for the data type and adhere to any
                provided constraints.
            description(string): Compliance's A brief description of the variable.
            inputType(string): Compliance's The input type of the variable. For detailed enum descriptions, refer to
                the `Features` tab.. Available values are 'SINGLE_SELECT, MULTI_SELECT, SINGLE_TEXT,
                MULTI_TEXT '.
            mandatory(boolean): Compliance's Indicates if the variable is mandatory.
            maxLength(integer): Compliance's The maximum length constraint for the `STRING` values. This is only
                applicable when the `inputType` is `SINGLE_TEXT` or `MULTI_TEXT`. Max length must be
                between 1 and 255, both inclusive.
            maxValue(integer): Compliance's The maximum value constraint for the `INTEGER` variable. This is only
                applicable when the `inputType` is `SINGLE_TEXT` or `MULTI_TEXT`.
            minValue(integer): Compliance's The minimum value constraint for the `INTEGER` variable. This is only
                applicable when the `inputType` is `SINGLE_TEXT` or `MULTI_TEXT`.
            name(string): Compliance's This is the name of the variable. It should be a concise and descriptive
                title that clearly identifies the variable. The name must be unique within the specified
                rule. pattern: ^[\\w\\ \\-\\(\\)]+$.
            selectionList(list): Compliance's selectionList (list of objects).
            validationRegex(string): Compliance's A regular expression pattern for constraining `STRING` values.
                This is only applicable when the `inputType` is `SINGLE_TEXT` or `MULTI_TEXT`.
            policy_id(str): policyId path parameter. The `id` of the compliance policy.
            rule_id(str): ruleId path parameter. The `id` of the rule within the compliance policy.
            id(str): id path parameter. The `id` of the variable.
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
            https://developer.cisco.com/docs/dna-center/#!update-an-existing-variable
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(policy_id, str, may_be_none=False)
        check_type(rule_id, str, may_be_none=False)
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
            "policyId": policy_id,
            "ruleId": rule_id,
            "id": id,
        }
        _payload = {
            "name": name,
            "description": description,
            "dataType": dataType,
            "mandatory": mandatory,
            "inputType": inputType,
            "selectionList": selectionList,
            "defaultValue": defaultValue,
            "maxLength": maxLength,
            "validationRegex": validationRegex,
            "minValue": minValue,
            "maxValue": maxValue,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_dfc7c061f9259ee891e60fd91235129_v3_1_6_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/compliancePolicys/{policyId}/rules/{r"
            + "uleId}/variables/{id}"
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
            "bpm_dfc7c061f9259ee891e60fd91235129_v3_1_6_0", json_data
        )

    def retrieve_site_assignments_for_policy(
        self, policy_id, headers=None, **request_parameters
    ):
        """Retrieve the list of site IDs to which the compliance policy is assigned.

        Args:
            policy_id(str): policyId path parameter. The `id` of the compliance policy.
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
            https://developer.cisco.com/docs/dna-center/#!retrieve-site-assignments-for-policy
        """
        check_type(headers, dict)
        check_type(policy_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "policyId": policy_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/compliancePolicys/{policyId}/siteAssi" + "gnments"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ff2c6d88250757ad836564779835dc3d_v3_1_6_0", json_data
        )

    def set_site_assignments_for_policy(
        self,
        policy_id,
        siteIds=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Use this API to assign new sites to the policy, update existing site allocations, or delete all site assignments
        by passing an empty list.  When a site assignment is deleted, the associated variable values, if present
        for that site, will be cleared.

        Args:
            siteIds(list): Compliance's An array of root site IDs linked to the policy. The `id` of the policy root
                site. (list of strings).
            policy_id(str): policyId path parameter. The `id` of the compliance policy.
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
            https://developer.cisco.com/docs/dna-center/#!set-site-assignments-for-policy
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(policy_id, str, may_be_none=False)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "policyId": policy_id,
        }
        _payload = {
            "siteIds": siteIds,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_eec9550d3b5c9c9a10e65c3ef2fc2d_v3_1_6_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/compliancePolicys/{policyId}/siteAssi" + "gnments"
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
            "bpm_eec9550d3b5c9c9a10e65c3ef2fc2d_v3_1_6_0", json_data
        )

    def retrieve_site_variables(
        self,
        policy_id,
        rule_id,
        site_id,
        inherited=None,
        headers=None,
        **request_parameters
    ):
        """Retrieve the site variables for the specified rule within the compliance policy.

        Args:
            policy_id(str): policyId path parameter. The `id` of the compliance policy.
            site_id(str): siteId path parameter. The `id` of the site to which compliance policy is associated.
            rule_id(str): ruleId path parameter. The `id` of the rule within the compliance policy.
            inherited(bool): _inherited query parameter. Include values explicitly set for this site; when false,
                null values indicate that the site inherits these values from the parent site or a
                higher level in the site hierarchy.
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
            https://developer.cisco.com/docs/dna-center/#!retrieve-site-variables
        """
        check_type(headers, dict)
        check_type(inherited, bool)
        check_type(policy_id, str, may_be_none=False)
        check_type(site_id, str, may_be_none=False)
        check_type(rule_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "_inherited": inherited,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "policyId": policy_id,
            "siteId": site_id,
            "ruleId": rule_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/compliancePolicys/{policyId}/sites/{s"
            + "iteId}/rules/{ruleId}/variables"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ba0a122d6605486bc76945f27bd8fb7_v3_1_6_0", json_data
        )

    def set_site_variables(
        self,
        policy_id,
        rule_id,
        site_id,
        variableValues=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Set site variable values for the specified rule within the compliance policy.

        Args:
            variableValues(list): Compliance's variableValues (list of objects).
            policy_id(str): policyId path parameter. The `id` of the compliance policy.
            site_id(str): siteId path parameter. The `id` of the site to which compliance policy is associated.
            rule_id(str): ruleId path parameter. The `id` of the rule within the compliance policy.
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
            https://developer.cisco.com/docs/dna-center/#!set-site-variables
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(policy_id, str, may_be_none=False)
        check_type(site_id, str, may_be_none=False)
        check_type(rule_id, str, may_be_none=False)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "policyId": policy_id,
            "siteId": site_id,
            "ruleId": rule_id,
        }
        _payload = {
            "variableValues": variableValues,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_d715bf675b1250118d4b201d1419065e_v3_1_6_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/compliancePolicys/{policyId}/sites/{s"
            + "iteId}/rules/{ruleId}/variables"
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
            "bpm_d715bf675b1250118d4b201d1419065e_v3_1_6_0", json_data
        )

    def get_field_notice_network_devices(
        self,
        limit=None,
        network_device_id=None,
        notice_count=None,
        offset=None,
        order=None,
        scan_status=None,
        sort_by=None,
        headers=None,
        **request_parameters
    ):
        """Get field notice network devices.

        Args:
            network_device_id(str): networkDeviceId query parameter. Id of the network device.
            scan_status(str): scanStatus query parameter. Status of the scan on the network device. Available values
                : NOT_SCANNED, IN_PROGRESS, SUCCESS, FAILED.
            notice_count(int): noticeCount query parameter. Return network devices with noticeCount greater than
                this noticeCount.
            offset(int): offset query parameter. The first record to show for this page; the first record is
                numbered 1. Default value is 1.
            limit(int): limit query parameter. The number of records to show for this page. Minimum value is 1.
                Maximum value is 500. Default value is 500.
            sort_by(str): sortBy query parameter. A property within the response to sort by.
            order(str): order query parameter. Whether ascending or descending order should be used to sort the
                response. Available values : asc, desc. Default value is asc.
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
            https://developer.cisco.com/docs/dna-center/#!get-field-notice-network-devices
        """
        check_type(headers, dict)
        check_type(network_device_id, str)
        check_type(scan_status, str)
        check_type(notice_count, int)
        check_type(offset, int)
        check_type(limit, int)
        check_type(sort_by, str)
        check_type(order, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "networkDeviceId": network_device_id,
            "scanStatus": scan_status,
            "noticeCount": notice_count,
            "offset": offset,
            "limit": limit,
            "sortBy": sort_by,
            "order": order,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/fieldNotices/results/networkDevices"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_bf89c9e9897659e496ff2c2c2cfb8d35_v3_1_6_0", json_data
        )

    def get_count_of_field_notice_network_devices(
        self,
        network_device_id=None,
        notice_count=None,
        scan_status=None,
        headers=None,
        **request_parameters
    ):
        """Get count of field notice network devices.

        Args:
            network_device_id(str): networkDeviceId query parameter. Id of the network device.
            scan_status(str): scanStatus query parameter. Status of the scan on the network device. Available values
                : NOT_SCANNED, IN_PROGRESS, SUCCESS, FAILED.
            notice_count(int): noticeCount query parameter. Return network devices with noticeCount greater than
                this noticeCount.
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
            https://developer.cisco.com/docs/dna-center/#!get-count-of-field-notice-network-devices
        """
        check_type(headers, dict)
        check_type(network_device_id, str)
        check_type(scan_status, str)
        check_type(notice_count, int)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "networkDeviceId": network_device_id,
            "scanStatus": scan_status,
            "noticeCount": notice_count,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/fieldNotices/results/networkDevices/c" + "ount"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_f4a44a87cc51ffb9be1cb2a6bdfa68_v3_1_6_0", json_data
        )

    def get_field_notice_network_device_by_device_id(
        self, network_device_id, headers=None, **request_parameters
    ):
        """Get field notice network device by device id.

        Args:
            network_device_id(str): networkDeviceId path parameter. Id of the network device.
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
            https://developer.cisco.com/docs/dna-center/#!get-field-notice-network-device-by-device-id
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
            "/dna/intent/api/v1/fieldNotices/results/networkDevices/{"
            + "networkDeviceId}"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_f9138e17f05f57fda724a4767aa35ad4_v3_1_6_0", json_data
        )

    def get_field_notices_affecting_the_network_device(
        self,
        network_device_id,
        id=None,
        limit=None,
        offset=None,
        order=None,
        sort_by=None,
        type=None,
        headers=None,
        **request_parameters
    ):
        """Get field notices affecting the network device.

        Args:
            network_device_id(str): networkDeviceId path parameter. Id of the network device.
            id(str): id query parameter. Id of the field notice.
            type(str): type query parameter. Return field notices with this type. Available values : SOFTWARE,
                HARDWARE.
            offset(int): offset query parameter. The first record to show for this page; the first record is
                numbered 1. Default value is 1.
            limit(int): limit query parameter. The number of records to show for this page. Minimum value is 1.
                Maximum value is 500. Default value is 500.
            sort_by(str): sortBy query parameter. A property within the response to sort by.
            order(str): order query parameter. Whether ascending or descending order should be used to sort the
                response. Available values : asc, desc. Default value is asc.
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
            https://developer.cisco.com/docs/dna-center/#!get-field-notices-affecting-the-network-device
        """
        check_type(headers, dict)
        check_type(id, str)
        check_type(type, str)
        check_type(offset, int)
        check_type(limit, int)
        check_type(sort_by, str)
        check_type(order, str)
        check_type(network_device_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "id": id,
            "type": type,
            "offset": offset,
            "limit": limit,
            "sortBy": sort_by,
            "order": order,
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

        e_url = (
            "/dna/intent/api/v1/fieldNotices/results/networkDevices/{"
            + "networkDeviceId}/notices"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_f44a1efb2d0f53209fdc441a3bbf073f_v3_1_6_0", json_data
        )

    def get_count_of_field_notices_affecting_the_network_device(
        self, network_device_id, id=None, type=None, headers=None, **request_parameters
    ):
        """Get count of field notices affecting the network device.

        Args:
            network_device_id(str): networkDeviceId path parameter. Id of the network device.
            id(str): id query parameter. Id of the field notice.
            type(str): type query parameter. Return field notices with this type. Available values : SOFTWARE,
                HARDWARE.
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
            https://developer.cisco.com/docs/dna-center/#!get-count-of-field-notices-affecting-the-network-device
        """
        check_type(headers, dict)
        check_type(id, str)
        check_type(type, str)
        check_type(network_device_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "id": id,
            "type": type,
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

        e_url = (
            "/dna/intent/api/v1/fieldNotices/results/networkDevices/{"
            + "networkDeviceId}/notices/count"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_af749446fd572cbad63745a6d55c5a_v3_1_6_0", json_data
        )

    def get_field_notice_affecting_the_network_device_by_device_id_and_notice_id(
        self, id, network_device_id, headers=None, **request_parameters
    ):
        """Get field notice affecting the network device by device Id and notice id.

        Args:
            network_device_id(str): networkDeviceId path parameter. Id of the network device.
            id(str): id path parameter. Id of the field notice.
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
            https://developer.cisco.com/docs/dna-center/#!get-field-notice-affecting-the-network-device-by-device-id-and-notice-id
        """
        check_type(headers, dict)
        check_type(network_device_id, str, may_be_none=False)
        check_type(id, str, may_be_none=False)
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
            "/dna/intent/api/v1/fieldNotices/results/networkDevices/{"
            + "networkDeviceId}/notices/{id}"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_f585d782d15b54b89e227ab1d01e6f57_v3_1_6_0", json_data
        )

    def get_field_notices(
        self,
        device_count=None,
        id=None,
        limit=None,
        offset=None,
        order=None,
        sort_by=None,
        type=None,
        headers=None,
        **request_parameters
    ):
        """Get field notices.

        Args:
            id(str): id query parameter. Id of the field notice.
            device_count(int): deviceCount query parameter. Return field notices with deviceCount greater than this
                deviceCount.
            type(str): type query parameter. Return field notices with this type. Available values : SOFTWARE,
                HARDWARE.
            offset(int): offset query parameter. The first record to show for this page; the first record is
                numbered 1. Default value is 1.
            limit(int): limit query parameter. The number of records to show for this page. Minimum value is 1.
                Maximum value is 500. Default value is 500.
            sort_by(str): sortBy query parameter. A property within the response to sort by.
            order(str): order query parameter. Whether ascending or descending order should be used to sort the
                response. Available values : asc, desc. Default value is asc.
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
            https://developer.cisco.com/docs/dna-center/#!get-field-notices
        """
        check_type(headers, dict)
        check_type(id, str)
        check_type(device_count, int)
        check_type(type, str)
        check_type(offset, int)
        check_type(limit, int)
        check_type(sort_by, str)
        check_type(order, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "id": id,
            "deviceCount": device_count,
            "type": type,
            "offset": offset,
            "limit": limit,
            "sortBy": sort_by,
            "order": order,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/fieldNotices/results/notices"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_aa335c92d485537bab1126533ac8ed7_v3_1_6_0", json_data
        )

    def get_count_of_field_notices(
        self, device_count=None, id=None, type=None, headers=None, **request_parameters
    ):
        """Get count of field notices.

        Args:
            id(str): id query parameter. Id of the field notice.
            device_count(int): deviceCount query parameter. Return field notices with deviceCount greater than this
                deviceCount.
            type(str): type query parameter. Return field notices with this type. Available values : SOFTWARE,
                HARDWARE.
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
            https://developer.cisco.com/docs/dna-center/#!get-count-of-field-notices
        """
        check_type(headers, dict)
        check_type(id, str)
        check_type(device_count, int)
        check_type(type, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "id": id,
            "deviceCount": device_count,
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

        e_url = "/dna/intent/api/v1/fieldNotices/results/notices/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_b172bd7cd55378bd25e4ae525a9179_v3_1_6_0", json_data
        )

    def get_field_notice_by_id(self, id, headers=None, **request_parameters):
        """Get field notice by Id.

        Args:
            id(str): id path parameter. Id of the field notice.
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
            https://developer.cisco.com/docs/dna-center/#!get-field-notice-by-id
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

        e_url = "/dna/intent/api/v1/fieldNotices/results/notices/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_fc5e9ea9a5acd9e461b88355330ee_v3_1_6_0", json_data
        )

    def get_field_notice_network_devices_for_the_notice(
        self,
        id,
        limit=None,
        network_device_id=None,
        offset=None,
        order=None,
        scan_status=None,
        sort_by=None,
        headers=None,
        **request_parameters
    ):
        """Get field notice network devices for the notice.

        Args:
            id(str): id path parameter. Id of the field notice.
            network_device_id(str): networkDeviceId query parameter. Id of the network device.
            scan_status(str): scanStatus query parameter. Status of the scan on the network device. Available values
                : NOT_SCANNED, IN_PROGRESS, SUCCESS, FAILED.
            offset(int): offset query parameter. The first record to show for this page; the first record is
                numbered 1. Default value is 1.
            limit(int): limit query parameter. The number of records to show for this page. Minimum value is 1.
                Maximum value is 500. Default value is 500.
            sort_by(str): sortBy query parameter. A property within the response to sort by.
            order(str): order query parameter. Whether ascending or descending order should be used to sort the
                response. Available values : asc, desc. Default value is asc.
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
            https://developer.cisco.com/docs/dna-center/#!get-field-notice-network-devices-for-the-notice
        """
        check_type(headers, dict)
        check_type(network_device_id, str)
        check_type(scan_status, str)
        check_type(offset, int)
        check_type(limit, int)
        check_type(sort_by, str)
        check_type(order, str)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "networkDeviceId": network_device_id,
            "scanStatus": scan_status,
            "offset": offset,
            "limit": limit,
            "sortBy": sort_by,
            "order": order,
        }
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

        e_url = (
            "/dna/intent/api/v1/fieldNotices/results/notices/{id}/net" + "workDevices"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_e015bf018f55499a59aae5c54264bf4_v3_1_6_0", json_data
        )

    def get_count_of_field_notice_network_devices_for_the_notice(
        self,
        id,
        network_device_id=None,
        scan_status=None,
        headers=None,
        **request_parameters
    ):
        """Get count of field notice network devices for the notice.

        Args:
            id(str): id path parameter. Id of the field notice.
            network_device_id(str): networkDeviceId query parameter. id of the network device.
            scan_status(str): scanStatus query parameter. status of the scan on the network device. Available values
                : NOT_SCANNED, IN_PROGRESS, SUCCESS, FAILED.
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
            https://developer.cisco.com/docs/dna-center/#!get-count-of-field-notice-network-devices-for-the-notice
        """
        check_type(headers, dict)
        check_type(network_device_id, str)
        check_type(scan_status, str)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "networkDeviceId": network_device_id,
            "scanStatus": scan_status,
        }
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

        e_url = (
            "/dna/intent/api/v1/fieldNotices/results/notices/{id}/net"
            + "workDevices/count"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_cffe4d51a6508e8c18de0d45d78294_v3_1_6_0", json_data
        )

    def get_field_notice_network_device_for_the_notice_by_network_device_id(
        self, id, network_device_id, headers=None, **request_parameters
    ):
        """Get field notice network device for the notice by network device id.

        Args:
            id(str): id path parameter. Id of the field notice.
            network_device_id(str): networkDeviceId path parameter. Id of the network device.
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
            https://developer.cisco.com/docs/dna-center/#!get-field-notice-network-device-for-the-notice-by-network-device-id
        """
        check_type(headers, dict)
        check_type(id, str, may_be_none=False)
        check_type(network_device_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
            "networkDeviceId": network_device_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/fieldNotices/results/notices/{id}/net"
            + "workDevices/{networkDeviceId}"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_e9343c828f586da856c48c8edee40b_v3_1_6_0", json_data
        )

    def get_field_notices_results_trend_over_time(
        self,
        limit=None,
        offset=None,
        scan_time=None,
        headers=None,
        **request_parameters
    ):
        """Get field notices results trend over time. The default sort is by scan time descending.

        Args:
            scan_time(int): scanTime query parameter. Return field notices trend with scanTime greater than this
                scanTime.
            offset(int): offset query parameter. The first record to show for this page; the first record is
                numbered 1. Default value is 1.
            limit(int): limit query parameter. The number of records to show for this page. Minimum value is 1.
                Maximum value is 500. Default value is 500.
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
            https://developer.cisco.com/docs/dna-center/#!get-field-notices-results-trend-over-time
        """
        check_type(headers, dict)
        check_type(scan_time, int)
        check_type(offset, int)
        check_type(limit, int)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "scanTime": scan_time,
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

        e_url = "/dna/intent/api/v1/fieldNotices/resultsTrend"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory("bpm_a7065d7d9654a4015c6e961a_v3_1_6_0", json_data)

    def get_count_of_field_notices_results_trend_over_time(
        self, scan_time=None, headers=None, **request_parameters
    ):
        """Get count of field notices results trend over time.

        Args:
            scan_time(int): scanTime query parameter. Return field notices trend with scanTime greater than this
                scanTime.
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
            https://developer.cisco.com/docs/dna-center/#!get-count-of-field-notices-results-trend-over-time
        """
        check_type(headers, dict)
        check_type(scan_time, int)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "scanTime": scan_time,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/fieldNotices/resultsTrend/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_f89484e88e57b292756b0c7e54b553_v3_1_6_0", json_data
        )

    def get_trial_details_for_field_notices_detection_on_network_devices(
        self, headers=None, **request_parameters
    ):
        """Get trial details for field notices detection on network devices.

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
            https://developer.cisco.com/docs/dna-center/#!get-trial-details-for-field-notices-detection-on-network-devices
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

        e_url = "/dna/intent/api/v1/fieldNotices/trials"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_d3893f52738eaf50a6732d2159_v3_1_6_0", json_data
        )

    def creates_a_trial_for_field_notices_detection_on_network_devices(
        self, headers=None, **request_parameters
    ):
        """Creates a trial for field notices detection on network devices. The consent to connect agreement must have been
        accepted in the UI for this to succeed. Please refer to the user guide at   for more details on consent
        to connect.

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
            https://developer.cisco.com/docs/dna-center/#!creates-a-trial-for-field-notices-detection-on-network-devices
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

        e_url = "/dna/intent/api/v1/fieldNotices/trials"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.post(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_be66c0a0582fa234daaa2019b6b6_v3_1_6_0", json_data
        )

    def triggers_a_field_notices_scan_for_the_supported_network_devices(
        self, failed_devices_only=None, headers=None, **request_parameters
    ):
        """Triggers a field notices scan for the supported network devices. The supported devices are switches, routers and
        wireless controllers. If a device is not supported, the FieldNoticeNetworkDevice scanStatus will be
        Failed with appropriate comments. The consent to connect agreement must have been accepted in the UI for
        this to succeed. Please refer to the user guide at   for more details on consent to connect.

        Args:
            failed_devices_only(bool): failedDevicesOnly query parameter. Used to specify if the scan should run
                only for the network devices that failed during the previous scan. If not specified,
                this parameter defaults to false.
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
            https://developer.cisco.com/docs/dna-center/#!triggers-a-field-notices-scan-for-the-supported-network-devices
        """
        check_type(headers, dict)
        check_type(failed_devices_only, bool)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "failedDevicesOnly": failed_devices_only,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/fieldNotices/triggerScan"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.post(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_fd0f9b4adc5572da4ccc64802a275f5_v3_1_6_0", json_data
        )

    def get_config_task_details(
        self, parent_task_id, headers=None, **request_parameters
    ):
        """Returns a config task result details by specified id.

        Args:
            parent_task_id(str): parentTaskId query parameter. task Id.
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
            https://developer.cisco.com/docs/dna-center/#!get-config-task-details
        """
        check_type(headers, dict)
        check_type(parent_task_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "parentTaskId": parent_task_id,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/network-device-config/task"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_cb73c1c44665d1ebbe934dd380f4f5e_v3_1_6_0", json_data
        )

    def commit_device_configuration(
        self,
        deviceId=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This operation would commit device running configuration to startup by issuing "write memory" to device.

        Args:
            deviceId(list): Compliance's UUID of the device. (list of strings).
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
            https://developer.cisco.com/docs/dna-center/#!commit-device-configuration
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
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_ba40975123ed50daa2f9f599cdf2d911_v3_1_6_0"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/network-device-config/write-memory"
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
            "bpm_ba40975123ed50daa2f9f599cdf2d911_v3_1_6_0", json_data
        )

    def get_network_bugs(
        self,
        device_count=None,
        id=None,
        limit=None,
        offset=None,
        order=None,
        severity=None,
        sort_by=None,
        headers=None,
        **request_parameters
    ):
        """Get network bugs.

        Args:
            id(str): id query parameter. The id of the network bug.
            device_count(int): deviceCount query parameter. Return network bugs with deviceCount greater than this
                deviceCount.
            severity(str): severity query parameter. Return network bugs with this severity. Available values :
                CATASTROPHIC, SEVERE, MODERATE.
            offset(int): offset query parameter. The first record to show for this page; the first record is
                numbered 1. Default value is 1.
            limit(int): limit query parameter. The number of records to show for this page. Minimum value is 1.
                Maximum value is 500. Default value is 500.
            sort_by(str): sortBy query parameter. A property within the response to sort by.
            order(str): order query parameter. Whether ascending or descending order should be used to sort the
                response. Available values : asc, desc. Default value is asc.
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
            https://developer.cisco.com/docs/dna-center/#!get-network-bugs
        """
        check_type(headers, dict)
        check_type(id, str)
        check_type(device_count, int)
        check_type(severity, str)
        check_type(offset, int)
        check_type(limit, int)
        check_type(sort_by, str)
        check_type(order, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "id": id,
            "deviceCount": device_count,
            "severity": severity,
            "offset": offset,
            "limit": limit,
            "sortBy": sort_by,
            "order": order,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/networkBugs/results/bugs"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a3217129c2295b27838cf486a35626f8_v3_1_6_0", json_data
        )

    def get_count_of_network_bugs(
        self,
        device_count=None,
        id=None,
        severity=None,
        headers=None,
        **request_parameters
    ):
        """Get count of network bugs.

        Args:
            id(str): id query parameter. Id of the network bug.
            device_count(int): deviceCount query parameter. Return network bugs with deviceCount greater than this
                deviceCount.
            severity(str): severity query parameter. Return network bugs with this severity. Available values :
                CATASTROPHIC, SEVERE, MODERATE.
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
            https://developer.cisco.com/docs/dna-center/#!get-count-of-network-bugs
        """
        check_type(headers, dict)
        check_type(id, str)
        check_type(device_count, int)
        check_type(severity, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "id": id,
            "deviceCount": device_count,
            "severity": severity,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/networkBugs/results/bugs/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_e1ec0f16d5e57cab08414ece382334d_v3_1_6_0", json_data
        )

    def get_network_bug_by_id(self, id, headers=None, **request_parameters):
        """Get network bug by Id.

        Args:
            id(str): id path parameter. Id of the network bug.
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
            https://developer.cisco.com/docs/dna-center/#!get-network-bug-by-id
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

        e_url = "/dna/intent/api/v1/networkBugs/results/bugs/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a7663a127d59d9afc45d4daa0ba477_v3_1_6_0", json_data
        )

    def get_network_bug_devices_for_the_bug(
        self,
        id,
        limit=None,
        network_device_id=None,
        offset=None,
        order=None,
        scan_mode=None,
        scan_status=None,
        sort_by=None,
        headers=None,
        **request_parameters
    ):
        """Get network bug devices for the bug.

        Args:
            id(str): id path parameter. Id of the network bug.
            network_device_id(str): networkDeviceId query parameter. Id of the network device.
            scan_mode(str): scanMode query parameter. Mode or the criteria using which the network device was
                scanned. Available values : ESSENTIALS, ADVANTAGE, CX_CLOUD, NOT_AVAILABLE.
            scan_status(str): scanStatus query parameter. Status of the scan on the network device. Available values
                : NOT_SCANNED, IN_PROGRESS, SUCCESS, FAILED, FALL_BACK.
            offset(int): offset query parameter. The first record to show for this page; the first record is
                numbered 1. Default value is 1.
            limit(int): limit query parameter. The number of records to show for this page. Minimum value is 1.
                Maximum value is 500. Default value is 500.
            sort_by(str): sortBy query parameter. A property within the response to sort by.
            order(str): order query parameter. Whether ascending or descending order should be used to sort the
                response. Available values : asc, desc. Default value is asc.
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
            https://developer.cisco.com/docs/dna-center/#!get-network-bug-devices-for-the-bug
        """
        check_type(headers, dict)
        check_type(network_device_id, str)
        check_type(scan_mode, str)
        check_type(scan_status, str)
        check_type(offset, int)
        check_type(limit, int)
        check_type(sort_by, str)
        check_type(order, str)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "networkDeviceId": network_device_id,
            "scanMode": scan_mode,
            "scanStatus": scan_status,
            "offset": offset,
            "limit": limit,
            "sortBy": sort_by,
            "order": order,
        }
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

        e_url = "/dna/intent/api/v1/networkBugs/results/bugs/{id}/network" + "Devices"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_d10f773fa5522384790bf1f198d861_v3_1_6_0", json_data
        )

    def get_count_of_network_bug_devices_for_the_bug(
        self,
        id,
        network_device_id=None,
        scan_mode=None,
        scan_status=None,
        headers=None,
        **request_parameters
    ):
        """Get count of network bug devices for the bug.

        Args:
            id(str): id path parameter. Id of the network bug.
            network_device_id(str): networkDeviceId query parameter. Id of the network device.
            scan_mode(str): scanMode query parameter. Mode or the criteria using which the network device was
                scanned. Available values : ESSENTIALS, ADVANTAGE, CX_CLOUD, NOT_AVAILABLE.
            scan_status(str): scanStatus query parameter. Status of the scan on the network device. Available values
                : NOT_SCANNED, IN_PROGRESS, SUCCESS, FAILED, FALL_BACK.
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
            https://developer.cisco.com/docs/dna-center/#!get-count-of-network-bug-devices-for-the-bug
        """
        check_type(headers, dict)
        check_type(network_device_id, str)
        check_type(scan_mode, str)
        check_type(scan_status, str)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "networkDeviceId": network_device_id,
            "scanMode": scan_mode,
            "scanStatus": scan_status,
        }
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

        e_url = (
            "/dna/intent/api/v1/networkBugs/results/bugs/{id}/network" + "Devices/count"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c7afe7c0c5c2898eabb7cbbdc4ef4_v3_1_6_0", json_data
        )

    def get_network_bug_device_for_the_bug_by_network_device_id(
        self, id, network_device_id, headers=None, **request_parameters
    ):
        """Get network bug device for the bug by network device id.

        Args:
            id(str): id path parameter. Id of the network bug.
            network_device_id(str): networkDeviceId path parameter. Id of the network device.
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
            https://developer.cisco.com/docs/dna-center/#!get-network-bug-device-for-the-bug-by-network-device-id
        """
        check_type(headers, dict)
        check_type(id, str, may_be_none=False)
        check_type(network_device_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
            "networkDeviceId": network_device_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/networkBugs/results/bugs/{id}/network"
            + "Devices/{networkDeviceId}"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c369b19255b95cffb73b8061e01a1f7d_v3_1_6_0", json_data
        )

    def get_network_bug_devices(
        self,
        bug_count=None,
        limit=None,
        network_device_id=None,
        offset=None,
        order=None,
        scan_mode=None,
        scan_status=None,
        sort_by=None,
        headers=None,
        **request_parameters
    ):
        """Get network bug devices.

        Args:
            network_device_id(str): networkDeviceId query parameter. Id of the network device.
            scan_mode(str): scanMode query parameter. Mode or the criteria using which the network device was
                scanned. Available values : ESSENTIALS, ADVANTAGE, CX_CLOUD, NOT_AVAILABLE.
            scan_status(str): scanStatus query parameter. Status of the scan on the network device. Available values
                : NOT_SCANNED, IN_PROGRESS, SUCCESS, FAILED, FALL_BACK.
            bug_count(int): bugCount query parameter. Return network devices with bugCount greater than this
                bugCount.
            offset(int): offset query parameter. The first record to show for this page; the first record is
                numbered 1. Default value is 1.
            limit(int): limit query parameter. The number of records to show for this page. Minimum value is 1.
                Maximum value is 500. Default value is 500.
            sort_by(str): sortBy query parameter. A property within the response to sort by.
            order(str): order query parameter. Whether ascending or descending order should be used to sort the
                response. Available values : asc, desc. Default value is asc.
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
            https://developer.cisco.com/docs/dna-center/#!get-network-bug-devices
        """
        check_type(headers, dict)
        check_type(network_device_id, str)
        check_type(scan_mode, str)
        check_type(scan_status, str)
        check_type(bug_count, int)
        check_type(offset, int)
        check_type(limit, int)
        check_type(sort_by, str)
        check_type(order, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "networkDeviceId": network_device_id,
            "scanMode": scan_mode,
            "scanStatus": scan_status,
            "bugCount": bug_count,
            "offset": offset,
            "limit": limit,
            "sortBy": sort_by,
            "order": order,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/networkBugs/results/networkDevices"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_f6011b1d24c53d1aa7dda9e0d3ee29b_v3_1_6_0", json_data
        )

    def get_count_of_network_bug_devices(
        self,
        bug_count=None,
        network_device_id=None,
        scan_mode=None,
        scan_status=None,
        headers=None,
        **request_parameters
    ):
        """Get count of network bug devices.

        Args:
            network_device_id(str): networkDeviceId query parameter. Id of the network device.
            scan_mode(str): scanMode query parameter. Mode or the criteria using which the network device was
                scanned. Available values : ESSENTIALS, ADVANTAGE, CX_CLOUD, NOT_AVAILABLE.
            scan_status(str): scanStatus query parameter. Status of the scan on the network device. Available values
                : NOT_SCANNED, IN_PROGRESS, SUCCESS, FAILED, FALL_BACK.
            bug_count(int): bugCount query parameter. Return network devices with bugCount greater than this
                bugCount.
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
            https://developer.cisco.com/docs/dna-center/#!get-count-of-network-bug-devices
        """
        check_type(headers, dict)
        check_type(network_device_id, str)
        check_type(scan_mode, str)
        check_type(scan_status, str)
        check_type(bug_count, int)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "networkDeviceId": network_device_id,
            "scanMode": scan_mode,
            "scanStatus": scan_status,
            "bugCount": bug_count,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/networkBugs/results/networkDevices/co" + "unt"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_aab9fd032d15280ac99b00b34600781_v3_1_6_0", json_data
        )

    def get_network_bug_device_by_device_id(
        self, network_device_id, headers=None, **request_parameters
    ):
        """Get network bug device by device id.

        Args:
            network_device_id(str): networkDeviceId path parameter. Id of the network device.
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
            https://developer.cisco.com/docs/dna-center/#!get-network-bug-device-by-device-id
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
            "/dna/intent/api/v1/networkBugs/results/networkDevices/{n"
            + "etworkDeviceId}"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_e2f8ce2370c6532da9181a319daf0fec_v3_1_6_0", json_data
        )

    def get_bugs_affecting_the_network_device(
        self,
        network_device_id,
        id=None,
        limit=None,
        offset=None,
        order=None,
        severity=None,
        sort_by=None,
        headers=None,
        **request_parameters
    ):
        """Get bugs affecting the network device.

        Args:
            network_device_id(str): networkDeviceId path parameter. Id of the network device.
            id(str): id query parameter. Id of the network bug.
            severity(str): severity query parameter. Return network bugs with this severity. Available values :
                CATASTROPHIC, SEVERE, MODERATE.
            offset(int): offset query parameter. The first record to show for this page; the first record is
                numbered 1. Default value is 1.
            limit(int): limit query parameter. The number of records to show for this page. Minimum value is 1.
                Maximum value is 500. Default value is 500.
            sort_by(str): sortBy query parameter. A property within the response to sort by.
            order(str): order query parameter. Whether ascending or descending order should be used to sort the
                response. Available values : asc, desc. Default value is asc.
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
            https://developer.cisco.com/docs/dna-center/#!get-bugs-affecting-the-network-device
        """
        check_type(headers, dict)
        check_type(id, str)
        check_type(severity, str)
        check_type(offset, int)
        check_type(limit, int)
        check_type(sort_by, str)
        check_type(order, str)
        check_type(network_device_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "id": id,
            "severity": severity,
            "offset": offset,
            "limit": limit,
            "sortBy": sort_by,
            "order": order,
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

        e_url = (
            "/dna/intent/api/v1/networkBugs/results/networkDevices/{n"
            + "etworkDeviceId}/bugs"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_aea65ed8cb2e55fb8d7c40abf2352504_v3_1_6_0", json_data
        )

    def get_count_of_bugs_affecting_the_network_device(
        self,
        network_device_id,
        id=None,
        severity=None,
        headers=None,
        **request_parameters
    ):
        """Get count of bugs affecting the network device.

        Args:
            network_device_id(str): networkDeviceId path parameter. Id of the network device.
            id(str): id query parameter. Id of the network bug.
            severity(str): severity query parameter. Return network bugs with this severity. Available values :
                CATASTROPHIC, SEVERE, MODERATE.
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
            https://developer.cisco.com/docs/dna-center/#!get-count-of-bugs-affecting-the-network-device
        """
        check_type(headers, dict)
        check_type(id, str)
        check_type(severity, str)
        check_type(network_device_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "id": id,
            "severity": severity,
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

        e_url = (
            "/dna/intent/api/v1/networkBugs/results/networkDevices/{n"
            + "etworkDeviceId}/bugs/count"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a3e7c7a84b195cf989715f228c4c3337_v3_1_6_0", json_data
        )

    def get_bug_affecting_the_network_device_by_device_id_and_bug_id(
        self, id, network_device_id, headers=None, **request_parameters
    ):
        """Get bug affecting the network device by device Id and bug id.

        Args:
            network_device_id(str): networkDeviceId path parameter. Id of the network device.
            id(str): id path parameter. Id of the network bug.
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
            https://developer.cisco.com/docs/dna-center/#!get-bug-affecting-the-network-device-by-device-id-and-bug-id
        """
        check_type(headers, dict)
        check_type(network_device_id, str, may_be_none=False)
        check_type(id, str, may_be_none=False)
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
            "/dna/intent/api/v1/networkBugs/results/networkDevices/{n"
            + "etworkDeviceId}/bugs/{id}"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_beba27ea019536da45eef3cade3ab67_v3_1_6_0", json_data
        )

    def get_network_bugs_results_trend_over_time(
        self,
        limit=None,
        offset=None,
        scan_time=None,
        headers=None,
        **request_parameters
    ):
        """Get network bugs results trend over time. The default sort is by scan time descending.

        Args:
            scan_time(int): scanTime query parameter. Return bugs trend with scanTime greater than this scanTime.
            offset(int): offset query parameter. The first record to show for this page; the first record is
                numbered 1. Default value is 1.
            limit(int): limit query parameter. The number of records to show for this page. Minimum value is 1.
                Maximum value is 500. Default value is 500.
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
            https://developer.cisco.com/docs/dna-center/#!get-network-bugs-results-trend-over-time
        """
        check_type(headers, dict)
        check_type(scan_time, int)
        check_type(offset, int)
        check_type(limit, int)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "scanTime": scan_time,
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

        e_url = "/dna/intent/api/v1/networkBugs/resultsTrend"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ad7e992ab6a526196819e35eb0418a4_v3_1_6_0", json_data
        )

    def get_count_of_network_bugs_results_trend_over_time(
        self, scan_time=None, headers=None, **request_parameters
    ):
        """Get count of network bugs results trend over time.

        Args:
            scan_time(int): scanTime query parameter. Return bugs trend with scanTime greater than this scanTime.
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
            https://developer.cisco.com/docs/dna-center/#!get-count-of-network-bugs-results-trend-over-time
        """
        check_type(headers, dict)
        check_type(scan_time, int)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "scanTime": scan_time,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/networkBugs/resultsTrend/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a240f89766435001b3ed25c3d23f0ffc_v3_1_6_0", json_data
        )

    def get_trial_details_for_bugs_detection_on_network_devices(
        self, headers=None, **request_parameters
    ):
        """Get trial details for bugs detection on network devices.

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
            https://developer.cisco.com/docs/dna-center/#!get-trial-details-for-bugs-detection-on-network-devices
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

        e_url = "/dna/intent/api/v1/networkBugs/trials"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a3479f3b91c5b73bdfed9f1cb6f7bb5_v3_1_6_0", json_data
        )

    def creates_a_trial_for_bugs_detection_on_network_devices(
        self, headers=None, **request_parameters
    ):
        """Creates a trial for bugs detection on network devices. The consent to connect agreement must have been accepted
        in the UI for this to succeed. Please refer to the user guide at   for more details on consent to
        connect.

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
            https://developer.cisco.com/docs/dna-center/#!creates-a-trial-for-bugs-detection-on-network-devices
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

        e_url = "/dna/intent/api/v1/networkBugs/trials"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.post(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c08d904cff256aca70a68901692a021_v3_1_6_0", json_data
        )

    def triggers_a_bugs_scan_for_the_supported_network_devices(
        self, failed_devices_only=None, headers=None, **request_parameters
    ):
        """Triggers a bugs scan for the supported network devices. The supported devices are switches and routers. If a
        device is not supported, the NetworkBugsDevice scanStatus will be Failed with appropriate comments.

        Args:
            failed_devices_only(bool): failedDevicesOnly query parameter. Used to specify if the scan should run
                only for the network devices that failed during the previous scan. If not specified,
                this parameter defaults to false.
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
            https://developer.cisco.com/docs/dna-center/#!triggers-a-bugs-scan-for-the-supported-network-devices
        """
        check_type(headers, dict)
        check_type(failed_devices_only, bool)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "failedDevicesOnly": failed_devices_only,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/networkBugs/triggerScan"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.post(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_b6c0f7132f5a1485b7b564818354d8_v3_1_6_0", json_data
        )

    def get_security_advisories_affecting_the_network_devices(
        self,
        cvss_base_score=None,
        device_count=None,
        id=None,
        limit=None,
        offset=None,
        order=None,
        security_impact_rating=None,
        sort_by=None,
        headers=None,
        **request_parameters
    ):
        """Get security advisories affecting the network devices.

        Args:
            id(str): id query parameter. Id of the advisory.
            device_count(int): deviceCount query parameter. Return advisories with deviceCount greater than this
                deviceCount.
            cvss_base_score(str): cvssBaseScore query parameter. Return advisories with cvssBaseScore greater than
                this cvssBaseScore. E.g. : 8.5.
            security_impact_rating(str): securityImpactRating query parameter. Return advisories with this
                securityImpactRating. Available values : CRITICAL, HIGH.
            offset(int): offset query parameter. The first record to show for this page; the first record is
                numbered 1. Default value is 1.
            limit(int): limit query parameter. The number of records to show for this page. Minimum value is 1.
                Maximum value is 500. Default value is 500.
            sort_by(str): sortBy query parameter. A property within the response to sort by.
            order(str): order query parameter. Whether ascending or descending order should be used to sort the
                response. Available values : asc, desc. Default value is asc.
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
            https://developer.cisco.com/docs/dna-center/#!get-security-advisories-affecting-the-network-devices
        """
        check_type(headers, dict)
        check_type(id, str)
        check_type(device_count, int)
        check_type(cvss_base_score, str)
        check_type(security_impact_rating, str)
        check_type(offset, int)
        check_type(limit, int)
        check_type(sort_by, str)
        check_type(order, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "id": id,
            "deviceCount": device_count,
            "cvssBaseScore": cvss_base_score,
            "securityImpactRating": security_impact_rating,
            "offset": offset,
            "limit": limit,
            "sortBy": sort_by,
            "order": order,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/securityAdvisories/results/advisories"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_aef04c74f2745a6ca3960d6c466856cf_v3_1_6_0", json_data
        )

    def get_count_of_security_advisories_affecting_the_network_devices(
        self,
        cvss_base_score=None,
        device_count=None,
        id=None,
        security_impact_rating=None,
        headers=None,
        **request_parameters
    ):
        """Get count of security advisories affecting the network devices.

        Args:
            id(str): id query parameter. Id of the security advisory.
            device_count(int): deviceCount query parameter. Return advisories with deviceCount greater than this
                deviceCount.
            cvss_base_score(str): cvssBaseScore query parameter. Return advisories with cvssBaseScore greater than
                this cvssBaseScore. E.g. : 8.5.
            security_impact_rating(str): securityImpactRating query parameter. Return advisories with this
                securityImpactRating. Available values : CRITICAL, HIGH.
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
            https://developer.cisco.com/docs/dna-center/#!get-count-of-security-advisories-affecting-the-network-devices
        """
        check_type(headers, dict)
        check_type(id, str)
        check_type(device_count, int)
        check_type(cvss_base_score, str)
        check_type(security_impact_rating, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "id": id,
            "deviceCount": device_count,
            "cvssBaseScore": cvss_base_score,
            "securityImpactRating": security_impact_rating,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/securityAdvisories/results/advisories" + "/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a0ee1bc9fe825b49aaf57eb14b4c90cf_v3_1_6_0", json_data
        )

    def get_security_advisory_affecting_the_network_devices_by_id(
        self, id, headers=None, **request_parameters
    ):
        """Get security advisory affecting the network devices by Id.

        Args:
            id(str): id path parameter. Id of the security advisory.
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
            https://developer.cisco.com/docs/dna-center/#!get-security-advisory-affecting-the-network-devices-by-id
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

        e_url = "/dna/intent/api/v1/securityAdvisories/results/advisories" + "/{id}"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_dca392c51998fec3821dfb312de_v3_1_6_0", json_data
        )

    def get_security_advisory_network_devices_for_the_security_advisory(
        self,
        id,
        limit=None,
        network_device_id=None,
        offset=None,
        order=None,
        scan_mode=None,
        scan_status=None,
        sort_by=None,
        headers=None,
        **request_parameters
    ):
        """Get security advisory network devices for the security advisory.

        Args:
            id(str): id path parameter. Id of the security advisory.
            network_device_id(str): networkDeviceId query parameter. Id of the network device.
            scan_mode(str): scanMode query parameter. Mode or the criteria using which the network device was
                scanned. Available values : ESSENTIALS, ADVANTAGE, CX_CLOUD, NOT_AVAILABLE.
            scan_status(str): scanStatus query parameter. Status of the scan on the network device. Available values
                : NOT_SCANNED, IN_PROGRESS, SUCCESS, FAILED, FALL_BACK.
            offset(int): offset query parameter. The first record to show for this page; the first record is
                numbered 1. Default value is 1.
            limit(int): limit query parameter. The number of records to show for this page. Minimum value is 1.
                Maximum value is 500. Default value is 500.
            sort_by(str): sortBy query parameter. A property within the response to sort by.
            order(str): order query parameter. Whether ascending or descending order should be used to sort the
                response. Available values : asc, desc. Default value is asc.
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
            https://developer.cisco.com/docs/dna-center/#!get-security-advisory-network-devices-for-the-security-advisory
        """
        check_type(headers, dict)
        check_type(network_device_id, str)
        check_type(scan_mode, str)
        check_type(scan_status, str)
        check_type(offset, int)
        check_type(limit, int)
        check_type(sort_by, str)
        check_type(order, str)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "networkDeviceId": network_device_id,
            "scanMode": scan_mode,
            "scanStatus": scan_status,
            "offset": offset,
            "limit": limit,
            "sortBy": sort_by,
            "order": order,
        }
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

        e_url = (
            "/dna/intent/api/v1/securityAdvisories/results/advisories"
            + "/{id}/networkDevices"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_d14f6e201c475f33a92d0222d76d40df_v3_1_6_0", json_data
        )

    def get_count_of_security_advisory_network_devices_for_the_security_advisory(
        self,
        id,
        network_device_id=None,
        scan_mode=None,
        scan_status=None,
        headers=None,
        **request_parameters
    ):
        """Get count of security advisory network devices for the security advisory.

        Args:
            id(str): id path parameter. Id of the security advisory.
            network_device_id(str): networkDeviceId query parameter. Id of the network device.
            scan_mode(str): scanMode query parameter. Mode or the criteria using which the network device was
                scanned. Available values : ESSENTIALS, ADVANTAGE, CX_CLOUD, NOT_AVAILABLE.
            scan_status(str): scanStatus query parameter. Status of the scan on the network device. Available values
                : NOT_SCANNED, IN_PROGRESS, SUCCESS, FAILED, FALL_BACK.
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
            https://developer.cisco.com/docs/dna-center/#!get-count-of-security-advisory-network-devices-for-the-security-advisory
        """
        check_type(headers, dict)
        check_type(network_device_id, str)
        check_type(scan_mode, str)
        check_type(scan_status, str)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "networkDeviceId": network_device_id,
            "scanMode": scan_mode,
            "scanStatus": scan_status,
        }
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

        e_url = (
            "/dna/intent/api/v1/securityAdvisories/results/advisories"
            + "/{id}/networkDevices/count"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_d5fcf338dd95610a4a65c77888b8ed4_v3_1_6_0", json_data
        )

    def get_security_advisory_network_device_for_the_security_advisory_by_network_device_id(
        self, id, network_device_id, headers=None, **request_parameters
    ):
        """Get security advisory network device for the security advisory by network device id.

        Args:
            id(str): id path parameter. Id of the security advisory.
            network_device_id(str): networkDeviceId path parameter. Id of the network device.
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
            https://developer.cisco.com/docs/dna-center/#!get-security-advisory-network-device-for-the-security-advisory-by-network-device-id
        """
        check_type(headers, dict)
        check_type(id, str, may_be_none=False)
        check_type(network_device_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
            "networkDeviceId": network_device_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/securityAdvisories/results/advisories"
            + "/{id}/networkDevices/{networkDeviceId}"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_cb8be1c50ca9f2fe769cd27b2da_v3_1_6_0", json_data
        )

    def get_security_advisory_network_devices(
        self,
        advisory_count=None,
        limit=None,
        network_device_id=None,
        offset=None,
        order=None,
        scan_mode=None,
        scan_status=None,
        sort_by=None,
        headers=None,
        **request_parameters
    ):
        """Get security advisory network devices.

        Args:
            network_device_id(str): networkDeviceId query parameter. Id of the network device.
            scan_mode(str): scanMode query parameter. Mode or the criteria using which the network device was
                scanned. Available values : ESSENTIALS, ADVANTAGE, CX_CLOUD, NOT_AVAILABLE.
            scan_status(str): scanStatus query parameter. Status of the scan on the network device. Available values
                : NOT_SCANNED, IN_PROGRESS, SUCCESS, FAILED, FALL_BACK.
            advisory_count(str): advisoryCount query parameter. Return network devices with advisoryCount greater
                than this advisoryCount.
            offset(int): offset query parameter. The first record to show for this page; the first record is
                numbered 1. Default value is 1.
            limit(int): limit query parameter. The number of records to show for this page. Minimum value is 1.
                Maximum value is 500. Default value is 500.
            sort_by(str): sortBy query parameter. A property within the response to sort by.
            order(str): order query parameter. Whether ascending or descending order should be used to sort the
                response. Available values : asc, desc. Default value is asc.
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
            https://developer.cisco.com/docs/dna-center/#!get-security-advisory-network-devices
        """
        check_type(headers, dict)
        check_type(network_device_id, str)
        check_type(scan_mode, str)
        check_type(scan_status, str)
        check_type(advisory_count, str)
        check_type(offset, int)
        check_type(limit, int)
        check_type(sort_by, str)
        check_type(order, str)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "networkDeviceId": network_device_id,
            "scanMode": scan_mode,
            "scanStatus": scan_status,
            "advisoryCount": advisory_count,
            "offset": offset,
            "limit": limit,
            "sortBy": sort_by,
            "order": order,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/securityAdvisories/results/networkDev" + "ices"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_b210c3633d5cfe8127056abae805c7_v3_1_6_0", json_data
        )

    def get_count_of_security_advisory_network_devices(
        self,
        advisory_count=None,
        network_device_id=None,
        scan_mode=None,
        scan_status=None,
        headers=None,
        **request_parameters
    ):
        """Get count of security advisory network devices.

        Args:
            network_device_id(str): networkDeviceId query parameter. Id of the network device.
            scan_mode(str): scanMode query parameter. Mode or the criteria using which the network device was
                scanned. Available values : ESSENTIALS, ADVANTAGE, CX_CLOUD, NOT_AVAILABLE.
            scan_status(str): scanStatus query parameter. Status of the scan on the network device. Available values
                : NOT_SCANNED, IN_PROGRESS, SUCCESS, FAILED, FALL_BACK.
            advisory_count(int): advisoryCount query parameter. Return network devices with advisoryCount greater
                than this advisoryCount.
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
            https://developer.cisco.com/docs/dna-center/#!get-count-of-security-advisory-network-devices
        """
        check_type(headers, dict)
        check_type(network_device_id, str)
        check_type(scan_mode, str)
        check_type(scan_status, str)
        check_type(advisory_count, int)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "networkDeviceId": network_device_id,
            "scanMode": scan_mode,
            "scanStatus": scan_status,
            "advisoryCount": advisory_count,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/securityAdvisories/results/networkDev" + "ices/count"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_eb1f5f93d0d549cbf99e032a73db16d_v3_1_6_0", json_data
        )

    def get_security_advisory_network_device_by_network_device_id(
        self, network_device_id, headers=None, **request_parameters
    ):
        """Get security advisory network device by network device id.

        Args:
            network_device_id(str): networkDeviceId path parameter. Id of the network device.
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
            https://developer.cisco.com/docs/dna-center/#!get-security-advisory-network-device-by-network-device-id
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
            "/dna/intent/api/v1/securityAdvisories/results/networkDev"
            + "ices/{networkDeviceId}"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_e22988bedfbb5202b1bab7e811d56f53_v3_1_6_0", json_data
        )

    def get_security_advisories_affecting_the_network_device(
        self,
        network_device_id,
        cvss_base_score=None,
        id=None,
        limit=None,
        offset=None,
        order=None,
        security_impact_rating=None,
        sort_by=None,
        headers=None,
        **request_parameters
    ):
        """Get security advisories affecting the network device.

        Args:
            network_device_id(str): networkDeviceId path parameter. Id of the network device.
            id(str): id query parameter. Id of the security advisory.
            cvss_base_score(str): cvssBaseScore query parameter. Return advisories with cvssBaseScore greater than
                this cvssBaseScore. E.g. : 8.5.
            security_impact_rating(str): securityImpactRating query parameter. Return advisories with this
                securityImpactRating. Available values : CRITICAL, HIGH.
            offset(int): offset query parameter. The first record to show for this page; the first record is
                numbered 1. Default value is 1.
            limit(int): limit query parameter. The number of records to show for this page. Minimum value is 1.
                Maximum value is 500. Default value is 500.
            sort_by(str): sortBy query parameter. A property within the response to sort by.
            order(str): order query parameter. Whether ascending or descending order should be used to sort the
                response. Available values : asc, desc. Default value is asc.
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
            https://developer.cisco.com/docs/dna-center/#!get-security-advisories-affecting-the-network-device
        """
        check_type(headers, dict)
        check_type(id, str)
        check_type(cvss_base_score, str)
        check_type(security_impact_rating, str)
        check_type(offset, int)
        check_type(limit, int)
        check_type(sort_by, str)
        check_type(order, str)
        check_type(network_device_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "id": id,
            "cvssBaseScore": cvss_base_score,
            "securityImpactRating": security_impact_rating,
            "offset": offset,
            "limit": limit,
            "sortBy": sort_by,
            "order": order,
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

        e_url = (
            "/dna/intent/api/v1/securityAdvisories/results/networkDev"
            + "ices/{networkDeviceId}/advisories"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c12818ede552109f463d18c23a5a13_v3_1_6_0", json_data
        )

    def get_count_of_security_advisories_affecting_the_network_device(
        self,
        network_device_id,
        cvss_base_score=None,
        id=None,
        security_impact_rating=None,
        headers=None,
        **request_parameters
    ):
        """Get count of security advisories affecting the network device.

        Args:
            network_device_id(str): networkDeviceId path parameter. Id of the network device.
            id(str): id query parameter. Id of the security advisory.
            cvss_base_score(str): cvssBaseScore query parameter. Return advisories with cvssBaseScore greater than
                this cvssBaseScore. E.g. : 8.5.
            security_impact_rating(str): securityImpactRating query parameter. Return advisories with this
                securityImpactRating. Available values : CRITICAL, HIGH.
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
            https://developer.cisco.com/docs/dna-center/#!get-count-of-security-advisories-affecting-the-network-device
        """
        check_type(headers, dict)
        check_type(id, str)
        check_type(cvss_base_score, str)
        check_type(security_impact_rating, str)
        check_type(network_device_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "id": id,
            "cvssBaseScore": cvss_base_score,
            "securityImpactRating": security_impact_rating,
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

        e_url = (
            "/dna/intent/api/v1/securityAdvisories/results/networkDev"
            + "ices/{networkDeviceId}/advisories/count"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a12932efe27956de8c356e40e959d6c2_v3_1_6_0", json_data
        )

    def get_security_advisory_affecting_the_network_device_by_device_id_and_advisory_id(
        self, id, network_device_id, headers=None, **request_parameters
    ):
        """Get security advisory affecting the network device by device Id and advisory id.

        Args:
            network_device_id(str): networkDeviceId path parameter. Id of the network device.
            id(str): id path parameter. Id of the security advisory.
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
            https://developer.cisco.com/docs/dna-center/#!get-security-advisory-affecting-the-network-device-by-device-id-and-advisory-id
        """
        check_type(headers, dict)
        check_type(network_device_id, str, may_be_none=False)
        check_type(id, str, may_be_none=False)
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
            "/dna/intent/api/v1/securityAdvisories/results/networkDev"
            + "ices/{networkDeviceId}/advisories/{id}"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_fc34a3eb64405e08b65fb830f2c1c05c_v3_1_6_0", json_data
        )

    def get_security_advisories_results_trend_over_time(
        self,
        limit=None,
        offset=None,
        scan_time=None,
        headers=None,
        **request_parameters
    ):
        """Get security advisories results trend over time. The default sort is by scan time descending.

        Args:
            scan_time(int): scanTime query parameter. Return advisories trend with scanTime greater than this
                scanTime.
            offset(int): offset query parameter. The first record to show for this page; the first record is
                numbered 1. Default value is 1.
            limit(int): limit query parameter. The number of records to show for this page. Minimum value is 1.
                Maximum value is 500. Default value is 500.
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
            https://developer.cisco.com/docs/dna-center/#!get-security-advisories-results-trend-over-time
        """
        check_type(headers, dict)
        check_type(scan_time, int)
        check_type(offset, int)
        check_type(limit, int)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "scanTime": scan_time,
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

        e_url = "/dna/intent/api/v1/securityAdvisories/resultsTrend"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c60e785a6915253b715d9416e684132_v3_1_6_0", json_data
        )

    def get_count_of_security_advisories_results_trend_over_time(
        self, scan_time=None, headers=None, **request_parameters
    ):
        """Get count of security advisories results trend over time.

        Args:
            scan_time(int): scanTime query parameter. Return advisories trend with scanTime greater than this
                scanTime.
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
            https://developer.cisco.com/docs/dna-center/#!get-count-of-security-advisories-results-trend-over-time
        """
        check_type(headers, dict)
        check_type(scan_time, int)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "scanTime": scan_time,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/securityAdvisories/resultsTrend/count"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_f083e6be591181051e43aebe7c7d_v3_1_6_0", json_data
        )

    def get_trial_details_for_security_advisories_detection_on_network_devices(
        self, headers=None, **request_parameters
    ):
        """Get trial details for security advisories detection on network devices.

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
            https://developer.cisco.com/docs/dna-center/#!get-trial-details-for-security-advisories-detection-on-network-devices
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

        e_url = "/dna/intent/api/v1/securityAdvisories/trials"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_fe4fd333ec815ec283443c490bde2741_v3_1_6_0", json_data
        )

    def creates_a_trial_for_security_advisories_detection_on_network_devices(
        self, headers=None, **request_parameters
    ):
        """Creates a trial for security advisories detection on network devices. The consent to connect agreement must have
        been accepted in the UI for this to succeed. Please refer to the user guide at   for more details on
        consent to connect.

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
            https://developer.cisco.com/docs/dna-center/#!creates-a-trial-for-security-advisories-detection-on-network-devices
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

        e_url = "/dna/intent/api/v1/securityAdvisories/trials"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.post(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_b209c580ed5c0aaf4c978f4dfc00bd_v3_1_6_0", json_data
        )

    def triggers_a_security_advisories_scan_for_the_supported_network_devices(
        self, failed_devices_only=None, headers=None, **request_parameters
    ):
        """Triggers a security advisories scan for the supported network devices. The supported devices are switches,
        routers and wireless controllers with IOS and IOS-XE. If a device is not supported, the
        SecurityAdvisoryNetworkDevice scanStatus will be Failed with appropriate comments.

        Args:
            failed_devices_only(bool): failedDevicesOnly query parameter. Used to specify if the scan should run
                only for the network devices that failed during the previous scan. If not specified,
                this parameter defaults to false.
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
            https://developer.cisco.com/docs/dna-center/#!triggers-a-security-advisories-scan-for-the-supported-network-devices
        """
        check_type(headers, dict)
        check_type(failed_devices_only, bool)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "failedDevicesOnly": failed_devices_only,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/securityAdvisories/triggerScan"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.post(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_cce0f5e813955eabb3c736d3b5952341_v3_1_6_0", json_data
        )


# Alias Functions

# -*- coding: utf-8 -*-
"""Cisco Catalyst Center Wired API wrapper.

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


class Wired(object):
    """Cisco Catalyst Center Wired API (version: 2.3.7.9).

    Wraps the Catalyst Center Wired
    API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new Wired
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Catalyst Center service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(Wired, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def get_configurations_for_intended_layer2_features_on_a_wired_device(
        self, feature, id, headers=None, **request_parameters
    ):
        """This API returns the configurations for the intended layer 2 features on a wired device. Even after the intended
        configurations are deployed using the API
        /intent/api/v1/networkDevices/{id}/configFeatures/intended/deploy, they continue to be a part of the
        intended features on the device. .

        Args:
            id(str): id path parameter. Network device ID of the wired device to configure. .
            feature(str): feature query parameter. Name of the feature to configure. The API
                /data/intent/api/wired/networkDevices/{id}/configFeatures/supported/layer2 can be used
                to get the list of features supported on a device. .
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
            https://developer.cisco.com/docs/dna-center/#!get-configurations-for-intended-layer2-features-on-a-wired-device
        """
        check_type(headers, dict)
        check_type(feature, str, may_be_none=False)
        check_type(id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "feature": feature,
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
            "/dna/intent/api/v1/intent/api/v1/wired/networkDevices/{i"
            + "d}/configFeatures/intended/layer2"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_d96b49e8c1a0594cb4e1946731f06411_v2_3_7_9", json_data
        )

    def deploy_the_configuration_model_on_the_network_device(
        self, network_device_id, preview_activity_id, headers=None, **request_parameters
    ):
        """This API deploys the configuration model on the network device. This is the final step 'Step 4' of the following
        workflow. Step 1Use 'POST
        /intent/api/v1/wired/networkDevices/{networkDeviceId}/configFeatures/intended/configurationModels' to
        start the provision of intended features. The response has a taskId which is the previewActivityId in
        all subsequent APIs. The task must be successfully complete before proceeding to the next step. It is
        not recommended to proceed when there is any task failure in this step. The API 'DELETE /intent/api/v1/w
        ired/networkDevices/{networkDeviceId}/configFeatures/intended/configurationModels/{previewActivityId}'
        can be used at any step to discard/cancel the provision of intended features. Step 2Use 'POST /intent/ap
        i/v1/wired/networkDevices/{networkDeviceId}/configFeatures/intended/configurationModels/{previewActivity
        Id}/networkDevices/{networkDeviceId}/config' to generate device CLIs for preview. The response has a
        task ID. The task must be successfully complete before using the GET API to view CLIs. It is not
        recommended to proceed when there is any task failure(s) in this step. The API 'DELETE /intent/api/v1/wi
        red/networkDevices/{networkDeviceId}/configFeatures/intended/configurationModels/{previewActivityId}'
        can be used at any step to discard/cancel the provision of intended features. Step 3Use 'GET /intent/api
        /v1/wired/networkDevices/{networkDeviceId}/configFeatures/intended/configurationModels/{previewActivityI
        d}/networkDevices/{networkDeviceId}/config' to view the CLIs that will be applied to the device. Step
        4Use 'POST /intent/api/v1/wired/networkDevices/{networkDeviceId}/configFeatures/intended/configurationMo
        dels/{previewActivityId}/deploy' to push the intent to the device. .

        Args:
            network_device_id(str): networkDeviceId path parameter. Network device ID of the wired device to
                provision. The API /intent/api/v1/network-device can be used to get the network device
                ID. .
            preview_activity_id(str): previewActivityId path parameter. Activity id from intent/api/v1/activity. .
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
            https://developer.cisco.com/docs/dna-center/#!deploy-the-configuration-model-on-the-network-device
        """
        check_type(headers, dict)
        check_type(network_device_id, str, may_be_none=False)
        check_type(preview_activity_id, str, may_be_none=False)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "networkDeviceId": network_device_id,
            "previewActivityId": preview_activity_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/intent/api/v1/wired/networkDevices/{n"
            + "etworkDeviceId}/configFeatures/intended/configurationMod"
            + "els/{previewActivityId}/deploy"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.post(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_b6139c3f3ef15bcf9a42f5283a6aea64_v2_3_7_9", json_data
        )

    def get_configurations_for_a_deployed_layer2_feature_on_a_wired_device(
        self, feature, id, headers=None, **request_parameters
    ):
        """The API returns configurations for a deployed layer 2 feature on a wired device. .

        Args:
            id(str): id path parameter. Network device ID of the wired device to retrieve configuration for. .
            feature(str): feature path parameter. Name of the feature to retrieve Layer 2 configuration for. The API
                /dna/intent/api/v1/networkDevices/{id}/configFeatures/supported/layer2 can be used to
                get the list of features supported on a device. .
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
            https://developer.cisco.com/docs/dna-center/#!get-configurations-for-a-deployed-layer2-feature-on-a-wired-device
        """
        check_type(headers, dict)
        check_type(id, str, may_be_none=False)
        check_type(feature, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
            "feature": feature,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/wired/networkDevices/{id}/configFeatu"
            + "res/deployed/layer2/{feature}"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_fcf9673050079b4abedf3ffc9777_v2_3_7_9", json_data
        )

    def get_number_of_configurations_for_a_deployed_layer2_feature_on_a_wired_device(
        self, feature, id, headers=None, **request_parameters
    ):
        """The API returns the number of configurations for a deployed layer 2 feature on a wired device. .

        Args:
            id(str): id path parameter. Network device ID of the wired device to retrieve configuration for. .
            feature(str): feature path parameter. Name of the feature to retrieve configuration for. The API
                /dna/intent/api/v1/networkDevices/{id}/configFeatures/supported/layer2 can be used to
                get the list of features supported on a device. .
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
            https://developer.cisco.com/docs/dna-center/#!get-number-of-configurations-for-a-deployed-layer2-feature-on-a-wired-device
        """
        check_type(headers, dict)
        check_type(id, str, may_be_none=False)
        check_type(feature, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
            "feature": feature,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/wired/networkDevices/{id}/configFeatu"
            + "res/deployed/layer2/{feature}/count"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_e495979e25a6559394fbad6fcd4c495a_v2_3_7_9", json_data
        )

    def create_configurations_for_intended_layer2_features_on_a_wired_device(
        self, id, headers=None, **request_parameters
    ):
        """This API creates configurations for the intended features on a wired device, if none have been added earlier.
        Only the feature configurations to be changed need to be added to the intended features. When the
        intended features are deployed to a device using the API
        /intent/api/v1/networkDevices/{id}/configFeatures/intended/deploy, they are applied on top of the
        existing configurations on the device. Any existing configurations on the device which are not included
        in the intended features, are retained on the device. .

        Args:
            id(str): id path parameter. Network device ID of the wired device to configure. .
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
            https://developer.cisco.com/docs/dna-center/#!create-configurations-for-intended-layer2-features-on-a-wired-device
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
            "/dna/intent/api/v1/wired/networkDevices/{id}/configFeatu"
            + "res/intended/layer2"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.post(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a862379cc525a79a01fc845fdda7d68_v2_3_7_9", json_data
        )

    def update_configurations_for_intended_layer2_features_on_a_wired_device(
        self, id, headers=None, **request_parameters
    ):
        """This API updates the configurations for the intended features on a wired device. Only the feature configurations
        to be changed need to be added to the intended features. Updates to intended features can be done over
        several iterations. Once the updates are complete, the intended features can be deployed to a device
        using the API /dna/intent/api/v1/networkDevices/{id}/configFeatures/intended/deploy. When the intended
        features are deployed, they are applied on top of the existing configurations on the device. Any
        existing configurations on the device which are not included in the intended features, are retained on
        the device. .

        Args:
            id(str): id path parameter. Network device ID of the wired device to configure. .
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
            https://developer.cisco.com/docs/dna-center/#!update-configurations-for-intended-layer2-features-on-a-wired-device
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

        e_url = (
            "/dna/intent/api/v1/wired/networkDevices/{id}/configFeatu"
            + "res/intended/layer2"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.put(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_ecf0984975fb7af51796da58aca21_v2_3_7_9", json_data
        )

    def get_configurations_for_an_intended_layer2_feature_on_a_wired_device(
        self, feature, id, headers=None, **request_parameters
    ):
        """This API returns the configurations for an intended layer 2 feature on a wired device. Even after the intended
        configurations are deployed using the API
        /dna/intent/api/v1/networkDevices/{id}/configFeatures/intended/deploy, they continue to be a part of the
        intended features on the device. .

        Args:
            id(str): id path parameter. Network device ID of the wired device to configure. .
            feature(str): feature path parameter. The name of the feature to be retrieved. .
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
            https://developer.cisco.com/docs/dna-center/#!get-configurations-for-an-intended-layer2-feature-on-a-wired-device
        """
        check_type(headers, dict)
        check_type(id, str, may_be_none=False)
        check_type(feature, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
            "feature": feature,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/wired/networkDevices/{id}/configFeatu"
            + "res/intended/layer2/{feature}"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_d1b2d399192a5da39b4ae3fe0f5288d4_v2_3_7_9", json_data
        )

    def delete_configurations_for_an_intended_layer2_feature_on_a_wired_device(
        self, feature, id, headers=None, **request_parameters
    ):
        """This API deletes the configurations for an intended feature on a wired device. Once all the updates to intended
        features are complete, they can be deployed to a device using the API
        /dna/intent/api/v1/networkDevices/{id}/configFeatures/intended/deploy. When the intended features are
        deployed, they are applied on top of the existing configurations on the device. Any existing
        configurations on the device which are not included in the intended features, are retained on the
        device. .

        Args:
            id(str): id path parameter. Network device ID of the wired device to configure. .
            feature(str): feature path parameter. Name of the feature to delete. .
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
            https://developer.cisco.com/docs/dna-center/#!delete-configurations-for-an-intended-layer2-feature-on-a-wired-device
        """
        check_type(headers, dict)
        check_type(id, str, may_be_none=False)
        check_type(feature, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
            "feature": feature,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/wired/networkDevices/{id}/configFeatu"
            + "res/intended/layer2/{feature}"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_d4649fef20535193fd86c95925bcf8_v2_3_7_9", json_data
        )

    def update_configurations_for_an_intended_layer2_feature_on_a_wired_device(
        self,
        feature,
        id,
        cdpGlobalConfig=None,
        cdpInterfaceConfig=None,
        dhcpSnoopingGlobalConfig=None,
        dhcpSnoopingInterfaceConfig=None,
        dot1xGlobalConfig=None,
        dot1xInterfaceConfig=None,
        igmpSnoopingGlobalConfig=None,
        lldpGlobalConfig=None,
        lldpInterfaceConfig=None,
        mabInterfaceConfig=None,
        mldSnoopingGlobalConfig=None,
        portChannelConfig=None,
        stpGlobalConfig=None,
        stpInterfaceConfig=None,
        switchportInterfaceConfig=None,
        trunkInterfaceConfig=None,
        vlanConfig=None,
        vtpGlobalConfig=None,
        vtpInterfaceConfig=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This API updates the configurations for an intended feature on a wired device. Updates to other intended
        features can be done over several iterations. Once all the updates to intended features are complete,
        they can be deployed to a device using the API
        /dna/intent/api/v1/networkDevices/{id}/configFeatures/intended/deploy. When the intended features are
        deployed, they are applied on top of the existing configurations on the device. Any existing
        configurations on the device which are not included in the intended features, are retained on the
        device. .

        Args:
            cdpGlobalConfig(object): Wired's cdpGlobalConfig.
            cdpInterfaceConfig(object): Wired's cdpInterfaceConfig.
            dhcpSnoopingGlobalConfig(object): Wired's dhcpSnoopingGlobalConfig.
            dhcpSnoopingInterfaceConfig(object): Wired's dhcpSnoopingInterfaceConfig.
            dot1xGlobalConfig(object): Wired's dot1xGlobalConfig.
            dot1xInterfaceConfig(object): Wired's dot1xInterfaceConfig.
            igmpSnoopingGlobalConfig(object): Wired's igmpSnoopingGlobalConfig.
            lldpGlobalConfig(object): Wired's lldpGlobalConfig.
            lldpInterfaceConfig(object): Wired's lldpInterfaceConfig.
            mabInterfaceConfig(object): Wired's mabInterfaceConfig.
            mldSnoopingGlobalConfig(object): Wired's mldSnoopingGlobalConfig.
            portChannelConfig(object): Wired's portChannelConfig.
            stpGlobalConfig(object): Wired's stpGlobalConfig.
            stpInterfaceConfig(object): Wired's stpInterfaceConfig.
            switchportInterfaceConfig(object): Wired's switchportInterfaceConfig.
            trunkInterfaceConfig(object): Wired's trunkInterfaceConfig.
            vlanConfig(object): Wired's vlanConfig.
            vtpGlobalConfig(object): Wired's vtpGlobalConfig.
            vtpInterfaceConfig(object): Wired's vtpInterfaceConfig.
            id(str): id path parameter. Network device ID of the wired device to configure. .
            feature(str): feature path parameter. Name of the feature to update configuration for. The feature must
                be already created. .
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
            https://developer.cisco.com/docs/dna-center/#!update-configurations-for-an-intended-layer2-feature-on-a-wired-device
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(id, str, may_be_none=False)
        check_type(feature, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
            "feature": feature,
        }
        _payload = {
            "cdpGlobalConfig": cdpGlobalConfig,
            "cdpInterfaceConfig": cdpInterfaceConfig,
            "dhcpSnoopingInterfaceConfig": dhcpSnoopingInterfaceConfig,
            "dhcpSnoopingGlobalConfig": dhcpSnoopingGlobalConfig,
            "dot1xInterfaceConfig": dot1xInterfaceConfig,
            "dot1xGlobalConfig": dot1xGlobalConfig,
            "lldpGlobalConfig": lldpGlobalConfig,
            "lldpInterfaceConfig": lldpInterfaceConfig,
            "mabInterfaceConfig": mabInterfaceConfig,
            "mldSnoopingGlobalConfig": mldSnoopingGlobalConfig,
            "igmpSnoopingGlobalConfig": igmpSnoopingGlobalConfig,
            "stpGlobalConfig": stpGlobalConfig,
            "stpInterfaceConfig": stpInterfaceConfig,
            "trunkInterfaceConfig": trunkInterfaceConfig,
            "vtpGlobalConfig": vtpGlobalConfig,
            "vtpInterfaceConfig": vtpInterfaceConfig,
            "vlanConfig": vlanConfig,
            "portChannelConfig": portChannelConfig,
            "switchportInterfaceConfig": switchportInterfaceConfig,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_ee7664344f50cb8f2c94beaa01629d_v2_3_7_9"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/wired/networkDevices/{id}/configFeatu"
            + "res/intended/layer2/{feature}"
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
            "bpm_ee7664344f50cb8f2c94beaa01629d_v2_3_7_9", json_data
        )

    def create_configurations_for_an_intended_layer2_feature_on_a_wired_device(
        self,
        feature,
        id,
        cdpGlobalConfig=None,
        cdpInterfaceConfig=None,
        dhcpSnoopingGlobalConfig=None,
        dhcpSnoopingInterfaceConfig=None,
        dot1xGlobalConfig=None,
        dot1xInterfaceConfig=None,
        igmpSnoopingGlobalConfig=None,
        lldpGlobalConfig=None,
        lldpInterfaceConfig=None,
        mabInterfaceConfig=None,
        mldSnoopingGlobalConfig=None,
        portChannelConfig=None,
        stpGlobalConfig=None,
        stpInterfaceConfig=None,
        switchportInterfaceConfig=None,
        trunkInterfaceConfig=None,
        vlanConfig=None,
        vtpGlobalConfig=None,
        vtpInterfaceConfig=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This API creates configurations for an intended feature on a wired device. Once all the updates to intended
        features are complete, they can be deployed to a device using the API
        /dna/intent/api/v1/networkDevices/{id}/configFeatures/intended/deploy. When the intended features are
        deployed, they are applied on top of the existing configurations on the device. Any existing
        configurations on the device which are not included in the intended features, are retained on the
        device. .

        Args:
            cdpGlobalConfig(object): Wired's cdpGlobalConfig.
            cdpInterfaceConfig(object): Wired's cdpInterfaceConfig.
            dhcpSnoopingGlobalConfig(object): Wired's dhcpSnoopingGlobalConfig.
            dhcpSnoopingInterfaceConfig(object): Wired's dhcpSnoopingInterfaceConfig.
            dot1xGlobalConfig(object): Wired's dot1xGlobalConfig.
            dot1xInterfaceConfig(object): Wired's dot1xInterfaceConfig.
            igmpSnoopingGlobalConfig(object): Wired's igmpSnoopingGlobalConfig.
            lldpGlobalConfig(object): Wired's lldpGlobalConfig.
            lldpInterfaceConfig(object): Wired's lldpInterfaceConfig.
            mabInterfaceConfig(object): Wired's mabInterfaceConfig.
            mldSnoopingGlobalConfig(object): Wired's mldSnoopingGlobalConfig.
            portChannelConfig(object): Wired's portChannelConfig.
            stpGlobalConfig(object): Wired's stpGlobalConfig.
            stpInterfaceConfig(object): Wired's stpInterfaceConfig.
            switchportInterfaceConfig(object): Wired's switchportInterfaceConfig.
            trunkInterfaceConfig(object): Wired's trunkInterfaceConfig.
            vlanConfig(object): Wired's vlanConfig.
            vtpGlobalConfig(object): Wired's vtpGlobalConfig.
            vtpInterfaceConfig(object): Wired's vtpInterfaceConfig.
            id(str): id path parameter. Network device ID of the wired device to configure. .
            feature(str): feature path parameter. Name of the feature to configure. The API
                /dna/intent/api/v1/networkDevices/{id}/configFeatures/supported/layer2 can be used to
                get the list of features supported on a device. .
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
            https://developer.cisco.com/docs/dna-center/#!create-configurations-for-an-intended-layer2-feature-on-a-wired-device
        """
        check_type(headers, dict)
        check_type(payload, dict)
        check_type(id, str, may_be_none=False)
        check_type(feature, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
            "feature": feature,
        }
        _payload = {
            "cdpGlobalConfig": cdpGlobalConfig,
            "cdpInterfaceConfig": cdpInterfaceConfig,
            "dhcpSnoopingInterfaceConfig": dhcpSnoopingInterfaceConfig,
            "dhcpSnoopingGlobalConfig": dhcpSnoopingGlobalConfig,
            "dot1xInterfaceConfig": dot1xInterfaceConfig,
            "dot1xGlobalConfig": dot1xGlobalConfig,
            "lldpGlobalConfig": lldpGlobalConfig,
            "lldpInterfaceConfig": lldpInterfaceConfig,
            "mabInterfaceConfig": mabInterfaceConfig,
            "mldSnoopingGlobalConfig": mldSnoopingGlobalConfig,
            "igmpSnoopingGlobalConfig": igmpSnoopingGlobalConfig,
            "stpGlobalConfig": stpGlobalConfig,
            "stpInterfaceConfig": stpInterfaceConfig,
            "trunkInterfaceConfig": trunkInterfaceConfig,
            "vtpGlobalConfig": vtpGlobalConfig,
            "vtpInterfaceConfig": vtpInterfaceConfig,
            "vlanConfig": vlanConfig,
            "portChannelConfig": portChannelConfig,
            "switchportInterfaceConfig": switchportInterfaceConfig,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator("jsd_d7b57050bdb98e9340d0bc4dba_v2_3_7_9").validate(
                _payload
            )

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/wired/networkDevices/{id}/configFeatu"
            + "res/intended/layer2/{feature}"
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
            "bpm_d7b57050bdb98e9340d0bc4dba_v2_3_7_9", json_data
        )

    def get_number_of_configurations_for_an_intended_layer2_feature_on_a_wired_device(
        self, feature, id, headers=None, **request_parameters
    ):
        """This API returns the count of the instances of the configurations for an intended layer 2 feature on a wired
        device. .

        Args:
            id(str): id path parameter. Network device ID of the wired device to configure. .
            feature(str): feature path parameter. Name of the feature to configure. The API
                /dna/intent/api/v1/networkDevices/{id}/configFeatures/supported/layer2 can be used to
                get the list of features supported on a device. .
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
            https://developer.cisco.com/docs/dna-center/#!get-number-of-configurations-for-an-intended-layer2-feature-on-a-wired-device
        """
        check_type(headers, dict)
        check_type(id, str, may_be_none=False)
        check_type(feature, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "id": id,
            "feature": feature,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/wired/networkDevices/{id}/configFeatu"
            + "res/intended/layer2/{feature}/count"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory("bpm_d2cca58398312cb0129d39d8c_v2_3_7_9", json_data)

    def get_the_supported_layer2_features_on_a_wired_device(
        self, id, headers=None, **request_parameters
    ):
        """The API returns the supported layer 2 features on a wired device. .

        Args:
            id(str): id path parameter. Network device ID of the wired device. .
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
            https://developer.cisco.com/docs/dna-center/#!get-the-supported-layer2-features-on-a-wired-device
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

        e_url = (
            "/dna/intent/api/v1/wired/networkDevices/{id}/configFeatu"
            + "res/supported/layer2"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c4684074beb50b1ae5e77141244ebbd_v2_3_7_9", json_data
        )

    def create_a_configuration_model_for_the_intended_configs_for_a_wired_device(
        self, network_device_id, headers=None, **request_parameters
    ):
        """Create a configuration model for the intended configs for a wired device. This is a pre-requisite to preview the
        generated device config for the provisioning intent. This is mandatory if the provisioning settings
        require Preview or ITSM Approval before deploying configurations on network devices. The API
        /intent/api/v1/provisioningSettings can be used to get or update provisioning settings. This API is
        'Step 1' in the following workflow Step 1Use 'POST
        /intent/api/v1/wired/networkDevices/{networkDeviceId}/configFeatures/intended/configurationModels' to
        start the provision of intended features. The response has a taskId which is the previewActivityId in
        all subsequent APIs. The task must be successfully complete before proceeding to the next step. It is
        not recommended to proceed when there is any task failure in this step. The API 'DELETE /intent/api/v1/w
        ired/networkDevices/{networkDeviceId}/configFeatures/intended/configurationModels/{previewActivityId}'
        can be used at any step to discard/cancel the provision of intended features. Step 2Use 'POST /intent/ap
        i/v1/wired/networkDevices/{networkDeviceId}/configFeatures/intended/configurationModels/{previewActivity
        Id}/networkDevices/{networkDeviceId}/config' to generate device CLIs for preview. The response has a
        task ID. The task must be successfully complete before using the GET API to view CLIs. It is not
        recommended to proceed when there is any task failure(s) in this step. The API 'DELETE /intent/api/v1/wi
        red/networkDevices/{networkDeviceId}/configFeatures/intended/configurationModels/{previewActivityId}'
        can be used at any step to discard/cancel the provision of intended features. Step 3Use 'GET /intent/api
        /v1/wired/networkDevices/{networkDeviceId}/configFeatures/intended/configurationModels/{previewActivityI
        d}/networkDevices/{networkDeviceId}/config' to view the CLIs that will be applied to the device. Step
        4Use 'POST /intent/api/v1/wired/networkDevices/{networkDeviceId}/configFeatures/intended/configurationMo
        dels/{previewActivityId}/deploy' to deploy the intent to the device. .

        Args:
            network_device_id(str): networkDeviceId path parameter. Network device ID of the wired device to
                provision. The API /intent/api/v1/network-device can be used to get the network device
                ID. .
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
            https://developer.cisco.com/docs/dna-center/#!create-a-configuration-model-for-the-intended-configs-for-a-wired-device
        """
        check_type(headers, dict)
        check_type(network_device_id, str, may_be_none=False)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
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
            "/dna/intent/api/v1/wired/networkDevices/{networkDeviceId"
            + "}/configFeatures/intended/configurationModels"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.post(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c74d2bae55f85924002ddb92fe064_v2_3_7_9", json_data
        )

    def delete_the_configuration_model(
        self, network_device_id, preview_activity_id, headers=None, **request_parameters
    ):
        """Deletes the configuration model. The API can be used at any step to discard/cancel the provision of intended
        features. .

        Args:
            network_device_id(str): networkDeviceId path parameter. Network device ID of the wired device to
                provision. The API /intent/api/v1/network-device can be used to get the network device
                ID. .
            preview_activity_id(str): previewActivityId path parameter. Activity id from POST
                /intent/api/v1/wired/networkDevices/{networkDeviceId}/configFeatures/intended/configurat
                ionModels or /intent/api/v1/wired/networkDevices/{networkDeviceId}/configFeatures/intend
                ed/configurationModels/{previewActivityId}/networkDevices/{networkDeviceId}/config .
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
            https://developer.cisco.com/docs/dna-center/#!delete-the-configuration-model
        """
        check_type(headers, dict)
        check_type(network_device_id, str, may_be_none=False)
        check_type(preview_activity_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "networkDeviceId": network_device_id,
            "previewActivityId": preview_activity_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/wired/networkDevices/{networkDeviceId"
            + "}/configFeatures/intended/configurationModels/{previewAc"
            + "tivityId}"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_fec9a36b80305b5593608e369fa05b64_v2_3_7_9", json_data
        )

    def generate_the_device_config_for_the_configuration_model(
        self, network_device_id, preview_activity_id, headers=None, **request_parameters
    ):
        """Generates the device config for the configuration model. This API is 'Step 2' in the following workflow  Step
        1Use 'POST
        /intent/api/v1/wired/networkDevices/{networkDeviceId}/configFeatures/intended/configurationModels' to
        start the provision of intended features. The response has a taskId which is the previewActivityId in
        all subsequent APIs. The task must be successfully complete before proceeding to the next step. It is
        not recommended to proceed when there is any task failure in this step. The API 'DELETE /intent/api/v1/w
        ired/networkDevices/{networkDeviceId}/configFeatures/intended/configurationModels/{previewActivityId}'
        can be used at any step to discard/cancel the provision of intended features. Step 2Use 'POST /intent/ap
        i/v1/wired/networkDevices/{networkDeviceId}/configFeatures/intended/configurationModels/{previewActivity
        Id}/networkDevices/{networkDeviceId}/config' to generate device CLIs for preview. The response has a
        task ID. The task must be successfully complete before using the GET API to view CLIs. It is not
        recommended to proceed when there is any task failure(s) in this step. The API 'DELETE /intent/api/v1/wi
        red/networkDevices/{networkDeviceId}/configFeatures/intended/configurationModels/{previewActivityId}'
        can be used at any step to discard/cancel the provision of intended features. Step 3Use 'GET /intent/api
        /v1/wired/networkDevices/{networkDeviceId}/configFeatures/intended/configurationModels/{previewActivityI
        d}/networkDevices/{networkDeviceId}/config' to view the CLIs that will be applied to the device. Step
        4Use 'POST /intent/api/v1/wired/networkDevices/{networkDeviceId}/configFeatures/intended/configurationMo
        dels/{previewActivityId}/deploy' to deploy the intent to the device. .

        Args:
            network_device_id(str): networkDeviceId path parameter. Network device ID of the wired device to
                provision. The API /intent/api/v1/network-device can be used to get the network device
                ID. .
            preview_activity_id(str): previewActivityId path parameter. Activity id is taskId from Step 1POST
                /intent/api/v1/wired/networkDevices/{networkDeviceId}/configFeatures/intended/configurat
                ionModels' .
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
            https://developer.cisco.com/docs/dna-center/#!generate-the-device-config-for-the-configuration-model
        """
        check_type(headers, dict)
        check_type(network_device_id, str, may_be_none=False)
        check_type(preview_activity_id, str, may_be_none=False)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "networkDeviceId": network_device_id,
            "previewActivityId": preview_activity_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/wired/networkDevices/{networkDeviceId"
            + "}/configFeatures/intended/configurationModels/{previewAc"
            + "tivityId}/config"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.post(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_e174c2cf0ecb5b52806a95a08477ae4d_v2_3_7_9", json_data
        )

    def gets_the_device_config_for_the_configuration_model(
        self, network_device_id, preview_activity_id, headers=None, **request_parameters
    ):
        """Gets the device config for the configuration model. This API is 'Step 3' in the following workflow. Step 1Use
        'POST /intent/api/v1/wired/networkDevices/{networkDeviceId}/configFeatures/intended/configurationModels'
        to start the provision of intended features. The response has a taskId which is the previewActivityId in
        all subsequent APIs. The task must be successfully complete before proceeding to the next step. It is
        not recommended to proceed when there is any task failure in this step. The API 'DELETE /intent/api/v1/w
        ired/networkDevices/{networkDeviceId}/configFeatures/intended/configurationModels/{previewActivityId}'
        can be used at any step to discard/cancel the provision of intended features. Step 2Use 'POST /intent/ap
        i/v1/wired/networkDevices/{networkDeviceId}/configFeatures/intended/configurationModels/{previewActivity
        Id}/networkDevices/{networkDeviceId}/config' to generate device CLIs for preview. The response has a
        task ID. The task must be successfully complete before using the GET API to view CLIs. It is not
        recommended to proceed when there is any task failure(s) in this step. The API 'DELETE /intent/api/v1/wi
        red/networkDevices/{networkDeviceId}/configFeatures/intended/configurationModels/{previewActivityId}'
        can be used at any step to discard/cancel the provision of intended features. Step 3Use 'GET /intent/api
        /v1/wired/networkDevices/{networkDeviceId}/configFeatures/intended/configurationModels/{previewActivityI
        d}/networkDevices/{networkDeviceId}/config' to view the CLIs that will be applied to the device. Step
        4Use 'POST /intent/api/v1/wired/networkDevices/{networkDeviceId}/configFeatures/intended/configurationMo
        dels/{previewActivityId}/deploy' to deploy the intent to the device. .

        Args:
            network_device_id(str): networkDeviceId path parameter. Network device ID of the wired device to
                provision. The API /intent/api/v1/network-device can be used to get the network device
                ID. .
            preview_activity_id(str): previewActivityId path parameter. Activity id is the taskId from Step 2'POST /
                intent/api/v1/wired/networkDevices/{networkDeviceId}/configFeatures/intended/configurati
                onModels/{previewActivityId}/networkDevices/{networkDeviceId}/config .
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
            https://developer.cisco.com/docs/dna-center/#!gets-the-device-config-for-the-configuration-model
        """
        check_type(headers, dict)
        check_type(network_device_id, str, may_be_none=False)
        check_type(preview_activity_id, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            "networkDeviceId": network_device_id,
            "previewActivityId": preview_activity_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = (
            "/dna/intent/api/v1/wired/networkDevices/{networkDeviceId"
            + "}/configFeatures/intended/configurationModels/{previewAc"
            + "tivityId}/config"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_f7fdcd6e2dd5f4eaf7ceed5e5856ba2_v2_3_7_9", json_data
        )

    def deploy_the_intended_configuration_features_on_a_wired_device(
        self, network_device_id, headers=None, **request_parameters
    ):
        """Deploy the intended configuration features on a wired device. This can be used only if the provisioning settings
        do not require Preview or ITSM Approval before deploying configurations on network devices. The API
        /intent/api/v1/provisioningSettings can be used to get or update provisioning settings. .

        Args:
            network_device_id(str): networkDeviceId path parameter. Network device ID of the wired device to
                provision. The API /intent/api/v1/network-device can be used to get the network device
                ID. .
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
            https://developer.cisco.com/docs/dna-center/#!deploy-the-intended-configuration-features-on-a-wired-device
        """
        check_type(headers, dict)
        check_type(network_device_id, str, may_be_none=False)
        if headers is not None:
            if "Content-Type" in headers:
                check_type(headers.get("Content-Type"), str, may_be_none=False)
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
            "/dna/intent/api/v1/wired/networkDevices/{networkDeviceId"
            + "}/configFeatures/intended/deploy"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.post(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a21cb2b7ea258e197f22082301cd1cc_v2_3_7_9", json_data
        )

    def get_device_deployment_status_connectivity(
        self, network_device_id, headers=None, **request_parameters
    ):
        """The API returns device deployment status based on filter criteria. .

        Args:
            network_device_id(str): networkDeviceId path parameter. Network device ID of the wired device to
                provision. The API /intent/api/v1/network-device can be used to get the network device
                ID. .
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
            https://developer.cisco.com/docs/dna-center/#!get-device-deployment-status-connectivity
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
            "/dna/intent/api/v1/wired/networkDevices/{networkDeviceId"
            + "}/configFeatures/intended/deviceDeployments"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_be5246ea895b5b958caa2c67d6e389_v2_3_7_9", json_data
        )

    def get_service_deployment_status(
        self, network_device_id, headers=None, **request_parameters
    ):
        """Returns service deployment status based on filter criteria. .

        Args:
            network_device_id(str): networkDeviceId path parameter. Network device ID of the wired device to
                provision. The API /intent/api/v1/network-device can be used to get the network device
                ID. .
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
            https://developer.cisco.com/docs/dna-center/#!get-service-deployment-status
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
            "/dna/intent/api/v1/wired/networkDevices/{networkDeviceId"
            + "}/configFeatures/intended/serviceDeployments"
        )
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_c16b9caed6045399a6e7744914195fee_v2_3_7_9", json_data
        )


# Alias Functions

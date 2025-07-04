# -*- coding: utf-8 -*-
"""Cisco DNA Center Sensors API wrapper.

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


class Sensors(object):
    """Cisco DNA Center Sensors API (version: 2.3.7.6).

    Wraps the DNA Center Sensors
    API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new Sensors
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the DNA Center service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(Sensors, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def edit_sensor_test_template_v1(
        self,
        _id=None,
        actionInProgress=None,
        apCoverage=None,
        connection=None,
        encryptionMode=None,
        frequency=None,
        lastModifiedTime=None,
        location=None,
        locationInfoList=None,
        modelVersion=None,
        name=None,
        numAssociatedSensor=None,
        numNeighborAPThreshold=None,
        profiles=None,
        radioAsSensorRemoved=None,
        rssiThreshold=None,
        runNow=None,
        scheduleInDays=None,
        sensors=None,
        showWlcUpgradeBanner=None,
        siteHierarchy=None,
        ssids=None,
        startTime=None,
        status=None,
        templateName=None,
        testScheduleMode=None,
        version=None,
        wlans=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Intent API to deploy, schedule, or edit and existing SENSOR test template .

        Args:
            _id(string): Sensors's The sensor test template unique identifier, generated at test creation time .
            actionInProgress(string): Sensors's Indication of inprogress action .
            apCoverage(list): Sensors's apCoverage (list of objects).
            connection(string): Sensors's connection type of test: WIRED, WIRELESS, BOTH .
            encryptionMode(string): Sensors's Encryption mode .
            frequency(object): Sensors's frequency.
            lastModifiedTime(integer): Sensors's Last modify time .
            location(string): Sensors's Location string .
            locationInfoList(list): Sensors's locationInfoList (list of objects).
            modelVersion(integer): Sensors's Test template object model version (must be 2) .
            name(string): Sensors's The sensor test template name, which is the same as in 'templateName' .
            numAssociatedSensor(integer): Sensors's Number of associated sensor .
            numNeighborAPThreshold(integer): Sensors's Number of neighboring AP threshold .
            profiles(list): Sensors's profiles (list of objects).
            radioAsSensorRemoved(boolean): Sensors's Radio as sensor removed .
            rssiThreshold(integer): Sensors's RSSI threshold .
            runNow(string): Sensors's Run now (YES, NO) .
            scheduleInDays(integer): Sensors's Bit-wise value of scheduled test days .
            sensors(list): Sensors's sensors (list of objects).
            showWlcUpgradeBanner(boolean): Sensors's Show WLC upgrade banner .
            siteHierarchy(string): Sensors's Site hierarchy .
            ssids(list): Sensors's ssids (list of objects).
            startTime(integer): Sensors's Start time .
            status(string): Sensors's Status of the test (RUNNING, NOTRUNNING) .
            templateName(string): Sensors's The test template name that is to be edited .
            testScheduleMode(string): Sensors's Test schedule mode (ONDEMAND, DEDICATED, SCHEDULED, CONTINUOUS,
                RUNNOW) .
            version(integer): Sensors's The sensor test template version (must be 2) .
            wlans(list): Sensors's WLANs list  (list of strings).
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
            https://developer.cisco.com/docs/dna-center/#!edit-sensor-test-template
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = {
            "templateName": templateName,
            "name": name,
            "_id": _id,
            "version": version,
            "modelVersion": modelVersion,
            "startTime": startTime,
            "lastModifiedTime": lastModifiedTime,
            "numAssociatedSensor": numAssociatedSensor,
            "location": location,
            "siteHierarchy": siteHierarchy,
            "status": status,
            "connection": connection,
            "actionInProgress": actionInProgress,
            "frequency": frequency,
            "rssiThreshold": rssiThreshold,
            "numNeighborAPThreshold": numNeighborAPThreshold,
            "scheduleInDays": scheduleInDays,
            "wlans": wlans,
            "ssids": ssids,
            "profiles": profiles,
            "testScheduleMode": testScheduleMode,
            "showWlcUpgradeBanner": showWlcUpgradeBanner,
            "radioAsSensorRemoved": radioAsSensorRemoved,
            "encryptionMode": encryptionMode,
            "runNow": runNow,
            "locationInfoList": locationInfoList,
            "sensors": sensors,
            "apCoverage": apCoverage,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_e2f9718de3d050819cdc6355a3a43200_v2_3_7_6"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/AssuranceScheduleSensorTest"
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
            "bpm_e2f9718de3d050819cdc6355a3a43200_v2_3_7_6", json_data
        )

    def create_sensor_test_template_v1(
        self,
        apCoverage=None,
        connection=None,
        encryptionMode=None,
        locationInfoList=None,
        modelVersion=None,
        name=None,
        profiles=None,
        runNow=None,
        sensors=None,
        ssids=None,
        version=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Intent API to create a SENSOR test template with a new SSID, existing SSID, or both new and existing SSID .

        Args:
            apCoverage(list): Sensors's apCoverage (list of objects).
            connection(string): Sensors's connection type of test: WIRED, WIRELESS, BOTH .
            encryptionMode(string): Sensors's Encryption mode .
            locationInfoList(list): Sensors's locationInfoList (list of objects).
            modelVersion(integer): Sensors's Test template object model version (must be 2) .
            name(string): Sensors's The sensor test template name .
            profiles(list): Sensors's profiles (list of objects).
            runNow(string): Sensors's Run now (YES, NO) .
            sensors(list): Sensors's sensors (list of objects).
            ssids(list): Sensors's ssids (list of objects).
            version(integer): Sensors's The sensor test template version (must be 2) .
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
            https://developer.cisco.com/docs/dna-center/#!create-sensor-test-template
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = {
            "name": name,
            "version": version,
            "modelVersion": modelVersion,
            "connection": connection,
            "ssids": ssids,
            "profiles": profiles,
            "encryptionMode": encryptionMode,
            "runNow": runNow,
            "locationInfoList": locationInfoList,
            "sensors": sensors,
            "apCoverage": apCoverage,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_f7dd6a6cf8d57499168aae05847ad34_v2_3_7_6"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/sensor"
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
            "bpm_f7dd6a6cf8d57499168aae05847ad34_v2_3_7_6", json_data
        )

    def delete_sensor_test_v1(self, template_name, headers=None, **request_parameters):
        """Intent API to delete an existing SENSOR test template .

        Args:
            template_name(str): templateName query parameter.
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
            https://developer.cisco.com/docs/dna-center/#!delete-sensor-test
        """
        check_type(headers, dict)
        check_type(template_name, str, may_be_none=False)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {
            "templateName": template_name,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/sensor"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_a1c0ac4386555300b7f4a541d8dba625_v2_3_7_6", json_data
        )

    def sensors_v1(self, site_id=None, headers=None, **request_parameters):
        """Intent API to get a list of SENSOR devices .

        Args:
            site_id(str): siteId query parameter.
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
            https://developer.cisco.com/docs/dna-center/#!sensors
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

        e_url = "/dna/intent/api/v1/sensor"
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(
                endpoint_full_url, params=_params, headers=_headers
            )
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory(
            "bpm_cda740c5bdc92fd150c334d0e4e_v2_3_7_6", json_data
        )

    def run_now_sensor_test_v1(
        self,
        templateName=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Intent API to run a deployed SENSOR test .

        Args:
            templateName(string): Sensors's Template Name.
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
            https://developer.cisco.com/docs/dna-center/#!run-now-sensor-test
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = {
            "templateName": templateName,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_cfadc5e4c912588389f4f63d2fb6e4ed_v2_3_7_6"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/sensor-run-now"
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
            "bpm_cfadc5e4c912588389f4f63d2fb6e4ed_v2_3_7_6", json_data
        )

    def duplicate_sensor_test_template_v1(
        self,
        newTemplateName=None,
        templateName=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """Intent API to duplicate an existing SENSOR test template .

        Args:
            newTemplateName(string): Sensors's Destination test template name .
            templateName(string): Sensors's Source test template name .
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
            https://developer.cisco.com/docs/dna-center/#!duplicate-sensor-test-template
        """
        check_type(headers, dict)
        check_type(payload, dict)
        if headers is not None:
            if "X-Auth-Token" in headers:
                check_type(headers.get("X-Auth-Token"), str, may_be_none=False)

        _params = {}
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {}
        _payload = {
            "templateName": templateName,
            "newTemplateName": newTemplateName,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator(
                "jsd_a352f6280e445075b3ea7cbf868c2d94_v2_3_7_6"
            ).validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = "/dna/intent/api/v1/sensorTestTemplate"
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
            "bpm_a352f6280e445075b3ea7cbf868c2d94_v2_3_7_6", json_data
        )

    # Alias Function
    def create_sensor_test_template(
        self,
        apCoverage=None,
        connection=None,
        encryptionMode=None,
        locationInfoList=None,
        modelVersion=None,
        name=None,
        profiles=None,
        runNow=None,
        sensors=None,
        ssids=None,
        version=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This function is an alias of create_sensor_test_template_v1 .
        Args:
            apCoverage(list): Sensors's apCoverage (list of objects).
            connection(string): Sensors's connection type of test: WIRED, WIRELESS, BOTH .
            encryptionMode(string): Sensors's Encryption mode .
            locationInfoList(list): Sensors's locationInfoList (list of objects).
            modelVersion(integer): Sensors's Test template object model version (must be 2) .
            name(string): Sensors's The sensor test template name .
            profiles(list): Sensors's profiles (list of objects).
            runNow(string): Sensors's Run now (YES, NO) .
            sensors(list): Sensors's sensors (list of objects).
            ssids(list): Sensors's ssids (list of objects).
            version(integer): Sensors's The sensor test template version (must be 2) .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of create_sensor_test_template_v1 .
        """
        return self.create_sensor_test_template_v1(
            apCoverage=apCoverage,
            connection=connection,
            encryptionMode=encryptionMode,
            locationInfoList=locationInfoList,
            modelVersion=modelVersion,
            name=name,
            profiles=profiles,
            runNow=runNow,
            sensors=sensors,
            ssids=ssids,
            version=version,
            headers=headers,
            payload=payload,
            active_validation=active_validation,
            **request_parameters
        )

    # Alias Function
    def run_now_sensor_test(
        self,
        templateName=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This function is an alias of run_now_sensor_test_v1 .
        Args:
            templateName(string): Sensors's Template Name.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of run_now_sensor_test_v1 .
        """
        return self.run_now_sensor_test_v1(
            templateName=templateName,
            headers=headers,
            payload=payload,
            active_validation=active_validation,
            **request_parameters
        )

    # Alias Function
    def delete_sensor_test(self, template_name, headers=None, **request_parameters):
        """This function is an alias of delete_sensor_test_v1 .
        Args:
            template_name(basestring): templateName query parameter.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of delete_sensor_test_v1 .
        """
        return self.delete_sensor_test_v1(
            template_name=template_name, headers=headers, **request_parameters
        )

    # Alias Function
    def duplicate_sensor_test_template(
        self,
        newTemplateName=None,
        templateName=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This function is an alias of duplicate_sensor_test_template_v1 .
        Args:
            newTemplateName(string): Sensors's Destination test template name .
            templateName(string): Sensors's Source test template name .
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of duplicate_sensor_test_template_v1 .
        """
        return self.duplicate_sensor_test_template_v1(
            newTemplateName=newTemplateName,
            templateName=templateName,
            headers=headers,
            payload=payload,
            active_validation=active_validation,
            **request_parameters
        )

    # Alias Function
    def sensors(self, site_id=None, headers=None, **request_parameters):
        """This function is an alias of sensors_v1 .
        Args:
            site_id(basestring): siteId query parameter.
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of sensors_v1 .
        """
        return self.sensors_v1(site_id=site_id, headers=headers, **request_parameters)

    # Alias Function
    def edit_sensor_test_template(
        self,
        _id=None,
        actionInProgress=None,
        apCoverage=None,
        connection=None,
        encryptionMode=None,
        frequency=None,
        lastModifiedTime=None,
        location=None,
        locationInfoList=None,
        modelVersion=None,
        name=None,
        numAssociatedSensor=None,
        numNeighborAPThreshold=None,
        profiles=None,
        radioAsSensorRemoved=None,
        rssiThreshold=None,
        runNow=None,
        scheduleInDays=None,
        sensors=None,
        showWlcUpgradeBanner=None,
        siteHierarchy=None,
        ssids=None,
        startTime=None,
        status=None,
        templateName=None,
        testScheduleMode=None,
        version=None,
        wlans=None,
        headers=None,
        payload=None,
        active_validation=True,
        **request_parameters
    ):
        """This function is an alias of edit_sensor_test_template_v1 .
        Args:
            _id(string): Sensors's The sensor test template unique identifier, generated at test creation time .
            actionInProgress(string): Sensors's Indication of inprogress action .
            apCoverage(list): Sensors's apCoverage (list of objects).
            connection(string): Sensors's connection type of test: WIRED, WIRELESS, BOTH .
            encryptionMode(string): Sensors's Encryption mode .
            frequency(object): Sensors's frequency.
            lastModifiedTime(integer): Sensors's Last modify time .
            location(string): Sensors's Location string .
            locationInfoList(list): Sensors's locationInfoList (list of objects).
            modelVersion(integer): Sensors's Test template object model version (must be 2) .
            name(string): Sensors's The sensor test template name, which is the same as in 'templateName' .
            numAssociatedSensor(integer): Sensors's Number of associated sensor .
            numNeighborAPThreshold(integer): Sensors's Number of neighboring AP threshold .
            profiles(list): Sensors's profiles (list of objects).
            radioAsSensorRemoved(boolean): Sensors's Radio as sensor removed .
            rssiThreshold(integer): Sensors's RSSI threshold .
            runNow(string): Sensors's Run now (YES, NO) .
            scheduleInDays(integer): Sensors's Bit-wise value of scheduled test days .
            sensors(list): Sensors's sensors (list of objects).
            showWlcUpgradeBanner(boolean): Sensors's Show WLC upgrade banner .
            siteHierarchy(string): Sensors's Site hierarchy .
            ssids(list): Sensors's ssids (list of objects).
            startTime(integer): Sensors's Start time .
            status(string): Sensors's Status of the test (RUNNING, NOTRUNNING) .
            templateName(string): Sensors's The test template name that is to be edited .
            testScheduleMode(string): Sensors's Test schedule mode (ONDEMAND, DEDICATED, SCHEDULED, CONTINUOUS,
                RUNNOW) .
            version(integer): Sensors's The sensor test template version (must be 2) .
            wlans(list): Sensors's WLANs list  (list of strings).
            headers(dict): Dictionary of HTTP Headers to send with the Request
                .
            payload(): A JSON serializable Python object to send in the
                body of the Request.
            active_validation(bool): Enable/Disable payload validation.
                Defaults to True.
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            This function returns the output of edit_sensor_test_template_v1 .
        """
        return self.edit_sensor_test_template_v1(
            _id=_id,
            actionInProgress=actionInProgress,
            apCoverage=apCoverage,
            connection=connection,
            encryptionMode=encryptionMode,
            frequency=frequency,
            lastModifiedTime=lastModifiedTime,
            location=location,
            locationInfoList=locationInfoList,
            modelVersion=modelVersion,
            name=name,
            numAssociatedSensor=numAssociatedSensor,
            numNeighborAPThreshold=numNeighborAPThreshold,
            profiles=profiles,
            radioAsSensorRemoved=radioAsSensorRemoved,
            rssiThreshold=rssiThreshold,
            runNow=runNow,
            scheduleInDays=scheduleInDays,
            sensors=sensors,
            showWlcUpgradeBanner=showWlcUpgradeBanner,
            siteHierarchy=siteHierarchy,
            ssids=ssids,
            startTime=startTime,
            status=status,
            templateName=templateName,
            testScheduleMode=testScheduleMode,
            version=version,
            wlans=wlans,
            headers=headers,
            payload=payload,
            active_validation=active_validation,
            **request_parameters
        )

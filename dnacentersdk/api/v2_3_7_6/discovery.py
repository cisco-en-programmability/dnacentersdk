# -*- coding: utf-8 -*-
"""Cisco DNA Center Discovery API wrapper.

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


class Discovery(object):
    """Cisco DNA Center Discovery API (version: 2.3.7.6).

    Wraps the DNA Center Discovery
    API and exposes the API as native Python
    methods that return native Python objects.

    """

    def __init__(self, session, object_factory, request_validator):
        """Initialize a new Discovery
        object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the DNA Center service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession)

        super(Discovery, self).__init__()

        self._session = session
        self._object_factory = object_factory
        self._request_validator = request_validator

    def delete_all_discovery(self,
                             headers=None,
                             **request_parameters):
        """Stops all the discoveries and removes them .

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

        e_url = ('/dna/intent/api/v1/discovery')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(endpoint_full_url, params=_params,
                                             headers=_headers)
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_a1d007749a7e5b99aabddf1543714a9a_v2_3_7_6', json_data)

    def updates_discovery_by_id(self,
                                attributeInfo=None,
                                cdpLevel=None,
                                deviceIds=None,
                                discoveryCondition=None,
                                discoveryStatus=None,
                                discoveryType=None,
                                enablePasswordList=None,
                                globalCredentialIdList=None,
                                httpReadCredential=None,
                                httpWriteCredential=None,
                                id=None,
                                ipAddressList=None,
                                ipFilterList=None,
                                isAutoCdp=None,
                                lldpLevel=None,
                                name=None,
                                netconfPort=None,
                                numDevices=None,
                                parentDiscoveryId=None,
                                passwordList=None,
                                preferredMgmtIPMethod=None,
                                protocolOrder=None,
                                retryCount=None,
                                snmpAuthPassphrase=None,
                                snmpAuthProtocol=None,
                                snmpMode=None,
                                snmpPrivPassphrase=None,
                                snmpPrivProtocol=None,
                                snmpRoCommunity=None,
                                snmpRoCommunityDesc=None,
                                snmpRwCommunity=None,
                                snmpRwCommunityDesc=None,
                                snmpUserName=None,
                                timeOut=None,
                                updateMgmtIp=None,
                                userNameList=None,
                                headers=None,
                                payload=None,
                                active_validation=True,
                                **request_parameters):
        """Stops or starts an existing discovery .

        Args:
            attributeInfo(object): Discovery's Deprecated .
            cdpLevel(integer): Discovery's CDP level to which neighbor devices to be discovered .
            deviceIds(string): Discovery's Ids of the devices discovered in a discovery .
            discoveryCondition(string): Discovery's To indicate the discovery status. Available options: Complete or
                In Progress .
            discoveryStatus(string): Discovery's Status of the discovery. Available options are: active, inactive,
                edit .
            discoveryType(string): Discovery's Type of the discovery. 'SINGLE', 'RANGE', 'MULTI RANGE', 'CDP',
                'LLDP', 'CIDR' .
            enablePasswordList(string): Discovery's Enable Password of the devices to be discovered .
            globalCredentialIdList(list): Discovery's List of global credential ids to be used  (list of strings).
            httpReadCredential(object): Discovery's httpReadCredential.
            httpWriteCredential(object): Discovery's httpWriteCredential.
            id(string): Discovery's Unique Discovery Id .
            ipAddressList(string): Discovery's List of IP address of the devices to be discovered .
            ipFilterList(string): Discovery's IP addresses of the devices to be filtered .
            isAutoCdp(boolean): Discovery's Flag to mention if CDP discovery or not .
            lldpLevel(integer): Discovery's LLDP level to which neighbor devices to be discovered .
            name(string): Discovery's Name for the discovery .
            netconfPort(string): Discovery's Netconf port on the device. Netconf will need valid sshv2 credentials
                for it to work .
            numDevices(integer): Discovery's Number of devices discovered in the discovery .
            parentDiscoveryId(string): Discovery's Parent Discovery Id from which the discovery was initiated .
            passwordList(string): Discovery's Password of the devices to be discovered .
            preferredMgmtIPMethod(string): Discovery's Preferred management IP method. Available options are 'None'
                and 'UseLoopBack' .
            protocolOrder(string): Discovery's Order of protocol (ssh/telnet) in which device connection will be
                tried. Ex: 'telnet': only telnet; 'ssh,telnet': ssh with higher order than telnet .
            retryCount(integer): Discovery's Number of times to try establishing connection to device .
            snmpAuthPassphrase(string): Discovery's Auth passphrase for SNMP .
            snmpAuthProtocol(string): Discovery's SNMP auth protocol. SHA' or 'MD5' .
            snmpMode(string): Discovery's Mode of SNMP. 'AUTHPRIV' or 'AUTHNOPRIV' or 'NOAUTHNOPRIV' .
            snmpPrivPassphrase(string): Discovery's Passphrase for SNMP privacy .
            snmpPrivProtocol(string): Discovery's SNMP privacy protocol. 'AES128' .
            snmpRoCommunity(string): Discovery's SNMP RO community of the devices to be discovered .
            snmpRoCommunityDesc(string): Discovery's Description for SNMP RO community .
            snmpRwCommunity(string): Discovery's SNMP RW community of the devices to be discovered .
            snmpRwCommunityDesc(string): Discovery's Description for SNMP RW community .
            snmpUserName(string): Discovery's SNMP username of the device .
            timeOut(integer): Discovery's Time to wait for device response. .
            updateMgmtIp(boolean): Discovery's Updates Management IP if multiple IPs are available for a device. If
                set to true, when a device is rediscovered with a different IP, the management IP is
                updated. Default value is false .
            userNameList(string): Discovery's Username of the devices to be discovered .
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
            'attributeInfo':
                attributeInfo,
            'cdpLevel':
                cdpLevel,
            'deviceIds':
                deviceIds,
            'discoveryCondition':
                discoveryCondition,
            'discoveryStatus':
                discoveryStatus,
            'discoveryType':
                discoveryType,
            'enablePasswordList':
                enablePasswordList,
            'globalCredentialIdList':
                globalCredentialIdList,
            'httpReadCredential':
                httpReadCredential,
            'httpWriteCredential':
                httpWriteCredential,
            'id':
                id,
            'ipAddressList':
                ipAddressList,
            'ipFilterList':
                ipFilterList,
            'isAutoCdp':
                isAutoCdp,
            'lldpLevel':
                lldpLevel,
            'name':
                name,
            'netconfPort':
                netconfPort,
            'numDevices':
                numDevices,
            'parentDiscoveryId':
                parentDiscoveryId,
            'passwordList':
                passwordList,
            'preferredMgmtIPMethod':
                preferredMgmtIPMethod,
            'protocolOrder':
                protocolOrder,
            'retryCount':
                retryCount,
            'snmpAuthPassphrase':
                snmpAuthPassphrase,
            'snmpAuthProtocol':
                snmpAuthProtocol,
            'snmpMode':
                snmpMode,
            'snmpPrivPassphrase':
                snmpPrivPassphrase,
            'snmpPrivProtocol':
                snmpPrivProtocol,
            'snmpRoCommunity':
                snmpRoCommunity,
            'snmpRoCommunityDesc':
                snmpRoCommunityDesc,
            'snmpRwCommunity':
                snmpRwCommunity,
            'snmpRwCommunityDesc':
                snmpRwCommunityDesc,
            'snmpUserName':
                snmpUserName,
            'timeOut':
                timeOut,
            'updateMgmtIp':
                updateMgmtIp,
            'userNameList':
                userNameList,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_f325b2c7e429566ba5ed9ae8253b5bef_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/discovery')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload,
                                          headers=_headers)
        else:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload)

        return self._object_factory('bpm_f325b2c7e429566ba5ed9ae8253b5bef_v2_3_7_6', json_data)

    def start_discovery(self,
                        cdpLevel=None,
                        discoveryType=None,
                        enablePasswordList=None,
                        globalCredentialIdList=None,
                        httpReadCredential=None,
                        httpWriteCredential=None,
                        ipAddressList=None,
                        ipFilterList=None,
                        lldpLevel=None,
                        name=None,
                        netconfPort=None,
                        passwordList=None,
                        preferredMgmtIPMethod=None,
                        protocolOrder=None,
                        retry=None,
                        snmpAuthPassphrase=None,
                        snmpAuthProtocol=None,
                        snmpMode=None,
                        snmpPrivPassphrase=None,
                        snmpPrivProtocol=None,
                        snmpROCommunity=None,
                        snmpROCommunityDesc=None,
                        snmpRWCommunity=None,
                        snmpRWCommunityDesc=None,
                        snmpUserName=None,
                        snmpVersion=None,
                        timeout=None,
                        userNameList=None,
                        headers=None,
                        payload=None,
                        active_validation=True,
                        **request_parameters):
        """Initiates discovery with the given parameters .

        Args:
            cdpLevel(integer): Discovery's CDP level to which neighbor devices are to be discovered .
            discoveryType(string): Discovery's Type of the discovery. 'SINGLE', 'RANGE', 'MULTI RANGE', 'CDP',
                'LLDP', 'CIDR' .
            enablePasswordList(list): Discovery's Enable Password of the devices to be discovered  (list of
                strings).
            globalCredentialIdList(list): Discovery's Global Credential Ids to be used for discovery  (list of
                strings).
            httpReadCredential(object): Discovery's httpReadCredential.
            httpWriteCredential(object): Discovery's httpWriteCredential.
            ipAddressList(string): Discovery's IP Address of devices to be discovered. Ex: '172.30.0.1' for SINGLE,
                CDP and LLDP; '72.30.0.1-172.30.0.4' for RANGE;
                '72.30.0.1-172.30.0.4,172.31.0.1-172.31.0.4' for MULTI RANGE; '172.30.0.1/20' for CIDR .
            ipFilterList(list): Discovery's IP Addresses of the devices to be filtered out during discovery  (list
                of strings).
            lldpLevel(integer): Discovery's LLDP level to which neighbor devices to be discovered .
            name(string): Discovery's Name of the discovery .
            netconfPort(string): Discovery's Netconf Port. It will need valid SSH credentials to work .
            passwordList(list): Discovery's Password of the devices to be discovered  (list of strings).
            preferredMgmtIPMethod(string): Discovery's Preferred Management IP Method.'None' or 'UseLoopBack'.
                Default is 'None' .
            protocolOrder(string): Discovery's Order of protocol (ssh/telnet) in which device connection will be
                tried. Ex: 'telnet': only telnet; 'ssh,telnet': ssh with higher order than telnet .
            retry(integer): Discovery's Number of times to try establishing connection to device .
            snmpAuthPassphrase(string): Discovery's Auth passphrase for SNMP .
            snmpAuthProtocol(string): Discovery's SNMP auth protocol. SHA' or 'MD5' .
            snmpMode(string): Discovery's Mode of SNMP. 'AUTHPRIV' or 'AUTHNOPRIV' or 'NOAUTHNOPRIV' .
            snmpPrivPassphrase(string): Discovery's Pass phrase for SNMP privacy .
            snmpPrivProtocol(string): Discovery's SNMP privacy protocol. 'AES128' .
            snmpROCommunity(string): Discovery's SNMP RO community of the devices to be discovered .
            snmpROCommunityDesc(string): Discovery's Description for SNMP RO community .
            snmpRWCommunity(string): Discovery's SNMP RW community of the devices to be discovered .
            snmpRWCommunityDesc(string): Discovery's Description for SNMP RW community .
            snmpUserName(string): Discovery's SNMP username of the device .
            snmpVersion(string): Discovery's Version of SNMP. v2 or v3 .
            timeout(integer): Discovery's Time to wait for device response in seconds .
            userNameList(list): Discovery's Username of the devices to be discovered  (list of strings).
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
            'cdpLevel':
                cdpLevel,
            'discoveryType':
                discoveryType,
            'enablePasswordList':
                enablePasswordList,
            'globalCredentialIdList':
                globalCredentialIdList,
            'httpReadCredential':
                httpReadCredential,
            'httpWriteCredential':
                httpWriteCredential,
            'ipAddressList':
                ipAddressList,
            'ipFilterList':
                ipFilterList,
            'lldpLevel':
                lldpLevel,
            'name':
                name,
            'netconfPort':
                netconfPort,
            'passwordList':
                passwordList,
            'preferredMgmtIPMethod':
                preferredMgmtIPMethod,
            'protocolOrder':
                protocolOrder,
            'retry':
                retry,
            'snmpAuthPassphrase':
                snmpAuthPassphrase,
            'snmpAuthProtocol':
                snmpAuthProtocol,
            'snmpMode':
                snmpMode,
            'snmpPrivPassphrase':
                snmpPrivPassphrase,
            'snmpPrivProtocol':
                snmpPrivProtocol,
            'snmpROCommunity':
                snmpROCommunity,
            'snmpROCommunityDesc':
                snmpROCommunityDesc,
            'snmpRWCommunity':
                snmpRWCommunity,
            'snmpRWCommunityDesc':
                snmpRWCommunityDesc,
            'snmpUserName':
                snmpUserName,
            'snmpVersion':
                snmpVersion,
            'timeout':
                timeout,
            'userNameList':
                userNameList,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_fdbe4ec3e9f252a988404dc94250b80d_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/discovery')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_fdbe4ec3e9f252a988404dc94250b80d_v2_3_7_6', json_data)

    def get_count_of_all_discovery_jobs(self,
                                        headers=None,
                                        **request_parameters):
        """Returns the count of all available discovery jobs .

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

        e_url = ('/dna/intent/api/v1/discovery/count')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_e37fcf36e3539492dfb9cd21e49620_v2_3_7_6', json_data)

    def get_discovery_jobs_by_ip(self,
                                 ip_address,
                                 limit=None,
                                 name=None,
                                 offset=None,
                                 headers=None,
                                 **request_parameters):
        """Returns the list of discovery jobs for the given IP .

        Args:
            offset(int,str): offset query parameter.
            limit(int,str): limit query parameter.
            ip_address(str): ipAddress query parameter.
            name(str): name query parameter.
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
        check_type(offset, (int, str))
        check_type(limit, (int, str))
        check_type(ip_address, str,
                   may_be_none=False)
        check_type(name, str)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'offset':
                offset,
            'limit':
                limit,
            'ipAddress':
                ip_address,
            'name':
                name,
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

        e_url = ('/dna/intent/api/v1/discovery/job')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_bde1ca5763fc552ab78cd3b2ecf119b1_v2_3_7_6', json_data)

    def delete_discovery_by_id(self,
                               id,
                               headers=None,
                               **request_parameters):
        """Stops the discovery for the given Discovery ID and removes it. Discovery ID can be obtained using the "Get
        Discoveries by range" API. .

        Args:
            id(str): id path parameter. Discovery ID .
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
        check_type(id, str,
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
            'id': id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/discovery/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(endpoint_full_url, params=_params,
                                             headers=_headers)
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_bb187b0c0a55e7e8089ac78eb29d8a2_v2_3_7_6', json_data)

    def get_discovery_by_id(self,
                            id,
                            headers=None,
                            **request_parameters):
        """Returns discovery by Discovery ID. Discovery ID can be obtained using the "Get Discoveries by range" API. .

        Args:
            id(str): id path parameter. Discovery ID .
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
        check_type(id, str,
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
            'id': id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/discovery/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_c4370f0a57d85355a7061d7671f1b613_v2_3_7_6', json_data)

    def get_list_of_discoveries_by_discovery_id(self,
                                                id,
                                                ip_address=None,
                                                limit=None,
                                                offset=None,
                                                headers=None,
                                                **request_parameters):
        """Returns the list of discovery jobs for the given Discovery ID. The results can be optionally filtered based on
        IP. Discovery ID can be obtained using the "Get Discoveries by range" API. .

        Args:
            id(str): id path parameter. Discovery ID .
            offset(int,str): offset query parameter. Starting index for the records .
            limit(int,str): limit query parameter. Number of records to fetch from the starting index .
            ip_address(str): ipAddress query parameter. Filter records based on IP address .
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
        check_type(offset, (int, str))
        check_type(limit, (int, str))
        check_type(ip_address, str)
        check_type(id, str,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'offset':
                offset,
            'limit':
                limit,
            'ipAddress':
                ip_address,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'id': id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/discovery/{id}/job')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_e369e19c1a835567855984d9f2c628ef_v2_3_7_6', json_data)

    def get_discovered_network_devices_by_discovery_id(self,
                                                       id,
                                                       task_id=None,
                                                       headers=None,
                                                       **request_parameters):
        """Returns the network devices discovered for the given Discovery ID. Discovery ID can be obtained using the "Get
        Discoveries by range" API. .

        Args:
            id(str): id path parameter. Discovery ID .
            task_id(str): taskId query parameter.
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
        check_type(task_id, str)
        check_type(id, str,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'taskId':
                task_id,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'id': id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/discovery/{id}/network-device')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_f478b876b38a5cf094d80eced531b1a0_v2_3_7_6', json_data)

    def get_devices_discovered_by_id(self,
                                     id,
                                     task_id=None,
                                     headers=None,
                                     **request_parameters):
        """Returns the count of network devices discovered in the given discovery. Discovery ID can be obtained using the
        "Get Discoveries by range" API. .

        Args:
            id(str): id path parameter. Discovery ID .
            task_id(str): taskId query parameter.
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
        check_type(task_id, str)
        check_type(id, str,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'taskId':
                task_id,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'id': id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/discovery/{id}/network-device/count')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_a2f0cb47996d5bf7a3d5de89e2a002bb_v2_3_7_6', json_data)

    def get_discovered_devices_by_range(self,
                                        id,
                                        records_to_return,
                                        start_index,
                                        task_id=None,
                                        headers=None,
                                        **request_parameters):
        """Returns the network devices discovered for the given discovery and for the given range. The maximum number of
        records that can be retrieved is 500. Discovery ID can be obtained using the "Get Discoveries by range"
        API. .

        Args:
            id(str): id path parameter. Discovery ID .
            start_index(int): startIndex path parameter. Starting index for the records .
            records_to_return(int): recordsToReturn path parameter. Number of records to fetch from the start index
                .
            task_id(str): taskId query parameter.
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
        check_type(task_id, str)
        check_type(id, str,
                   may_be_none=False)
        check_type(start_index, int,
                   may_be_none=False)
        check_type(records_to_return, int,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'taskId':
                task_id,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'id': id,
            'startIndex': start_index,
            'recordsToReturn': records_to_return,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/discovery/{id}/network-'
                 + 'device/{startIndex}/{recordsToReturn}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_fd0ae0041dc59fb8aae545a8199d7b4_v2_3_7_6', json_data)

    def get_network_devices_from_discovery(self,
                                           id,
                                           cli_status=None,
                                           http_status=None,
                                           ip_address=None,
                                           netconf_status=None,
                                           ping_status=None,
                                           snmp_status=None,
                                           sort_by=None,
                                           sort_order=None,
                                           task_id=None,
                                           headers=None,
                                           **request_parameters):
        """Returns the devices discovered in the given discovery based on given filters. Discovery ID can be obtained using
        the "Get Discoveries by range" API. .

        Args:
            id(str): id path parameter. Discovery ID .
            task_id(str): taskId query parameter.
            sort_by(str): sortBy query parameter. Sort by field. Available values are pingStatus,
                cliStatus,snmpStatus, httpStatus and netconfStatus .
            sort_order(str): sortOrder query parameter. Order of sorting based on sortBy. Available values
                are 'asc' and 'des' .
            ip_address(str, list, set, tuple): ipAddress query parameter. IP Address of the device .
            ping_status(str, list, set, tuple): pingStatus query parameter. Ping status for the IP during the
                job run. Available values are 'SUCCESS', 'FAILURE', 'NOT-PROVIDED' and 'NOT-VALIDATED' .
            snmp_status(str, list, set, tuple): snmpStatus query parameter. SNMP status for the IP during the
                job run. Available values are 'SUCCESS', 'FAILURE', 'NOT-PROVIDED' and 'NOT-VALIDATED' .
            cli_status(str, list, set, tuple): cliStatus query parameter. CLI status for the IP during the
                job run. Available values are 'SUCCESS', 'FAILURE', 'NOT-PROVIDED' and 'NOT-VALIDATED' .
            netconf_status(str, list, set, tuple): netconfStatus query parameter. NETCONF status for the IP
                during the job run. Available values are 'SUCCESS', 'FAILURE', 'NOT-PROVIDED' and 'NOT-
                VALIDATED' .
            http_status(str, list, set, tuple): httpStatus query parameter. HTTP staus for the IP during the
                job run. Available values are 'SUCCESS', 'FAILURE', 'NOT-PROVIDED' and 'NOT-VALIDATED' .
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
        check_type(task_id, str)
        check_type(sort_by, str)
        check_type(sort_order, str)
        check_type(ip_address, (str, list, set, tuple))
        check_type(ping_status, (str, list, set, tuple))
        check_type(snmp_status, (str, list, set, tuple))
        check_type(cli_status, (str, list, set, tuple))
        check_type(netconf_status, (str, list, set, tuple))
        check_type(http_status, (str, list, set, tuple))
        check_type(id, str,
                   may_be_none=False)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'taskId':
                task_id,
            'sortBy':
                sort_by,
            'sortOrder':
                sort_order,
            'ipAddress':
                ip_address,
            'pingStatus':
                ping_status,
            'snmpStatus':
                snmp_status,
            'cliStatus':
                cli_status,
            'netconfStatus':
                netconf_status,
            'httpStatus':
                http_status,
        }
        _params.update(request_parameters)
        _params = dict_from_items_with_values(_params)

        path_params = {
            'id': id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/discovery/{id}/summary')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_b212632561f886c01676b12a2b1_v2_3_7_6', json_data)

    def delete_discovery_by_specified_range(self,
                                            records_to_delete,
                                            start_index,
                                            headers=None,
                                            **request_parameters):
        """Stops discovery for the given range and removes them .

        Args:
            start_index(int): startIndex path parameter. Starting index for the records .
            records_to_delete(int): recordsToDelete path parameter. Number of records to delete from the starting
                index .
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
        check_type(start_index, int,
                   may_be_none=False)
        check_type(records_to_delete, int,
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
            'startIndex': start_index,
            'recordsToDelete': records_to_delete,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/discovery/{startIndex}/{recordsToDele'
                 + 'te}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(endpoint_full_url, params=_params,
                                             headers=_headers)
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_cba543cfb0957e9bc38d8c7f49f3e47_v2_3_7_6', json_data)

    def get_discoveries_by_range(self,
                                 records_to_return,
                                 start_index,
                                 headers=None,
                                 **request_parameters):
        """Returns the discoveries by specified range .

        Args:
            start_index(int): startIndex path parameter. Starting index for the records .
            records_to_return(int): recordsToReturn path parameter. Number of records to fetch from the starting
                index .
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
        check_type(start_index, int,
                   may_be_none=False)
        check_type(records_to_return, int,
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
            'startIndex': start_index,
            'recordsToReturn': records_to_return,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/discovery/{startIndex}/{recordsToRetu'
                 + 'rn}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_e847420499a7592d993b7c7dff809f0d_v2_3_7_6', json_data)

    def get_global_credentials(self,
                               credential_sub_type,
                               order=None,
                               sort_by=None,
                               headers=None,
                               **request_parameters):
        """Returns global credential for the given credential sub type .

        Args:
            credential_sub_type(str): credentialSubType query parameter. Credential type as CLI /
                SNMPV2_READ_COMMUNITY / SNMPV2_WRITE_COMMUNITY / SNMPV3 / HTTP_WRITE / HTTP_READ /
                NETCONF .
            sort_by(str): sortBy query parameter. Field to sort the results by. Sorts by 'instanceId' if no
                value is provided .
            order(str): order query parameter. Order of sorting. 'asc' or 'des' .
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
        check_type(credential_sub_type, str,
                   may_be_none=False)
        check_type(sort_by, str)
        check_type(order, str)
        if headers is not None:
            if 'X-Auth-Token' in headers:
                check_type(headers.get('X-Auth-Token'),
                           str, may_be_none=False)

        _params = {
            'credentialSubType':
                credential_sub_type,
            'sortBy':
                sort_by,
            'order':
                order,
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

        e_url = ('/dna/intent/api/v1/global-credential')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_ce4a30581da554591309dd423a91e7a_v2_3_7_6', json_data)

    def update_cli_credentials(self,
                               comments=None,
                               credentialType=None,
                               description=None,
                               enablePassword=None,
                               id=None,
                               instanceTenantId=None,
                               instanceUuid=None,
                               password=None,
                               username=None,
                               headers=None,
                               payload=None,
                               active_validation=True,
                               **request_parameters):
        """Updates global CLI credentials .

        Args:
            comments(string): Discovery's Comments to identify the CLI credential .
            credentialType(string): Discovery's Credential type to identify the application that uses the CLI
                credential . Available values are 'GLOBAL' and 'APP'.
            description(string): Discovery's Description for CLI Credentials .
            enablePassword(string): Discovery's CLI Enable Password .
            id(string): Discovery's Id of the CLI Credential in UUID format .
            instanceTenantId(string): Discovery's Deprecated .
            instanceUuid(string): Discovery's Deprecated .
            password(string): Discovery's CLI Password .
            username(string): Discovery's CLI Username .
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
        _payload = {
            'comments':
                comments,
            'credentialType':
                credentialType,
            'description':
                description,
            'enablePassword':
                enablePassword,
            'id':
                id,
            'instanceTenantId':
                instanceTenantId,
            'instanceUuid':
                instanceUuid,
            'password':
                password,
            'username':
                username,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_d39d23589e85db0a63c414057c_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/global-credential/cli')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload,
                                          headers=_headers)
        else:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload)

        return self._object_factory('bpm_d39d23589e85db0a63c414057c_v2_3_7_6', json_data)

    def create_cli_credentials(self,
                               headers=None,
                               payload=None,
                               active_validation=True,
                               **request_parameters):
        """Adds global CLI credential .

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
            self._request_validator('jsd_c524f0ec199e5435bcaee56b423532e7_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/global-credential/cli')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_c524f0ec199e5435bcaee56b423532e7_v2_3_7_6', json_data)

    def create_http_read_credentials(self,
                                     headers=None,
                                     payload=None,
                                     active_validation=True,
                                     **request_parameters):
        """Adds HTTP read credentials .

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
            self._request_validator('jsd_ffcaccdd9f2530abf66adc98c3f0201_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/global-credential/http-read')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_ffcaccdd9f2530abf66adc98c3f0201_v2_3_7_6', json_data)

    def update_http_read_credential(self,
                                    comments=None,
                                    credentialType=None,
                                    description=None,
                                    id=None,
                                    instanceTenantId=None,
                                    instanceUuid=None,
                                    password=None,
                                    port=None,
                                    secure=None,
                                    username=None,
                                    headers=None,
                                    payload=None,
                                    active_validation=True,
                                    **request_parameters):
        """Updates global HTTP Read credential .

        Args:
            comments(string): Discovery's Comments to identify the HTTP(S) Read credential .
            credentialType(string): Discovery's Credential type to identify the application that uses the HTTP(S)
                Read credential . Available values are 'GLOBAL' and 'APP'.
            description(string): Discovery's Description for HTTP(S) Read Credential .
            id(string): Discovery's Id of the HTTP(S) Read Credential in UUID format .
            instanceTenantId(string): Discovery's Deprecated .
            instanceUuid(string): Discovery's Deprecated .
            password(string): Discovery's HTTP(S) Read Password .
            port(integer): Discovery's HTTP(S) Port. Valid port should be in the range of 1 to 65535. .
            secure(boolean): Discovery's Flag for HTTPS Read .
            username(string): Discovery's HTTP(S) Read Username .
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
            'comments':
                comments,
            'credentialType':
                credentialType,
            'description':
                description,
            'id':
                id,
            'instanceTenantId':
                instanceTenantId,
            'instanceUuid':
                instanceUuid,
            'password':
                password,
            'port':
                port,
            'secure':
                secure,
            'username':
                username,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_d1845268faf55f98bc952872259f16f_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/global-credential/http-read')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload,
                                          headers=_headers)
        else:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload)

        return self._object_factory('bpm_d1845268faf55f98bc952872259f16f_v2_3_7_6', json_data)

    def update_http_write_credentials(self,
                                      comments=None,
                                      credentialType=None,
                                      description=None,
                                      id=None,
                                      instanceTenantId=None,
                                      instanceUuid=None,
                                      password=None,
                                      port=None,
                                      secure=None,
                                      username=None,
                                      headers=None,
                                      payload=None,
                                      active_validation=True,
                                      **request_parameters):
        """Updates global HTTP write credentials .

        Args:
            comments(string): Discovery's Comments to identify the HTTP(S) Write credential .
            credentialType(string): Discovery's Credential type to identify the application that uses the HTTP(S)
                Write credential . Available values are 'GLOBAL' and 'APP'.
            description(string): Discovery's Description for HTTP(S) Write Credential .
            id(string): Discovery's Id of the HTTP(S) Write Credential in UUID format .
            instanceTenantId(string): Discovery's Deprecated .
            instanceUuid(string): Discovery's Deprecated .
            password(string): Discovery's HTTP(S) Write Password .
            port(integer): Discovery's HTTP(S) Port. Valid port should be in the range of 1 to 65535. .
            secure(boolean): Discovery's Flag for HTTPS Write .
            username(string): Discovery's HTTP(S) Write Username .
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
        _payload = {
            'comments':
                comments,
            'credentialType':
                credentialType,
            'description':
                description,
            'id':
                id,
            'instanceTenantId':
                instanceTenantId,
            'instanceUuid':
                instanceUuid,
            'password':
                password,
            'port':
                port,
            'secure':
                secure,
            'username':
                username,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_f6536a8f01d5863856a0a8308198e15_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/global-credential/http-write')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload,
                                          headers=_headers)
        else:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload)

        return self._object_factory('bpm_f6536a8f01d5863856a0a8308198e15_v2_3_7_6', json_data)

    def create_http_write_credentials(self,
                                      headers=None,
                                      payload=None,
                                      active_validation=True,
                                      **request_parameters):
        """Adds global HTTP write credentials .

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
            self._request_validator('jsd_f77386a48895fa59dcddcc7dd4addb5_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/global-credential/http-write')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_f77386a48895fa59dcddcc7dd4addb5_v2_3_7_6', json_data)

    def update_netconf_credentials(self,
                                   comments=None,
                                   credentialType=None,
                                   description=None,
                                   id=None,
                                   instanceTenantId=None,
                                   instanceUuid=None,
                                   netconfPort=None,
                                   headers=None,
                                   payload=None,
                                   active_validation=True,
                                   **request_parameters):
        """Updates global netconf credentials .

        Args:
            comments(string): Discovery's Comments to identify the netconf credential .
            credentialType(string): Discovery's Credential type to identify the application that uses the netconf
                credential . Available values are 'GLOBAL' and 'APP'.
            description(string): Discovery's Description for Netconf Credentials .
            id(string): Discovery's Id of the Netconf Credential in UUID format .
            instanceTenantId(string): Discovery's Deprecated .
            instanceUuid(string): Discovery's Deprecated .
            netconfPort(string): Discovery's Netconf port on the device. Valid port should be in the range of 1 to
                65535. .
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
        _payload = {
            'comments':
                comments,
            'credentialType':
                credentialType,
            'description':
                description,
            'id':
                id,
            'instanceTenantId':
                instanceTenantId,
            'instanceUuid':
                instanceUuid,
            'netconfPort':
                netconfPort,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_f7cf4f24d54c6944a31ed308f8361_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/global-credential/netconf')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload,
                                          headers=_headers)
        else:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload)

        return self._object_factory('bpm_f7cf4f24d54c6944a31ed308f8361_v2_3_7_6', json_data)

    def create_netconf_credentials(self,
                                   headers=None,
                                   payload=None,
                                   active_validation=True,
                                   **request_parameters):
        """Adds global netconf credentials .

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
            self._request_validator('jsd_f5645e6e819558fa08761dee45ca406_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/global-credential/netconf')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_f5645e6e819558fa08761dee45ca406_v2_3_7_6', json_data)

    def update_snmp_read_community(self,
                                   comments=None,
                                   credentialType=None,
                                   description=None,
                                   instanceUuid=None,
                                   readCommunity=None,
                                   headers=None,
                                   payload=None,
                                   active_validation=True,
                                   **request_parameters):
        """Updates global SNMP read community .

        Args:
            comments(string): Discovery's Comments to identify the credential .
            credentialType(string): Discovery's Credential type to identify the application that uses the credential
                . Available values are 'GLOBAL' and 'APP'.
            description(string): Discovery's Name/Description of the credential .
            instanceUuid(string): Discovery's Credential UUID .
            readCommunity(string): Discovery's SNMP read community. NO!$DATA!$ for no value change .
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
        _payload = {
            'comments':
                comments,
            'credentialType':
                credentialType,
            'description':
                description,
            'instanceUuid':
                instanceUuid,
            'readCommunity':
                readCommunity,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_e3d7ad943d3a50fb8c3be7327669e557_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/global-credential/snmpv2-read-'
                 + 'community')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload,
                                          headers=_headers)
        else:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload)

        return self._object_factory('bpm_e3d7ad943d3a50fb8c3be7327669e557_v2_3_7_6', json_data)

    def create_snmp_read_community(self,
                                   headers=None,
                                   payload=None,
                                   active_validation=True,
                                   **request_parameters):
        """Adds global SNMP read community .

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
            self._request_validator('jsd_d16471a58805b4aa2c757209d188aed_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/global-credential/snmpv2-read-'
                 + 'community')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_d16471a58805b4aa2c757209d188aed_v2_3_7_6', json_data)

    def create_snmp_write_community(self,
                                    headers=None,
                                    payload=None,
                                    active_validation=True,
                                    **request_parameters):
        """Adds global SNMP write community .

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
            self._request_validator('jsd_a3a1bf404bf5772828f66f1e10f074d_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/global-credential/snmpv2-write-'
                 + 'community')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_a3a1bf404bf5772828f66f1e10f074d_v2_3_7_6', json_data)

    def update_snmp_write_community(self,
                                    comments=None,
                                    credentialType=None,
                                    description=None,
                                    instanceUuid=None,
                                    writeCommunity=None,
                                    headers=None,
                                    payload=None,
                                    active_validation=True,
                                    **request_parameters):
        """Updates global SNMP write community .

        Args:
            comments(string): Discovery's Comments to identify the credential .
            credentialType(string): Discovery's Credential type to identify the application that uses the credential
                . Available values are 'GLOBAL' and 'APP'.
            description(string): Discovery's Name/Description of the credential .
            instanceUuid(string): Discovery's Credential UUID .
            writeCommunity(string): Discovery's SNMP write community. NO!$DATA!$ for no value change .
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
            'comments':
                comments,
            'credentialType':
                credentialType,
            'description':
                description,
            'instanceUuid':
                instanceUuid,
            'writeCommunity':
                writeCommunity,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_c9ea5c02b2b7368cac785f30_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/global-credential/snmpv2-write-'
                 + 'community')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload,
                                          headers=_headers)
        else:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload)

        return self._object_factory('bpm_c9ea5c02b2b7368cac785f30_v2_3_7_6', json_data)

    def update_snmpv3_credentials(self,
                                  authPassword=None,
                                  authType=None,
                                  comments=None,
                                  credentialType=None,
                                  description=None,
                                  id=None,
                                  instanceTenantId=None,
                                  instanceUuid=None,
                                  privacyPassword=None,
                                  privacyType=None,
                                  snmpMode=None,
                                  username=None,
                                  headers=None,
                                  payload=None,
                                  active_validation=True,
                                  **request_parameters):
        """Updates global SNMPv3 credential .

        Args:
            authPassword(string): Discovery's Auth Password for SNMP .
            authType(string): Discovery's SNMP auth protocol. 'SHA' or 'MD5' . Available values are 'SHA' and 'MD5'.
            comments(string): Discovery's Comments to identify the SNMPv3 credential .
            credentialType(string): Discovery's Credential type to identify the application that uses the SNMPv3
                credential . Available values are 'GLOBAL' and 'APP'.
            description(string): Discovery's Description for Snmp V3 Credential .
            id(string): Discovery's Id of the SNMP V3 Credential in UUID format .
            instanceTenantId(string): Discovery's Deprecated .
            instanceUuid(string): Discovery's Deprecated .
            privacyPassword(string): Discovery's Privacy Password for SNMP privacy .
            privacyType(string): Discovery's SNMP privacy protocol . Available values are 'AES128'.
            snmpMode(string): Discovery's Mode of SNMP. 'AUTHPRIV' or 'AUTHNOPRIV' or 'NOAUTHNOPRIV' . Available
                values are 'AUTHPRIV', 'AUTHNOPRIV' and 'NOAUTHNOPRIV'.
            username(string): Discovery's SNMP V3 Username .
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
        _payload = {
            'authPassword':
                authPassword,
            'authType':
                authType,
            'comments':
                comments,
            'credentialType':
                credentialType,
            'description':
                description,
            'id':
                id,
            'instanceTenantId':
                instanceTenantId,
            'instanceUuid':
                instanceUuid,
            'privacyPassword':
                privacyPassword,
            'privacyType':
                privacyType,
            'snmpMode':
                snmpMode,
            'username':
                username,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_bdc981805b5fad0a038966d52558_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/global-credential/snmpv3')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload,
                                          headers=_headers)
        else:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload)

        return self._object_factory('bpm_bdc981805b5fad0a038966d52558_v2_3_7_6', json_data)

    def create_snmpv3_credentials(self,
                                  headers=None,
                                  payload=None,
                                  active_validation=True,
                                  **request_parameters):
        """Adds global SNMPv3 credentials .

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
            self._request_validator('jsd_ecdb2d14c29b5bf3ad79ed2e3cc70715_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/global-credential/snmpv3')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_ecdb2d14c29b5bf3ad79ed2e3cc70715_v2_3_7_6', json_data)

    def delete_global_credentials_by_id(self,
                                        global_credential_id,
                                        headers=None,
                                        **request_parameters):
        """Deletes global credential for the given ID .

        Args:
            global_credential_id(str): globalCredentialId path parameter. ID of global-credential .
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
        check_type(global_credential_id, str,
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
            'globalCredentialId': global_credential_id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/global-'
                 + 'credential/{globalCredentialId}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(endpoint_full_url, params=_params,
                                             headers=_headers)
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_a82cc61ddeae50969464f7b5d7d6bbf1_v2_3_7_6', json_data)

    def update_global_credentials(self,
                                  global_credential_id,
                                  siteUuids=None,
                                  headers=None,
                                  payload=None,
                                  active_validation=True,
                                  **request_parameters):
        """Update global credential for network devices in site(s) .

        Args:
            siteUuids(list): Discovery's List of siteUuids where credential is to be updated  (list of strings).
            global_credential_id(str): globalCredentialId path parameter. Global credential Uuid .
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
        check_type(global_credential_id, str,
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
            'globalCredentialId': global_credential_id,
        }
        _payload = {
            'siteUuids':
                siteUuids,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_f5d13316c8f53a0b78d881c738a15c6_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/global-'
                 + 'credential/{globalCredentialId}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload,
                                          headers=_headers)
        else:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload)

        return self._object_factory('bpm_f5d13316c8f53a0b78d881c738a15c6_v2_3_7_6', json_data)

    def get_credential_sub_type_by_credential_id(self,
                                                 id,
                                                 headers=None,
                                                 **request_parameters):
        """Returns the credential sub type for the given Id .

        Args:
            id(str): id path parameter. Global Credential ID .
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
        check_type(id, str,
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
            'id': id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/global-credential/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_a37de9e4e5fab8c65b0701b074fd2_v2_3_7_6', json_data)

    def get_snmp_properties(self,
                            headers=None,
                            **request_parameters):
        """Returns SNMP properties .

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

        e_url = ('/dna/intent/api/v1/snmp-property')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_dfb02d27503fab05602db7311e90_v2_3_7_6', json_data)

    def create_update_snmp_properties(self,
                                      headers=None,
                                      payload=None,
                                      active_validation=True,
                                      **request_parameters):
        """Adds SNMP properties .

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
            self._request_validator('jsd_da593242978c5047bb6b62b7f9475326_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v1/snmp-property')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_da593242978c5047bb6b62b7f9475326_v2_3_7_6', json_data)

    def update_global_credentials_v2(self,
                                     cliCredential=None,
                                     httpsRead=None,
                                     httpsWrite=None,
                                     snmpV2cRead=None,
                                     snmpV2cWrite=None,
                                     snmpV3=None,
                                     headers=None,
                                     payload=None,
                                     active_validation=True,
                                     **request_parameters):
        """API to update device credentials. Multiple credentials can be passed at once, but only a single credential of a
        given type can be passed at once. Please refer sample Request Body for more information. .

        Args:
            cliCredential(object): Discovery's cliCredential.
            httpsRead(object): Discovery's httpsRead.
            httpsWrite(object): Discovery's httpsWrite.
            snmpV2cRead(object): Discovery's snmpV2cRead.
            snmpV2cWrite(object): Discovery's snmpV2cWrite.
            snmpV3(object): Discovery's snmpV3.
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
            'cliCredential':
                cliCredential,
            'snmpV2cRead':
                snmpV2cRead,
            'snmpV2cWrite':
                snmpV2cWrite,
            'snmpV3':
                snmpV3,
            'httpsRead':
                httpsRead,
            'httpsWrite':
                httpsWrite,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_b3323a24b275402b97c7e9ccfd78c91_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v2/global-credential')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload,
                                          headers=_headers)
        else:
            json_data = self._session.put(endpoint_full_url, params=_params,
                                          json=_payload)

        return self._object_factory('bpm_b3323a24b275402b97c7e9ccfd78c91_v2_3_7_6', json_data)

    def create_global_credentials_v2(self,
                                     cliCredential=None,
                                     httpsRead=None,
                                     httpsWrite=None,
                                     snmpV2cRead=None,
                                     snmpV2cWrite=None,
                                     snmpV3=None,
                                     headers=None,
                                     payload=None,
                                     active_validation=True,
                                     **request_parameters):
        """API to create new global credentials. Multiple credentials of various types can be passed at once. Please refer
        sample Request Body for more information. .

        Args:
            cliCredential(list): Discovery's cliCredential (list of objects).
            httpsRead(list): Discovery's httpsRead (list of objects).
            httpsWrite(list): Discovery's httpsWrite (list of objects).
            snmpV2cRead(list): Discovery's snmpV2cRead (list of objects).
            snmpV2cWrite(list): Discovery's snmpV2cWrite (list of objects).
            snmpV3(list): Discovery's snmpV3 (list of objects).
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
            'cliCredential':
                cliCredential,
            'snmpV2cRead':
                snmpV2cRead,
            'snmpV2cWrite':
                snmpV2cWrite,
            'snmpV3':
                snmpV3,
            'httpsRead':
                httpsRead,
            'httpsWrite':
                httpsWrite,
        }
        _payload.update(payload or {})
        _payload = dict_from_items_with_values(_payload)
        if active_validation:
            self._request_validator('jsd_d2ece28b509b8ef80b2b8c5c5f36_v2_3_7_6')\
                .validate(_payload)

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v2/global-credential')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload,
                                           headers=_headers)
        else:
            json_data = self._session.post(endpoint_full_url, params=_params,
                                           json=_payload)

        return self._object_factory('bpm_d2ece28b509b8ef80b2b8c5c5f36_v2_3_7_6', json_data)

    def get_all_global_credentials_v2(self,
                                      headers=None,
                                      **request_parameters):
        """API to get device credentials' details. It fetches all global credentials of all types at once, without the need
        to pass any input parameters. .

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

        e_url = ('/dna/intent/api/v2/global-credential')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.get(endpoint_full_url, params=_params,
                                          headers=_headers)
        else:
            json_data = self._session.get(endpoint_full_url, params=_params)

        return self._object_factory('bpm_a473a278a325c67abd310df49bae1bb_v2_3_7_6', json_data)

    def delete_global_credential_v2(self,
                                    id,
                                    headers=None,
                                    **request_parameters):
        """Delete a global credential. Only 'id' of the credential has to be passed. .

        Args:
            id(str): id path parameter. Global Credential id   .
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
        check_type(id, str,
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
            'id': id,
        }

        with_custom_headers = False
        _headers = self._session.headers or {}
        if headers:
            _headers.update(dict_of_str(headers))
            with_custom_headers = True

        e_url = ('/dna/intent/api/v2/global-credential/{id}')
        endpoint_full_url = apply_path_params(e_url, path_params)
        if with_custom_headers:
            json_data = self._session.delete(endpoint_full_url, params=_params,
                                             headers=_headers)
        else:
            json_data = self._session.delete(endpoint_full_url, params=_params)

        return self._object_factory('bpm_caa7cd8d7a3550cfb102cd3498494d04_v2_3_7_6', json_data)

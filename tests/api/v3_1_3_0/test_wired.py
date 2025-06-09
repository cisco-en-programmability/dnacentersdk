# -*- coding: utf-8 -*-
"""CatalystCenterAPI wired API fixtures and tests.

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
import pytest
from fastjsonschema.exceptions import JsonSchemaException
from dnacentersdk.exceptions import MalformedRequest
from tests.environment import DNA_CENTER_VERSION

pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '3.1.3.0', reason='version does not match')


def is_valid_get_configurations_for_intended_layer2_features_on_a_wired_device(json_schema_validate, obj):
    json_schema_validate('jsd_d96b49e8c1a0594cb4e1946731f06411_v3_1_3_0').validate(obj)
    return True


def get_configurations_for_intended_layer2_features_on_a_wired_device(api):
    endpoint_result = api.wired.get_configurations_for_intended_layer2_features_on_a_wired_device(
        feature='string',
        id='string'
    )
    return endpoint_result


@pytest.mark.wired
def test_get_configurations_for_intended_layer2_features_on_a_wired_device(api, validator):
    try:
        assert is_valid_get_configurations_for_intended_layer2_features_on_a_wired_device(
            validator,
            get_configurations_for_intended_layer2_features_on_a_wired_device(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_configurations_for_intended_layer2_features_on_a_wired_device_default_val(api):
    endpoint_result = api.wired.get_configurations_for_intended_layer2_features_on_a_wired_device(
        feature=None,
        id='string'
    )
    return endpoint_result


@pytest.mark.wired
def test_get_configurations_for_intended_layer2_features_on_a_wired_device_default_val(api, validator):
    try:
        assert is_valid_get_configurations_for_intended_layer2_features_on_a_wired_device(
            validator,
            get_configurations_for_intended_layer2_features_on_a_wired_device_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_deploy_the_configuration_model_on_the_network_device(json_schema_validate, obj):
    json_schema_validate('jsd_b6139c3f3ef15bcf9a42f5283a6aea64_v3_1_3_0').validate(obj)
    return True


def deploy_the_configuration_model_on_the_network_device(api):
    endpoint_result = api.wired.deploy_the_configuration_model_on_the_network_device(
        active_validation=True,
        network_device_id='string',
        payload=None,
        preview_activity_id='string'
    )
    return endpoint_result


@pytest.mark.wired
def test_deploy_the_configuration_model_on_the_network_device(api, validator):
    try:
        assert is_valid_deploy_the_configuration_model_on_the_network_device(
            validator,
            deploy_the_configuration_model_on_the_network_device(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def deploy_the_configuration_model_on_the_network_device_default_val(api):
    endpoint_result = api.wired.deploy_the_configuration_model_on_the_network_device(
        active_validation=True,
        network_device_id='string',
        payload=None,
        preview_activity_id='string'
    )
    return endpoint_result


@pytest.mark.wired
def test_deploy_the_configuration_model_on_the_network_device_default_val(api, validator):
    try:
        assert is_valid_deploy_the_configuration_model_on_the_network_device(
            validator,
            deploy_the_configuration_model_on_the_network_device_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_configurations_for_a_deployed_layer2_feature_on_a_wired_device(json_schema_validate, obj):
    json_schema_validate('jsd_8747fcf9673050079b4abedf3ffc9777_v3_1_3_0').validate(obj)
    return True


def get_configurations_for_a_deployed_layer2_feature_on_a_wired_device(api):
    endpoint_result = api.wired.get_configurations_for_a_deployed_layer2_feature_on_a_wired_device(
        feature='string',
        id='string'
    )
    return endpoint_result


@pytest.mark.wired
def test_get_configurations_for_a_deployed_layer2_feature_on_a_wired_device(api, validator):
    try:
        assert is_valid_get_configurations_for_a_deployed_layer2_feature_on_a_wired_device(
            validator,
            get_configurations_for_a_deployed_layer2_feature_on_a_wired_device(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_configurations_for_a_deployed_layer2_feature_on_a_wired_device_default_val(api):
    endpoint_result = api.wired.get_configurations_for_a_deployed_layer2_feature_on_a_wired_device(
        feature='string',
        id='string'
    )
    return endpoint_result


@pytest.mark.wired
def test_get_configurations_for_a_deployed_layer2_feature_on_a_wired_device_default_val(api, validator):
    try:
        assert is_valid_get_configurations_for_a_deployed_layer2_feature_on_a_wired_device(
            validator,
            get_configurations_for_a_deployed_layer2_feature_on_a_wired_device_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_number_of_configurations_for_a_deployed_layer2_feature_on_a_wired_device(json_schema_validate, obj):
    json_schema_validate('jsd_e495979e25a6559394fbad6fcd4c495a_v3_1_3_0').validate(obj)
    return True


def get_number_of_configurations_for_a_deployed_layer2_feature_on_a_wired_device(api):
    endpoint_result = api.wired.get_number_of_configurations_for_a_deployed_layer2_feature_on_a_wired_device(
        feature='string',
        id='string'
    )
    return endpoint_result


@pytest.mark.wired
def test_get_number_of_configurations_for_a_deployed_layer2_feature_on_a_wired_device(api, validator):
    try:
        assert is_valid_get_number_of_configurations_for_a_deployed_layer2_feature_on_a_wired_device(
            validator,
            get_number_of_configurations_for_a_deployed_layer2_feature_on_a_wired_device(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_number_of_configurations_for_a_deployed_layer2_feature_on_a_wired_device_default_val(api):
    endpoint_result = api.wired.get_number_of_configurations_for_a_deployed_layer2_feature_on_a_wired_device(
        feature='string',
        id='string'
    )
    return endpoint_result


@pytest.mark.wired
def test_get_number_of_configurations_for_a_deployed_layer2_feature_on_a_wired_device_default_val(api, validator):
    try:
        assert is_valid_get_number_of_configurations_for_a_deployed_layer2_feature_on_a_wired_device(
            validator,
            get_number_of_configurations_for_a_deployed_layer2_feature_on_a_wired_device_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_configurations_for_intended_layer2_features_on_a_wired_device(json_schema_validate, obj):
    json_schema_validate('jsd_0a862379cc525a79a01fc845fdda7d68_v3_1_3_0').validate(obj)
    return True


def create_configurations_for_intended_layer2_features_on_a_wired_device(api):
    endpoint_result = api.wired.create_configurations_for_intended_layer2_features_on_a_wired_device(
        active_validation=True,
        id='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.wired
def test_create_configurations_for_intended_layer2_features_on_a_wired_device(api, validator):
    try:
        assert is_valid_create_configurations_for_intended_layer2_features_on_a_wired_device(
            validator,
            create_configurations_for_intended_layer2_features_on_a_wired_device(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_configurations_for_intended_layer2_features_on_a_wired_device_default_val(api):
    endpoint_result = api.wired.create_configurations_for_intended_layer2_features_on_a_wired_device(
        active_validation=True,
        id='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.wired
def test_create_configurations_for_intended_layer2_features_on_a_wired_device_default_val(api, validator):
    try:
        assert is_valid_create_configurations_for_intended_layer2_features_on_a_wired_device(
            validator,
            create_configurations_for_intended_layer2_features_on_a_wired_device_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_configurations_for_intended_layer2_features_on_a_wired_device(json_schema_validate, obj):
    json_schema_validate('jsd_350ecf0984975fb7af51796da58aca21_v3_1_3_0').validate(obj)
    return True


def update_configurations_for_intended_layer2_features_on_a_wired_device(api):
    endpoint_result = api.wired.update_configurations_for_intended_layer2_features_on_a_wired_device(
        active_validation=True,
        id='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.wired
def test_update_configurations_for_intended_layer2_features_on_a_wired_device(api, validator):
    try:
        assert is_valid_update_configurations_for_intended_layer2_features_on_a_wired_device(
            validator,
            update_configurations_for_intended_layer2_features_on_a_wired_device(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_configurations_for_intended_layer2_features_on_a_wired_device_default_val(api):
    endpoint_result = api.wired.update_configurations_for_intended_layer2_features_on_a_wired_device(
        active_validation=True,
        id='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.wired
def test_update_configurations_for_intended_layer2_features_on_a_wired_device_default_val(api, validator):
    try:
        assert is_valid_update_configurations_for_intended_layer2_features_on_a_wired_device(
            validator,
            update_configurations_for_intended_layer2_features_on_a_wired_device_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_configurations_for_an_intended_layer2_feature_on_a_wired_device(json_schema_validate, obj):
    json_schema_validate('jsd_d1b2d399192a5da39b4ae3fe0f5288d4_v3_1_3_0').validate(obj)
    return True


def get_configurations_for_an_intended_layer2_feature_on_a_wired_device(api):
    endpoint_result = api.wired.get_configurations_for_an_intended_layer2_feature_on_a_wired_device(
        feature='string',
        id='string'
    )
    return endpoint_result


@pytest.mark.wired
def test_get_configurations_for_an_intended_layer2_feature_on_a_wired_device(api, validator):
    try:
        assert is_valid_get_configurations_for_an_intended_layer2_feature_on_a_wired_device(
            validator,
            get_configurations_for_an_intended_layer2_feature_on_a_wired_device(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_configurations_for_an_intended_layer2_feature_on_a_wired_device_default_val(api):
    endpoint_result = api.wired.get_configurations_for_an_intended_layer2_feature_on_a_wired_device(
        feature='string',
        id='string'
    )
    return endpoint_result


@pytest.mark.wired
def test_get_configurations_for_an_intended_layer2_feature_on_a_wired_device_default_val(api, validator):
    try:
        assert is_valid_get_configurations_for_an_intended_layer2_feature_on_a_wired_device(
            validator,
            get_configurations_for_an_intended_layer2_feature_on_a_wired_device_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_configurations_for_an_intended_layer2_feature_on_a_wired_device(json_schema_validate, obj):
    json_schema_validate('jsd_50d4649fef20535193fd86c95925bcf8_v3_1_3_0').validate(obj)
    return True


def delete_configurations_for_an_intended_layer2_feature_on_a_wired_device(api):
    endpoint_result = api.wired.delete_configurations_for_an_intended_layer2_feature_on_a_wired_device(
        feature='string',
        id='string'
    )
    return endpoint_result


@pytest.mark.wired
def test_delete_configurations_for_an_intended_layer2_feature_on_a_wired_device(api, validator):
    try:
        assert is_valid_delete_configurations_for_an_intended_layer2_feature_on_a_wired_device(
            validator,
            delete_configurations_for_an_intended_layer2_feature_on_a_wired_device(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_configurations_for_an_intended_layer2_feature_on_a_wired_device_default_val(api):
    endpoint_result = api.wired.delete_configurations_for_an_intended_layer2_feature_on_a_wired_device(
        feature='string',
        id='string'
    )
    return endpoint_result


@pytest.mark.wired
def test_delete_configurations_for_an_intended_layer2_feature_on_a_wired_device_default_val(api, validator):
    try:
        assert is_valid_delete_configurations_for_an_intended_layer2_feature_on_a_wired_device(
            validator,
            delete_configurations_for_an_intended_layer2_feature_on_a_wired_device_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_update_configurations_for_an_intended_layer2_feature_on_a_wired_device(json_schema_validate, obj):
    json_schema_validate('jsd_12ee7664344f50cb8f2c94beaa01629d_v3_1_3_0').validate(obj)
    return True


def update_configurations_for_an_intended_layer2_feature_on_a_wired_device(api):
    endpoint_result = api.wired.update_configurations_for_an_intended_layer2_feature_on_a_wired_device(
        active_validation=True,
        cdpGlobalConfig={'items': [[{'configType': 'string', 'timer': 0, 'isCdpEnabled': True, 'isLogDuplexMismatchEnabled': True, 'isAdvertiseV2Enabled': True, 'holdTime': 0}]]},
        cdpInterfaceConfig={'items': [[{'configType': 'string', 'interfaceName': 'string', 'isCdpEnabled': True, 'isLogDuplexMismatchEnabled': True}]]},
        dhcpSnoopingGlobalConfig={'items': [[{'configType': 'string', 'isDhcpSnoopingEnabled': True, 'databaseAgent': {'configType': 'string', 'agentUrl': 'string', 'timeout': 0, 'writeDelay': 0}, 'isGleaningEnabled': True, 'proxyBridgeVlans': 'string', 'dhcpSnoopingVlans': 'string'}]]},
        dhcpSnoopingInterfaceConfig={'items': [[{'configType': 'string', 'interfaceName': 'string', 'isTrustedInterface': True, 'messageRateLimit': 0}]]},
        dot1xGlobalConfig={'items': [[{'configType': 'string', 'authenticationConfigMode': 'string', 'isDot1xEnabled': True}]]},
        dot1xInterfaceConfig={'items': [[{'configType': 'string', 'interfaceName': 'string', 'authenticationOrder': {'configType': 'string', 'items': ['string']}}]]},
        feature='string',
        id='string',
        igmpSnoopingGlobalConfig={'items': [[{'configType': 'string', 'isIgmpSnoopingEnabled': True, 'isQuerierEnabled': True, 'querierAddress': 'string', 'querierQueryInterval': 0, 'querierVersion': 'string', 'igmpSnoopingVlanSettings': {'configType': 'string', 'items': [{'configType': 'string', 'vlanId': 0, 'isIgmpSnoopingEnabled': True, 'isImmediateLeaveEnabled': True, 'isQuerierEnabled': True, 'querierAddress': 'string', 'querierQueryInterval': 0, 'querierVersion': 'string', 'igmpSnoopingVlanMrouters': {'configType': 'string', 'items': [{'configType': 'string', 'interfaceName': 'string'}]}}]}}]]},
        lldpGlobalConfig={'items': [[{'configType': 'string', 'timer': 0, 'isLldpEnabled': True, 'reinitializationDelay': 0, 'holdTime': 0}]]},
        lldpInterfaceConfig={'items': [[{'configType': 'string', 'interfaceName': 'string', 'adminStatus': 'string'}]]},
        mabInterfaceConfig={'items': [[{'configType': 'string', 'interfaceName': 'string', 'isMabEnabled': True}]]},
        mldSnoopingGlobalConfig={'items': [[{'configType': 'string', 'isMldSnoopingEnabled': True, 'isSuppressListenerMessagesEnabled': True, 'isQuerierEnabled': True, 'querierAddress': 'string', 'querierQueryInterval': 0, 'querierVersion': 'string', 'mldSnoopingVlanSettings': {'configType': 'string', 'items': [{'configType': 'string', 'vlanId': 0, 'isMldSnoopingEnabled': True, 'isImmediateLeaveEnabled': True, 'isQuerierEnabled': True, 'querierAddress': 'string', 'querierQueryInterval': 0, 'querierVersion': 'string', 'mldSnoopingVlanMrouters': {'configType': 'string', 'items': [{'configType': 'string', 'interfaceName': 'string'}]}}]}}]]},
        payload=None,
        portChannelConfig={'items': [[{'configType': 'string', 'isAutoEnabled': True, 'loadBalancingMethod': 'string', 'lacpSystemPriority': 0, 'portchannels': {'configType': 'string', 'items': [{'AnyOf': {'EtherchannelConfig': {'configType': 'string', 'name': 'string', 'minLinks': 0, 'memberPorts': {'configType': 'string', 'items': [{'configType': 'string', 'interfaceName': 'string', 'mode': 'string'}]}}, 'LacpPortchannelConfig': {'configType': 'string', 'name': 'string', 'minLinks': 0, 'memberPorts': {'configType': 'string', 'items': [{'configType': 'string', 'interfaceName': 'string', 'mode': 'string', 'portPriority': 0, 'rate': 0}]}}, 'PagpPortchannelConfig': {'configType': 'string', 'name': 'string', 'minLinks': 0, 'memberPorts': {'configType': 'string', 'items': [{'configType': 'string', 'interfaceName': 'string', 'mode': 'string', 'portPriority': 0, 'learnMethod': 'string'}]}}}}]}}]]},
        stpGlobalConfig={'items': [[{'configType': 'string', 'stpMode': 'string', 'isBackboneFastEnabled': True, 'isEtherChannelGuardEnabled': True, 'isExtendedSystemIdEnabled': True, 'isLoggingEnabled': True, 'isLoopGuardEnabled': True, 'portFastMode': 'string', 'isBpduFilterEnabled': True, 'isBpduGuardEnabled': True, 'isUplinkFastEnabled': True, 'transmitHoldCount': 0, 'uplinkFastMaxUpdateRate': 0, 'stpInstances': {'configType': 'string', 'items': [{'configType': 'string', 'vlanId': 0, 'priority': 0, 'timers': {'configType': 'string', 'forwardDelay': 0, 'helloInterval': 0, 'maxAge': 0, 'isStpEnabled': True}}]}}]]},
        stpInterfaceConfig={'items': [{'configType': 'string', 'interfaceName': 'string', 'guardMode': 'string', 'bpduFilter': 'string', 'bpduGuard': 'string', 'pathCost': 0, 'portFastMode': 'string', 'priority': 0, 'portVlanCostSettings': {'configType': 'string', 'items': [{'configType': 'string', 'cost': 0, 'vlans': 'string'}]}, 'portVlanPrioritySettings': {'configType': 'string', 'items': [{'configType': 'string', 'priority': 0, 'vlans': 'string'}]}}]},
        switchportInterfaceConfig={'items': [[{'configType': 'string', 'interfaceName': 'string', 'description': 'string', 'mode': 'string', 'accessVlan': 0, 'voiceVlan': 0, 'adminStatus': 'string', 'trunkAllowedVlans': 'string', 'nativeVlan': 0}]]},
        trunkInterfaceConfig={'items': [[{'configType': 'string', 'interfaceName': 'string', 'isProtected': True, 'isDtpNegotiationEnabled': True, 'pruneEligibleVlans': 'string'}]]},
        vlanConfig={'items': [[{'configType': 'string', 'vlanId': 0, 'name': 'string', 'isVlanEnabled': True}]]},
        vtpGlobalConfig={'items': [[{'configType': 'string', 'mode': 'string', 'version': 'string', 'domainName': 'string', 'isPruningEnabled': True, 'configurationFileName': 'string', 'sourceInterface': 'string'}]]},
        vtpInterfaceConfig={'items': [[{'configType': 'string', 'interfaceName': 'string', 'isVtpEnabled': True}]]}
    )
    return endpoint_result


@pytest.mark.wired
def test_update_configurations_for_an_intended_layer2_feature_on_a_wired_device(api, validator):
    try:
        assert is_valid_update_configurations_for_an_intended_layer2_feature_on_a_wired_device(
            validator,
            update_configurations_for_an_intended_layer2_feature_on_a_wired_device(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def update_configurations_for_an_intended_layer2_feature_on_a_wired_device_default_val(api):
    endpoint_result = api.wired.update_configurations_for_an_intended_layer2_feature_on_a_wired_device(
        active_validation=True,
        cdpGlobalConfig=None,
        cdpInterfaceConfig=None,
        dhcpSnoopingGlobalConfig=None,
        dhcpSnoopingInterfaceConfig=None,
        dot1xGlobalConfig=None,
        dot1xInterfaceConfig=None,
        feature='string',
        id='string',
        igmpSnoopingGlobalConfig=None,
        lldpGlobalConfig=None,
        lldpInterfaceConfig=None,
        mabInterfaceConfig=None,
        mldSnoopingGlobalConfig=None,
        payload=None,
        portChannelConfig=None,
        stpGlobalConfig=None,
        stpInterfaceConfig=None,
        switchportInterfaceConfig=None,
        trunkInterfaceConfig=None,
        vlanConfig=None,
        vtpGlobalConfig=None,
        vtpInterfaceConfig=None
    )
    return endpoint_result


@pytest.mark.wired
def test_update_configurations_for_an_intended_layer2_feature_on_a_wired_device_default_val(api, validator):
    try:
        assert is_valid_update_configurations_for_an_intended_layer2_feature_on_a_wired_device(
            validator,
            update_configurations_for_an_intended_layer2_feature_on_a_wired_device_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_configurations_for_an_intended_layer2_feature_on_a_wired_device(json_schema_validate, obj):
    json_schema_validate('jsd_162286d7b57050bdb98e9340d0bc4dba_v3_1_3_0').validate(obj)
    return True


def create_configurations_for_an_intended_layer2_feature_on_a_wired_device(api):
    endpoint_result = api.wired.create_configurations_for_an_intended_layer2_feature_on_a_wired_device(
        active_validation=True,
        cdpGlobalConfig={'items': [[{'configType': 'string', 'timer': 0, 'isCdpEnabled': True, 'isLogDuplexMismatchEnabled': True, 'isAdvertiseV2Enabled': True, 'holdTime': 0}]]},
        cdpInterfaceConfig={'items': [[{'configType': 'string', 'interfaceName': 'string', 'isCdpEnabled': True, 'isLogDuplexMismatchEnabled': True}]]},
        dhcpSnoopingGlobalConfig={'items': [[{'configType': 'string', 'isDhcpSnoopingEnabled': True, 'databaseAgent': {'configType': 'string', 'agentUrl': 'string', 'timeout': 0, 'writeDelay': 0}, 'isGleaningEnabled': True, 'proxyBridgeVlans': 'string', 'dhcpSnoopingVlans': 'string'}]]},
        dhcpSnoopingInterfaceConfig={'items': [[{'configType': 'string', 'interfaceName': 'string', 'isTrustedInterface': True, 'messageRateLimit': 0}]]},
        dot1xGlobalConfig={'items': [[{'configType': 'string', 'authenticationConfigMode': 'string', 'isDot1xEnabled': True}]]},
        dot1xInterfaceConfig={'items': [[{'configType': 'string', 'interfaceName': 'string', 'authenticationOrder': {'configType': 'string', 'items': ['string']}}]]},
        feature='string',
        id='string',
        igmpSnoopingGlobalConfig={'items': [[{'configType': 'string', 'isIgmpSnoopingEnabled': True, 'isQuerierEnabled': True, 'querierAddress': 'string', 'querierQueryInterval': 0, 'querierVersion': 'string', 'igmpSnoopingVlanSettings': {'configType': 'string', 'items': [{'configType': 'string', 'vlanId': 0, 'isIgmpSnoopingEnabled': True, 'isImmediateLeaveEnabled': True, 'isQuerierEnabled': True, 'querierAddress': 'string', 'querierQueryInterval': 0, 'querierVersion': 'string', 'igmpSnoopingVlanMrouters': {'configType': 'string', 'items': [{'configType': 'string', 'interfaceName': 'string'}]}}]}}]]},
        lldpGlobalConfig={'items': [[{'configType': 'string', 'timer': 0, 'isLldpEnabled': True, 'reinitializationDelay': 0, 'holdTime': 0}]]},
        lldpInterfaceConfig={'items': [[{'configType': 'string', 'interfaceName': 'string', 'adminStatus': 'string'}]]},
        mabInterfaceConfig={'items': [[{'configType': 'string', 'interfaceName': 'string', 'isMabEnabled': True}]]},
        mldSnoopingGlobalConfig={'items': [[{'configType': 'string', 'isMldSnoopingEnabled': True, 'isSuppressListenerMessagesEnabled': True, 'isQuerierEnabled': True, 'querierAddress': 'string', 'querierQueryInterval': 0, 'querierVersion': 'string', 'mldSnoopingVlanSettings': {'configType': 'string', 'items': [{'configType': 'string', 'vlanId': 0, 'isMldSnoopingEnabled': True, 'isImmediateLeaveEnabled': True, 'isQuerierEnabled': True, 'querierAddress': 'string', 'querierQueryInterval': 0, 'querierVersion': 'string', 'mldSnoopingVlanMrouters': {'configType': 'string', 'items': [{'configType': 'string', 'interfaceName': 'string'}]}}]}}]]},
        payload=None,
        portChannelConfig={'items': [[{'configType': 'string', 'isAutoEnabled': True, 'loadBalancingMethod': 'string', 'lacpSystemPriority': 0, 'portchannels': {'configType': 'string', 'items': [{'AnyOf': {'EtherchannelConfig': {'configType': 'string', 'name': 'string', 'minLinks': 0, 'memberPorts': {'configType': 'string', 'items': [{'configType': 'string', 'interfaceName': 'string', 'mode': 'string'}]}}, 'LacpPortchannelConfig': {'configType': 'string', 'name': 'string', 'minLinks': 0, 'memberPorts': {'configType': 'string', 'items': [{'configType': 'string', 'interfaceName': 'string', 'mode': 'string', 'portPriority': 0, 'rate': 0}]}}, 'PagpPortchannelConfig': {'configType': 'string', 'name': 'string', 'minLinks': 0, 'memberPorts': {'configType': 'string', 'items': [{'configType': 'string', 'interfaceName': 'string', 'mode': 'string', 'portPriority': 0, 'learnMethod': 'string'}]}}}}]}}]]},
        stpGlobalConfig={'items': [[{'configType': 'string', 'stpMode': 'string', 'isBackboneFastEnabled': True, 'isEtherChannelGuardEnabled': True, 'isExtendedSystemIdEnabled': True, 'isLoggingEnabled': True, 'isLoopGuardEnabled': True, 'portFastMode': 'string', 'isBpduFilterEnabled': True, 'isBpduGuardEnabled': True, 'isUplinkFastEnabled': True, 'transmitHoldCount': 0, 'uplinkFastMaxUpdateRate': 0, 'stpInstances': {'configType': 'string', 'items': [{'configType': 'string', 'vlanId': 0, 'priority': 0, 'timers': {'configType': 'string', 'forwardDelay': 0, 'helloInterval': 0, 'maxAge': 0, 'isStpEnabled': True}}]}}]]},
        stpInterfaceConfig={'items': [{'configType': 'string', 'interfaceName': 'string', 'guardMode': 'string', 'bpduFilter': 'string', 'bpduGuard': 'string', 'pathCost': 0, 'portFastMode': 'string', 'priority': 0, 'portVlanCostSettings': {'configType': 'string', 'items': [{'configType': 'string', 'cost': 0, 'vlans': 'string'}]}, 'portVlanPrioritySettings': {'configType': 'string', 'items': [{'configType': 'string', 'priority': 0, 'vlans': 'string'}]}}]},
        switchportInterfaceConfig={'items': [[{'configType': 'string', 'interfaceName': 'string', 'description': 'string', 'mode': 'string', 'accessVlan': 0, 'voiceVlan': 0, 'adminStatus': 'string', 'trunkAllowedVlans': 'string', 'nativeVlan': 0}]]},
        trunkInterfaceConfig={'items': [[{'configType': 'string', 'interfaceName': 'string', 'isProtected': True, 'isDtpNegotiationEnabled': True, 'pruneEligibleVlans': 'string'}]]},
        vlanConfig={'items': [[{'configType': 'string', 'vlanId': 0, 'name': 'string', 'isVlanEnabled': True}]]},
        vtpGlobalConfig={'items': [[{'configType': 'string', 'mode': 'string', 'version': 'string', 'domainName': 'string', 'isPruningEnabled': True, 'configurationFileName': 'string', 'sourceInterface': 'string'}]]},
        vtpInterfaceConfig={'items': [[{'configType': 'string', 'interfaceName': 'string', 'isVtpEnabled': True}]]}
    )
    return endpoint_result


@pytest.mark.wired
def test_create_configurations_for_an_intended_layer2_feature_on_a_wired_device(api, validator):
    try:
        assert is_valid_create_configurations_for_an_intended_layer2_feature_on_a_wired_device(
            validator,
            create_configurations_for_an_intended_layer2_feature_on_a_wired_device(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_configurations_for_an_intended_layer2_feature_on_a_wired_device_default_val(api):
    endpoint_result = api.wired.create_configurations_for_an_intended_layer2_feature_on_a_wired_device(
        active_validation=True,
        cdpGlobalConfig=None,
        cdpInterfaceConfig=None,
        dhcpSnoopingGlobalConfig=None,
        dhcpSnoopingInterfaceConfig=None,
        dot1xGlobalConfig=None,
        dot1xInterfaceConfig=None,
        feature='string',
        id='string',
        igmpSnoopingGlobalConfig=None,
        lldpGlobalConfig=None,
        lldpInterfaceConfig=None,
        mabInterfaceConfig=None,
        mldSnoopingGlobalConfig=None,
        payload=None,
        portChannelConfig=None,
        stpGlobalConfig=None,
        stpInterfaceConfig=None,
        switchportInterfaceConfig=None,
        trunkInterfaceConfig=None,
        vlanConfig=None,
        vtpGlobalConfig=None,
        vtpInterfaceConfig=None
    )
    return endpoint_result


@pytest.mark.wired
def test_create_configurations_for_an_intended_layer2_feature_on_a_wired_device_default_val(api, validator):
    try:
        assert is_valid_create_configurations_for_an_intended_layer2_feature_on_a_wired_device(
            validator,
            create_configurations_for_an_intended_layer2_feature_on_a_wired_device_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_number_of_configurations_for_an_intended_layer2_feature_on_a_wired_device(json_schema_validate, obj):
    json_schema_validate('jsd_1614364d2cca58398312cb0129d39d8c_v3_1_3_0').validate(obj)
    return True


def get_number_of_configurations_for_an_intended_layer2_feature_on_a_wired_device(api):
    endpoint_result = api.wired.get_number_of_configurations_for_an_intended_layer2_feature_on_a_wired_device(
        feature='string',
        id='string'
    )
    return endpoint_result


@pytest.mark.wired
def test_get_number_of_configurations_for_an_intended_layer2_feature_on_a_wired_device(api, validator):
    try:
        assert is_valid_get_number_of_configurations_for_an_intended_layer2_feature_on_a_wired_device(
            validator,
            get_number_of_configurations_for_an_intended_layer2_feature_on_a_wired_device(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_number_of_configurations_for_an_intended_layer2_feature_on_a_wired_device_default_val(api):
    endpoint_result = api.wired.get_number_of_configurations_for_an_intended_layer2_feature_on_a_wired_device(
        feature='string',
        id='string'
    )
    return endpoint_result


@pytest.mark.wired
def test_get_number_of_configurations_for_an_intended_layer2_feature_on_a_wired_device_default_val(api, validator):
    try:
        assert is_valid_get_number_of_configurations_for_an_intended_layer2_feature_on_a_wired_device(
            validator,
            get_number_of_configurations_for_an_intended_layer2_feature_on_a_wired_device_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_the_supported_layer2_features_on_a_wired_device(json_schema_validate, obj):
    json_schema_validate('jsd_3c4684074beb50b1ae5e77141244ebbd_v3_1_3_0').validate(obj)
    return True


def get_the_supported_layer2_features_on_a_wired_device(api):
    endpoint_result = api.wired.get_the_supported_layer2_features_on_a_wired_device(
        id='string'
    )
    return endpoint_result


@pytest.mark.wired
def test_get_the_supported_layer2_features_on_a_wired_device(api, validator):
    try:
        assert is_valid_get_the_supported_layer2_features_on_a_wired_device(
            validator,
            get_the_supported_layer2_features_on_a_wired_device(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_the_supported_layer2_features_on_a_wired_device_default_val(api):
    endpoint_result = api.wired.get_the_supported_layer2_features_on_a_wired_device(
        id='string'
    )
    return endpoint_result


@pytest.mark.wired
def test_get_the_supported_layer2_features_on_a_wired_device_default_val(api, validator):
    try:
        assert is_valid_get_the_supported_layer2_features_on_a_wired_device(
            validator,
            get_the_supported_layer2_features_on_a_wired_device_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_create_a_configuration_model_for_the_intended_configs_for_a_wired_device(json_schema_validate, obj):
    json_schema_validate('jsd_594c74d2bae55f85924002ddb92fe064_v3_1_3_0').validate(obj)
    return True


def create_a_configuration_model_for_the_intended_configs_for_a_wired_device(api):
    endpoint_result = api.wired.create_a_configuration_model_for_the_intended_configs_for_a_wired_device(
        active_validation=True,
        network_device_id='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.wired
def test_create_a_configuration_model_for_the_intended_configs_for_a_wired_device(api, validator):
    try:
        assert is_valid_create_a_configuration_model_for_the_intended_configs_for_a_wired_device(
            validator,
            create_a_configuration_model_for_the_intended_configs_for_a_wired_device(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def create_a_configuration_model_for_the_intended_configs_for_a_wired_device_default_val(api):
    endpoint_result = api.wired.create_a_configuration_model_for_the_intended_configs_for_a_wired_device(
        active_validation=True,
        network_device_id='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.wired
def test_create_a_configuration_model_for_the_intended_configs_for_a_wired_device_default_val(api, validator):
    try:
        assert is_valid_create_a_configuration_model_for_the_intended_configs_for_a_wired_device(
            validator,
            create_a_configuration_model_for_the_intended_configs_for_a_wired_device_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_delete_the_configuration_model(json_schema_validate, obj):
    json_schema_validate('jsd_fec9a36b80305b5593608e369fa05b64_v3_1_3_0').validate(obj)
    return True


def delete_the_configuration_model(api):
    endpoint_result = api.wired.delete_the_configuration_model(
        network_device_id='string',
        preview_activity_id='string'
    )
    return endpoint_result


@pytest.mark.wired
def test_delete_the_configuration_model(api, validator):
    try:
        assert is_valid_delete_the_configuration_model(
            validator,
            delete_the_configuration_model(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def delete_the_configuration_model_default_val(api):
    endpoint_result = api.wired.delete_the_configuration_model(
        network_device_id='string',
        preview_activity_id='string'
    )
    return endpoint_result


@pytest.mark.wired
def test_delete_the_configuration_model_default_val(api, validator):
    try:
        assert is_valid_delete_the_configuration_model(
            validator,
            delete_the_configuration_model_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_generate_the_device_config_for_the_configuration_model(json_schema_validate, obj):
    json_schema_validate('jsd_e174c2cf0ecb5b52806a95a08477ae4d_v3_1_3_0').validate(obj)
    return True


def generate_the_device_config_for_the_configuration_model(api):
    endpoint_result = api.wired.generate_the_device_config_for_the_configuration_model(
        active_validation=True,
        network_device_id='string',
        payload=None,
        preview_activity_id='string'
    )
    return endpoint_result


@pytest.mark.wired
def test_generate_the_device_config_for_the_configuration_model(api, validator):
    try:
        assert is_valid_generate_the_device_config_for_the_configuration_model(
            validator,
            generate_the_device_config_for_the_configuration_model(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def generate_the_device_config_for_the_configuration_model_default_val(api):
    endpoint_result = api.wired.generate_the_device_config_for_the_configuration_model(
        active_validation=True,
        network_device_id='string',
        payload=None,
        preview_activity_id='string'
    )
    return endpoint_result


@pytest.mark.wired
def test_generate_the_device_config_for_the_configuration_model_default_val(api, validator):
    try:
        assert is_valid_generate_the_device_config_for_the_configuration_model(
            validator,
            generate_the_device_config_for_the_configuration_model_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_gets_the_device_config_for_the_configuration_model(json_schema_validate, obj):
    json_schema_validate('jsd_9f7fdcd6e2dd5f4eaf7ceed5e5856ba2_v3_1_3_0').validate(obj)
    return True


def gets_the_device_config_for_the_configuration_model(api):
    endpoint_result = api.wired.gets_the_device_config_for_the_configuration_model(
        network_device_id='string',
        preview_activity_id='string'
    )
    return endpoint_result


@pytest.mark.wired
def test_gets_the_device_config_for_the_configuration_model(api, validator):
    try:
        assert is_valid_gets_the_device_config_for_the_configuration_model(
            validator,
            gets_the_device_config_for_the_configuration_model(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def gets_the_device_config_for_the_configuration_model_default_val(api):
    endpoint_result = api.wired.gets_the_device_config_for_the_configuration_model(
        network_device_id='string',
        preview_activity_id='string'
    )
    return endpoint_result


@pytest.mark.wired
def test_gets_the_device_config_for_the_configuration_model_default_val(api, validator):
    try:
        assert is_valid_gets_the_device_config_for_the_configuration_model(
            validator,
            gets_the_device_config_for_the_configuration_model_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_deploy_the_intended_configuration_features_on_a_wired_device(json_schema_validate, obj):
    json_schema_validate('jsd_1a21cb2b7ea258e197f22082301cd1cc_v3_1_3_0').validate(obj)
    return True


def deploy_the_intended_configuration_features_on_a_wired_device(api):
    endpoint_result = api.wired.deploy_the_intended_configuration_features_on_a_wired_device(
        active_validation=True,
        network_device_id='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.wired
def test_deploy_the_intended_configuration_features_on_a_wired_device(api, validator):
    try:
        assert is_valid_deploy_the_intended_configuration_features_on_a_wired_device(
            validator,
            deploy_the_intended_configuration_features_on_a_wired_device(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def deploy_the_intended_configuration_features_on_a_wired_device_default_val(api):
    endpoint_result = api.wired.deploy_the_intended_configuration_features_on_a_wired_device(
        active_validation=True,
        network_device_id='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.wired
def test_deploy_the_intended_configuration_features_on_a_wired_device_default_val(api, validator):
    try:
        assert is_valid_deploy_the_intended_configuration_features_on_a_wired_device(
            validator,
            deploy_the_intended_configuration_features_on_a_wired_device_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_device_deployment_status_connectivity(json_schema_validate, obj):
    json_schema_validate('jsd_44be5246ea895b5b958caa2c67d6e389_v3_1_3_0').validate(obj)
    return True


def get_device_deployment_status_connectivity(api):
    endpoint_result = api.wired.get_device_deployment_status_connectivity(
        network_device_id='string'
    )
    return endpoint_result


@pytest.mark.wired
def test_get_device_deployment_status_connectivity(api, validator):
    try:
        assert is_valid_get_device_deployment_status_connectivity(
            validator,
            get_device_deployment_status_connectivity(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_device_deployment_status_connectivity_default_val(api):
    endpoint_result = api.wired.get_device_deployment_status_connectivity(
        network_device_id='string'
    )
    return endpoint_result


@pytest.mark.wired
def test_get_device_deployment_status_connectivity_default_val(api, validator):
    try:
        assert is_valid_get_device_deployment_status_connectivity(
            validator,
            get_device_deployment_status_connectivity_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_service_deployment_status(json_schema_validate, obj):
    json_schema_validate('jsd_c16b9caed6045399a6e7744914195fee_v3_1_3_0').validate(obj)
    return True


def get_service_deployment_status(api):
    endpoint_result = api.wired.get_service_deployment_status(
        network_device_id='string'
    )
    return endpoint_result


@pytest.mark.wired
def test_get_service_deployment_status(api, validator):
    try:
        assert is_valid_get_service_deployment_status(
            validator,
            get_service_deployment_status(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_service_deployment_status_default_val(api):
    endpoint_result = api.wired.get_service_deployment_status(
        network_device_id='string'
    )
    return endpoint_result


@pytest.mark.wired
def test_get_service_deployment_status_default_val(api, validator):
    try:
        assert is_valid_get_service_deployment_status(
            validator,
            get_service_deployment_status_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e

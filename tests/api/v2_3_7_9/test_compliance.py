# -*- coding: utf-8 -*-
"""CatalystCenterAPI compliance API fixtures and tests.

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
import pytest
from fastjsonschema.exceptions import JsonSchemaException
from dnacentersdk.exceptions import MalformedRequest
from tests.environment import DNA_CENTER_VERSION

pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '2.3.7.9', reason='version does not match')


def is_valid_get_compliance_status(json_schema_validate, obj):
    json_schema_validate('jsd_4a1de7ff46fa5da09c5051c06ad07f2c_v2_3_7_9').validate(obj)
    return True


def get_compliance_status(api):
    endpoint_result = api.compliance.get_compliance_status(
        compliance_status='string',
        device_uuid='string',
        limit=0,
        offset=0
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_compliance_status(api, validator):
    try:
        assert is_valid_get_compliance_status(
            validator,
            get_compliance_status(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_compliance_status_default_val(api):
    endpoint_result = api.compliance.get_compliance_status(
        compliance_status=None,
        device_uuid=None,
        limit=None,
        offset=None
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_compliance_status_default_val(api, validator):
    try:
        assert is_valid_get_compliance_status(
            validator,
            get_compliance_status_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_run_compliance(json_schema_validate, obj):
    json_schema_validate('jsd_0802306a0a8d545698d1d59a9be90e51_v2_3_7_9').validate(obj)
    return True


def run_compliance(api):
    endpoint_result = api.compliance.run_compliance(
        active_validation=True,
        categories=['string'],
        deviceUuids=['string'],
        payload=None,
        triggerFull=True
    )
    return endpoint_result


@pytest.mark.compliance
def test_run_compliance(api, validator):
    try:
        assert is_valid_run_compliance(
            validator,
            run_compliance(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def run_compliance_default_val(api):
    endpoint_result = api.compliance.run_compliance(
        active_validation=True,
        categories=None,
        deviceUuids=None,
        payload=None,
        triggerFull=None
    )
    return endpoint_result


@pytest.mark.compliance
def test_run_compliance_default_val(api, validator):
    try:
        assert is_valid_run_compliance(
            validator,
            run_compliance_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_compliance_status_count(json_schema_validate, obj):
    json_schema_validate('jsd_079c37ce8136584f9e2ed471fc896ef9_v2_3_7_9').validate(obj)
    return True


def get_compliance_status_count(api):
    endpoint_result = api.compliance.get_compliance_status_count(
        compliance_status='string'
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_compliance_status_count(api, validator):
    try:
        assert is_valid_get_compliance_status_count(
            validator,
            get_compliance_status_count(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_compliance_status_count_default_val(api):
    endpoint_result = api.compliance.get_compliance_status_count(
        compliance_status=None
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_compliance_status_count_default_val(api, validator):
    try:
        assert is_valid_get_compliance_status_count(
            validator,
            get_compliance_status_count_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_compliance_detail(json_schema_validate, obj):
    json_schema_validate('jsd_6395adeaeb8157da972efb7b91e1e2cb_v2_3_7_9').validate(obj)
    return True


def get_compliance_detail(api):
    endpoint_result = api.compliance.get_compliance_detail(
        compliance_status='string',
        compliance_type='string',
        device_uuid='string',
        limit=0,
        offset=0
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_compliance_detail(api, validator):
    try:
        assert is_valid_get_compliance_detail(
            validator,
            get_compliance_detail(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_compliance_detail_default_val(api):
    endpoint_result = api.compliance.get_compliance_detail(
        compliance_status=None,
        compliance_type=None,
        device_uuid=None,
        limit=None,
        offset=None
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_compliance_detail_default_val(api, validator):
    try:
        assert is_valid_get_compliance_detail(
            validator,
            get_compliance_detail_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_compliance_detail_count(json_schema_validate, obj):
    json_schema_validate('jsd_d3d38fed534f5aeaa80f5a8c63694708_v2_3_7_9').validate(obj)
    return True


def get_compliance_detail_count(api):
    endpoint_result = api.compliance.get_compliance_detail_count(
        compliance_status='string',
        compliance_type='string'
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_compliance_detail_count(api, validator):
    try:
        assert is_valid_get_compliance_detail_count(
            validator,
            get_compliance_detail_count(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_compliance_detail_count_default_val(api):
    endpoint_result = api.compliance.get_compliance_detail_count(
        compliance_status=None,
        compliance_type=None
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_compliance_detail_count_default_val(api, validator):
    try:
        assert is_valid_get_compliance_detail_count(
            validator,
            get_compliance_detail_count_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_compliance_remediation(json_schema_validate, obj):
    json_schema_validate('jsd_a233477d86a459eab3c5e9352c1c9d3e_v2_3_7_9').validate(obj)
    return True


def compliance_remediation(api):
    endpoint_result = api.compliance.compliance_remediation(
        active_validation=True,
        id='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.compliance
def test_compliance_remediation(api, validator):
    try:
        assert is_valid_compliance_remediation(
            validator,
            compliance_remediation(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def compliance_remediation_default_val(api):
    endpoint_result = api.compliance.compliance_remediation(
        active_validation=True,
        id='string',
        payload=None
    )
    return endpoint_result


@pytest.mark.compliance
def test_compliance_remediation_default_val(api, validator):
    try:
        assert is_valid_compliance_remediation(
            validator,
            compliance_remediation_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_device_compliance_status(json_schema_validate, obj):
    json_schema_validate('jsd_41da8e5cdd435db0b1da1684be8f15b8_v2_3_7_9').validate(obj)
    return True


def device_compliance_status(api):
    endpoint_result = api.compliance.device_compliance_status(
        device_uuid='string'
    )
    return endpoint_result


@pytest.mark.compliance
def test_device_compliance_status(api, validator):
    try:
        assert is_valid_device_compliance_status(
            validator,
            device_compliance_status(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def device_compliance_status_default_val(api):
    endpoint_result = api.compliance.device_compliance_status(
        device_uuid='string'
    )
    return endpoint_result


@pytest.mark.compliance
def test_device_compliance_status_default_val(api, validator):
    try:
        assert is_valid_device_compliance_status(
            validator,
            device_compliance_status_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_compliance_details_of_device(json_schema_validate, obj):
    json_schema_validate('jsd_90b70e1b6a2f51a59690669a4b2fd3f0_v2_3_7_9').validate(obj)
    return True


def compliance_details_of_device(api):
    endpoint_result = api.compliance.compliance_details_of_device(
        category='string',
        compliance_type='string',
        device_uuid='string',
        diff_list=True,
        remediation_supported=True,
        status='string'
    )
    return endpoint_result


@pytest.mark.compliance
def test_compliance_details_of_device(api, validator):
    try:
        assert is_valid_compliance_details_of_device(
            validator,
            compliance_details_of_device(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def compliance_details_of_device_default_val(api):
    endpoint_result = api.compliance.compliance_details_of_device(
        category=None,
        compliance_type=None,
        device_uuid='string',
        diff_list=None,
        remediation_supported=None,
        status=None
    )
    return endpoint_result


@pytest.mark.compliance
def test_compliance_details_of_device_default_val(api, validator):
    try:
        assert is_valid_compliance_details_of_device(
            validator,
            compliance_details_of_device_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_field_notice_network_devices(json_schema_validate, obj):
    json_schema_validate('jsd_bf89c9e9897659e496ff2c2c2cfb8d35_v2_3_7_9').validate(obj)
    return True


def get_field_notice_network_devices(api):
    endpoint_result = api.compliance.get_field_notice_network_devices(
        limit=0,
        network_device_id='string',
        notice_count=0,
        offset=0,
        order='string',
        scan_status='string',
        sort_by='string'
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_field_notice_network_devices(api, validator):
    try:
        assert is_valid_get_field_notice_network_devices(
            validator,
            get_field_notice_network_devices(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_field_notice_network_devices_default_val(api):
    endpoint_result = api.compliance.get_field_notice_network_devices(
        limit=None,
        network_device_id=None,
        notice_count=None,
        offset=None,
        order=None,
        scan_status=None,
        sort_by=None
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_field_notice_network_devices_default_val(api, validator):
    try:
        assert is_valid_get_field_notice_network_devices(
            validator,
            get_field_notice_network_devices_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_count_of_field_notice_network_devices(json_schema_validate, obj):
    json_schema_validate('jsd_50f4a44a87cc51ffb9be1cb2a6bdfa68_v2_3_7_9').validate(obj)
    return True


def get_count_of_field_notice_network_devices(api):
    endpoint_result = api.compliance.get_count_of_field_notice_network_devices(
        network_device_id='string',
        notice_count=0,
        scan_status='string'
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_count_of_field_notice_network_devices(api, validator):
    try:
        assert is_valid_get_count_of_field_notice_network_devices(
            validator,
            get_count_of_field_notice_network_devices(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_count_of_field_notice_network_devices_default_val(api):
    endpoint_result = api.compliance.get_count_of_field_notice_network_devices(
        network_device_id=None,
        notice_count=None,
        scan_status=None
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_count_of_field_notice_network_devices_default_val(api, validator):
    try:
        assert is_valid_get_count_of_field_notice_network_devices(
            validator,
            get_count_of_field_notice_network_devices_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_field_notice_network_device_by_device_id(json_schema_validate, obj):
    json_schema_validate('jsd_f9138e17f05f57fda724a4767aa35ad4_v2_3_7_9').validate(obj)
    return True


def get_field_notice_network_device_by_device_id(api):
    endpoint_result = api.compliance.get_field_notice_network_device_by_device_id(
        network_device_id='string'
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_field_notice_network_device_by_device_id(api, validator):
    try:
        assert is_valid_get_field_notice_network_device_by_device_id(
            validator,
            get_field_notice_network_device_by_device_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_field_notice_network_device_by_device_id_default_val(api):
    endpoint_result = api.compliance.get_field_notice_network_device_by_device_id(
        network_device_id='string'
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_field_notice_network_device_by_device_id_default_val(api, validator):
    try:
        assert is_valid_get_field_notice_network_device_by_device_id(
            validator,
            get_field_notice_network_device_by_device_id_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_field_notices_affecting_the_network_device(json_schema_validate, obj):
    json_schema_validate('jsd_f44a1efb2d0f53209fdc441a3bbf073f_v2_3_7_9').validate(obj)
    return True


def get_field_notices_affecting_the_network_device(api):
    endpoint_result = api.compliance.get_field_notices_affecting_the_network_device(
        id='string',
        limit=0,
        network_device_id='string',
        offset=0,
        order='string',
        sort_by='string',
        type='string'
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_field_notices_affecting_the_network_device(api, validator):
    try:
        assert is_valid_get_field_notices_affecting_the_network_device(
            validator,
            get_field_notices_affecting_the_network_device(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_field_notices_affecting_the_network_device_default_val(api):
    endpoint_result = api.compliance.get_field_notices_affecting_the_network_device(
        id=None,
        limit=None,
        network_device_id='string',
        offset=None,
        order=None,
        sort_by=None,
        type=None
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_field_notices_affecting_the_network_device_default_val(api, validator):
    try:
        assert is_valid_get_field_notices_affecting_the_network_device(
            validator,
            get_field_notices_affecting_the_network_device_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_count_of_field_notices_affecting_the_network_device(json_schema_validate, obj):
    json_schema_validate('jsd_63af749446fd572cbad63745a6d55c5a_v2_3_7_9').validate(obj)
    return True


def get_count_of_field_notices_affecting_the_network_device(api):
    endpoint_result = api.compliance.get_count_of_field_notices_affecting_the_network_device(
        id='string',
        network_device_id='string',
        type='string'
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_count_of_field_notices_affecting_the_network_device(api, validator):
    try:
        assert is_valid_get_count_of_field_notices_affecting_the_network_device(
            validator,
            get_count_of_field_notices_affecting_the_network_device(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_count_of_field_notices_affecting_the_network_device_default_val(api):
    endpoint_result = api.compliance.get_count_of_field_notices_affecting_the_network_device(
        id=None,
        network_device_id='string',
        type=None
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_count_of_field_notices_affecting_the_network_device_default_val(api, validator):
    try:
        assert is_valid_get_count_of_field_notices_affecting_the_network_device(
            validator,
            get_count_of_field_notices_affecting_the_network_device_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_field_notice_affecting_the_network_device_by_device_id_and_notice_id(json_schema_validate, obj):
    json_schema_validate('jsd_f585d782d15b54b89e227ab1d01e6f57_v2_3_7_9').validate(obj)
    return True


def get_field_notice_affecting_the_network_device_by_device_id_and_notice_id(api):
    endpoint_result = api.compliance.get_field_notice_affecting_the_network_device_by_device_id_and_notice_id(
        id='string',
        network_device_id='string'
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_field_notice_affecting_the_network_device_by_device_id_and_notice_id(api, validator):
    try:
        assert is_valid_get_field_notice_affecting_the_network_device_by_device_id_and_notice_id(
            validator,
            get_field_notice_affecting_the_network_device_by_device_id_and_notice_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_field_notice_affecting_the_network_device_by_device_id_and_notice_id_default_val(api):
    endpoint_result = api.compliance.get_field_notice_affecting_the_network_device_by_device_id_and_notice_id(
        id='string',
        network_device_id='string'
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_field_notice_affecting_the_network_device_by_device_id_and_notice_id_default_val(api, validator):
    try:
        assert is_valid_get_field_notice_affecting_the_network_device_by_device_id_and_notice_id(
            validator,
            get_field_notice_affecting_the_network_device_by_device_id_and_notice_id_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_field_notices(json_schema_validate, obj):
    json_schema_validate('jsd_2aa335c92d485537bab1126533ac8ed7_v2_3_7_9').validate(obj)
    return True


def get_field_notices(api):
    endpoint_result = api.compliance.get_field_notices(
        device_count=0,
        id='string',
        limit=0,
        offset=0,
        order='string',
        sort_by='string',
        type='string'
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_field_notices(api, validator):
    try:
        assert is_valid_get_field_notices(
            validator,
            get_field_notices(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_field_notices_default_val(api):
    endpoint_result = api.compliance.get_field_notices(
        device_count=None,
        id=None,
        limit=None,
        offset=None,
        order=None,
        sort_by=None,
        type=None
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_field_notices_default_val(api, validator):
    try:
        assert is_valid_get_field_notices(
            validator,
            get_field_notices_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_count_of_field_notices(json_schema_validate, obj):
    json_schema_validate('jsd_15b172bd7cd55378bd25e4ae525a9179_v2_3_7_9').validate(obj)
    return True


def get_count_of_field_notices(api):
    endpoint_result = api.compliance.get_count_of_field_notices(
        device_count=0,
        id='string',
        type='string'
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_count_of_field_notices(api, validator):
    try:
        assert is_valid_get_count_of_field_notices(
            validator,
            get_count_of_field_notices(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_count_of_field_notices_default_val(api):
    endpoint_result = api.compliance.get_count_of_field_notices(
        device_count=None,
        id=None,
        type=None
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_count_of_field_notices_default_val(api, validator):
    try:
        assert is_valid_get_count_of_field_notices(
            validator,
            get_count_of_field_notices_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_field_notice_by_id(json_schema_validate, obj):
    json_schema_validate('jsd_485fc5e9ea9a5acd9e461b88355330ee_v2_3_7_9').validate(obj)
    return True


def get_field_notice_by_id(api):
    endpoint_result = api.compliance.get_field_notice_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_field_notice_by_id(api, validator):
    try:
        assert is_valid_get_field_notice_by_id(
            validator,
            get_field_notice_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_field_notice_by_id_default_val(api):
    endpoint_result = api.compliance.get_field_notice_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_field_notice_by_id_default_val(api, validator):
    try:
        assert is_valid_get_field_notice_by_id(
            validator,
            get_field_notice_by_id_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_field_notice_network_devices_for_the_notice(json_schema_validate, obj):
    json_schema_validate('jsd_6e015bf018f55499a59aae5c54264bf4_v2_3_7_9').validate(obj)
    return True


def get_field_notice_network_devices_for_the_notice(api):
    endpoint_result = api.compliance.get_field_notice_network_devices_for_the_notice(
        id='string',
        limit=0,
        network_device_id='string',
        offset=0,
        order='string',
        scan_status='string',
        sort_by='string'
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_field_notice_network_devices_for_the_notice(api, validator):
    try:
        assert is_valid_get_field_notice_network_devices_for_the_notice(
            validator,
            get_field_notice_network_devices_for_the_notice(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_field_notice_network_devices_for_the_notice_default_val(api):
    endpoint_result = api.compliance.get_field_notice_network_devices_for_the_notice(
        id='string',
        limit=None,
        network_device_id=None,
        offset=None,
        order=None,
        scan_status=None,
        sort_by=None
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_field_notice_network_devices_for_the_notice_default_val(api, validator):
    try:
        assert is_valid_get_field_notice_network_devices_for_the_notice(
            validator,
            get_field_notice_network_devices_for_the_notice_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_count_of_field_notice_network_devices_for_the_notice(json_schema_validate, obj):
    json_schema_validate('jsd_49cffe4d51a6508e8c18de0d45d78294_v2_3_7_9').validate(obj)
    return True


def get_count_of_field_notice_network_devices_for_the_notice(api):
    endpoint_result = api.compliance.get_count_of_field_notice_network_devices_for_the_notice(
        id='string',
        network_device_id='string',
        scan_status='string'
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_count_of_field_notice_network_devices_for_the_notice(api, validator):
    try:
        assert is_valid_get_count_of_field_notice_network_devices_for_the_notice(
            validator,
            get_count_of_field_notice_network_devices_for_the_notice(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_count_of_field_notice_network_devices_for_the_notice_default_val(api):
    endpoint_result = api.compliance.get_count_of_field_notice_network_devices_for_the_notice(
        id='string',
        network_device_id=None,
        scan_status=None
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_count_of_field_notice_network_devices_for_the_notice_default_val(api, validator):
    try:
        assert is_valid_get_count_of_field_notice_network_devices_for_the_notice(
            validator,
            get_count_of_field_notice_network_devices_for_the_notice_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_field_notice_network_device_for_the_notice_by_network_device_id(json_schema_validate, obj):
    json_schema_validate('jsd_04e9343c828f586da856c48c8edee40b_v2_3_7_9').validate(obj)
    return True


def get_field_notice_network_device_for_the_notice_by_network_device_id(api):
    endpoint_result = api.compliance.get_field_notice_network_device_for_the_notice_by_network_device_id(
        id='string',
        network_device_id='string'
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_field_notice_network_device_for_the_notice_by_network_device_id(api, validator):
    try:
        assert is_valid_get_field_notice_network_device_for_the_notice_by_network_device_id(
            validator,
            get_field_notice_network_device_for_the_notice_by_network_device_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_field_notice_network_device_for_the_notice_by_network_device_id_default_val(api):
    endpoint_result = api.compliance.get_field_notice_network_device_for_the_notice_by_network_device_id(
        id='string',
        network_device_id='string'
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_field_notice_network_device_for_the_notice_by_network_device_id_default_val(api, validator):
    try:
        assert is_valid_get_field_notice_network_device_for_the_notice_by_network_device_id(
            validator,
            get_field_notice_network_device_for_the_notice_by_network_device_id_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_field_notices_results_trend_over_time(json_schema_validate, obj):
    json_schema_validate('jsd_79872073a7065d7d9654a4015c6e961a_v2_3_7_9').validate(obj)
    return True


def get_field_notices_results_trend_over_time(api):
    endpoint_result = api.compliance.get_field_notices_results_trend_over_time(
        limit=0,
        offset=0,
        scan_time=0
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_field_notices_results_trend_over_time(api, validator):
    try:
        assert is_valid_get_field_notices_results_trend_over_time(
            validator,
            get_field_notices_results_trend_over_time(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_field_notices_results_trend_over_time_default_val(api):
    endpoint_result = api.compliance.get_field_notices_results_trend_over_time(
        limit=None,
        offset=None,
        scan_time=None
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_field_notices_results_trend_over_time_default_val(api, validator):
    try:
        assert is_valid_get_field_notices_results_trend_over_time(
            validator,
            get_field_notices_results_trend_over_time_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_count_of_field_notices_results_trend_over_time(json_schema_validate, obj):
    json_schema_validate('jsd_20f89484e88e57b292756b0c7e54b553_v2_3_7_9').validate(obj)
    return True


def get_count_of_field_notices_results_trend_over_time(api):
    endpoint_result = api.compliance.get_count_of_field_notices_results_trend_over_time(
        scan_time=0
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_count_of_field_notices_results_trend_over_time(api, validator):
    try:
        assert is_valid_get_count_of_field_notices_results_trend_over_time(
            validator,
            get_count_of_field_notices_results_trend_over_time(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_count_of_field_notices_results_trend_over_time_default_val(api):
    endpoint_result = api.compliance.get_count_of_field_notices_results_trend_over_time(
        scan_time=None
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_count_of_field_notices_results_trend_over_time_default_val(api, validator):
    try:
        assert is_valid_get_count_of_field_notices_results_trend_over_time(
            validator,
            get_count_of_field_notices_results_trend_over_time_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_creates_a_trial_for_field_notices_detection_on_network_devices(json_schema_validate, obj):
    json_schema_validate('jsd_5820be66c0a0582fa234daaa2019b6b6_v2_3_7_9').validate(obj)
    return True


def creates_a_trial_for_field_notices_detection_on_network_devices(api):
    endpoint_result = api.compliance.creates_a_trial_for_field_notices_detection_on_network_devices(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.compliance
def test_creates_a_trial_for_field_notices_detection_on_network_devices(api, validator):
    try:
        assert is_valid_creates_a_trial_for_field_notices_detection_on_network_devices(
            validator,
            creates_a_trial_for_field_notices_detection_on_network_devices(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def creates_a_trial_for_field_notices_detection_on_network_devices_default_val(api):
    endpoint_result = api.compliance.creates_a_trial_for_field_notices_detection_on_network_devices(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.compliance
def test_creates_a_trial_for_field_notices_detection_on_network_devices_default_val(api, validator):
    try:
        assert is_valid_creates_a_trial_for_field_notices_detection_on_network_devices(
            validator,
            creates_a_trial_for_field_notices_detection_on_network_devices_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_trial_details_for_field_notices_detection_on_network_devices(json_schema_validate, obj):
    json_schema_validate('jsd_475203d3893f52738eaf50a6732d2159_v2_3_7_9').validate(obj)
    return True


def get_trial_details_for_field_notices_detection_on_network_devices(api):
    endpoint_result = api.compliance.get_trial_details_for_field_notices_detection_on_network_devices(

    )
    return endpoint_result


@pytest.mark.compliance
def test_get_trial_details_for_field_notices_detection_on_network_devices(api, validator):
    try:
        assert is_valid_get_trial_details_for_field_notices_detection_on_network_devices(
            validator,
            get_trial_details_for_field_notices_detection_on_network_devices(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_trial_details_for_field_notices_detection_on_network_devices_default_val(api):
    endpoint_result = api.compliance.get_trial_details_for_field_notices_detection_on_network_devices(

    )
    return endpoint_result


@pytest.mark.compliance
def test_get_trial_details_for_field_notices_detection_on_network_devices_default_val(api, validator):
    try:
        assert is_valid_get_trial_details_for_field_notices_detection_on_network_devices(
            validator,
            get_trial_details_for_field_notices_detection_on_network_devices_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_triggers_a_field_notices_scan_for_the_supported_network_devices(json_schema_validate, obj):
    json_schema_validate('jsd_8fd0f9b4adc5572da4ccc64802a275f5_v2_3_7_9').validate(obj)
    return True


def triggers_a_field_notices_scan_for_the_supported_network_devices(api):
    endpoint_result = api.compliance.triggers_a_field_notices_scan_for_the_supported_network_devices(
        active_validation=True,
        failed_devices_only=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.compliance
def test_triggers_a_field_notices_scan_for_the_supported_network_devices(api, validator):
    try:
        assert is_valid_triggers_a_field_notices_scan_for_the_supported_network_devices(
            validator,
            triggers_a_field_notices_scan_for_the_supported_network_devices(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def triggers_a_field_notices_scan_for_the_supported_network_devices_default_val(api):
    endpoint_result = api.compliance.triggers_a_field_notices_scan_for_the_supported_network_devices(
        active_validation=True,
        failed_devices_only=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.compliance
def test_triggers_a_field_notices_scan_for_the_supported_network_devices_default_val(api, validator):
    try:
        assert is_valid_triggers_a_field_notices_scan_for_the_supported_network_devices(
            validator,
            triggers_a_field_notices_scan_for_the_supported_network_devices_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_config_task_details(json_schema_validate, obj):
    json_schema_validate('jsd_5cb73c1c44665d1ebbe934dd380f4f5e_v2_3_7_9').validate(obj)
    return True


def get_config_task_details(api):
    endpoint_result = api.compliance.get_config_task_details(
        parent_task_id='string'
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_config_task_details(api, validator):
    try:
        assert is_valid_get_config_task_details(
            validator,
            get_config_task_details(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_config_task_details_default_val(api):
    endpoint_result = api.compliance.get_config_task_details(
        parent_task_id=None
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_config_task_details_default_val(api, validator):
    try:
        assert is_valid_get_config_task_details(
            validator,
            get_config_task_details_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_commit_device_configuration(json_schema_validate, obj):
    json_schema_validate('jsd_ba40975123ed50daa2f9f599cdf2d911_v2_3_7_9').validate(obj)
    return True


def commit_device_configuration(api):
    endpoint_result = api.compliance.commit_device_configuration(
        active_validation=True,
        deviceId=['string'],
        payload=None
    )
    return endpoint_result


@pytest.mark.compliance
def test_commit_device_configuration(api, validator):
    try:
        assert is_valid_commit_device_configuration(
            validator,
            commit_device_configuration(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def commit_device_configuration_default_val(api):
    endpoint_result = api.compliance.commit_device_configuration(
        active_validation=True,
        deviceId=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.compliance
def test_commit_device_configuration_default_val(api, validator):
    try:
        assert is_valid_commit_device_configuration(
            validator,
            commit_device_configuration_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_network_bugs(json_schema_validate, obj):
    json_schema_validate('jsd_a3217129c2295b27838cf486a35626f8_v2_3_7_9').validate(obj)
    return True


def get_network_bugs(api):
    endpoint_result = api.compliance.get_network_bugs(
        device_count=0,
        id='string',
        limit=0,
        offset=0,
        order='string',
        severity='string',
        sort_by='string'
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_network_bugs(api, validator):
    try:
        assert is_valid_get_network_bugs(
            validator,
            get_network_bugs(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_network_bugs_default_val(api):
    endpoint_result = api.compliance.get_network_bugs(
        device_count=None,
        id=None,
        limit=None,
        offset=None,
        order=None,
        severity=None,
        sort_by=None
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_network_bugs_default_val(api, validator):
    try:
        assert is_valid_get_network_bugs(
            validator,
            get_network_bugs_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_count_of_network_bugs(json_schema_validate, obj):
    json_schema_validate('jsd_5e1ec0f16d5e57cab08414ece382334d_v2_3_7_9').validate(obj)
    return True


def get_count_of_network_bugs(api):
    endpoint_result = api.compliance.get_count_of_network_bugs(
        device_count=0,
        id='string',
        severity='string'
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_count_of_network_bugs(api, validator):
    try:
        assert is_valid_get_count_of_network_bugs(
            validator,
            get_count_of_network_bugs(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_count_of_network_bugs_default_val(api):
    endpoint_result = api.compliance.get_count_of_network_bugs(
        device_count=None,
        id=None,
        severity=None
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_count_of_network_bugs_default_val(api, validator):
    try:
        assert is_valid_get_count_of_network_bugs(
            validator,
            get_count_of_network_bugs_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_network_bug_by_id(json_schema_validate, obj):
    json_schema_validate('jsd_90a7663a127d59d9afc45d4daa0ba477_v2_3_7_9').validate(obj)
    return True


def get_network_bug_by_id(api):
    endpoint_result = api.compliance.get_network_bug_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_network_bug_by_id(api, validator):
    try:
        assert is_valid_get_network_bug_by_id(
            validator,
            get_network_bug_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_network_bug_by_id_default_val(api):
    endpoint_result = api.compliance.get_network_bug_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_network_bug_by_id_default_val(api, validator):
    try:
        assert is_valid_get_network_bug_by_id(
            validator,
            get_network_bug_by_id_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_network_bug_devices_for_the_bug(json_schema_validate, obj):
    json_schema_validate('jsd_25d10f773fa5522384790bf1f198d861_v2_3_7_9').validate(obj)
    return True


def get_network_bug_devices_for_the_bug(api):
    endpoint_result = api.compliance.get_network_bug_devices_for_the_bug(
        id='string',
        limit=0,
        network_device_id='string',
        offset=0,
        order='string',
        scan_mode='string',
        scan_status='string',
        sort_by='string'
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_network_bug_devices_for_the_bug(api, validator):
    try:
        assert is_valid_get_network_bug_devices_for_the_bug(
            validator,
            get_network_bug_devices_for_the_bug(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_network_bug_devices_for_the_bug_default_val(api):
    endpoint_result = api.compliance.get_network_bug_devices_for_the_bug(
        id='string',
        limit=None,
        network_device_id=None,
        offset=None,
        order=None,
        scan_mode=None,
        scan_status=None,
        sort_by=None
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_network_bug_devices_for_the_bug_default_val(api, validator):
    try:
        assert is_valid_get_network_bug_devices_for_the_bug(
            validator,
            get_network_bug_devices_for_the_bug_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_count_of_network_bug_devices_for_the_bug(json_schema_validate, obj):
    json_schema_validate('jsd_723c7afe7c0c5c2898eabb7cbbdc4ef4_v2_3_7_9').validate(obj)
    return True


def get_count_of_network_bug_devices_for_the_bug(api):
    endpoint_result = api.compliance.get_count_of_network_bug_devices_for_the_bug(
        id='string',
        network_device_id='string',
        scan_mode='string',
        scan_status='string'
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_count_of_network_bug_devices_for_the_bug(api, validator):
    try:
        assert is_valid_get_count_of_network_bug_devices_for_the_bug(
            validator,
            get_count_of_network_bug_devices_for_the_bug(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_count_of_network_bug_devices_for_the_bug_default_val(api):
    endpoint_result = api.compliance.get_count_of_network_bug_devices_for_the_bug(
        id='string',
        network_device_id=None,
        scan_mode=None,
        scan_status=None
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_count_of_network_bug_devices_for_the_bug_default_val(api, validator):
    try:
        assert is_valid_get_count_of_network_bug_devices_for_the_bug(
            validator,
            get_count_of_network_bug_devices_for_the_bug_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_network_bug_device_for_the_bug_by_network_device_id(json_schema_validate, obj):
    json_schema_validate('jsd_c369b19255b95cffb73b8061e01a1f7d_v2_3_7_9').validate(obj)
    return True


def get_network_bug_device_for_the_bug_by_network_device_id(api):
    endpoint_result = api.compliance.get_network_bug_device_for_the_bug_by_network_device_id(
        id='string',
        network_device_id='string'
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_network_bug_device_for_the_bug_by_network_device_id(api, validator):
    try:
        assert is_valid_get_network_bug_device_for_the_bug_by_network_device_id(
            validator,
            get_network_bug_device_for_the_bug_by_network_device_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_network_bug_device_for_the_bug_by_network_device_id_default_val(api):
    endpoint_result = api.compliance.get_network_bug_device_for_the_bug_by_network_device_id(
        id='string',
        network_device_id='string'
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_network_bug_device_for_the_bug_by_network_device_id_default_val(api, validator):
    try:
        assert is_valid_get_network_bug_device_for_the_bug_by_network_device_id(
            validator,
            get_network_bug_device_for_the_bug_by_network_device_id_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_network_bug_devices(json_schema_validate, obj):
    json_schema_validate('jsd_2f6011b1d24c53d1aa7dda9e0d3ee29b_v2_3_7_9').validate(obj)
    return True


def get_network_bug_devices(api):
    endpoint_result = api.compliance.get_network_bug_devices(
        bug_count=0,
        limit=0,
        network_device_id='string',
        offset=0,
        order='string',
        scan_mode='string',
        scan_status='string',
        sort_by='string'
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_network_bug_devices(api, validator):
    try:
        assert is_valid_get_network_bug_devices(
            validator,
            get_network_bug_devices(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_network_bug_devices_default_val(api):
    endpoint_result = api.compliance.get_network_bug_devices(
        bug_count=None,
        limit=None,
        network_device_id=None,
        offset=None,
        order=None,
        scan_mode=None,
        scan_status=None,
        sort_by=None
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_network_bug_devices_default_val(api, validator):
    try:
        assert is_valid_get_network_bug_devices(
            validator,
            get_network_bug_devices_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_count_of_network_bug_devices(json_schema_validate, obj):
    json_schema_validate('jsd_9aab9fd032d15280ac99b00b34600781_v2_3_7_9').validate(obj)
    return True


def get_count_of_network_bug_devices(api):
    endpoint_result = api.compliance.get_count_of_network_bug_devices(
        bug_count=0,
        network_device_id='string',
        scan_mode='string',
        scan_status='string'
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_count_of_network_bug_devices(api, validator):
    try:
        assert is_valid_get_count_of_network_bug_devices(
            validator,
            get_count_of_network_bug_devices(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_count_of_network_bug_devices_default_val(api):
    endpoint_result = api.compliance.get_count_of_network_bug_devices(
        bug_count=None,
        network_device_id=None,
        scan_mode=None,
        scan_status=None
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_count_of_network_bug_devices_default_val(api, validator):
    try:
        assert is_valid_get_count_of_network_bug_devices(
            validator,
            get_count_of_network_bug_devices_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_network_bug_device_by_device_id(json_schema_validate, obj):
    json_schema_validate('jsd_e2f8ce2370c6532da9181a319daf0fec_v2_3_7_9').validate(obj)
    return True


def get_network_bug_device_by_device_id(api):
    endpoint_result = api.compliance.get_network_bug_device_by_device_id(
        network_device_id='string'
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_network_bug_device_by_device_id(api, validator):
    try:
        assert is_valid_get_network_bug_device_by_device_id(
            validator,
            get_network_bug_device_by_device_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_network_bug_device_by_device_id_default_val(api):
    endpoint_result = api.compliance.get_network_bug_device_by_device_id(
        network_device_id='string'
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_network_bug_device_by_device_id_default_val(api, validator):
    try:
        assert is_valid_get_network_bug_device_by_device_id(
            validator,
            get_network_bug_device_by_device_id_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_bugs_affecting_the_network_device(json_schema_validate, obj):
    json_schema_validate('jsd_aea65ed8cb2e55fb8d7c40abf2352504_v2_3_7_9').validate(obj)
    return True


def get_bugs_affecting_the_network_device(api):
    endpoint_result = api.compliance.get_bugs_affecting_the_network_device(
        id='string',
        limit=0,
        network_device_id='string',
        offset=0,
        order='string',
        severity='string',
        sort_by='string'
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_bugs_affecting_the_network_device(api, validator):
    try:
        assert is_valid_get_bugs_affecting_the_network_device(
            validator,
            get_bugs_affecting_the_network_device(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_bugs_affecting_the_network_device_default_val(api):
    endpoint_result = api.compliance.get_bugs_affecting_the_network_device(
        id=None,
        limit=None,
        network_device_id='string',
        offset=None,
        order=None,
        severity=None,
        sort_by=None
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_bugs_affecting_the_network_device_default_val(api, validator):
    try:
        assert is_valid_get_bugs_affecting_the_network_device(
            validator,
            get_bugs_affecting_the_network_device_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_count_of_bugs_affecting_the_network_device(json_schema_validate, obj):
    json_schema_validate('jsd_a3e7c7a84b195cf989715f228c4c3337_v2_3_7_9').validate(obj)
    return True


def get_count_of_bugs_affecting_the_network_device(api):
    endpoint_result = api.compliance.get_count_of_bugs_affecting_the_network_device(
        id='string',
        network_device_id='string',
        severity='string'
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_count_of_bugs_affecting_the_network_device(api, validator):
    try:
        assert is_valid_get_count_of_bugs_affecting_the_network_device(
            validator,
            get_count_of_bugs_affecting_the_network_device(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_count_of_bugs_affecting_the_network_device_default_val(api):
    endpoint_result = api.compliance.get_count_of_bugs_affecting_the_network_device(
        id=None,
        network_device_id='string',
        severity=None
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_count_of_bugs_affecting_the_network_device_default_val(api, validator):
    try:
        assert is_valid_get_count_of_bugs_affecting_the_network_device(
            validator,
            get_count_of_bugs_affecting_the_network_device_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_bug_affecting_the_network_device_by_device_id_and_bug_id(json_schema_validate, obj):
    json_schema_validate('jsd_3beba27ea019536da45eef3cade3ab67_v2_3_7_9').validate(obj)
    return True


def get_bug_affecting_the_network_device_by_device_id_and_bug_id(api):
    endpoint_result = api.compliance.get_bug_affecting_the_network_device_by_device_id_and_bug_id(
        id='string',
        network_device_id='string'
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_bug_affecting_the_network_device_by_device_id_and_bug_id(api, validator):
    try:
        assert is_valid_get_bug_affecting_the_network_device_by_device_id_and_bug_id(
            validator,
            get_bug_affecting_the_network_device_by_device_id_and_bug_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_bug_affecting_the_network_device_by_device_id_and_bug_id_default_val(api):
    endpoint_result = api.compliance.get_bug_affecting_the_network_device_by_device_id_and_bug_id(
        id='string',
        network_device_id='string'
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_bug_affecting_the_network_device_by_device_id_and_bug_id_default_val(api, validator):
    try:
        assert is_valid_get_bug_affecting_the_network_device_by_device_id_and_bug_id(
            validator,
            get_bug_affecting_the_network_device_by_device_id_and_bug_id_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_network_bugs_results_trend_over_time(json_schema_validate, obj):
    json_schema_validate('jsd_4ad7e992ab6a526196819e35eb0418a4_v2_3_7_9').validate(obj)
    return True


def get_network_bugs_results_trend_over_time(api):
    endpoint_result = api.compliance.get_network_bugs_results_trend_over_time(
        limit=0,
        offset=0,
        scan_time=0
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_network_bugs_results_trend_over_time(api, validator):
    try:
        assert is_valid_get_network_bugs_results_trend_over_time(
            validator,
            get_network_bugs_results_trend_over_time(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_network_bugs_results_trend_over_time_default_val(api):
    endpoint_result = api.compliance.get_network_bugs_results_trend_over_time(
        limit=None,
        offset=None,
        scan_time=None
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_network_bugs_results_trend_over_time_default_val(api, validator):
    try:
        assert is_valid_get_network_bugs_results_trend_over_time(
            validator,
            get_network_bugs_results_trend_over_time_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_count_of_network_bugs_results_trend_over_time(json_schema_validate, obj):
    json_schema_validate('jsd_a240f89766435001b3ed25c3d23f0ffc_v2_3_7_9').validate(obj)
    return True


def get_count_of_network_bugs_results_trend_over_time(api):
    endpoint_result = api.compliance.get_count_of_network_bugs_results_trend_over_time(
        scan_time=0
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_count_of_network_bugs_results_trend_over_time(api, validator):
    try:
        assert is_valid_get_count_of_network_bugs_results_trend_over_time(
            validator,
            get_count_of_network_bugs_results_trend_over_time(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_count_of_network_bugs_results_trend_over_time_default_val(api):
    endpoint_result = api.compliance.get_count_of_network_bugs_results_trend_over_time(
        scan_time=None
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_count_of_network_bugs_results_trend_over_time_default_val(api, validator):
    try:
        assert is_valid_get_count_of_network_bugs_results_trend_over_time(
            validator,
            get_count_of_network_bugs_results_trend_over_time_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_creates_a_trial_for_bugs_detection_on_network_devices(json_schema_validate, obj):
    json_schema_validate('jsd_7c08d904cff256aca70a68901692a021_v2_3_7_9').validate(obj)
    return True


def creates_a_trial_for_bugs_detection_on_network_devices(api):
    endpoint_result = api.compliance.creates_a_trial_for_bugs_detection_on_network_devices(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.compliance
def test_creates_a_trial_for_bugs_detection_on_network_devices(api, validator):
    try:
        assert is_valid_creates_a_trial_for_bugs_detection_on_network_devices(
            validator,
            creates_a_trial_for_bugs_detection_on_network_devices(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def creates_a_trial_for_bugs_detection_on_network_devices_default_val(api):
    endpoint_result = api.compliance.creates_a_trial_for_bugs_detection_on_network_devices(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.compliance
def test_creates_a_trial_for_bugs_detection_on_network_devices_default_val(api, validator):
    try:
        assert is_valid_creates_a_trial_for_bugs_detection_on_network_devices(
            validator,
            creates_a_trial_for_bugs_detection_on_network_devices_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_trial_details_for_bugs_detection_on_network_devices(json_schema_validate, obj):
    json_schema_validate('jsd_5a3479f3b91c5b73bdfed9f1cb6f7bb5_v2_3_7_9').validate(obj)
    return True


def get_trial_details_for_bugs_detection_on_network_devices(api):
    endpoint_result = api.compliance.get_trial_details_for_bugs_detection_on_network_devices(

    )
    return endpoint_result


@pytest.mark.compliance
def test_get_trial_details_for_bugs_detection_on_network_devices(api, validator):
    try:
        assert is_valid_get_trial_details_for_bugs_detection_on_network_devices(
            validator,
            get_trial_details_for_bugs_detection_on_network_devices(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_trial_details_for_bugs_detection_on_network_devices_default_val(api):
    endpoint_result = api.compliance.get_trial_details_for_bugs_detection_on_network_devices(

    )
    return endpoint_result


@pytest.mark.compliance
def test_get_trial_details_for_bugs_detection_on_network_devices_default_val(api, validator):
    try:
        assert is_valid_get_trial_details_for_bugs_detection_on_network_devices(
            validator,
            get_trial_details_for_bugs_detection_on_network_devices_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_triggers_a_bugs_scan_for_the_supported_network_devices(json_schema_validate, obj):
    json_schema_validate('jsd_37b6c0f7132f5a1485b7b564818354d8_v2_3_7_9').validate(obj)
    return True


def triggers_a_bugs_scan_for_the_supported_network_devices(api):
    endpoint_result = api.compliance.triggers_a_bugs_scan_for_the_supported_network_devices(
        active_validation=True,
        failed_devices_only=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.compliance
def test_triggers_a_bugs_scan_for_the_supported_network_devices(api, validator):
    try:
        assert is_valid_triggers_a_bugs_scan_for_the_supported_network_devices(
            validator,
            triggers_a_bugs_scan_for_the_supported_network_devices(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def triggers_a_bugs_scan_for_the_supported_network_devices_default_val(api):
    endpoint_result = api.compliance.triggers_a_bugs_scan_for_the_supported_network_devices(
        active_validation=True,
        failed_devices_only=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.compliance
def test_triggers_a_bugs_scan_for_the_supported_network_devices_default_val(api, validator):
    try:
        assert is_valid_triggers_a_bugs_scan_for_the_supported_network_devices(
            validator,
            triggers_a_bugs_scan_for_the_supported_network_devices_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_security_advisories_affecting_the_network_devices(json_schema_validate, obj):
    json_schema_validate('jsd_aef04c74f2745a6ca3960d6c466856cf_v2_3_7_9').validate(obj)
    return True


def get_security_advisories_affecting_the_network_devices(api):
    endpoint_result = api.compliance.get_security_advisories_affecting_the_network_devices(
        cvss_base_score='string',
        device_count=0,
        id='string',
        limit=0,
        offset=0,
        order='string',
        security_impact_rating='string',
        sort_by='string'
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_security_advisories_affecting_the_network_devices(api, validator):
    try:
        assert is_valid_get_security_advisories_affecting_the_network_devices(
            validator,
            get_security_advisories_affecting_the_network_devices(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_security_advisories_affecting_the_network_devices_default_val(api):
    endpoint_result = api.compliance.get_security_advisories_affecting_the_network_devices(
        cvss_base_score=None,
        device_count=None,
        id=None,
        limit=None,
        offset=None,
        order=None,
        security_impact_rating=None,
        sort_by=None
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_security_advisories_affecting_the_network_devices_default_val(api, validator):
    try:
        assert is_valid_get_security_advisories_affecting_the_network_devices(
            validator,
            get_security_advisories_affecting_the_network_devices_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_count_of_security_advisories_affecting_the_network_devices(json_schema_validate, obj):
    json_schema_validate('jsd_a0ee1bc9fe825b49aaf57eb14b4c90cf_v2_3_7_9').validate(obj)
    return True


def get_count_of_security_advisories_affecting_the_network_devices(api):
    endpoint_result = api.compliance.get_count_of_security_advisories_affecting_the_network_devices(
        cvss_base_score='string',
        device_count=0,
        id='string',
        security_impact_rating='string'
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_count_of_security_advisories_affecting_the_network_devices(api, validator):
    try:
        assert is_valid_get_count_of_security_advisories_affecting_the_network_devices(
            validator,
            get_count_of_security_advisories_affecting_the_network_devices(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_count_of_security_advisories_affecting_the_network_devices_default_val(api):
    endpoint_result = api.compliance.get_count_of_security_advisories_affecting_the_network_devices(
        cvss_base_score=None,
        device_count=None,
        id=None,
        security_impact_rating=None
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_count_of_security_advisories_affecting_the_network_devices_default_val(api, validator):
    try:
        assert is_valid_get_count_of_security_advisories_affecting_the_network_devices(
            validator,
            get_count_of_security_advisories_affecting_the_network_devices_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_security_advisory_affecting_the_network_devices_by_id(json_schema_validate, obj):
    json_schema_validate('jsd_37724dca392c51998fec3821dfb312de_v2_3_7_9').validate(obj)
    return True


def get_security_advisory_affecting_the_network_devices_by_id(api):
    endpoint_result = api.compliance.get_security_advisory_affecting_the_network_devices_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_security_advisory_affecting_the_network_devices_by_id(api, validator):
    try:
        assert is_valid_get_security_advisory_affecting_the_network_devices_by_id(
            validator,
            get_security_advisory_affecting_the_network_devices_by_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_security_advisory_affecting_the_network_devices_by_id_default_val(api):
    endpoint_result = api.compliance.get_security_advisory_affecting_the_network_devices_by_id(
        id='string'
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_security_advisory_affecting_the_network_devices_by_id_default_val(api, validator):
    try:
        assert is_valid_get_security_advisory_affecting_the_network_devices_by_id(
            validator,
            get_security_advisory_affecting_the_network_devices_by_id_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_security_advisory_network_devices_for_the_security_advisory(json_schema_validate, obj):
    json_schema_validate('jsd_d14f6e201c475f33a92d0222d76d40df_v2_3_7_9').validate(obj)
    return True


def get_security_advisory_network_devices_for_the_security_advisory(api):
    endpoint_result = api.compliance.get_security_advisory_network_devices_for_the_security_advisory(
        id='string',
        limit=0,
        network_device_id='string',
        offset=0,
        order='string',
        scan_mode='string',
        scan_status='string',
        sort_by='string'
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_security_advisory_network_devices_for_the_security_advisory(api, validator):
    try:
        assert is_valid_get_security_advisory_network_devices_for_the_security_advisory(
            validator,
            get_security_advisory_network_devices_for_the_security_advisory(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_security_advisory_network_devices_for_the_security_advisory_default_val(api):
    endpoint_result = api.compliance.get_security_advisory_network_devices_for_the_security_advisory(
        id='string',
        limit=None,
        network_device_id=None,
        offset=None,
        order=None,
        scan_mode=None,
        scan_status=None,
        sort_by=None
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_security_advisory_network_devices_for_the_security_advisory_default_val(api, validator):
    try:
        assert is_valid_get_security_advisory_network_devices_for_the_security_advisory(
            validator,
            get_security_advisory_network_devices_for_the_security_advisory_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_count_of_security_advisory_network_devices_for_the_security_advisory(json_schema_validate, obj):
    json_schema_validate('jsd_3d5fcf338dd95610a4a65c77888b8ed4_v2_3_7_9').validate(obj)
    return True


def get_count_of_security_advisory_network_devices_for_the_security_advisory(api):
    endpoint_result = api.compliance.get_count_of_security_advisory_network_devices_for_the_security_advisory(
        id='string',
        network_device_id='string',
        scan_mode='string',
        scan_status='string'
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_count_of_security_advisory_network_devices_for_the_security_advisory(api, validator):
    try:
        assert is_valid_get_count_of_security_advisory_network_devices_for_the_security_advisory(
            validator,
            get_count_of_security_advisory_network_devices_for_the_security_advisory(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_count_of_security_advisory_network_devices_for_the_security_advisory_default_val(api):
    endpoint_result = api.compliance.get_count_of_security_advisory_network_devices_for_the_security_advisory(
        id='string',
        network_device_id=None,
        scan_mode=None,
        scan_status=None
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_count_of_security_advisory_network_devices_for_the_security_advisory_default_val(api, validator):
    try:
        assert is_valid_get_count_of_security_advisory_network_devices_for_the_security_advisory(
            validator,
            get_count_of_security_advisory_network_devices_for_the_security_advisory_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_security_advisory_network_device_for_the_security_advisory_by_network_device_id(json_schema_validate, obj):
    json_schema_validate('jsd_60544cb8be1c50ca9f2fe769cd27b2da_v2_3_7_9').validate(obj)
    return True


def get_security_advisory_network_device_for_the_security_advisory_by_network_device_id(api):
    endpoint_result = api.compliance.get_security_advisory_network_device_for_the_security_advisory_by_network_device_id(
        id='string',
        network_device_id='string'
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_security_advisory_network_device_for_the_security_advisory_by_network_device_id(api, validator):
    try:
        assert is_valid_get_security_advisory_network_device_for_the_security_advisory_by_network_device_id(
            validator,
            get_security_advisory_network_device_for_the_security_advisory_by_network_device_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_security_advisory_network_device_for_the_security_advisory_by_network_device_id_default_val(api):
    endpoint_result = api.compliance.get_security_advisory_network_device_for_the_security_advisory_by_network_device_id(
        id='string',
        network_device_id='string'
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_security_advisory_network_device_for_the_security_advisory_by_network_device_id_default_val(api, validator):
    try:
        assert is_valid_get_security_advisory_network_device_for_the_security_advisory_by_network_device_id(
            validator,
            get_security_advisory_network_device_for_the_security_advisory_by_network_device_id_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_security_advisory_network_devices(json_schema_validate, obj):
    json_schema_validate('jsd_60b210c3633d5cfe8127056abae805c7_v2_3_7_9').validate(obj)
    return True


def get_security_advisory_network_devices(api):
    endpoint_result = api.compliance.get_security_advisory_network_devices(
        advisory_count='string',
        limit=0,
        network_device_id='string',
        offset=0,
        order='string',
        scan_mode='string',
        scan_status='string',
        sort_by='string'
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_security_advisory_network_devices(api, validator):
    try:
        assert is_valid_get_security_advisory_network_devices(
            validator,
            get_security_advisory_network_devices(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_security_advisory_network_devices_default_val(api):
    endpoint_result = api.compliance.get_security_advisory_network_devices(
        advisory_count=None,
        limit=None,
        network_device_id=None,
        offset=None,
        order=None,
        scan_mode=None,
        scan_status=None,
        sort_by=None
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_security_advisory_network_devices_default_val(api, validator):
    try:
        assert is_valid_get_security_advisory_network_devices(
            validator,
            get_security_advisory_network_devices_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_count_of_security_advisory_network_devices(json_schema_validate, obj):
    json_schema_validate('jsd_9eb1f5f93d0d549cbf99e032a73db16d_v2_3_7_9').validate(obj)
    return True


def get_count_of_security_advisory_network_devices(api):
    endpoint_result = api.compliance.get_count_of_security_advisory_network_devices(
        advisory_count=0,
        network_device_id='string',
        scan_mode='string',
        scan_status='string'
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_count_of_security_advisory_network_devices(api, validator):
    try:
        assert is_valid_get_count_of_security_advisory_network_devices(
            validator,
            get_count_of_security_advisory_network_devices(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_count_of_security_advisory_network_devices_default_val(api):
    endpoint_result = api.compliance.get_count_of_security_advisory_network_devices(
        advisory_count=None,
        network_device_id=None,
        scan_mode=None,
        scan_status=None
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_count_of_security_advisory_network_devices_default_val(api, validator):
    try:
        assert is_valid_get_count_of_security_advisory_network_devices(
            validator,
            get_count_of_security_advisory_network_devices_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_security_advisory_network_device_by_network_device_id(json_schema_validate, obj):
    json_schema_validate('jsd_e22988bedfbb5202b1bab7e811d56f53_v2_3_7_9').validate(obj)
    return True


def get_security_advisory_network_device_by_network_device_id(api):
    endpoint_result = api.compliance.get_security_advisory_network_device_by_network_device_id(
        network_device_id='string'
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_security_advisory_network_device_by_network_device_id(api, validator):
    try:
        assert is_valid_get_security_advisory_network_device_by_network_device_id(
            validator,
            get_security_advisory_network_device_by_network_device_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_security_advisory_network_device_by_network_device_id_default_val(api):
    endpoint_result = api.compliance.get_security_advisory_network_device_by_network_device_id(
        network_device_id='string'
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_security_advisory_network_device_by_network_device_id_default_val(api, validator):
    try:
        assert is_valid_get_security_advisory_network_device_by_network_device_id(
            validator,
            get_security_advisory_network_device_by_network_device_id_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_security_advisories_affecting_the_network_device(json_schema_validate, obj):
    json_schema_validate('jsd_74c12818ede552109f463d18c23a5a13_v2_3_7_9').validate(obj)
    return True


def get_security_advisories_affecting_the_network_device(api):
    endpoint_result = api.compliance.get_security_advisories_affecting_the_network_device(
        cvss_base_score='string',
        id='string',
        limit=0,
        network_device_id='string',
        offset=0,
        order='string',
        security_impact_rating='string',
        sort_by='string'
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_security_advisories_affecting_the_network_device(api, validator):
    try:
        assert is_valid_get_security_advisories_affecting_the_network_device(
            validator,
            get_security_advisories_affecting_the_network_device(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_security_advisories_affecting_the_network_device_default_val(api):
    endpoint_result = api.compliance.get_security_advisories_affecting_the_network_device(
        cvss_base_score=None,
        id=None,
        limit=None,
        network_device_id='string',
        offset=None,
        order=None,
        security_impact_rating=None,
        sort_by=None
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_security_advisories_affecting_the_network_device_default_val(api, validator):
    try:
        assert is_valid_get_security_advisories_affecting_the_network_device(
            validator,
            get_security_advisories_affecting_the_network_device_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_count_of_security_advisories_affecting_the_network_device(json_schema_validate, obj):
    json_schema_validate('jsd_a12932efe27956de8c356e40e959d6c2_v2_3_7_9').validate(obj)
    return True


def get_count_of_security_advisories_affecting_the_network_device(api):
    endpoint_result = api.compliance.get_count_of_security_advisories_affecting_the_network_device(
        cvss_base_score='string',
        id='string',
        network_device_id='string',
        security_impact_rating='string'
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_count_of_security_advisories_affecting_the_network_device(api, validator):
    try:
        assert is_valid_get_count_of_security_advisories_affecting_the_network_device(
            validator,
            get_count_of_security_advisories_affecting_the_network_device(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_count_of_security_advisories_affecting_the_network_device_default_val(api):
    endpoint_result = api.compliance.get_count_of_security_advisories_affecting_the_network_device(
        cvss_base_score=None,
        id=None,
        network_device_id='string',
        security_impact_rating=None
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_count_of_security_advisories_affecting_the_network_device_default_val(api, validator):
    try:
        assert is_valid_get_count_of_security_advisories_affecting_the_network_device(
            validator,
            get_count_of_security_advisories_affecting_the_network_device_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_security_advisory_affecting_the_network_device_by_device_id_and_advisory_id(json_schema_validate, obj):
    json_schema_validate('jsd_fc34a3eb64405e08b65fb830f2c1c05c_v2_3_7_9').validate(obj)
    return True


def get_security_advisory_affecting_the_network_device_by_device_id_and_advisory_id(api):
    endpoint_result = api.compliance.get_security_advisory_affecting_the_network_device_by_device_id_and_advisory_id(
        id='string',
        network_device_id='string'
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_security_advisory_affecting_the_network_device_by_device_id_and_advisory_id(api, validator):
    try:
        assert is_valid_get_security_advisory_affecting_the_network_device_by_device_id_and_advisory_id(
            validator,
            get_security_advisory_affecting_the_network_device_by_device_id_and_advisory_id(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_security_advisory_affecting_the_network_device_by_device_id_and_advisory_id_default_val(api):
    endpoint_result = api.compliance.get_security_advisory_affecting_the_network_device_by_device_id_and_advisory_id(
        id='string',
        network_device_id='string'
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_security_advisory_affecting_the_network_device_by_device_id_and_advisory_id_default_val(api, validator):
    try:
        assert is_valid_get_security_advisory_affecting_the_network_device_by_device_id_and_advisory_id(
            validator,
            get_security_advisory_affecting_the_network_device_by_device_id_and_advisory_id_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_security_advisories_results_trend_over_time(json_schema_validate, obj):
    json_schema_validate('jsd_0c60e785a6915253b715d9416e684132_v2_3_7_9').validate(obj)
    return True


def get_security_advisories_results_trend_over_time(api):
    endpoint_result = api.compliance.get_security_advisories_results_trend_over_time(
        limit=0,
        offset=0,
        scan_time=0
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_security_advisories_results_trend_over_time(api, validator):
    try:
        assert is_valid_get_security_advisories_results_trend_over_time(
            validator,
            get_security_advisories_results_trend_over_time(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_security_advisories_results_trend_over_time_default_val(api):
    endpoint_result = api.compliance.get_security_advisories_results_trend_over_time(
        limit=None,
        offset=None,
        scan_time=None
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_security_advisories_results_trend_over_time_default_val(api, validator):
    try:
        assert is_valid_get_security_advisories_results_trend_over_time(
            validator,
            get_security_advisories_results_trend_over_time_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_count_of_security_advisories_results_trend_over_time(json_schema_validate, obj):
    json_schema_validate('jsd_7259f083e6be591181051e43aebe7c7d_v2_3_7_9').validate(obj)
    return True


def get_count_of_security_advisories_results_trend_over_time(api):
    endpoint_result = api.compliance.get_count_of_security_advisories_results_trend_over_time(
        scan_time=0
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_count_of_security_advisories_results_trend_over_time(api, validator):
    try:
        assert is_valid_get_count_of_security_advisories_results_trend_over_time(
            validator,
            get_count_of_security_advisories_results_trend_over_time(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_count_of_security_advisories_results_trend_over_time_default_val(api):
    endpoint_result = api.compliance.get_count_of_security_advisories_results_trend_over_time(
        scan_time=None
    )
    return endpoint_result


@pytest.mark.compliance
def test_get_count_of_security_advisories_results_trend_over_time_default_val(api, validator):
    try:
        assert is_valid_get_count_of_security_advisories_results_trend_over_time(
            validator,
            get_count_of_security_advisories_results_trend_over_time_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_trial_details_for_security_advisories_detection_on_network_devices(json_schema_validate, obj):
    json_schema_validate('jsd_fe4fd333ec815ec283443c490bde2741_v2_3_7_9').validate(obj)
    return True


def get_trial_details_for_security_advisories_detection_on_network_devices(api):
    endpoint_result = api.compliance.get_trial_details_for_security_advisories_detection_on_network_devices(

    )
    return endpoint_result


@pytest.mark.compliance
def test_get_trial_details_for_security_advisories_detection_on_network_devices(api, validator):
    try:
        assert is_valid_get_trial_details_for_security_advisories_detection_on_network_devices(
            validator,
            get_trial_details_for_security_advisories_detection_on_network_devices(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_trial_details_for_security_advisories_detection_on_network_devices_default_val(api):
    endpoint_result = api.compliance.get_trial_details_for_security_advisories_detection_on_network_devices(

    )
    return endpoint_result


@pytest.mark.compliance
def test_get_trial_details_for_security_advisories_detection_on_network_devices_default_val(api, validator):
    try:
        assert is_valid_get_trial_details_for_security_advisories_detection_on_network_devices(
            validator,
            get_trial_details_for_security_advisories_detection_on_network_devices_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_creates_a_trial_for_security_advisories_detection_on_network_devices(json_schema_validate, obj):
    json_schema_validate('jsd_84b209c580ed5c0aaf4c978f4dfc00bd_v2_3_7_9').validate(obj)
    return True


def creates_a_trial_for_security_advisories_detection_on_network_devices(api):
    endpoint_result = api.compliance.creates_a_trial_for_security_advisories_detection_on_network_devices(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.compliance
def test_creates_a_trial_for_security_advisories_detection_on_network_devices(api, validator):
    try:
        assert is_valid_creates_a_trial_for_security_advisories_detection_on_network_devices(
            validator,
            creates_a_trial_for_security_advisories_detection_on_network_devices(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def creates_a_trial_for_security_advisories_detection_on_network_devices_default_val(api):
    endpoint_result = api.compliance.creates_a_trial_for_security_advisories_detection_on_network_devices(
        active_validation=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.compliance
def test_creates_a_trial_for_security_advisories_detection_on_network_devices_default_val(api, validator):
    try:
        assert is_valid_creates_a_trial_for_security_advisories_detection_on_network_devices(
            validator,
            creates_a_trial_for_security_advisories_detection_on_network_devices_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_triggers_a_security_advisories_scan_for_the_supported_network_devices(json_schema_validate, obj):
    json_schema_validate('jsd_cce0f5e813955eabb3c736d3b5952341_v2_3_7_9').validate(obj)
    return True


def triggers_a_security_advisories_scan_for_the_supported_network_devices(api):
    endpoint_result = api.compliance.triggers_a_security_advisories_scan_for_the_supported_network_devices(
        active_validation=True,
        failed_devices_only=True,
        payload=None
    )
    return endpoint_result


@pytest.mark.compliance
def test_triggers_a_security_advisories_scan_for_the_supported_network_devices(api, validator):
    try:
        assert is_valid_triggers_a_security_advisories_scan_for_the_supported_network_devices(
            validator,
            triggers_a_security_advisories_scan_for_the_supported_network_devices(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def triggers_a_security_advisories_scan_for_the_supported_network_devices_default_val(api):
    endpoint_result = api.compliance.triggers_a_security_advisories_scan_for_the_supported_network_devices(
        active_validation=True,
        failed_devices_only=None,
        payload=None
    )
    return endpoint_result


@pytest.mark.compliance
def test_triggers_a_security_advisories_scan_for_the_supported_network_devices_default_val(api, validator):
    try:
        assert is_valid_triggers_a_security_advisories_scan_for_the_supported_network_devices(
            validator,
            triggers_a_security_advisories_scan_for_the_supported_network_devices_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e

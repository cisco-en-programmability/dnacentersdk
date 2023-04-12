# -*- coding: utf-8 -*-
"""DNACenterAPI platform API fixtures and tests.

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
import pytest
from fastjsonschema.exceptions import JsonSchemaException
from dnacentersdk.exceptions import MalformedRequest
from tests.environment import DNA_CENTER_VERSION

pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '2.3.5.3', reason='version does not match')


def is_valid_cisco_dna_center_packages_summary(json_schema_validate, obj):
    json_schema_validate('jsd_0c3bdcd996dd5d988d0d77ce8f732014_v2_3_5_3').validate(obj)
    return True


def cisco_dna_center_packages_summary(api):
    endpoint_result = api.platform.cisco_dna_center_packages_summary(

    )
    return endpoint_result


@pytest.mark.platform
def test_cisco_dna_center_packages_summary(api, validator):
    try:
        assert is_valid_cisco_dna_center_packages_summary(
            validator,
            cisco_dna_center_packages_summary(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def cisco_dna_center_packages_summary_default_val(api):
    endpoint_result = api.platform.cisco_dna_center_packages_summary(

    )
    return endpoint_result


@pytest.mark.platform
def test_cisco_dna_center_packages_summary_default_val(api, validator):
    try:
        assert is_valid_cisco_dna_center_packages_summary(
            validator,
            cisco_dna_center_packages_summary_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_release_summary(json_schema_validate, obj):
    json_schema_validate('jsd_63206c9b144b5dc2ba26e51798f8bede_v2_3_5_3').validate(obj)
    return True


def release_summary(api):
    endpoint_result = api.platform.release_summary(

    )
    return endpoint_result


@pytest.mark.platform
def test_release_summary(api, validator):
    try:
        assert is_valid_release_summary(
            validator,
            release_summary(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def release_summary_default_val(api):
    endpoint_result = api.platform.release_summary(

    )
    return endpoint_result


@pytest.mark.platform
def test_release_summary_default_val(api, validator):
    try:
        assert is_valid_release_summary(
            validator,
            release_summary_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_nodes_configuration_summary(json_schema_validate, obj):
    json_schema_validate('jsd_0f0c26c266e552d6b0f1f68da8e60e16_v2_3_5_3').validate(obj)
    return True


def nodes_configuration_summary(api):
    endpoint_result = api.platform.nodes_configuration_summary(

    )
    return endpoint_result


@pytest.mark.platform
def test_nodes_configuration_summary(api, validator):
    try:
        assert is_valid_nodes_configuration_summary(
            validator,
            nodes_configuration_summary(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def nodes_configuration_summary_default_val(api):
    endpoint_result = api.platform.nodes_configuration_summary(

    )
    return endpoint_result


@pytest.mark.platform
def test_nodes_configuration_summary_default_val(api, validator):
    try:
        assert is_valid_nodes_configuration_summary(
            validator,
            nodes_configuration_summary_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e

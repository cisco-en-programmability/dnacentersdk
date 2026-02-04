# -*- coding: utf-8 -*-
"""DNACenterAPI know_your_network API fixtures and tests.

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

pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '3.1.6.0', reason='version does not match')


def is_valid_get_energy_summary_analytics(json_schema_validate, obj):
    json_schema_validate('jsd_d0b2cc705afb536fab6fd0848baa73c0_v3_1_6_0').validate(obj)
    return True


def get_energy_summary_analytics(api):
    endpoint_result = api.know_your_network.get_energy_summary_analytics(
        active_validation=True,
        aggregateAttributes=[{'name': 'string', 'function': 'string'}],
        attributes=['string'],
        endTime=0,
        filters=[{'logicalOperator': 'string', 'filters': [{'key': 'string', 'operator': 'string', 'value': ['string']}]}],
        groupBy=['string'],
        page={'limit': 0, 'offset': 0, 'sortBy': [{'name': 'string', 'order': 'string', 'function': 'string'}]},
        payload=None,
        startTime=0
    )
    return endpoint_result


@pytest.mark.know_your_network
def test_get_energy_summary_analytics(api, validator):
    try:
        assert is_valid_get_energy_summary_analytics(
            validator,
            get_energy_summary_analytics(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_energy_summary_analytics_default_val(api):
    endpoint_result = api.know_your_network.get_energy_summary_analytics(
        active_validation=True,
        aggregateAttributes=None,
        attributes=None,
        endTime=None,
        filters=None,
        groupBy=None,
        page=None,
        payload=None,
        startTime=None
    )
    return endpoint_result


@pytest.mark.know_your_network
def test_get_energy_summary_analytics_default_val(api, validator):
    try:
        assert is_valid_get_energy_summary_analytics(
            validator,
            get_energy_summary_analytics_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_get_energy_trend_analytics(json_schema_validate, obj):
    json_schema_validate('jsd_568503de4a255bc6849a7c9cec69f13c_v3_1_6_0').validate(obj)
    return True


def get_energy_trend_analytics(api):
    endpoint_result = api.know_your_network.get_energy_trend_analytics(
        active_validation=True,
        aggregateAttributes=[{'name': 'string', 'function': 'string'}],
        attributes=['string'],
        endTime=0,
        filters=[{'logicalOperator': 'string', 'filters': [{'key': 'string', 'operator': 'string', 'value': ['string']}]}],
        groupBy=['string'],
        page={'limit': 0, 'offset': 0, 'timestampOrder': 'string'},
        payload=None,
        startTime=0
    )
    return endpoint_result


@pytest.mark.know_your_network
def test_get_energy_trend_analytics(api, validator):
    try:
        assert is_valid_get_energy_trend_analytics(
            validator,
            get_energy_trend_analytics(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_energy_trend_analytics_default_val(api):
    endpoint_result = api.know_your_network.get_energy_trend_analytics(
        active_validation=True,
        aggregateAttributes=None,
        attributes=None,
        endTime=None,
        filters=None,
        groupBy=None,
        page=None,
        payload=None,
        startTime=None
    )
    return endpoint_result


@pytest.mark.know_your_network
def test_get_energy_trend_analytics_default_val(api, validator):
    try:
        assert is_valid_get_energy_trend_analytics(
            validator,
            get_energy_trend_analytics_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e

# -*- coding: utf-8 -*-
"""DNACenterAPI issues API fixtures and tests.

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

pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '2.3.3.0', reason='version does not match')


def is_valid_get_issue_enrichment_details(json_schema_validate, obj):
    json_schema_validate('jsd_02f2f039811951c0af53e3381ae91225_v2_3_3_0').validate(obj)
    return True


def get_issue_enrichment_details(api):
    endpoint_result = api.issues.get_issue_enrichment_details(

    )
    return endpoint_result


@pytest.mark.issues
def test_get_issue_enrichment_details(api, validator):
    try:
        assert is_valid_get_issue_enrichment_details(
            validator,
            get_issue_enrichment_details(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def get_issue_enrichment_details_default_val(api):
    endpoint_result = api.issues.get_issue_enrichment_details(

    )
    return endpoint_result


@pytest.mark.issues
def test_get_issue_enrichment_details_default_val(api, validator):
    try:
        assert is_valid_get_issue_enrichment_details(
            validator,
            get_issue_enrichment_details_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e


def is_valid_issues(json_schema_validate, obj):
    json_schema_validate('jsd_759522aaef3b519ba8b9fb2cbf43b985_v2_3_3_0').validate(obj)
    return True


def issues(api):
    endpoint_result = api.issues.issues(
        ai_driven='string',
        device_id='string',
        end_time=0,
        issue_status='string',
        mac_address='string',
        priority='string',
        site_id='string',
        start_time=0
    )
    return endpoint_result


@pytest.mark.issues
def test_issues(api, validator):
    try:
        assert is_valid_issues(
            validator,
            issues(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest)):
            print(original_e)
            raise original_e


def issues_default_val(api):
    endpoint_result = api.issues.issues(
        ai_driven=None,
        device_id=None,
        end_time=None,
        issue_status=None,
        mac_address=None,
        priority=None,
        site_id=None,
        start_time=None
    )
    return endpoint_result


@pytest.mark.issues
def test_issues_default_val(api, validator):
    try:
        assert is_valid_issues(
            validator,
            issues_default_val(api)
        )
    except Exception as original_e:
        with pytest.raises((JsonSchemaException, MalformedRequest, TypeError)):
            raise original_e

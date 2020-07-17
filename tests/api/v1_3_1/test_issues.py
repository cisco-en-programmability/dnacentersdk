# -*- coding: utf-8 -*-
"""DNACenterAPI issues API fixtures and tests.

Copyright (c) 2019 Cisco and/or its affiliates.

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
from tests.environment import DNA_CENTER_VERSION
from tests.models.schema_validator import json_schema_validate


pytestmark = pytest.mark.skipif(DNA_CENTER_VERSION != '1.3.1', reason='version does not match')


def is_valid_get_issue_enrichment_details(obj):
    json_schema_validate('jsd_868439bb4e89a6e4_v1_3_1').validate(obj)
    return True


def get_issue_enrichment_details(api):
    endpoint_result = api.issues.get_issue_enrichment_details(

    )
    return endpoint_result


@pytest.mark.issues
def test_get_issue_enrichment_details(api):
    assert is_valid_get_issue_enrichment_details(
        get_issue_enrichment_details(api)
    )


def get_issue_enrichment_details_default(api):
    endpoint_result = api.issues.get_issue_enrichment_details(

    )
    return endpoint_result


@pytest.mark.issues
def test_get_issue_enrichment_details_default(api):
    try:
        assert is_valid_get_issue_enrichment_details(
            get_issue_enrichment_details_default(api)
        )
    except Exception as original_e:
        with pytest.raises(TypeError, match="but instead we received None"):
            raise original_e

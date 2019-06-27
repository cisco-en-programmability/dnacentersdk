# -*- coding: utf-8 -*-
"""DNACenterAPI template_programmer API fixtures and tests.

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
import dnacentersdk




# 01b0-9a25-4b9a-b259
def is_valid_gets_the_templates_available(obj):
    some_keys = [  ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


def gets_the_templates_available(api):
    endpoint_result = api.template_programmer.gets_the_templates_available( param_filter_conflicting_templates = None, param_product_family = None, param_product_series = None, param_product_type = None, param_project_id = None, param_software_type = None, param_software_version = None, payload = '' )
    return endpoint_result


def test_gets_the_templates_available(api):
    assert is_valid_gets_the_templates_available(gets_the_templates_available(api))


# 109d-1b4f-4289-aecd
def is_valid_get_projects(obj):
    return len(obj) > 0 and all([ item for item in obj ])


def get_projects(api):
    endpoint_result = api.template_programmer.get_projects( param_name = None, payload = '' )
    return endpoint_result


def test_get_projects(api):
    assert is_valid_get_projects(get_projects(api))


# 83a3-b940-4cb8-8787
def is_valid_get_template_details(obj):
    some_keys = [ 'author', 'composite', 'containingTemplates', 'createTime' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


def get_template_details(api):
    endpoint_result = api.template_programmer.get_template_details( path_param_template_id = gets_the_templates_available(api)[0].templateId, param_latest_version = None, payload = '' )
    return endpoint_result


def test_get_template_details(api):
    assert is_valid_get_template_details(get_template_details(api))


# c8bf-6b65-414a-9bc7
def is_valid_get_template_versions(obj):
    return len(obj) > 0 and all([ item for item in obj ])


def get_template_versions(api):
    endpoint_result = api.template_programmer.get_template_versions( path_param_template_id = gets_the_templates_available(api)[0].templateId, payload = '' )
    return endpoint_result


def test_get_template_versions(api):
    assert is_valid_get_template_versions(get_template_versions(api))


# 9c9a-7857-41cb-b41f
def is_valid_get_template_deployment_status(obj):
    some_keys = [ 'deploymentId', 'deploymentName', 'devices', 'duration' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


def get_template_deployment_status(api):
    endpoint_result = api.template_programmer.get_template_deployment_status( path_param_deployment_id = '', payload = '' )
    return endpoint_result


@pytest.mark.skip(reason="no way of currently testing this")
def test_get_template_deployment_status(api):
    assert is_valid_get_template_deployment_status(get_template_deployment_status(api))


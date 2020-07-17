# -*- coding: utf-8 -*-
"""DNACenterAPI custom_caller API fixtures and tests.

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


@pytest.fixture(scope="session")
def custom_caller(api):
    api.custom_caller.add_api('get_global_credentials',
                              lambda: api.custom_caller.call_api(
                                  'GET',
                                  '/dna/intent/api/v1/global-credential',
                                  params={
                                      'credentialSubType': 'NETCONF'
                                  })
                              )
    api.custom_caller.add_api('create_netconf_credentials',
                              lambda: api.custom_caller.call_api(
                                  'POST',
                                  '/dna/intent/api/v1/global-credential/netconf',
                                  json=[{
                                      "netconfPort": "65533"
                                  }])
                              )
    api.custom_caller.add_api('delete_global_credentials_by_id',
                              lambda global_credential_id:
                                  api.custom_caller.call_api(
                                      'DELETE',
                                      '/dna/intent/api/v1/global-credential/${globalCredentialId}',
                                      path_params={
                                          'globalCredentialId': global_credential_id,
                                      })
                              )
    return api.custom_caller


@pytest.mark.custom_caller
def test_custom_caller(custom_caller):
    original_credentials = custom_caller.get_global_credentials().response
    assert original_credentials is not None
    create_response = custom_caller.create_netconf_credentials()
    assert create_response is not None
    delete_response = custom_caller.delete_global_credentials_by_id('string')
    assert delete_response is not None
    credentials_removed = custom_caller.get_global_credentials().response
    assert credentials_removed is not None

# authentication

import pytest
import dnacentersdk


def is_valid_authentication_api(obj):
    some_keys = [  ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_authentication_api(api):
    endpoint_result = api.authentication.authentication_api( username = 'devnetuser', password = 'Cisco123!')
    assert is_valid_authentication_api(endpoint_result)


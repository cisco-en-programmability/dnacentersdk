# authentication

import pytest
import dnacentersdk


# ac8a-e94c-4e69-a09d
def is_valid_authentication_api(obj):
    some_keys = [  ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])


# ac8a-e94c-4e69-a09d
def authentication_api(api):
    endpoint_result = api.authentication.authentication_api( username = 'devnetuser', password = 'Cisco123!' )
    return endpoint_result

# ac8a-e94c-4e69-a09d
def test_authentication_api(api):
    assert is_valid_authentication_api(authentication_api(api))


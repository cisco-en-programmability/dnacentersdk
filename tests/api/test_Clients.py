# clients

import pytest
import dnacentersdk


def is_valid_get_overall_client_health(obj):
    some_keys = [  ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

def test_get_overall_client_health(api):
    endpoint_result = api.clients.get_overall_client_health( param_timestamp = '1560376277')
    assert is_valid_get_overall_client_health(endpoint_result)


def is_valid_get_client_detail(obj):
    some_keys = [ 'detail', 'connectionInfo' ]
    return True if len(some_keys) == 0 else any([ obj.get(item) is not None for item in some_keys ])

@pytest.mark.skip(reason="no way of currently testing this")
def test_get_client_detail(api):
    endpoint_result = api.clients.get_client_detail( param_mac_address = '1c:36:bb:25:3e:12', param_timestamp = '1560376277')
    assert is_valid_get_client_detail(endpoint_result)


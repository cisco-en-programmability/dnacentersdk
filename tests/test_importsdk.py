import pytest


class TestImportSDK:
    """Set the sdk-level variables."""
    def setup(self, base_url):
        self.username = "username"
        self.password = "password"
        self.encoded_auth = "dXNlcm5hbWU6cGFzc3dvcmQ="
        self.base_url = base_url
        self.verify = False
        self.debug = True
        self.version = "2.3.3.0"


@pytest.fixture
def import_fixture(mock_dna_center_server, base_url):
    sdk_sample_values = TestImportSDK()
    sdk_sample_values.setup(base_url)
    return sdk_sample_values


@pytest.fixture
def reset_env_vars(monkeypatch):
    monkeypatch.delenv("DNA_CENTER_BASE_URL", raising=False)
    monkeypatch.delenv("DNA_CENTER_USERNAME", raising=False)
    monkeypatch.delenv("DNA_CENTER_PASSWORD", raising=False)
    monkeypatch.delenv("DNA_CENTER_ENCODED_AUTH", raising=False)


@pytest.mark.importsdk
def test_get_enviroment_before_import_1(monkeypatch, reset_env_vars, import_fixture):
    """Tests if the package gets the values of the env variables before import."""
    monkeypatch.setenv("DNA_CENTER_USERNAME", import_fixture.username)
    monkeypatch.setenv("DNA_CENTER_PASSWORD", import_fixture.password)
    monkeypatch.setenv("DNA_CENTER_BASE_URL", import_fixture.base_url)
    from dnacentersdk import DNACenterAPI
    DNACenterAPI(verify=import_fixture.verify, debug=import_fixture.debug)
    return True


@pytest.mark.importsdk
def test_get_enviroment_before_import_2(monkeypatch, reset_env_vars, import_fixture):
    """Tests if the package gets the values of the env variables before import."""
    monkeypatch.setenv("DNA_CENTER_ENCODED_AUTH", import_fixture.encoded_auth)
    monkeypatch.setenv("DNA_CENTER_BASE_URL", import_fixture.base_url)
    from dnacentersdk import DNACenterAPI
    DNACenterAPI(verify=import_fixture.verify, debug=import_fixture.debug)
    return True


@pytest.mark.importsdk
def test_get_enviroment_after_import_1(monkeypatch, reset_env_vars, import_fixture):
    """Tests if the package gets the values of the env variables after import."""
    from dnacentersdk import DNACenterAPI
    monkeypatch.setenv("DNA_CENTER_USERNAME", import_fixture.username)
    monkeypatch.setenv("DNA_CENTER_PASSWORD", import_fixture.password)
    monkeypatch.setenv("DNA_CENTER_BASE_URL", import_fixture.base_url)
    DNACenterAPI(verify=import_fixture.verify, debug=import_fixture.debug)
    return True


@pytest.mark.importsdk
def test_get_enviroment_after_import_2(monkeypatch, reset_env_vars, import_fixture):
    """Tests if the package gets the values of the env variables after import."""
    from dnacentersdk import DNACenterAPI
    monkeypatch.setenv("DNA_CENTER_ENCODED_AUTH", import_fixture.encoded_auth)
    monkeypatch.setenv("DNA_CENTER_BASE_URL", import_fixture.base_url)
    DNACenterAPI(verify=import_fixture.verify, debug=import_fixture.debug)
    return True


@pytest.mark.importsdk
def test_get_enviroment_exception_1(monkeypatch, reset_env_vars, import_fixture):
    """Remove part of the SECRET env vars and assert AccessTokenError is raised."""
    monkeypatch.setenv("DNA_CENTER_USERNAME", import_fixture.username)
    # missing password or encoded_auth
    monkeypatch.setenv("DNA_CENTER_BASE_URL", import_fixture.base_url)
    from dnacentersdk import DNACenterAPI, AccessTokenError
    with pytest.raises(AccessTokenError):
        DNACenterAPI(verify=import_fixture.verify, debug=import_fixture.debug)


@pytest.mark.importsdk
def test_get_enviroment_exception_2(monkeypatch, reset_env_vars, import_fixture):
    """Remove part of the SECRET env vars and assert AccessTokenError is raised."""
    # missing username or encoded_auth
    monkeypatch.setenv("DNA_CENTER_PASSWORD", import_fixture.password)
    monkeypatch.setenv("DNA_CENTER_BASE_URL", import_fixture.base_url)
    from dnacentersdk import DNACenterAPI, AccessTokenError
    with pytest.raises(AccessTokenError):
        DNACenterAPI(verify=import_fixture.verify, debug=import_fixture.debug)


@pytest.mark.importsdk
def test_get_enviroment_exception_3(monkeypatch, reset_env_vars, import_fixture):
    """Remove the SECRET env vars and assert AccessTokenError is raised."""
    # missing encoded_auth or (username and password)
    monkeypatch.setenv("DNA_CENTER_BASE_URL", import_fixture.base_url)
    from dnacentersdk import DNACenterAPI, AccessTokenError
    with pytest.raises(AccessTokenError):
        DNACenterAPI(verify=import_fixture.verify, debug=import_fixture.debug)

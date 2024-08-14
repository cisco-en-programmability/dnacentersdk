# -*- coding: utf-8 -*-
"""Package environment variables.

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

import os

#: name of the environment debug variable
DEBUG_ENVIRONMENT_VARIABLE = 'DNA_CENTER_DEBUG'

# DNA Center API version. Format: MAJOR.MINOR.PATCH
#: name of the environment version variable
VERSION_ENVIRONMENT_VARIABLE = 'DNA_CENTER_VERSION'

#: name of the environment username variable
USERNAME_ENVIRONMENT_VARIABLE = 'DNA_CENTER_USERNAME'

#: name of the environment password variable
PASSWORD_ENVIRONMENT_VARIABLE = 'DNA_CENTER_PASSWORD'

#: name of the environment encoded_auth variable
ENCODED_AUTH_ENVIRONMENT_VARIABLE = 'DNA_CENTER_ENCODED_AUTH'

#: name of the environment base_url variable
BASE_URL_ENVIRONMENT_VARIABLE = 'DNA_CENTER_BASE_URL'

#: name of the environment single_request_timeout variable
SINGLE_REQUEST_TIMEOUT_ENVIRONMENT_VARIABLE = \
    'DNA_CENTER_SINGLE_REQUEST_TIMEOUT'

#: name of the environment wait_on_rate_limit variable
WAIT_ON_RATE_LIMIT_ENVIRONMENT_VARIABLE = 'DNA_CENTER_WAIT_ON_RATE_LIMIT'

#: name of the environment verify variable
VERIFY_ENVIRONMENT_VARIABLE = 'DNA_CENTER_VERIFY'


def _is_bool(value):
    if isinstance(value, str):
        return 'true' in value.lower()
    else:
        return bool(value)


def _get_env_value(env_var, env_type, cast_func):
    env_var_value = os.getenv(env_var)
    if isinstance(env_var_value, env_type):
        return env_var_value
    elif env_var_value is not None:
        return cast_func(env_var_value)
    else:
        return env_var_value


def get_env_username():
    DNA_CENTER_USERNAME = os.getenv(USERNAME_ENVIRONMENT_VARIABLE)
    return DNA_CENTER_USERNAME


def get_env_password():
    DNA_CENTER_PASSWORD = os.getenv(PASSWORD_ENVIRONMENT_VARIABLE)
    return DNA_CENTER_PASSWORD


def get_env_encoded_auth():
    DNA_CENTER_ENCODED_AUTH = os.getenv(ENCODED_AUTH_ENVIRONMENT_VARIABLE)
    return DNA_CENTER_ENCODED_AUTH


def get_env_debug():
    DNA_CENTER_DEBUG = _get_env_value(
        DEBUG_ENVIRONMENT_VARIABLE,
        str, _is_bool)
    return DNA_CENTER_DEBUG


def get_env_version():
    DNA_CENTER_VERSION = _get_env_value(
        VERSION_ENVIRONMENT_VARIABLE, str, str)
    return DNA_CENTER_VERSION


def get_env_base_url():
    DNA_CENTER_BASE_URL = _get_env_value(
        BASE_URL_ENVIRONMENT_VARIABLE, str, str)
    return DNA_CENTER_BASE_URL


def get_env_single_request_timeout():
    DNA_CENTER_SINGLE_REQUEST_TIMEOUT = _get_env_value(
        SINGLE_REQUEST_TIMEOUT_ENVIRONMENT_VARIABLE,
        int, int)
    return DNA_CENTER_SINGLE_REQUEST_TIMEOUT


def get_env_wait_on_rate_limit():
    DNA_CENTER_WAIT_ON_RATE_LIMIT = _get_env_value(
        WAIT_ON_RATE_LIMIT_ENVIRONMENT_VARIABLE,
        bool, _is_bool)
    return DNA_CENTER_WAIT_ON_RATE_LIMIT


def get_env_verify():
    DNA_CENTER_VERIFY = _get_env_value(VERIFY_ENVIRONMENT_VARIABLE, bool, _is_bool)
    return DNA_CENTER_VERIFY

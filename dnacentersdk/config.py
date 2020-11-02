# -*- coding: utf-8 -*-
# Package configuration.

# Copyright (c) 2019-2020 Cisco and/or its affiliates.

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# Package Constants

#: **debug** default value.
DEFAULT_DEBUG = 'False'

#: **version** default value.
DEFAULT_VERSION = '2.1.2'

#: **base_url** default value.
DEFAULT_BASE_URL = 'https://sandboxdnac.cisco.com:443'

#: **single_request_timeout** default value.
#: Timeout (in seconds) for the RESTful HTTP requests.
DEFAULT_SINGLE_REQUEST_TIMEOUT = 60

#: **wait_on_rate_limit** default value.
#: Enables or disables automatic rate-limit handling.
DEFAULT_WAIT_ON_RATE_LIMIT = True

#: **verify** default value.
#: Controls whether to verify the server's TLS certificate or not.
DEFAULT_VERIFY = True

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

#: name of the environment verify variable
VERIFY_STRING_ENVIRONMENT_VARIABLE = 'DNA_CENTER_VERIFY_STRING'

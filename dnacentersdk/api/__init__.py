# -*- coding: utf-8 -*-
"""DNA Center API wrappers.

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

from past.types import basestring

from dnacentersdk.config import (
    DEFAULT_BASE_URL, DEFAULT_SINGLE_REQUEST_TIMEOUT,
    DEFAULT_WAIT_ON_RATE_LIMIT, DEFAULT_VERIFY,
)
from dnacentersdk.environment import (
    DNA_CENTER_USERNAME, DNA_CENTER_PASSWORD,
    DNA_CENTER_ENCODED_AUTH
)
from dnacentersdk.exceptions import AccessTokenError
from dnacentersdk.models.mydict import mydict_data_factory
from dnacentersdk.models.schema_validator import json_schema_validate
from dnacentersdk.restsession import RestSession
from dnacentersdk.utils import check_type

from .authentication import Authentication
from .template_programmer import TemplateProgrammer
from .tag import Tag
from .network_discovery import NetworkDiscovery
from .task import Task
from .command_runner import CommandRunner
from .file import File
from .path_trace import PathTrace
from .swim import Swim
from .pnp import Pnp
from .site_profile import SiteProfile
from .devices import Devices
from .sites import Sites
from .networks import Networks
from .clients import Clients
from .non_fabric_wireless import NonFabricWireless
from .fabric_wired import FabricWired


class DNACenterAPI(object):
    """DNA Center API wrapper.

    Creates a 'session' for all API calls through a created DNACenterAPI
    object.  The 'session' handles authentication, provides the needed headers,
    and checks all responses for error conditions.

    DNACenterAPI wraps all of the individual DNA Center APIs and represents
    them in a simple hierarchical structure.
    """

    def __init__(self, username=None,
                 password=None,
                 encoded_auth=None,
                 base_url=DEFAULT_BASE_URL,
                 single_request_timeout=DEFAULT_SINGLE_REQUEST_TIMEOUT,
                 wait_on_rate_limit=DEFAULT_WAIT_ON_RATE_LIMIT,
                 verify=DEFAULT_VERIFY,
                 object_factory=mydict_data_factory,
                 validator=json_schema_validate):
        """Create a new DNACenterAPI object.
        An access token is required to interact with the DNA Center APIs.
        This package supports two methods for you to generate the
        authorization token:

          1. Provide a encoded_auth value (username:password encoded in
          base 64). *This has priority over the following method*

          2. Provide username and password values.

        This package supports two methods for you to set those values:

          1. Provide the parameter. That is the encoded_auth or
          username and password parameters.

          2. If an argument is not supplied, the package checks for
          its environment variable counterpart. That is the
          DNA_CENTER_ENCODED_AUTH, DNA_CENTER_USERNAME,
          DNA_CENTER_PASSWORD.

        When not given enough parameters an AccessTokenError is raised.

        Args:
            base_url(basestring): The base URL to be prefixed to the
                individual API endpoint suffixes.
                Defaults to dnacentersdk.DEFAULT_BASE_URL.
            username(basestring): HTTP Basic Auth username.
            password(basestring): HTTP Basic Auth password.
            encoded_auth(basestring): HTTP Basic Auth base64 encoded string.
            single_request_timeout(int): Timeout (in seconds) for RESTful HTTP
                requests. Defaults to
                dnacentersdk.config.DEFAULT_SINGLE_REQUEST_TIMEOUT.
            wait_on_rate_limit(bool): Enables or disables automatic rate-limit
                handling. Defaults to
                dnacentersdk.config.DEFAULT_WAIT_ON_RATE_LIMIT.
            verify(bool,basestring): Controls whether we verify the server’s
                TLS certificate, or a string, in which case it must be a path
                to a CA bundle to use. Defaults to
                dnacentersdk.config.DEFAULT_VERIFY.
            object_factory(callable): The factory function to use to create
                Python objects from the returned DNA Center JSON data objects.
            validator(callable): The factory function to use to validate
                Python objects sent in the body of the request.

        Returns:
            DNACenterAPI: A new DNACenterAPI object.

        Raises:
            TypeError: If the parameter types are incorrect.
            AccessTokenError: If an access token is not provided via the
                access_token argument or an environment variable.

        """
        check_type(base_url, basestring)
        check_type(single_request_timeout, int)
        check_type(wait_on_rate_limit, bool)
        check_type(username, basestring, may_be_none=True)
        check_type(password, basestring, may_be_none=True)
        check_type(encoded_auth, basestring, may_be_none=True)
        check_type(verify, (bool, basestring), may_be_none=False)

        if username is None:
            username = DNA_CENTER_USERNAME

        if password is None:
            password = DNA_CENTER_PASSWORD

        if encoded_auth is None:
            encoded_auth = DNA_CENTER_ENCODED_AUTH

        # Init Authentication wrapper early to use for basicAuth requests
        self.authentication = Authentication(
            base_url, object_factory,
            single_request_timeout=single_request_timeout,
            verify=verify,
        )

        # Check if the user has provided the required basicAuth parameters
        if encoded_auth is None and (username is None or password is None):
            raise AccessTokenError(
                "You need an access token to interact with the DNA Center"
                " APIs. DNA Center uses HTTP Basic Auth to create an access"
                " token. You must provide the username and password or just"
                " the encoded_auth, either by setting each parameter or its"
                " environment variable counterpart ("
                "DNA_CENTER_USERNAME, DNA_CENTER_PASSWORD,"
                " DNA_CENTER_ENCODED_AUTH)."
            )

        def get_access_token():
            return self.authentication.authentication_api(
                username=username,
                password=password,
                encoded_auth=encoded_auth).Token

        # Create the API session
        # All of the API calls associated with a DNACenterAPI object will
        # leverage a single RESTful 'session' connecting to the DNA Center
        # cloud.
        self._session = RestSession(
            get_access_token=get_access_token,
            access_token=get_access_token(),
            base_url=base_url,
            single_request_timeout=single_request_timeout,
            wait_on_rate_limit=wait_on_rate_limit,
            verify=verify,
        )

        # API wrappers
        self.template_programmer = \
            TemplateProgrammer(self._session, object_factory, validator)
        self.tag = \
            Tag(self._session, object_factory, validator)
        self.network_discovery = \
            NetworkDiscovery(self._session, object_factory, validator)
        self.task = \
            Task(self._session, object_factory, validator)
        self.command_runner = \
            CommandRunner(self._session, object_factory, validator)
        self.file = \
            File(self._session, object_factory, validator)
        self.path_trace = \
            PathTrace(self._session, object_factory, validator)
        self.swim = \
            Swim(self._session, object_factory, validator)
        self.pnp = \
            Pnp(self._session, object_factory, validator)
        self.site_profile = \
            SiteProfile(self._session, object_factory, validator)
        self.devices = \
            Devices(self._session, object_factory, validator)
        self.sites = \
            Sites(self._session, object_factory, validator)
        self.networks = \
            Networks(self._session, object_factory, validator)
        self.clients = \
            Clients(self._session, object_factory, validator)
        self.non_fabric_wireless = \
            NonFabricWireless(self._session, object_factory, validator)
        self.fabric_wired = \
            FabricWired(self._session, object_factory, validator)

    @property
    def session(self):
        """The DNA Center API session."""
        return self._session

    @property
    def access_token(self):
        """The access token used for API calls to the DNA Center service."""
        return self._session.access_token

    @property
    def base_url(self):
        """The base URL prefixed to the individual API endpoint suffixes."""
        return self._session.base_url

    @property
    def single_request_timeout(self):
        """Timeout (in seconds) for an single HTTP request."""
        return self._session.single_request_timeout

    @property
    def wait_on_rate_limit(self):
        """Automatic rate-limit handling enabled / disabled."""
        return self._session.wait_on_rate_limit

    @property
    def verify(self):
        """The verify (TLS Certificate) for the API endpoints."""
        return self._session._verify

.. _Quickstart:

.. currentmodule:: dnacentersdk

==========
Quickstart
==========

*Dive in!*  ...to get started using the dnacentersdk package:

Make sure that you have:

* dnacentersdk :ref:`installed <Install>`
* dnacentersdk :ref:`upgraded to the latest version <Upgrade>`

Get your DNA Center Access Token
---------------------------------

To interact with the DNA Center APIs, you must have a **DNA Center Access Token**.
A DNA Center Access Token is how the DNA Center APIs validate access and identify the
requesting user.

As a `best practice`__, you can store your DNA 'credentials' as
an environment variables in your development or production environment. 

By default, dnacentersdk will look for the following environment variables to create new connection objects:

    * ``DNA_CENTER_DEBUG`` - Tells the SDK whether to log request and response information. Useful for debugging and seeing what is going on under the hood. Defaults to False.

    * ``DNA_CENTER_VERSION`` - DNA Center API version to use. Defaults to '1.3.0'.

    * ``DNA_CENTER_ENCODED_AUTH`` - It takes priority. It is the `username:password` encoded in base 64.
      For example 'ZGV2bmV0dXNlcjpDaXNjbzEyMyEK' which decoded is 'devnetuser:Cisco123!'

    * ``DNA_CENTER_USERNAME`` - HTTP Basic Auth username.

    * ``DNA_CENTER_PASSWORD`` - HTTP Basic Auth password.

    * ``DNA_CENTER_BASE_URL`` - The base URL to be prefixed to the individual API endpoint suffixes. Defaults to 'https://sandboxdnac2.cisco.com:443'.

    * ``DNA_CENTER_SINGLE_REQUEST_TIMEOUT`` - Timeout (in seconds) for RESTful HTTP requests. Defaults to 60.

    * ``DNA_CENTER_WAIT_ON_RATE_LIMIT`` - Enables or disables automatic rate-limit handling. Defaults to True.

    * ``DNA_CENTER_VERIFY`` - Controls whether to verify the server's TLS certificate or not. Defaults to True.

__ https://12factor.net/config


However, you choose to set it, if you have ``VERSION``, ``DNA_CENTER_USERNAME`` and ``DNA_CENTER_PASSWORD``, or
``VERSION`` and ``DNA_CENTER_ENCODED_AUTH`` environment variables, you are good to go.
dnacentersdk will use them to create your access token when creating new :class:`DNACenterAPI` objects.

If you don't want to set your credentials as environment variables, you
can manually provide them as parameters when creating a DNACenterAPI object.


Set credentials as environment variables
-----------------------------------------

There are many places and diverse ways that you can set an environment
variable, which can include:

    * A setting within your development IDE
    * A setting in your container / PaaS service
    * A statement in a shell script that configures and launches your app

It can be as simple as setting it in your CLI before running your script...

.. code-block:: bash

    $ DNA_CENTER_USERNAME=your_username_here
    $ DNA_CENTER_PASSWORD=your_password_here
    $ python myscript.py

...or putting your credentials in a shell script that you ``source`` when your
shell starts up or before your run a script:

.. code-block:: bash

    $ cat mycredentials.sh
    export DNA_CENTER_ENCODED_AUTH=your_encoded_auth_here
    $ source mycredentials.sh
    $ python myscript.py


Create a DNACenterAPI "Connection Object"
------------------------------------------

To make interacting with the DNA Center APIs as simple and intuitive as
possible, all of the APIs have 'wrapped' underneath a single interface.  To get
started, import the :class:`DNACenterAPI` class and create an API "connection
object".

.. code-block:: python

    >>> from dnacentersdk import DNACenterAPI
    >>> api = DNACenterAPI()

As discussed above (`Get your DNA Center Access Token`_), dnacentersdk defaults
to pulling from environment variables to generate your access token.
If you do not have those environment variables set and you try to
create a new :class:`DNACenterAPI` object without providing them,
a :exc:`AccessTokenError` will be raised (a :exc:`dnacentersdkException` subclass).

.. code-block:: python

    >>> from dnacentersdk import DNACenterAPI
    >>> api = DNACenterAPI()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "dnacentersdk/__init__.py", line 237, in __init__
        raise AccessTokenError(error_message)
    AccessTokenError: You need an access token to interact with the DNA Center
    APIs. DNA Center uses HTTP Basic Auth to create an access
    token. You must provide the username and password or just
    the encoded_auth, either by setting each parameter or its
    environment variable counterpart (DNA_CENTER_USERNAME,
    DNA_CENTER_PASSWORD, DNA_CENTER_ENCODED_AUTH).


If you don't provide a known version and try to create a new :class:`DNACenterAPI`, a :exc:`VersionError` will be raised.

.. code-block:: python

    >>> from dnacentersdk import DNACenterAPI
    >>> api = DNACenterAPI(username='devnetuser', password='Cisco123!', base_url='https://sandboxdnac2.cisco.com:443', version='0.1.12')
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "dnacentersdk/__init__.py", line 209, in __init__
        raise VersionError(error_message)
    VersionError: Unknown API version, known versions are 1.2.10 and 1.3.0.


Use the arguments to manually provide enough information for the HTTP Basic Auth process, 
when creating a new :class:`DNACenterAPI` connection object.

.. code-block:: python

    >>> from dnacentersdk import DNACenterAPI
    >>> # Create a DNACenterAPI connection object; it uses DNA Center sandbox URL and encoded_auth, with DNA Center API version 1.2.10
    >>> api = DNACenterAPI(encoded_auth='ZGV2bmV0dXNlcjpDaXNjbzEyMyEK', base_url="https://sandboxdnac2.cisco.com:443", version='1.2.10')

.. code-block:: python

    >>> from dnacentersdk import DNACenterAPI
    >>> # Create a DNACenterAPI connection object; it uses DNA Center username and password, with DNA Center API version 1.2.10
    >>> # The base_url used by default is `from dnacentersdk.config import DEFAULT_BASE_URL`
    >>> api = DNACenterAPI(username='devnetuser', password='Cisco123!', base_url="https://sandboxdnac2.cisco.com:443", version='1.2.10')

Note that this can be very useful if you are reading authentication credentials
from a file or database and/or when you want to create more than one connection object.

.. code-block:: python

    >>> from dnacentersdk import DNACenterAPI
    >>> kingston_auth = 'ZG5hY2VudGVydXNlcjpDaXNjbzEyMyEK'
    >>> london_auth = ('london', 'rcx0cf43!')
    >>> kingston_api = DNACenterAPI(encoded_auth=kingston_auth, base_url="https://sandboxdnac2.cisco.com:443", version='1.2.10')
    >>> london_api = DNACenterAPI(*london_auth, base_url="https://128.107.71.199:443", version='1.3.0')  # * Unpacks tuple


Certificates
------------

Besides username, password, encoded_auth, base_url, and version, there are other parameters when creating the :class:`DNACenterAPI`, many of them have a default value (check `Package Constants`_ for more).

When dealing with certificates, the most important one is the ``verify`` parameter.

To avoid getting errors like the following:

.. code-block:: python

    >>> from dnacentersdk import DNACenterAPI
    >>> own_dna = DNACenterAPI(encoded_auth='dXNlcm5hbWU6cGFzc3dvcmQK', 
    ... base_url="https://128.107.71.199:443", version='1.3.0')
    requests.exceptions.SLError: HTTPSConnectionPool(host='128.107.71.199', port=443):
    Max retries exceeded with url: /dna/system/api/v1/auth/token (Caused by
    SSLError (SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate
    verify failed: self signed certificate in certificate chain (_ssl.c:1076)')))
    >>>

Include the verify parameter and set it to False:

.. code-block:: python

    >>> from dnacentersdk import DNACenterAPI
    >>> own_dna = DNACenterAPI(encoded_auth='dXNlcm5hbWU6cGFzc3dvcmQK', 
    ... base_url="https://128.107.71.199:443", version='1.3.0',
    ... verify=False)
    InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate
     verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
      InsecureRequestWarning)
    >>>


You will see urllib3 warnings instead. If you want to disable them, the easiest way is with:

.. code-block:: python

    >>> import urllib3
    >>> urllib3.disable_warnings()


Package Constants
------------------

The following are the default values pulled ``from dnacentersdk.config`` and used when creating the connection object.

.. automodule:: dnacentersdk.config
    :members:
    :no-undoc-members:
    :exclude-members: DEBUG_ENVIRONMENT_VARIABLE, VERSION_ENVIRONMENT_VARIABLE, USERNAME_ENVIRONMENT_VARIABLE, PASSWORD_ENVIRONMENT_VARIABLE, ENCODED_AUTH_ENVIRONMENT_VARIABLE, BASE_URL_ENVIRONMENT_VARIABLE, SINGLE_REQUEST_TIMEOUT_ENVIRONMENT_VARIABLE, WAIT_ON_RATE_LIMIT_ENVIRONMENT_VARIABLE, VERIFY_ENVIRONMENT_VARIABLE, VERIFY_STRING_ENVIRONMENT_VARIABLE 


Making API Calls
----------------

Now that you have created a :class:`DNACenterAPI` "connection object," you are
ready to start making API calls.

.. code-block:: python

    >>> api.pnp.get_workflows()[0]
    {
      'version': 1,
      'name': 'test',
      'description': '',
      'useState': 'Available',
      'type': 'Standard',
      'addedOn': 1559538796969,
      'lastupdateOn': 1560455244769,
      'startTime': 0,
      'endTime': 0,
      'execTime': 0,
      'currTaskIdx': 0,
      'tasks': [{'taskSeqNo': 0,
        'name': 'Config Download',
        'type': 'Config',
        'startTime': 0,
        'endTime': 0,
        'timeTaken': 0,
        'currWorkItemIdx': 0,
        'workItemList': [],
        'configInfo': {'configId': '62066037-55cd-4c05-8e09-45674994a274',
        'configFileUrl': None,
        'fileServiceId': None,
        'saveToStartUp': True,
        'connLossRollBack': True,
        'configParameters': None}}],
      'addToInventory': True,
      'tenantId': '5bd3634ab2bea0004c3ebb58',
      'id': '5cf4ac6c568ecc000779da5c'
    }

It really is that easy.

All of the calls have been wrapped and represented as native Python method
calls, like :meth:`DNACenterAPI.pnp.get_workflows() <dnacentersdk.api.v1_2_10.pnp.Pnp.get_workflows>` which gets the workflows details
for the pnp - see 
the `Get Workflows
<https://pubhub.devnetcloud.com/media/dna-center-api-1210/docs/swagger_dnacp_1210_annotated.html#!/PnP/getWorkflows>`_ API endpoint
documentation.

As you can see, we have represented the API endpoints using simple terms
that are aligned with the API docs; for example, representing the ``/onboarding/pnp-workflow``
API endpoint as a ``pnp.get_workflows()`` method available underneath the
:class:`DNACenterAPI` connection object.

A full list of the available API methods, with their descriptions and
parameters, is available in the :ref:`User API Doc`. A summary of the structure is available 
for :ref:`v1.2.10 <v1_2_10 summary>` and :ref:`v1.3.0 <v1_3_0 summary>`.

You can easily access and call any of these methods directly from your
:class:`DNACenterAPI` connection object:

.. code-block:: python

    >>> api.pnp.get_device_list(limit=1)
    [{'version': 1,
      'deviceInfo': {'serialNumber': '1234567890s',
      'name': 'Postname-add',
      'pid': 'ws-c9300',
      'lastSyncTime': 0,
      'addedOn': 1559870763581,
      'lastUpdateOn': 1559870763581,
      'firstContact': 0,
      'lastContact': 0,
      'state': 'Unclaimed',
      'onbState': 'Not Contacted',
      'cmState': 'Not Contacted',
      'source': 'User',
      'reloadRequested': False,
      'aaaCredentials': {'username': '', 'password': ''},
      'populateInventory': False,
      'stack': False,
      'sudiRequired': False,
      'validActions': {'editSUDI': True,
        'editWfParams': True,
        'delete': True,
        'claim': True,
        'unclaim': True,
        'reset': False}},
      'workflowParameters': {},
      'runSummaryList': [{'timestamp': 1559870763581,
        'details': 'User Added Device',
        'errorFlag': False}],
      'tenantId': '5bd3634ab2bea0004c3ebb58',
      'id': '5cf9bd2b568ecc000779da65'}]


Catching Exceptions
-------------------

If something should go wrong with the API call, an exception will be raised.
:exc:`ApiError` exceptions are raised when an error condition is
returned from the DNA Center cloud.  Details will be provided in the error
message.

.. code-block:: python

    >>> from dnacentersdk import DNACenterAPI, ApiError
    >>> api = DNACenterAPI(username='devnetuser', password='Cisco123!')
    >>> # The base_url used by default is `from dnacentersdk.config import DEFAULT_BASE_URL`
    >>> task = api.task.get_task_by_operationid(
         limit=2,
         offset=1,
         operation_id='xyz')
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "dnacentersdk/api/task.py", line 584, in get_task_by_operationid
        json=payload)
      File "dnacentersdk/restsession.py", line 280, in get
        response = self.request('GET', url, erc, params=params, **kwargs)
      File "dnacentersdk/restsession.py", line 236, in request
        check_response_code(response, erc)
      File "dnacentersdk/utils.py", line 217, in check_response_code
        raise ApiError(response)
    dnacentersdk.exceptions.ApiError: [500] Server Error - errorId=20,
    componentName=CRUD executeQuery Failed! errorId=20,componentName=CRUD
    executeQuery Failed! Named query not known: task.findTaskByOperationId
    >>>

You can catch any errors returned by the DNA Center cloud by catching
:exc:`ApiError` exceptions in a try-except block.

.. code-block:: python

    >>> from dnacentersdk.exceptions import ApiError
    >>> try:
    ...     task = api.task.get_task_by_operationid(
    ...       limit=2,
    ...       offset=1,
    ...       operation_id='xyz')
    ... except ApiError as e:
    ...     print(e)
    ApiError: [500] Server Error - errorId=20,componentName=CRUD executeQuery Failed! errorId=20,
    componentName=CRUD executeQuery Failed! Named query not known: task.findTaskByOperationId
    >>>

dnacentersdk will also raise a number of other standard errors
(:exc:`TypeError`, :exc:`ValueError`, etc.); however, these errors are usually
caused by incorrect use of the package or methods and should be sorted while
debugging your app.


Working with Returned Objects
-----------------------------

The DNA Center cloud returns data objects in JSON format, like so:

.. code-block:: json

    [{ "version": 1,
      "deviceInfo": { "serialNumber":  "1234567890s",
      "name":  "Postname-add ",
      "pid":  "ws-c9300 ",
      "lastSyncTime": 0,
      "addedOn": 1559870763581,
      "lastUpdateOn": 1559870763581,
      "firstContact": 0,
      "lastContact": 0,
      "state":  "Unclaimed ",
      "onbState":  "Not Contacted ",
      "cmState":  "Not Contacted ",
      "source":  "User ",
      "reloadRequested": false,
      "aaaCredentials": { "username":  "",  "password":  ""},
      "populateInventory": false,
      "stack": false,
      "sudiRequired": false,
      "validActions": { "editSUDI": true,
        "editWfParams": true,
        "delete": true,
        "claim": true,
        "unclaim": true,
        "reset": false}},
      "workflowParameters": {},
      "runSummaryList": [{ "timestamp": 1559870763581,
        "details":  "User Added Device ",
        "errorFlag": false}],
      "tenantId":  "5bd3634ab2bea0004c3ebb58 ",
      "id":  "5cf9bd2b568ecc000779da65 "}]


Sure, JSON data objects can easily be parsed and represented in Python using
dictionaries, but when working with an 'object' wouldn't it be nice to be able
to work with it like an object - using native object syntax (like accessing
attributes using '.' notation)? dnacentersdk enables you to do just that:

.. code-block:: python

    >>> pnp_devices = api.pnp.get_device_list()
    >>> pnp_devices[0].id
    '5cf9bd2b568ecc000779da65'
    >>> pnp_devices[0].deviceInfo.state
    'Unclaimed'
    >>> pnp_devices[0].deviceInfo.serialNumber
    '1234567890s'

Representing and treating DNA Center data objects as Python data objects, can really
help clean up your code and make coding easier:

    1.  You don't need to create variables to hold the data attributes, just
        use the attributes available underneath the data object.

        .. code-block:: python

            >>> # Do this
            >>> api.pnp.get_device_history(serial_number=pnp_devices[0].deviceInfo.serialNumber)
            {'response': [{'timestamp': 1559870763581, 'details': 'User Added Device', 'errorFlag': False}], 'statusCode': 200}
            >>> # Instead of this
            >>> device_serialNumber = pnp_devices[0].deviceInfo.serialNumber
            >>> api.pnp.get_device_history(serial_number=device_serialNumber)
            {'response': [{'timestamp': 1559870763581, 'details': 'User Added Device', 'errorFlag': False}], 'statusCode': 200}

    2.  When accessing 'optional' attributes, like ``pnp_devices[0].workflowParameters.configList``
        attribute of DNA Center PnP object, the response object will return ``None`` when
        the attribute is not present and will return the attribute's value when
        it is present.  This avoids some boiler plate code and/or needless
        exception handling, when working with optional attributes.

        .. code-block:: python

            >>> # Instead of doing this
            >>> for d in devices:
            ...     if hasattr(d, 'workflowParameters') and hasattr(d.workflowParameters, 'configList'):
            ...         # Do something with the configList attribute
            ...         pass
            >>> # Or this
            >>> try:
            ...     for d in devices:
            ...         # Do something with the configList attribute
            ...         d.workflowParameters.configList
            ... except AttributeError as e:
            ...     pass
            >>> # You can do this, which is cleaner
            >>> for d in devices:
            ...     if d.workflowParameters and d.workflowParameters.configList:
            ...         # Do something with the configList attribute
            ...         pass


    3.  It just feels more *natural*.  :-)  When iterating through sequences,
        and working with objects in those sequences (see the next section),
        working with objects as objects is definitely more Pythonic.

        The Zen of Python (`PEP 20`_):
            "Beautiful is better than ugly."
            "Simple is better than complex."

The currently modeled :ref:`DNA Center Data Object` with its
functions, is available :ref:`here <DNA Center Data Object>` in the
:ref:`User API Doc`.


**What if DNA Center adds new data attributes?**

Attribute access WILL WORK for the newly added attributes (yes, without a
package update!).  dnacentersdk is written to automatically take advantage
of new attributes and data as they are returned.


Adding API call definitions
-----------------------------

Custom caller functions help you:

  1. Add support for custom API calls.

  2. Add support for API calls that are/were not documented when the SDK was released.


.. code-block:: python

    from dnacentersdk import api

    # Create a DNACenterAPI connection object;
    # it uses DNA Center sandbox URL, username and password, with DNA Center API version 1.2.10.,
    # and requests to verify the server's TLS certificate with verify=True.
    dnac = api.DNACenterAPI(username="devnetuser",
                            password="Cisco123!",
                            base_url="https://sandboxdnac2.cisco.com:443",
                            version='1.2.10',
                            verify=True)

    # Add your custom API call to the connection object.
    # Define the get_global_credentials function.
    # Call it with:
    #     get_global_credentials('NETCONF')
    def get_global_credentials(subtype):
        return dnac.custom_caller.call_api('GET',
                                   '/dna/intent/api/v1/global-credential',
                                   params={
                                       'credentialSubType': subtype
                                   })


    # Add your custom API call to the connection object.
    # Define the delete_global_credentials_by_id function
    # under the custom_caller wrapper.
    # Call it with:
    #     dnac.custom_caller.delete_global_credentials_by_id('be456g16-14fd-4cac-94b7-ac3b8f9f')
    dnac.custom_caller.add_api('delete_global_credentials_by_id',
                              lambda global_credential_id:
                                  dnac.custom_caller.call_api(
                                      'DELETE',
                                      '/dna/intent/api/v1/global-credential/${credentialId}',
                                      path_params={
                                          'credentialId': global_credential_id,
                                      })
                              )

    # Advance usage example using Custom Caller functions.
    def setup_custom():
        """
        Defines the get_global_credentials and create_netconf_credentials functions
        under the custom_caller wrapper, and with help documentation
        in two different ways.

        Check that they have been added with
            'get_global_credentials' in dir(dnac.custom_caller)
            'create_netconf_credentials' in dir(dnac.custom_caller)

        Quickly check that you indeed have them as functions with
            type(getattr(dnac.custom_caller, 'create_netconf_credentials'))
            type(getattr(dnac.custom_caller, 'create_netconf_credentials'))

        Check the documentation with
            help(dnac.custom_caller.get_global_credentials)
            help(dnac.custom_caller.create_netconf_credentials)

        """

        # Alternative 1: Definition with helper function.
        def _get_global_credentials(credential_type):
            """Custom global credential API call, returns response attribute

                Args:
                    credential_type(str): Credential type as CLI
                        / SNMPV2_READ_COMMUNITY /
                        SNMPV2_WRITE_COMMUNITY / SNMPV3 /
                        HTTP_WRITE / HTTP_READ / NETCONF. 

                Returns: 
                    MyDict: JSON response. Access the object's properties by using
                    the dot notation or the bracket notation.
            """
            return dnac.custom_caller.call_api(
                                        'GET',
                                        '/dna/intent/api/v1/global-credential',
                                        params={
                                            'credentialSubType': credential_type
                                        }).response
        # Finally add the function as an attribute.
        dnac.custom_caller.add_api('get_global_credentials', _get_global_credentials)

        # Alternative 2: Definition with lambda function.
        dnac.custom_caller.add_api('create_netconf_credentials',
                                lambda port:
                                    dnac.custom_caller.call_api(
                                        'POST',
                                        '/dna/intent/api/v1/global-credential/netconf',
                                        json=[{
                                            "netconfPort": port
                                        }])
                                )
        # Finally add the documentation
        dnac.custom_caller.create_netconf_credentials.__doc__ = """
            Custom global credential API call to add NETCONF credentials
            
            Receives:
                port(string): Netconf port number
            
            Returns: JSON response.
            """


Check out the `Custom Caller`_ documentation to begin using it.


.. _Custom Caller: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#custom-caller


*Copyright (c) 2019 Cisco and/or its affiliates.*

.. _PEP 20: https://www.python.org/dev/peps/pep-0020/

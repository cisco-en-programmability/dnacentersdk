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
A DNA Center Access Token is how the DNA Center APIs validate access.


Use your DNA Center Access Token
---------------------------------

As a `best practice`__, you can store your DNA Center access token 'credential' as
an environment variable in your development or production environment.  By
default, dnacentersdk will look for a ``DNA_CENTER_ACCESS_TOKEN`` environment
variable when creating new connection objects.

__ https://12factor.net/config

There are many places and diverse ways that you can set an environment
variable, which can include:

    * A setting within your development IDE
    * A setting in your container / PaaS service
    * A statement in a shell script that configures and launches your app

It can be as simple as setting it in your CLI before running your script...

.. code-block:: bash

    $ DNA_CENTER_ACCESS_TOKEN=your_access_token_here
    $ python myscript.py

...or putting your credentials in a shell script that you ``source`` when your
shell starts up or before your run a script:

.. code-block:: bash

    $ cat mycredentials.sh
    export DNA_CENTER_ACCESS_TOKEN=your_access_token_here
    $ source mycredentials.sh
    $ python myscript.py

However you choose to set it, if you have your access token stored in a
``DNA_CENTER_ACCESS_TOKEN`` environment variable when using dnacentersdk, you are
good to go.  dnacentersdk will pull and use this access token, by default,
when creating new :class:`DNACenterAPI` objects.

If you don't want to set your access token as an environment variable, or
perhaps your application will acquire access tokens via some other means, you
can manually provide your access token when creating a DNACenterAPI object.


Create a DNACenterAPI "Connection Object"
------------------------------------------

To make interacting with the DNA Center APIs as simple and intuitive as
possible, all of the APIs have 'wrapped' underneath a single interface.  To get
started, import the :class:`DNACenterAPI` class and create an API "connection
object".

.. code-block:: python

    >>> from dnacentersdk import DNACenterAPI
    >>> api = DNACenterAPI()

As discussed above (`Use your DNA Center Access Token`_), dnacentersdk defaults
to pulling your DNA Center access token from a ``DNA_CENTER_ACCESS_TOKEN`` environment
variable.  If you do not have this environment variable set and you try to
create a new :class:`DNACenterAPI` object without providing a DNA Center access
token, a :exc:`AccessTokenError` will be raised (a :exc:`dnacentersdkException` subclass).

.. code-block:: python

    >>> from dnacentersdk import DNACenterAPI
    >>> api = DNACenterAPI()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "dnacentersdk/__init__.py", line 147, in __init__
        raise AccessTokenError(error_message)
    AccessTokenError: You must provide a DNA Center access token to interact with the DNA Center 
    APIs, either via a DNA_CENTER_ACCESS_TOKEN environment variable or via the access_token argument.
    To interact with the APIs and get your access_token, you could provide either username and 
    password arguments or the encoded_auth argument.

Use the ``access_token`` argument to manually provide your access token, when
creating a new :class:`DNACenterAPI` connection object.

.. code-block:: python

    >>> from dnacentersdk import DNACenterAPI
    >>> api = DNACenterAPI(access_token='eyJ0eXAi...Ghg')

Note that this can be very useful if you are reading in access token(s) from a
file or database and/or when you want to create more than one connection
object.

.. code-block:: python

    >>> from dnacentersdk import DNACenterAPI
    >>> kingston_at = 'eyJ0eXBt...Fdc'
    >>> london_at = 'eyJ0eXAi...Ghg'
    >>> kingston_api = DNACenterAPI(access_token=kingston_at)
    >>> london_api = DNACenterAPI(access_token=london_at)


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
calls, like :meth:`DNACenterAPI.pnp.get_workflows() <dnacentersdk.api.pnp.Pnp.get_workflows>` which gets the workflows details
for the pnp - see 
the `Get Workflows
<https://pubhub.devnetcloud.com/media/dnac-api-docs-1-3/docs/swagger-1.3-v2_annotated.html#!/PnP/getWorkflows>`_ API endpoint
documentation.

As you can see, we have represented the API endpoints using simple terms
that are aligned with the API docs; for example, representing the ``/onboarding/pnp-workflow``
API endpoint as a ``pnp.get_workflows()`` method available underneath the
:class:`DNACenterAPI` connection object.

A full list of the available API methods, with their descriptions and
parameters, is available in the :ref:`User API Doc`, and a brief summary of the
structure is provided here.


.. include:: api_structure_table.rst

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

    >>> try:
    ...     task = api.task.get_task_by_operationid(
    ...       limit=2,
    ...       offset=1,
    ...       operation_id='xyz')
    ... except Exception as e:
    ...     print(e)
    [500] Server Error - errorId=20,componentName=CRUD executeQuery
    Failed! errorId=20,componentName=CRUD executeQuery Failed!
    Named query not known: task.findTaskByOperationId
    >>>

dnacentersdk will also raise a number of other standard errors
(:exc:`TypeError`, :exc:`ValueError`, etc.); however, these errors are usually
caused by incorrect use of the package or methods and should be sorted while
debugging your app.


Working with Returned Objects
-----------------------------

The DNA Center cloud returns data objects in JSON format, like so:

.. code-block:: json

    [{ "version ": 1,
      "deviceInfo ": { "serialNumber ":  "1234567890s ",
      "name ":  "Postname-add ",
      "pid ":  "ws-c9300 ",
      "lastSyncTime ": 0,
      "addedOn ": 1559870763581,
      "lastUpdateOn ": 1559870763581,
      "firstContact ": 0,
      "lastContact ": 0,
      "state ":  "Unclaimed ",
      "onbState ":  "Not Contacted ",
      "cmState ":  "Not Contacted ",
      "source ":  "User ",
      "reloadRequested ": false,
      "aaaCredentials ": { "username ":  " ",  "password ":  " "},
      "populateInventory ": false,
      "stack ": false,
      "sudiRequired ": false,
      "validActions ": { "editSUDI ": true,
        "editWfParams ": true,
        "delete ": true,
        "claim ": true,
        "unclaim ": true,
        "reset ": false}},
      "workflowParameters ": {},
      "runSummaryList ": [{ "timestamp ": 1559870763581,
        "details ":  "User Added Device ",
        "errorFlag ": false}],
      "tenantId ":  "5bd3634ab2bea0004c3ebb58 ",
      "id ":  "5cf9bd2b568ecc000779da65 "}]


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


*Copyright (c) 2019 Cisco and/or its affiliates.*

.. _PEP 20: https://www.python.org/dev/peps/pep-0020/

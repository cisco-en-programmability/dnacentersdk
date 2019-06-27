.. _Quickstart:

.. currentmodule:: dnacentersdk

==========
Quickstart
==========

*Dive in!*  ...to get started using the dnacentersdk package:

Make sure that you have:


__ DNA Center_

Get your DNA Center Access Token
---------------------------------
#TODO: add info.

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
    To interact with the APIs and get your access_token, you could provideeither username and 
    password arguments or via the encodedAuth argument.

Use the ``access_token`` argument to manually provide your access token, when
creating a new :class:`DNACenterAPI` connection object.

.. code-block:: python

    >>> from dnacentersdk import DNACenterAPI
    >>> api = DNACenterAPI(access_token='lkj345w...')

Note that this can be very useful if you are reading in access token(s) from a
file or database and/or when you want to create more than one connection
object.

.. code-block:: python

    >>> from dnacentersdk import DNACenterAPI
    >>> chris_at = 'lkj345w...'
    >>> veronica_at = 'kl45kln...'
    >>> chris_api = DNACenterAPI(access_token=chris_at)
    >>> veronica_api = DNACenterAPI(access_token=veronica_at)


Making API Calls
----------------

Now that you have created a :class:`DNACenterAPI` "connection object," you are
ready to start making API calls.

.. code-block:: python

    >>> dnac.pnp.get_workflows()[0]
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



Catching Exceptions
-------------------



Working with Returned Objects
-----------------------------



**What if DNA Center adds new data attributes?**






*Copyright (c) 2019 Cisco and/or its affiliates.*


.. _DNA Center: https://www.cisco.com/c/en/us/products/cloud-systems-management/dna-center/index.html
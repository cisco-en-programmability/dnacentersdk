.. _User API Doc:

.. currentmodule:: dnacentersdk

============
User API Doc
============


DNACenterAPI
=============

The :class:`DNACenterAPI` class creates "connection objects" for working with the DNA Center APIs and hierarchically organizes the DNA Center APIs and their endpoints underneath these connection objects.


.. include:: api_structure_table.rst


.. autoclass:: DNACenterAPI()
    :members:

    .. automethod:: DNACenterAPI.__init__



.. _template_programmer:

template_programmer
-------------------

.. autoclass:: dnacentersdk.api.template_programmer.TemplateProgrammer()



.. _tag:

tag
---

.. autoclass:: dnacentersdk.api.tag.Tag()



.. _network_discovery:

network_discovery
-----------------

.. autoclass:: dnacentersdk.api.network_discovery.NetworkDiscovery()



.. _task:

task
----

.. autoclass:: dnacentersdk.api.task.Task()



.. _command_runner:

command_runner
--------------

.. autoclass:: dnacentersdk.api.command_runner.CommandRunner()



.. _file:

file
----

.. autoclass:: dnacentersdk.api.file.File()



.. _path_trace:

path_trace
----------

.. autoclass:: dnacentersdk.api.path_trace.PathTrace()



.. _swim:

swim
----

.. autoclass:: dnacentersdk.api.swim.Swim()



.. _pnp:

pnp
---

.. autoclass:: dnacentersdk.api.pnp.Pnp()



.. _site_profile:

site_profile
------------

.. autoclass:: dnacentersdk.api.site_profile.SiteProfile()



.. _devices:

devices
-------

.. autoclass:: dnacentersdk.api.devices.Devices()



.. _sites:

sites
-----

.. autoclass:: dnacentersdk.api.sites.Sites()



.. _networks:

networks
--------

.. autoclass:: dnacentersdk.api.networks.Networks()



.. _clients:

clients
-------

.. autoclass:: dnacentersdk.api.clients.Clients()



.. _non_fabric_wireless:

non_fabric_wireless
-------------------

.. autoclass:: dnacentersdk.api.non_fabric_wireless.NonFabricWireless()



.. _fabric_wired:

fabric_wired
------------

.. autoclass:: dnacentersdk.api.fabric_wired.FabricWired()



.. _authentication:

authentication
--------------

.. autoclass:: dnacentersdk.api.authentication.Authentication()


.. _DNA Center Data Object:

DNA Center Data Object
=======================


.. _MyDict:

MyDict
------

.. autoclass:: dnacentersdk.models.mydict.MyDict()
    :members:
    :exclude-members: get_dict, clear, fromkeys, pop, popitem, setdefault, update, values

.. _Exceptions:

Exceptions
==========

.. autoexception:: dnacentersdkException()
    :show-inheritance:
    :members:

.. autoexception:: AccessTokenError()
    :show-inheritance:
    :members:

.. autoexception:: ApiError()
    :show-inheritance:
    :members:

.. autoexception:: RateLimitError()
    :show-inheritance:
    :members:

.. autoexception:: RateLimitWarning()
    :show-inheritance:
    :members:

.. autoexception:: MalformedRequest()
    :show-inheritance:
    :members:


.. _Warnings:

Warnings
========

.. autoexception:: RateLimitWarning()
    :show-inheritance:
    :members:


*Copyright (c) 2019 Cisco and/or its affiliates.*
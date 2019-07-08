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



.. _Template Programmer:

template_programmer
-------------------

.. autoclass:: dnacentersdk.api.template_programmer.TemplateProgrammer()



.. _Tag:

tag
---

.. autoclass:: dnacentersdk.api.tag.Tag()



.. _Network Discovery:

network_discovery
-----------------

.. autoclass:: dnacentersdk.api.network_discovery.NetworkDiscovery()



.. _Task:

task
----

.. autoclass:: dnacentersdk.api.task.Task()



.. _Command Runner:

command_runner
--------------

.. autoclass:: dnacentersdk.api.command_runner.CommandRunner()



.. _File:

file
----

.. autoclass:: dnacentersdk.api.file.File()



.. _Path Trace:

path_trace
----------

.. autoclass:: dnacentersdk.api.path_trace.PathTrace()



.. _Non-Fabric Wireless:

non_fabric_wireless
-------------------

.. autoclass:: dnacentersdk.api.non_fabric_wireless.NonFabricWireless()



.. _Fabric Wired:

fabric_wired
------------

.. autoclass:: dnacentersdk.api.fabric_wired.FabricWired()



.. _Devices:

devices
-------

.. autoclass:: dnacentersdk.api.devices.Devices()



.. _Sites:

sites
-----

.. autoclass:: dnacentersdk.api.sites.Sites()



.. _Networks:

networks
--------

.. autoclass:: dnacentersdk.api.networks.Networks()



.. _Clients:

clients
-------

.. autoclass:: dnacentersdk.api.clients.Clients()



.. _PnP:

pnp
---

.. autoclass:: dnacentersdk.api.pnp.Pnp()



.. _SWIM:

swim
----

.. autoclass:: dnacentersdk.api.swim.Swim()



.. _Site Profile:

site_profile
------------

.. autoclass:: dnacentersdk.api.site_profile.SiteProfile()


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

.. autoexception:: MalformedResponse()
    :show-inheritance:
    :members:

.. autoexception:: MalformedRequest()
    :show-inheritance:
    :members:

.. autoexception:: DownloadFailure()
    :show-inheritance:
    :members:


.. _Warnings:

Warnings
========

.. autoexception:: RateLimitWarning()
    :show-inheritance:
    :members:


*Copyright (c) 2019 Cisco and/or its affiliates.*
.. _User API Doc:

.. currentmodule:: dnacentersdk

============
User API Doc
============


-------------
DNACenterAPI
-------------

The :class:`DNACenterAPI` class creates "connection objects" for working with the DNA Center APIs and hierarchically organizes the DNA Center APIs and their endpoints underneath these connection objects.


DNACenterAPI summary structure
===============================


.. _v1_2_10 summary:

v1.2.10 summary
-----------------------------

.. include:: api_structure_table_v1_2_10.rst


.. _v1_3_0 summary:

v1.3.0 summary
-----------------------------

.. include:: api_structure_table_v1_3_0.rst


DNACenterAPI Class
========================

.. autoclass:: DNACenterAPI()
    :members:

    .. automethod:: DNACenterAPI.__init__



.. _authentication:

authentication
--------------

.. autoclass:: dnacentersdk.api.authentication.Authentication()



.. _custom_caller:

custom_caller
-------------

.. autoclass:: dnacentersdk.api.custom_caller.CustomCaller()


DNACenterAPI v1.2.10
===============================

.. _clients_1_2_10:

clients
-------

.. autoclass:: dnacentersdk.api.v1_2_10.clients.Clients()



.. _command_runner_1_2_10:

command_runner
--------------

.. autoclass:: dnacentersdk.api.v1_2_10.command_runner.CommandRunner()



.. _devices_1_2_10:

devices
-------

.. autoclass:: dnacentersdk.api.v1_2_10.devices.Devices()



.. _fabric_wired_1_2_10:

fabric_wired
------------

.. autoclass:: dnacentersdk.api.v1_2_10.fabric_wired.FabricWired()



.. _file_1_2_10:

file
----

.. autoclass:: dnacentersdk.api.v1_2_10.file.File()



.. _network_discovery_1_2_10:

network_discovery
-----------------

.. autoclass:: dnacentersdk.api.v1_2_10.network_discovery.NetworkDiscovery()



.. _networks_1_2_10:

networks
--------

.. autoclass:: dnacentersdk.api.v1_2_10.networks.Networks()



.. _non_fabric_wireless_1_2_10:

non_fabric_wireless
-------------------

.. autoclass:: dnacentersdk.api.v1_2_10.non_fabric_wireless.NonFabricWireless()



.. _path_trace_1_2_10:

path_trace
----------

.. autoclass:: dnacentersdk.api.v1_2_10.path_trace.PathTrace()



.. _pnp_1_2_10:

pnp
---

.. autoclass:: dnacentersdk.api.v1_2_10.pnp.Pnp()



.. _swim_1_2_10:

swim
----

.. autoclass:: dnacentersdk.api.v1_2_10.swim.Swim()



.. _site_profile_1_2_10:

site_profile
------------

.. autoclass:: dnacentersdk.api.v1_2_10.site_profile.SiteProfile()



.. _sites_1_2_10:

sites
-----

.. autoclass:: dnacentersdk.api.v1_2_10.sites.Sites()



.. _tag_1_2_10:

tag
---

.. autoclass:: dnacentersdk.api.v1_2_10.tag.Tag()



.. _task_1_2_10:

task
----

.. autoclass:: dnacentersdk.api.v1_2_10.task.Task()



.. _template_programmer_1_2_10:

template_programmer
-------------------

.. autoclass:: dnacentersdk.api.v1_2_10.template_programmer.TemplateProgrammer()




DNACenterAPI v1.3.0
===============================

.. _clients_1_3_0:

clients
-------

.. autoclass:: dnacentersdk.api.v1_3_0.clients.Clients()



.. _command_runner_1_3_0:

command_runner
--------------

.. autoclass:: dnacentersdk.api.v1_3_0.command_runner.CommandRunner()



.. _devices_1_3_0:

devices
-------

.. autoclass:: dnacentersdk.api.v1_3_0.devices.Devices()



.. _fabric_wired_1_3_0:

fabric_wired
------------

.. autoclass:: dnacentersdk.api.v1_3_0.fabric_wired.FabricWired()



.. _file_1_3_0:

file
----

.. autoclass:: dnacentersdk.api.v1_3_0.file.File()



.. _network_discovery_1_3_0:

network_discovery
-----------------

.. autoclass:: dnacentersdk.api.v1_3_0.network_discovery.NetworkDiscovery()



.. _networks_1_3_0:

networks
--------

.. autoclass:: dnacentersdk.api.v1_3_0.networks.Networks()



.. _non_fabric_wireless_1_3_0:

non_fabric_wireless
-------------------

.. autoclass:: dnacentersdk.api.v1_3_0.non_fabric_wireless.NonFabricWireless()



.. _path_trace_1_3_0:

path_trace
----------

.. autoclass:: dnacentersdk.api.v1_3_0.path_trace.PathTrace()



.. _pnp_1_3_0:

pnp
---

.. autoclass:: dnacentersdk.api.v1_3_0.pnp.Pnp()



.. _swim_1_3_0:

swim
----

.. autoclass:: dnacentersdk.api.v1_3_0.swim.Swim()



.. _site_profile_1_3_0:

site_profile
------------

.. autoclass:: dnacentersdk.api.v1_3_0.site_profile.SiteProfile()



.. _sites_1_3_0:

sites
-----

.. autoclass:: dnacentersdk.api.v1_3_0.sites.Sites()



.. _tag_1_3_0:

tag
---

.. autoclass:: dnacentersdk.api.v1_3_0.tag.Tag()



.. _task_1_3_0:

task
----

.. autoclass:: dnacentersdk.api.v1_3_0.task.Task()



.. _template_programmer_1_3_0:

template_programmer
-------------------

.. autoclass:: dnacentersdk.api.v1_3_0.template_programmer.TemplateProgrammer()


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

.. autoexception:: AccessTokenError()
    :show-inheritance:
    :members:

.. autoexception:: ApiError()
    :show-inheritance:
    :members:

.. autoexception:: MalformedRequest()
    :show-inheritance:
    :members:

.. autoexception:: RateLimitError()
    :show-inheritance:
    :members:

.. autoexception:: RateLimitWarning()
    :show-inheritance:
    :members:

.. autoexception:: VersionError()
    :show-inheritance:
    :members:

.. autoexception:: dnacentersdkException()
    :show-inheritance:
    :members:


.. _Warnings:

Warnings
========

.. autoexception:: RateLimitWarning()
    :show-inheritance:
    :members:


*Copyright (c) 2019 Cisco and/or its affiliates.*
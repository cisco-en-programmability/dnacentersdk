dnacentersdk
============

*Work with the DNA Center APIs in native Python!*

-------------------------------------------------------------------------------

**dnacentersdk** is a *community-developed* Python library for working with the Cisco DNA Center APIs. Our goal is to make interacting with DNA Center in Python a *native* and *natural* experience!

.. code-block:: python

    from dnacentersdk import DNACenterAPI

    # Create a DNACenterAPI connection object
    dnac = DNACenterAPI(
        username="devnetuser",
        password="Cisco123!",
        base_url="https://sandboxdnac.cisco.com:443",
        version="3.1.3.0",
        verify=True
    )

    # Find all devices that belong to the "Switches and Hubs" family
    devices = dnac.devices.get_device_list(family="Switches and Hubs")

    for device in devices.response:
        print("{:20s}{}".format(device.hostname, device.upTime))

    # Find all tags
    all_tags = dnac.tag.get_tag(sort_by="name", order="des")
    demo_tags = [tag for tag in all_tags.response if "Demo" in tag.name]

    # Delete demo tags
    for tag in demo_tags:
        dnac.tag.delete_tag(tag.id)

    # Create a new demo tag
    demo_tag = dnac.tag.create_tag(name="dna Demo")
    task = dnac.task.get_task_by_id(task_id=demo_tag.response.taskId)

    if not task.response.isError:
        created_tag = dnac.tag.get_tag(name="dna Demo")
        updated_tag = dnac.tag.update_tag(
            id=created_tag.response[0].id,
            name="Updated " + created_tag.response[0].name,
            description="DNA demo tag"
        )
        print(dnac.task.get_task_by_id(task_id=updated_tag.response.taskId).response.progress)

        # Retrieve updated tag
        result = dnac.tag.get_tag(name="Updated dna Demo")
        print(result)
    else:
        print("Unfortunately", task.response.progress)
        print("Reason:", task.response.failureReason)

    # Custom API examples
    def setup_custom():
        dnac.custom_caller.add_api(
            "get_global_credentials",
            lambda credential_type: dnac.custom_caller.call_api(
                "GET",
                "/dna/intent/api/v1/global-credential",
                params={"credentialSubType": credential_type}
            ).response
        )
        dnac.custom_caller.add_api(
            "create_netconf_credentials",
            lambda port: dnac.custom_caller.call_api(
                "POST",
                "/dna/intent/api/v1/global-credential/netconf",
                json=[{"netconfPort": port}]
            )
        )

    setup_custom()
    dnac.custom_caller.create_netconf_credentials("65533")
    print(dnac.custom_caller.get_global_credentials("NETCONF"))

Introduction
------------

Check out the complete Introduction_

**dnacentersdk handles all of this for you:**

- Reads your DNA Center credentials from environment variables.
- Reads your DNA Center API version from the `DNA_CENTER_VERSION` environment variable.
- Handles TLS certificate verification with the `verify` parameter.
- Enables debug mode via the `DNA_CENTER_DEBUG` environment variable.
- Exposes all DNA Center API calls as native Python methods organized in a hierarchical tree.
- Offers IDE auto-completion support (e.g., in `PyCharm_`).
- Converts all JSON responses to native Python objects with dot notation access.
- Handles rate-limiting automatically.
- Refreshes authentication tokens when they expire.
- Provides resource management via context managers and explicit connection cleanup.

Resource Management
-------------------

You can manage the HTTP connection lifecycle in several ways:

**Context Manager**

.. code-block:: python

    from dnacentersdk import DNACenterAPI

    with DNACenterAPI() as dnac:
        devices = dnac.devices.get_device_list()

**Explicit Close**

.. code-block:: python

    from dnacentersdk import DNACenterAPI

    dnac = DNACenterAPI()
    try:
        devices = dnac.devices.get_device_list()
    finally:
        dnac.close()

**Automatic Cleanup via GC**

.. code-block:: python

    from dnacentersdk import DNACenterAPI

    def get_devices():
        dnac = DNACenterAPI()
        return dnac.devices.get_device_list()

    devices = get_devices()

**Legacy Usage**

.. code-block:: python

    from dnacentersdk import DNACenterAPI

    dnac = DNACenterAPI()
    devices = dnac.devices.get_device_list()

Installation
------------

**Install via pip**

.. code-block:: bash

    pip install dnacentersdk

**Upgrade to the latest version**

.. code-block:: bash

    pip install --upgrade dnacentersdk

Compatibility Matrix
--------------------

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - Cisco DNA Center version
     - dnacentersdk version
   * - 2.3.5.3
     - 2.6.11
   * - 2.3.7.6
     - 2.7.7
   * - 2.3.7.7
     - 2.8.6
   * - 2.3.7.9
     - 2.8.14
   * - 3.1.3.0
     - 2.10.2

Documentation
-------------

Visit: https://dnacentersdk.readthedocs.io

Start with the Quickstart_ to get up and running quickly.

Release Notes
-------------

See the releases_ page for details on features and fixes.

Questions, Support & Discussion
-------------------------------

This is a *community-supported* project. For questions or issues, use the issues_ page.

Contributing
------------

dnacentersdk_ is community-driven. Feedback, suggestions, and code contributions are welcome! See the Contributing_ guide.

Inspiration
-----------

This library is inspired by the webexteamssdk_ project.

Changelog
---------

All notable changes are documented in the CHANGELOG_.

The library may continue to evolve as Cisco DNA Center APIs change.

*Copyright (c) 2019–2025 Cisco Systems.*

.. _Introduction: https://dnacentersdk.readthedocs.io/en/latest/api/intro.html
.. _Quickstart: https://dnacentersdk.readthedocs.io/en/latest/api/quickstart.html
.. _dnacentersdk: https://github.com/cisco-en-programmability/dnacentersdk
.. _issues: https://github.com/cisco-en-programmability/dnacentersdk/issues
.. _releases: https://github.com/cisco-en-programmability/dnacentersdk/releases
.. _Contributing: https://github.com/cisco-en-programmability/dnacentersdk/blob/master/docs/contributing.rst
.. _webexteamssdk: https://github.com/CiscoDevNet/webexteamssdk
.. _CHANGELOG: https://github.com/cisco-en-programmability/dnacentersdk/blob/main/CHANGELOG.md
.. _PyCharm: https://www.jetbrains.com/pycharm

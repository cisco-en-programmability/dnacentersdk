=============
dnacentersdk
=============

*Work with the DNA Center APIs in native Python!*

-------------------------------------------------------------------------------

**dnacentersdk** is a *community developed* Python library for working with the DNA Center APIs.  Our goal is to make working with DNA Center in Python a *native* and *natural* experience!

.. code-block:: python

    from dnacentersdk import api

    # Create a DNACenterAPI connection object;
    # it uses DNA Center sandbox URL, username and password, with DNA Center API version 2.3.5.3.
    # and requests to verify the server's TLS certificate with verify=True.
    dnac = api.DNACenterAPI(username="devnetuser",
                            password="Cisco123!",
                            base_url="https://sandboxdnac.cisco.com:443",
                            version='2.3.7.6',
                            verify=True)

    # Find all devices that have 'Switches and Hubs' in their family
    devices = dnac.devices.get_device_list(family='Switches and Hubs')

    # Print all of demo devices
    for device in devices.response:
        print('{:20s}{}'.format(device.hostname, device.upTime))

    # Find all tags
    all_tags = dnac.tag.get_tag(sort_by='name', order='des')
    demo_tags = [tag for tag in all_tags.response if 'Demo' in tag.name ]

    #  Delete all of the demo tags
    for tag in demo_tags:
        dnac.tag.delete_tag(tag.id)
    
    # Create a new demo tag
    demo_tag = dnac.tag.create_tag(name='dna Demo')
    task_demo_tag = dnac.task.get_task_by_id(task_id=demo_tag.response.taskId)

    if not task_demo_tag.response.isError:
        # Retrieve created tag
        created_tag = dnac.tag.get_tag(name='dna Demo')

        # Update tag
        update_tag = dnac.tag.update_tag(id=created_tag.response[0].id, 
                                         name='Updated ' + created_tag.response[0].name,
                                         description='DNA demo tag')
        
        print(dnac.task.get_task_by_id(task_id=update_tag.response.taskId).response.progress)
        
        # Retrieved updated
        updated_tag = dnac.tag.get_tag(name='Updated dna Demo')
        print(updated_tag)
    else:
        # Get task error details 
        print('Unfortunately ', task_demo_tag.response.progress)
        print('Reason: ', task_demo_tag.response.failureReason)

    # Advance usage example using Custom Caller functions
    # Define the get_global_credentials and create_netconf_credentials functions
    # under the custom_caller wrapper.
    # Call them with:
    #     dnac.custom_caller.get_global_credentials('NETCONF')
    #     dnac.custom_caller.create_netconf_credentials('65533')
    def setup_custom():
        dnac.custom_caller.add_api('get_global_credentials',
                                lambda credential_type:
                                    dnac.custom_caller.call_api(
                                        'GET',
                                        '/dna/intent/api/v1/global-credential',
                                        params={
                                            'credentialSubType': credential_type
                                        }).response
                                )
        dnac.custom_caller.add_api('create_netconf_credentials',
                                lambda port:
                                    dnac.custom_caller.call_api(
                                        'POST',
                                        '/dna/intent/api/v1/global-credential/netconf',
                                        json=[{
                                            "netconfPort": port
                                        }])
                                )

    # Add the custom API calls to the connection object under the custom_caller wrapper
    setup_custom()
    # Call the newly added functions
    dnac.custom_caller.create_netconf_credentials('65533')
    print(dnac.custom_caller.get_global_credentials('NETCONF'))


Introduction
------------
Check out the complete Introduction_

**dnacentersdk handles all of this for you:**

+ Reads your DNA Center credentials from environment variables.

+ Reads your DNA Center API version from environment variable DNA_CENTER_VERSION.

+ Controls whether to verify the server's TLS certificate or not according to the verify parameter.

+ Reads your DNA Center debug from environment variable DNA_CENTER_DEBUG. Boolean.

+ Wraps and represents all DNA Center API calls as a simple hierarchical tree of
  native-Python methods

+ If your Python IDE supports **auto-completion** (like `PyCharm_`), you can
  navigate the available methods and object attributes right within your IDE

+ Represents all returned JSON objects as native Python objects - you can
  access all of the object's attributes using native *dot.syntax*

+ **Automatic Rate-Limit Handling**  Sending a lot of requests to DNA Center?
  Don't worry; we have you covered.  DNA Center will respond with a rate-limit
  response, which will automatically be caught and "handled" for you.

+ **Refresh token** Each time the token becomes invalid, the SDK will generate a new valid token for you.

Installation
------------

Installing and upgrading dnacentersdk is easy:

**Install via PIP**

.. code-block:: bash

    $ pip install dnacentersdk

**Upgrading to the latest Version**

.. code-block:: bash

    $ pip install dnacentersdk --upgrade


Compatibility matrix
--------------------
The following table shows the supported versions.

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - Cisco DNA Center version
     - Python "dnacentersdk" version
   * - 2.2.2.3
     - 2.3.3
   * - 2.2.3.3
     - 2.4.11
   * - 2.3.3.0
     - 2.5.6
   * - 2.3.5.3
     - 2.6.11
   * - 2.3.7.6
     - 2.7.4

   

If your SDK is older please consider updating it first.

Documentation
-------------

**Excellent documentation is now available at:**
https://dnacentersdk.readthedocs.io

Check out the Quickstart_ to dive in and begin using dnacentersdk.


Release Notes
-------------

Please see the releases_ page for release notes on the incremental functionality and bug fixes incorporated into the published releases.


Questions, Support & Discussion
-------------------------------

dnacentersdk is a *community developed* and *community supported* project.  If you experience any issues using this package, please report them using the issues_ page.


Contribution
------------

dnacentersdk_ is a community development projects.  Feedback, thoughts, ideas, and code contributions are welcome!  Please see the `Contributing`_ guide for more information.


Inspiration
------------

This library is inspired by the webexteamssdk_  library


Changelog
---------

All notable changes to this project will be documented in the CHANGELOG_ file.

The development team may make additional name changes as the library evolves with the Cisco DNA Center APIs.


*Copyright (c) 2019-2021 Cisco Systems.*

.. _Introduction: https://dnacentersdk.readthedocs.io/en/latest/api/intro.html
.. _dnacentersdk.readthedocs.io: https://dnacentersdk.readthedocs.io
.. _Quickstart: https://dnacentersdk.readthedocs.io/en/latest/api/quickstart.html
.. _dnacentersdk: https://github.com/cisco-en-programmability/dnacentersdk
.. _issues: https://github.com/cisco-en-programmability/dnacentersdk/issues
.. _pull requests: https://github.com/cisco-en-programmability/dnacentersdk/pulls
.. _releases: https://github.com/cisco-en-programmability/dnacentersdk/releases
.. _the repository: dnacentersdk_
.. _pull request: `pull requests`_
.. _Contributing: https://github.com/cisco-en-programmability/dnacentersdk/blob/master/docs/contributing.rst
.. _webexteamssdk: https://github.com/CiscoDevNet/webexteamssdk
.. _CHANGELOG: https://github.com/cisco-en-programmability/dnacentersdk/blob/main/CHANGELOG.md

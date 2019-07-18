=============
dnacentersdk
=============

*Work with the DNA Center APIs in native Python!*

-------------------------------------------------------------------------------

**dnacentersdk** is a *community developed* Python library for working with the DNA Center APIs.  Our goal is to make working with DNA Center in Python a *native* and *natural* experience!

.. code-block:: python

    from dnacentersdk import api

    dnac = api.DNACenterAPI(username="devnetuser", password="Cisco123!")

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

That's more than 10 DNA Center API calls in less than 41 lines of code (with comments, whitespaces and print statemets).

dnacentersdk makes your life better...  `Learn how!`__

__ Introduction_


Installation
------------

Installing and upgrading dnacentersdk is easy:

**Install via PIP**

.. code-block:: bash

    $ pip install dnacentersdk

**Upgrading to the latest Version**

.. code-block:: bash

    $ pip install dnacentersdk --upgrade


Documentation
-------------

**Excellent documentation is now available at:**
http://dnacentersdk.readthedocs.io

Check out the Quickstart_ to dive in and begin using dnacentersdk.


Release Notes
-------------

Please see the releases_ page for release notes on the incremental functionality and bug fixes incorporated into the published releases.


Questions, Support & Discussion
-------------------------------

dnacentersdk is a *community developed* and *community supported* project.  If you experience any issues using this package, please report them using the issues_ page.

Please join the `Python DNA Center Devs`__ DNA Center space to ask questions, join the discussion, and share your projects and creations.

__ Community_


Contribution
------------

dnacentersdk_ is a community development projects.  Feedback, thoughts, ideas, and code contributions are welcome!  Please see the `Contributing`_ guide for more information.


*Copyright (c) 2019 Cisco and/or its affiliates.*

.. _Introduction: http://dnacentersdk.readthedocs.io/en/latest/user/intro.html
.. _dnacentersdk.readthedocs.io: https://dnacentersdk.readthedocs.io
.. _Quickstart: http://dnacentersdk.readthedocs.io/en/latest/user/quickstart.html
.. _examples: https://github.com/zapodeanu/dnacentersdk/tree/master/examples
.. _dnacentersdk: https://github.com/zapodeanu/dnacentersdk
.. _issues: https://github.com/zapodeanu/dnacentersdk/issues
.. _Community: #
.. _projects: https://github.com/zapodeanu/dnacentersdk/projects
.. _pull requests: https://github.com/zapodeanu/dnacentersdk/pulls
.. _releases: https://github.com/zapodeanu/dnacentersdk/releases
.. _the repository: dnacentersdk_
.. _pull request: `pull requests`_
.. _Contributing: https://github.com/zapodeanu/dnacentersdk/blob/master/docs/contributing.rst

..
   _to_do: Change urls.
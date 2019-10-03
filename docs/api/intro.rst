.. _Introduction:

============
Introduction
============


Work with the DNA Center APIs in Native Python!
------------------------------------------------

Sure, working with the DNA Center APIs is easy (see
`api_docs`_).  They are RESTful,  naturally structured,
require only a simple Access Token for authentication, and the data is
elegantly represented in intuitive JSON.  What could be easier?

.. code-block:: python

    import requests

    URL = 'https://sandboxdnac2.cisco.com:443/dna/intent/api/v1/network-device' 
    ACCESS_TOKEN = '<your_access_token>'

    family = '<family_name>'
    headers = {'X-Auth-Token': ACCESS_TOKEN,
               'Content-type': 'application/json;charset=utf-8'}
    params_data = { 'family': family }
    response = requests.get(URL, params=params_data, headers=headers)
    if response.status_code == 200:
        device_response = response.json['response']
        for device in device_response:
            print('{:20s}{}'.format(device['hostname'], device['upTime']))
    else:
        # Oops something went wrong...  Better do something about it.
        print(response.status_code, response.text)

Like I said, EASY.  However, in use, the code can become rather repetitive...

- You have to setup the environment every time
- You have to remember URLs, request parameters and JSON formats
  (or reference the docs)
- You have to parse the returned JSON and work with multiple layers of list
  and dictionary indexes


Enter **dnacentersdk**, a simple API wrapper that wraps all of the DNA Center API
calls and returned JSON objects within native Python objects and methods.

With dnacentersdk, the above Python code can be consolidated to the following:

.. code-block:: python

    from dnacentersdk import api

    dnac = api.DNACenterAPI(base_url='https://sandboxdnac2.cisco.com:443', version='1.3.0')
    # Or even just dnac = api.DNACenterAPI() as base_url and version have those values.
    try:
        devices = dnac.devices.get_device_list(family='Switches and Hubs')
        for device in devices.response:
            print('{:20s}{}'.format(device.hostname, device.upTime))
    except ApiError as e:
        print(e)


**dnacentersdk handles all of this for you:**

+ Reads your DNA Center credentials from environment variables (DNA_CENTER_ENCODED_AUTH, DNA_CENTER_USERNAME, DNA_CENTER_PASSWORD)

+ Reads your DNA Center API version from environment variable DNA_CENTER_VERSION. Supported versions: '1.2.10' and '1.3.0'. Now with version and base_url, you have more control.

+ Controls whether to verify the server's TLS certificate or not according to the verify parameter.

+ Reads your DNA Center debug from environment variable DNA_CENTER_DEBUG. Boolean, it controls whether to log information about DNA Center APIs' request and response process.

+ Wraps and represents all DNA Center API calls as a simple hierarchical tree of
  native-Python methods (with default arguments provided everywhere possible!)

+ If your Python IDE supports **auto-completion** (like PyCharm_), you can
  navigate the available methods and object attributes right within your IDE

+ Represents all returned JSON objects as native Python objects - you can
  access all of the object's attributes using native *dot.syntax*

+ **Automatic Rate-Limit Handling**  Sending a lot of requests to DNA Center?
  Don't worry; we have you covered.  DNA Center will respond with a rate-limit
  response, which will automatically be caught and "handled" for you.  Your
  requests and script will automatically be "paused" for the amount of time
  specified by DNA Center, while we wait for the DNA Center rate-limit timer to cool
  down.  After the cool-down, your request will automatically be retried, and
  your script will continue to run as normal.  Handling all of this requires
  zero (0) changes to your code - you're welcome.  😎

  Just know that if you are are sending a lot of requests, your script might
  take longer to run if your requests are getting rate limited.


All of this, combined, lets you do powerful things simply:

.. code-block:: python

    from dnacentersdk import api

    # Create a DNACenterAPI connection object; it uses DNA Center sandbox URL, username and password, with DNA Center API version 1.2.10.
    dnac = api.DNACenterAPI(username="devnetuser", password="Cisco123!", base_url="https://sandboxdnac2.cisco.com:443", version='1.2.10')

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

Head over to the :ref:`Quickstart` page to begin working with the
**DNA Center APIs in native Python**!


.. _MITLicense:

MIT License
-----------

dnacentersdk is currently licensed under the `MIT Open Source License`_, and
distributed as a source distribution (no binaries) via :ref:`PyPI <Install>`,
and the complete :ref:`source code <Source Code>` is available on GitHub.

dnacentersdk License
---------------------

.. include:: ../../LICENSE


*Copyright (c) 2019 Cisco and/or its affiliates.*


.. _MIT Open Source License: https://opensource.org/licenses/MIT
.. _api_docs: https://developer.cisco.com/site/dna-center-rest-api/#
.. _PyCharm: https://www.jetbrains.com/pycharm/


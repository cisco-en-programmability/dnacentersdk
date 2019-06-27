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

    URL = 'https://sandboxdnac.cisco.com:443/api/v1/network-device' 
    ACCESS_TOKEN = '<your_access_token>'
    ROOM_ID = '<room_id>'

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

    dnac = api.DNACenterAPI()
    try:
        devices = dnac.devices.get_device_list(param_family='Switches and Hubs')
        for device in devices.response:
            print('{:20s}{}'.format(device.hostname, device.upTime))
    except ApiError as e:
        print(e)


**dnacentersdk handles all of this for you:**

+ Reads your DNA Center access token from a ``DNA_CENTER_ACCESS_TOKEN`` environment
  variable

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

    dnac = api.DNACenterAPI(username="devnetuser", password="Cisco123!")

    # Find all devices that have 'Switches and Hubs' in their family
    devices = dnac.devices.get_device_list(param_family='Switches and Hubs')

    # Print all of demo devices
    for device in devices.response:
        print('{:20s}{}'.format(device.hostname, device.upTime))

    #TODO: Add more examples.


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

.. _Contributing:

============
Contributing
============

*dnacentersdk* is a community development project.  Feedback, thoughts, ideas, and code contributions are most welcome!


How to contribute Feedback, Issues, Thoughts and Ideas
=======================================================

Please use the `issues`_ page to report issues or post ideas for enhancement.

Join our `dnacentersdk - DNA Center SDK - Python Community Contributors <#>`_ DNA Center space to join the conversation with other contributors to this project.



Interested in Contributing Code?
================================


Developer Scripts
-----------------

We have created some scripts to automate everyday actions needed when working on the project.  Please see the `script`_ directory, and it's README for more information.


Notes on the Test Suite
-----------------------

To test all the API endpoints, the account that you use for testing must be an *admin* user for your DNA Center Organization.  Additionally, you should know that that the testing process creates some test 
tags, sites, devices and etc. as part of executing the test suite. We strongly recommend *NOT* running the test suite using your personal DNA Center account (not that you can't; it's just that you probably don't want it cluttering your account with all these test artifacts).

If you cannot create a test account with *admin* privileges or configure your environment to run the test suite locally, you may always submit your code via a pull request.  Our GitHub/Travis CI setup runs the test suite against all pull requests.  All tests must pass before your pull request is accepted.


Contributing Code - Using the CI Automated Testing
--------------------------------------------------

1. Check for open `issues`_ or create a new *issue* for the item you want to work on and make sure to comment and let us know that you are working on it.

2. Fork a copy of the `repository`_ and clone your forked repository to your development environment.

3. Run ``script/setup`` to install the development dependencies and setup your environment.

4. Configure the following environment variables in your development environment:

   * ``TEST_DNA_CENTER_ENCODED_AUTH`` - Your test account's DNA Center encoded_auth (username:password encoded in base 64). This variable has priority over username and password.

   * ``TEST_DNA_CENTER_USERNAME`` - Your test account's DNA Center username.

   * ``TEST_DNA_CENTER_PASSWORD`` - Your test account's DNA Center password.

   * ``DEBUG_ENVIRONMENT_VARIABLE`` - Your test's debug variable, which controls whether to log information about DNA Center APIs' request and response process.

   * ``VERSION_ENVIRONMENT_VARIABLE`` - The DNA Center API's version for your test account.


5. Add your code to your forked repository.

   If you are creating some new feature or functionality (excellent!), please also write a `test`_ to verify that your code works as expected.

6. We follow `PEP8`_ reasonably strictly for this project.  Please make sure your code passes the linter.

   Run ``script/test lint`` or simply run ``flake8`` from the project root.

7. Commit your changes.

8. Submit a `pull request`_.  The GitHub/Travis CI system runs the test suite against your pull request code.  If any tests fail, please review your changes.  If everything looks good, we will gladly merge your request!


Contributing Code - Running the Test Suite Locally
--------------------------------------------------

1. Check for open `issues`_ or create a new 'issue' for the item you want to work on and make sure to comment and let us know that you are working on it.

2. Fork a copy of the `repository`_ and clone your forked repository to your development environment.

   Run ``script/setup`` to install the development dependencies and setup your environment.

3. Configure the following environment variables in your development environment:

   * ``TEST_DNA_CENTER_ENCODED_AUTH`` - Your test account's DNA Center encoded_auth (username:password encoded in base 64). This variable has priority over username and password.

   * ``TEST_DNA_CENTER_USERNAME`` - Your test account's DNA Center username.

   * ``TEST_DNA_CENTER_PASSWORD`` - Your test account's DNA Center password.

   * ``DEBUG_ENVIRONMENT_VARIABLE`` - Your test's debug variable, which controls whether to log information about DNA Center APIs' request and response process.

   * ``VERSION_ENVIRONMENT_VARIABLE`` - The DNA Center API's version for your test account.


   *Example:*

   .. code-block:: bash

       #!/usr/bin/env bash
       export TEST_DNA_CENTER_ENCODED_AUTH="<test account's username:password encoded in base 64>"

4. Configure the following config variables in your development configuration as you see fit:

   * ``LOCAL_SOFTWARE_IMAGE_NAME`` - Your test local software image name for test_swim.
   * ``LOCAL_SOFTWARE_IMAGE_PATH`` - Your test local software image path for test_swim.
   * ``BORDER_DEVICE_SDA_FABRIC_PATH`` - Your test border device sda fabric path for test_fabric_wired.
   * ``NEW_ENTERPRISE_SSID_NAME`` - Your test new enterprise ssid name for test_non_fabric_wireless.
   * ``NEW_MANAGED_APLOCATIONS`` - Your test new managed aplocations for test_non_fabric_wireless.
   * ``SITE_PROFILE_DEVICE_IP`` - Your test site profile device ip for test_site_profile.
   * ``MERAKI_ORG_ID`` - Your test meraki org id (list of strings) for test_devices.
   * ``NEW_VIRTUAL_ACCOUNT_PAYLOAD`` - Your test new virtual account payload for test_pnp.

5. Add your code to your forked repository.

   If you are creating some new feature or functionality (excellent!), please also write a `test`_ to verify that your code works as expected.

6. We follow `PEP8`_ reasonably strictly for this project.  Please make sure your code passes the linter.

   Run ``script/test lint`` from the project root.

7. Commit your changes.

8. Ensure your code passes all of the default tests.

   Run ``script/test`` and ensure all tests execute successfully.

9. Submit a `pull request`_.  If everything looks good, we will gladly merge your request!


.. _script: https://github.com/cisco-en-programmability/dnacentersdk/tree/master/script
.. _issues: https://github.com/cisco-en-programmability/dnacentersdk/issues
.. _repository: https://github.com/cisco-en-programmability/dnacentersdk
.. _test: https://github.com/cisco-en-programmability/dnacentersdk/tree/master/tests
.. _PEP8: https://www.python.org/dev/peps/pep-0008/
.. _pull request: https://github.com/cisco-en-programmability/dnacentersdk/pulls


..
   _comment: Change `dnacentersdk - DNA Center SDK - Python Community Contributors <#>` to valid url.
..
   _to_do: Check if it has a working CI configuration, else remove CI (Github and Travis) doc's references.
..
   _to_do: Change github urls.

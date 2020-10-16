.. _Contributing:

============
Contributing
============

*dnacentersdk* is a community development project.  Feedback, thoughts, ideas, and code contributions are most welcome!


How to contribute Feedback, Issues, Thoughts and Ideas
=======================================================

Please use the `issues`_ page to report issues or post ideas for enhancement.


Interested in Contributing Code?
================================


Developer Scripts
-----------------

We have created some scripts to automate everyday actions needed when working on the project.  Please see the `script`_ directory, and it's README for more information.


Notes on the Test Suite
-----------------------

The test suite is grouped by DNAC versions supported in the DNAC SDK.

The test suite uses a mockup server, instead of calling to a DNAC server directly.

The mockup server is not perfect, that is why it is sometimes necessary to rerun a failed test, we do this by using `pytest-rerunfailures`.
On the `script/test` file, you can find the `pytest-rerunfailures` settings, adjust them locally if strictly necessary.


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

   * ``VERSION_ENVIRONMENT_VARIABLE`` - The DNA Center API's version used to test the SDK.


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

   * ``VERSION_ENVIRONMENT_VARIABLE`` - The DNA Center API's version used to test the SDK.


   *Example:*

   .. code-block:: bash

       #!/usr/bin/env bash
       export TEST_DNA_CENTER_ENCODED_AUTH="<test account's username:password encoded in base 64>"

4. Add your code to your forked repository.

   If you are creating some new feature or functionality (excellent!), please also write a `test`_ to verify that your code works as expected.

5. We follow `PEP8`_ reasonably strictly for this project.  Please make sure your code passes the linter.

   Run ``script/test lint`` from the project root.

6. Commit your changes.

7. Ensure your code passes all of the default tests for all the involved DNAC versions.

   Run ``script/test`` and ensure all tests execute successfully.

8. Submit a `pull request`_.  If everything looks good, we will gladly merge your request!


.. _script: https://github.com/cisco-en-programmability/dnacentersdk/tree/master/script
.. _issues: https://github.com/cisco-en-programmability/dnacentersdk/issues
.. _repository: https://github.com/cisco-en-programmability/dnacentersdk
.. _test: https://github.com/cisco-en-programmability/dnacentersdk/tree/master/tests
.. _PEP8: https://www.python.org/dev/peps/pep-0008/
.. _pull request: https://github.com/cisco-en-programmability/dnacentersdk/pulls

# -*- coding: utf-8 -*-
"""IPython Project Console.

Used to interactively work with the main package contents in IPython.
"""


import dnacentersdk

__copyright__ = "Copyright (c) 2019 Cisco and/or its affiliates."
__license__ = "MIT"


api = dnacentersdk.DNACenterAPI(verify=False)

# -*- coding: utf-8 -*-
"""Cisco Catalyst Center GetSiteAnalyticsForTheChildSitesOfGivenParentSiteAndOtherQueryParametersV1
data model.

Copyright (c) 2024 Cisco Systems.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


import json
from builtins import *

import fastjsonschema

from dnacentersdk.exceptions import MalformedRequest


class JSONSchemaValidatorFd376C6A5D9382D5Bee853C43031(object):
    """GetSiteAnalyticsForTheChildSitesOfGivenParentSiteAndOtherQueryPara
    metersV1 request schema definition."""

    def __init__(self):
        super(JSONSchemaValidatorFd376C6A5D9382D5Bee853C43031, self).__init__()
        self._validator = fastjsonschema.compile(
            json.loads(
                """{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "page": {
                "properties": {
                "count": {
                "type": "integer"
                },
                "limit": {
                "type": "integer"
                },
                "offset": {
                "type": "integer"
                },
                "sortBy": {
                "properties": {
                "name": {
                "type": "string"
                },
                "order": {
                "type": "string"
                }
                },
                "type": "object"
                }
                },
                "type": "object"
                },
                "response": {
                "items": {
                "properties": {
                "apCount": {
                "type": "integer"
                },
                "connectionSpeedAverage": {
                "type": "integer"
                },
                "connectionSpeedClientCount": {
                "type": "integer"
                },
                "connectionSpeedFailureCount": {
                "type": "integer"
                },
                "connectionSpeedFailureImpactedEntities": {
                "properties": {
                "apCount": {
                "type": "integer"
                },
                "buildingCount": {
                "type": "integer"
                },
                "floorCount": {
                "type": "integer"
                },
                "sitesCount": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "connectionSpeedFailureMetrics": {
                "properties": {
                "failureApCount": {
                "type": "integer"
                },
                "failureClientCount": {
                "type": "integer"
                },
                "failurePercentage": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "connectionSpeedImpactedEntities": {
                "properties": {
                "apCount": {
                "type": "integer"
                },
                "buildingCount": {
                "type": "integer"
                },
                "floorCount": {
                "type": "integer"
                },
                "sitesCount": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "connectionSpeedSuccessCount": {
                "type": "integer"
                },
                "connectionSpeedSuccessPercentage": {
                "type": "integer"
                },
                "connectionSpeedTotalCount": {
                "type": "integer"
                },
                "coverageAverage": {
                "type": "integer"
                },
                "coverageClientCount": {
                "type": "integer"
                },
                "coverageFailureCount": {
                "type": "integer"
                },
                "coverageFailureImpactedEntities": {
                "properties": {
                "apCount": {
                "type": "integer"
                },
                "buildingCount": {
                "type": "integer"
                },
                "floorCount": {
                "type": "integer"
                },
                "sitesCount": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "coverageFailureMetrics": {
                "properties": {
                "failureApCount": {
                "type": "integer"
                },
                "failureClientCount": {
                "type": "integer"
                },
                "failurePercentage": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "coverageImpactedEntities": {
                "properties": {
                "apCount": {
                "type": "integer"
                },
                "buildingCount": {
                "type": "integer"
                },
                "floorCount": {
                "type": "integer"
                },
                "sitesCount": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "coverageSuccessCount": {
                "type": "integer"
                },
                "coverageSuccessPercentage": {
                "type": "integer"
                },
                "coverageTotalCount": {
                "type": "integer"
                },
                "id": {
                "type": "string"
                },
                "onboardingAttemptsClientCount": {
                "type": "integer"
                },
                "onboardingAttemptsFailureCount": {
                "type": "integer"
                },
                "onboardingAttemptsFailureImpactedEntities": {
                "properties": {
                "apCount": {
                "type": "integer"
                },
                "buildingCount": {
                "type": "integer"
                },
                "floorCount": {
                "type": "integer"
                },
                "sitesCount": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "onboardingAttemptsFailureMetrics": {
                "properties": {
                "failureApCount": {
                "type": "integer"
                },
                "failureClientCount": {
                "type": "integer"
                },
                "failurePercentage": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "onboardingAttemptsImpactedEntities": {
                "properties": {
                "apCount": {
                "type": "integer"
                },
                "buildingCount": {
                "type": "integer"
                },
                "floorCount": {
                "type": "integer"
                },
                "sitesCount": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "onboardingAttemptsSuccessCount": {
                "type": "integer"
                },
                "onboardingAttemptsSuccessPercentage": {
                "type": "integer"
                },
                "onboardingAttemptsTotalCount": {
                "type": "integer"
                },
                "onboardingDurationAverage": {
                "type": "integer"
                },
                "onboardingDurationClientCount": {
                "type": "integer"
                },
                "onboardingDurationFailureCount": {
                "type": "integer"
                },
                "onboardingDurationFailureImpactedEntities": {
                "properties": {
                "apCount": {
                "type": "integer"
                },
                "buildingCount": {
                "type": "integer"
                },
                "floorCount": {
                "type": "integer"
                },
                "sitesCount": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "onboardingDurationFailureMetrics": {
                "properties": {
                "failureApCount": {
                "type": "integer"
                },
                "failureClientCount": {
                "type": "integer"
                },
                "failurePercentage": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "onboardingDurationImpactedEntities": {
                "properties": {
                "apCount": {
                "type": "integer"
                },
                "buildingCount": {
                "type": "integer"
                },
                "floorCount": {
                "type": "integer"
                },
                "sitesCount": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "onboardingDurationSuccessCount": {
                "type": "integer"
                },
                "onboardingDurationSuccessPercentage": {
                "type": "integer"
                },
                "onboardingDurationTotalCount": {
                "type": "integer"
                },
                "roamingAttemptsClientCount": {
                "type": "integer"
                },
                "roamingAttemptsFailureCount": {
                "type": "integer"
                },
                "roamingAttemptsFailureImpactedEntities": {
                "properties": {
                "apCount": {
                "type": "integer"
                },
                "buildingCount": {
                "type": "integer"
                },
                "floorCount": {
                "type": "integer"
                },
                "sitesCount": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "roamingAttemptsFailureMetrics": {
                "properties": {
                "failureApCount": {
                "type": "integer"
                },
                "failureClientCount": {
                "type": "integer"
                },
                "failurePercentage": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "roamingAttemptsImpactedEntities": {
                "properties": {
                "apCount": {
                "type": "integer"
                },
                "buildingCount": {
                "type": "integer"
                },
                "floorCount": {
                "type": "integer"
                },
                "sitesCount": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "roamingAttemptsSuccessCount": {
                "type": "integer"
                },
                "roamingAttemptsSuccessPercentage": {
                "type": "integer"
                },
                "roamingAttemptsTotalCount": {
                "type": "integer"
                },
                "roamingDurationAverage": {
                "type": "integer"
                },
                "roamingDurationClientCount": {
                "type": "integer"
                },
                "roamingDurationFailureCount": {
                "type": "integer"
                },
                "roamingDurationFailureImpactedEntities": {
                "properties": {
                "apCount": {
                "type": "integer"
                },
                "buildingCount": {
                "type": "integer"
                },
                "floorCount": {
                "type": "integer"
                },
                "sitesCount": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "roamingDurationFailureMetrics": {
                "properties": {
                "failureApCount": {
                "type": "integer"
                },
                "failureClientCount": {
                "type": "integer"
                },
                "failurePercentage": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "roamingDurationImpactedEntities": {
                "properties": {
                "apCount": {
                "type": "integer"
                },
                "buildingCount": {
                "type": "integer"
                },
                "floorCount": {
                "type": "integer"
                },
                "sitesCount": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "roamingDurationSuccessCount": {
                "type": "integer"
                },
                "roamingDurationSuccessPercentage": {
                "type": "integer"
                },
                "roamingDurationTotalCount": {
                "type": "integer"
                },
                "siteHierarchy": {
                "type": "string"
                },
                "siteHierarchyId": {
                "type": "string"
                },
                "siteId": {
                "type": "string"
                },
                "siteType": {
                "type": "string"
                }
                },
                "type": "object"
                },
                "type": "array"
                },
                "version": {
                "type": "string"
                }
                },
                "type": "object"
                }""".replace(
                    "\n" + " " * 16, ""
                )
            )
        )

    def validate(self, request):
        try:
            self._validator(request)
        except fastjsonschema.exceptions.JsonSchemaException as e:
            raise MalformedRequest(
                "{} is invalid. Reason: {}".format(request, e.message)
            )

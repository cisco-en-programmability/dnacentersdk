# -*- coding: utf-8 -*-
"""Cisco Catalyst Center ReadFabricSitesWithHealthSummaryFromIdV1 data model.

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


class JSONSchemaValidatorDaad662049Da50A985DbD37A3A7Fd28C(object):
    """ReadFabricSitesWithHealthSummaryFromIdV1 request schema
    definition."""
    def __init__(self):
        super(JSONSchemaValidatorDaad662049Da50A985DbD37A3A7Fd28C, self).__init__()
        self._validator = fastjsonschema.compile(json.loads(
            '''{
                "$schema": "http://json-schema.org/draft-04/schema#",
                "properties": {
                "response": {
                "properties": {
                "aaaStatusFairHealthDeviceCount": {
                "type": "integer"
                },
                "aaaStatusGoodHealthDeviceCount": {
                "type": "integer"
                },
                "aaaStatusGoodHealthPercentage": {
                "type": "integer"
                },
                "aaaStatusPoorHealthDeviceCount": {
                "type": "integer"
                },
                "aaaStatusTotalHealthDeviceCount": {
                "type": "integer"
                },
                "associatedL2VnCount": {
                "type": "integer"
                },
                "associatedL3VnCount": {
                "type": "integer"
                },
                "bgpBgpSiteFairHealthDeviceCount": {
                "type": "integer"
                },
                "bgpBgpSiteGoodHealthDeviceCount": {
                "type": "integer"
                },
                "bgpBgpSiteGoodHealthPercentage": {
                "type": "integer"
                },
                "bgpBgpSitePoorHealthDeviceCount": {
                "type": "number"
                },
                "bgpBgpSiteTotalHealthDeviceCount": {
                "type": "integer"
                },
                "bgpEvpnFairHealthDeviceCount": {
                "type": "number"
                },
                "bgpEvpnGoodHealthDeviceCount": {
                "type": "number"
                },
                "bgpEvpnGoodHealthPercentage": {
                "type": "object"
                },
                "bgpEvpnPoorHealthDeviceCount": {
                "type": "number"
                },
                "bgpEvpnTotalHealthDeviceCount": {
                "type": "number"
                },
                "bgpPeerInfraVnFairHealthDeviceCount": {
                "type": "number"
                },
                "bgpPeerInfraVnGoodHealthDeviceCount": {
                "type": "integer"
                },
                "bgpPeerInfraVnPoorHealthDeviceCount": {
                "type": "integer"
                },
                "bgpPeerInfraVnScoreGoodHealthPercentage": {
                "type": "integer"
                },
                "bgpPeerInfraVnTotalHealthDeviceCount": {
                "type": "integer"
                },
                "bgpPubsubSiteFairHealthDeviceCount": {
                "type": "integer"
                },
                "bgpPubsubSiteGoodHealthDeviceCount": {
                "type": "integer"
                },
                "bgpPubsubSiteGoodHealthPercentage": {
                "type": "integer"
                },
                "bgpPubsubSitePoorHealthDeviceCount": {
                "type": "number"
                },
                "bgpPubsubSiteTotalHealthDeviceCount": {
                "type": "integer"
                },
                "borderToControlPlaneFairHealthDeviceCount": {
                "type": "integer"
                },
                "borderToControlPlaneGoodHealthDeviceCount": {
                "type": "integer"
                },
                "borderToControlPlaneGoodHealthPercentage": {
                "type": "integer"
                },
                "borderToControlPlanePoorHealthDeviceCount": {
                "type": "number"
                },
                "borderToControlPlaneTotalHealthDeviceCount": {
                "type": "integer"
                },
                "connectivityFairHealthDeviceCount": {
                "type": "integer"
                },
                "connectivityGoodHealthDeviceCount": {
                "type": "integer"
                },
                "connectivityGoodHealthPercentage": {
                "type": "integer"
                },
                "connectivityPoorHealthDeviceCount": {
                "type": "integer"
                },
                "connectivityTotalHealthDeviceCount": {
                "type": "integer"
                },
                "controlPlaneFairHealthDeviceCount": {
                "type": "integer"
                },
                "controlPlaneGoodHealthDeviceCount": {
                "type": "integer"
                },
                "controlPlaneGoodHealthPercentage": {
                "type": "integer"
                },
                "controlPlanePoorHealthDeviceCount": {
                "type": "number"
                },
                "controlPlaneTotalHealthDeviceCount": {
                "type": "integer"
                },
                "ctsEnvDataDownloadFairHealthDeviceCount": {
                "type": "number"
                },
                "ctsEnvDataDownloadGoodHealthDeviceCount": {
                "type": "integer"
                },
                "ctsEnvDataDownloadGoodHealthPercentage": {
                "type": "integer"
                },
                "ctsEnvDataDownloadPoorHealthDeviceCount": {
                "type": "integer"
                },
                "ctsEnvDataDownloadTotalHealthDeviceCount": {
                "type": "integer"
                },
                "fairHealthDeviceCount": {
                "type": "integer"
                },
                "goodHealthDeviceCount": {
                "type": "integer"
                },
                "goodHealthPercentage": {
                "type": "integer"
                },
                "id": {
                "type": "string"
                },
                "infraFairHealthDeviceCount": {
                "type": "number"
                },
                "infraGoodHealthDeviceCount": {
                "type": "integer"
                },
                "infraGoodHealthPercentage": {
                "type": "integer"
                },
                "infraPoorHealthDeviceCount": {
                "type": "number"
                },
                "infraTotalHealthDeviceCount": {
                "type": "integer"
                },
                "lispSessionFairHealthDeviceCount": {
                "type": "number"
                },
                "lispSessionGoodHealthDeviceCount": {
                "type": "integer"
                },
                "lispSessionGoodHealthPercentage": {
                "type": "integer"
                },
                "lispSessionPoorHealthDeviceCount": {
                "type": "integer"
                },
                "lispSessionTotalHealthDeviceCount": {
                "type": "integer"
                },
                "name": {
                "type": "string"
                },
                "networkProtocol": {
                "type": "string"
                },
                "peerScoreFairHealthDeviceCount": {
                "type": "number"
                },
                "peerScoreGoodHealthDeviceCount": {
                "type": "number"
                },
                "peerScoreGoodHealthPercentage": {
                "type": "object"
                },
                "peerScorePoorHealthDeviceCount": {
                "type": "number"
                },
                "peerScoreTotalHealthDeviceCount": {
                "type": "number"
                },
                "poorHealthDeviceCount": {
                "type": "integer"
                },
                "portChannelFairHealthDeviceCount": {
                "type": "integer"
                },
                "portChannelGoodHealthDeviceCount": {
                "type": "integer"
                },
                "portChannelGoodHealthPercentage": {
                "type": "integer"
                },
                "portChannelPoorHealthDeviceCount": {
                "type": "integer"
                },
                "portChannelTotalHealthDeviceCount": {
                "type": "integer"
                },
                "pubsubInfraVnFairHealthDeviceCount": {
                "type": "integer"
                },
                "pubsubInfraVnGoodHealthDeviceCount": {
                "type": "integer"
                },
                "pubsubInfraVnGoodHealthPercentage": {
                "type": "integer"
                },
                "pubsubInfraVnPoorHealthDeviceCount": {
                "type": "integer"
                },
                "pubsubInfraVnTotalHealthDeviceCount": {
                "type": "integer"
                },
                "totalDeviceCount": {
                "type": "integer"
                }
                },
                "type": "object"
                }
                },
                "type": "object"
                }'''.replace("\n" + ' ' * 16, '')
        ))

    def validate(self, request):
        try:
            self._validator(request)
        except fastjsonschema.exceptions.JsonSchemaException as e:
            raise MalformedRequest(
                '{} is invalid. Reason: {}'.format(request, e.message)
            )

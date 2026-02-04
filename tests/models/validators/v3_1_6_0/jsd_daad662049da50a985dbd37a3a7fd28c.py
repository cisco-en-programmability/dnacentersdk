# -*- coding: utf-8 -*-
"""Cisco Catalyst Center ReadFabricSitesWithHealthSummaryFromId data model.

Copyright (c) 2025 Cisco Systems.

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

from __future__ import absolute_import, division, print_function, unicode_literals

import json
from builtins import *

import fastjsonschema

from dnacentersdk.exceptions import MalformedRequest


class JSONSchemaValidatorDaad662049Da50A985DbD37A3A7Fd28C(object):
    """ReadFabricSitesWithHealthSummaryFromId request schema definition."""
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
                "type": "number"
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
                "type": "number"
                },
                "bgpBgpSitePoorHealthDeviceCount": {
                "type": "integer"
                },
                "bgpBgpSiteTotalHealthDeviceCount": {
                "type": "integer"
                },
                "bgpEvpnFairHealthDeviceCount": {
                "type": "integer"
                },
                "bgpEvpnGoodHealthDeviceCount": {
                "type": "integer"
                },
                "bgpEvpnGoodHealthPercentage": {
                "type": "number"
                },
                "bgpEvpnPoorHealthDeviceCount": {
                "type": "integer"
                },
                "bgpEvpnTotalHealthDeviceCount": {
                "type": "integer"
                },
                "bgpPeerInfraVnFairHealthDeviceCount": {
                "type": "integer"
                },
                "bgpPeerInfraVnGoodHealthDeviceCount": {
                "type": "integer"
                },
                "bgpPeerInfraVnPoorHealthDeviceCount": {
                "type": "integer"
                },
                "bgpPeerInfraVnScoreGoodHealthPercentage": {
                "type": "number"
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
                "type": "number"
                },
                "bgpPubsubSitePoorHealthDeviceCount": {
                "type": "integer"
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
                "type": "number"
                },
                "borderToControlPlanePoorHealthDeviceCount": {
                "type": "integer"
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
                "type": "number"
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
                "type": "number"
                },
                "controlPlanePoorHealthDeviceCount": {
                "type": "integer"
                },
                "controlPlaneTotalHealthDeviceCount": {
                "type": "integer"
                },
                "ctsEnvDataDownloadFairHealthDeviceCount": {
                "type": "integer"
                },
                "ctsEnvDataDownloadGoodHealthDeviceCount": {
                "type": "integer"
                },
                "ctsEnvDataDownloadGoodHealthPercentage": {
                "type": "number"
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
                "type": "number"
                },
                "id": {
                "type": "string"
                },
                "infraFairHealthDeviceCount": {
                "type": "integer"
                },
                "infraGoodHealthDeviceCount": {
                "type": "integer"
                },
                "infraGoodHealthPercentage": {
                "type": "number"
                },
                "infraPoorHealthDeviceCount": {
                "type": "integer"
                },
                "infraTotalHealthDeviceCount": {
                "type": "integer"
                },
                "lispSessionFairHealthDeviceCount": {
                "type": "integer"
                },
                "lispSessionGoodHealthDeviceCount": {
                "type": "integer"
                },
                "lispSessionGoodHealthPercentage": {
                "type": "number"
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
                "type": "integer"
                },
                "peerScoreGoodHealthDeviceCount": {
                "type": "integer"
                },
                "peerScoreGoodHealthPercentage": {
                "type": "number"
                },
                "peerScorePoorHealthDeviceCount": {
                "type": "integer"
                },
                "peerScoreTotalHealthDeviceCount": {
                "type": "integer"
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
                "type": "number"
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
                "type": "number"
                },
                "pubsubInfraVnPoorHealthDeviceCount": {
                "type": "integer"
                },
                "pubsubInfraVnTotalHealthDeviceCount": {
                "type": "integer"
                },
                "totalDeviceCount": {
                "type": "integer"
                },
                "totalHealthDeviceCount": {
                "type": "integer"
                }
                },
                "type": "object"
                },
                "version": {
                "type": "string"
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

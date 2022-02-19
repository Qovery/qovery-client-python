"""
    Qovery API

    - Qovery is the fastest way to deploy your full-stack apps on any Cloud provider. - ℹ️ The API is stable and still in development.   # noqa: E501

    The version of the OpenAPI document: 1.0.1
    Contact: support+api+documentation@qovery.com
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import qovery
from qovery.model.community_usage import CommunityUsage
from qovery.model.community_usage_response import CommunityUsageResponse
from qovery.model.cost import Cost
from qovery.model.current_cost import CurrentCost
from qovery.model.paid_usage import PaidUsage
from qovery.model.paid_usage_response import PaidUsageResponse
from qovery.model.remaining_credits import RemainingCredits
globals()['CommunityUsage'] = CommunityUsage
globals()['CommunityUsageResponse'] = CommunityUsageResponse
globals()['Cost'] = Cost
globals()['CurrentCost'] = CurrentCost
globals()['PaidUsage'] = PaidUsage
globals()['PaidUsageResponse'] = PaidUsageResponse
globals()['RemainingCredits'] = RemainingCredits
from qovery.model.organization_current_cost_response import OrganizationCurrentCostResponse


class TestOrganizationCurrentCostResponse(unittest.TestCase):
    """OrganizationCurrentCostResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testOrganizationCurrentCostResponse(self):
        """Test OrganizationCurrentCostResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = OrganizationCurrentCostResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()

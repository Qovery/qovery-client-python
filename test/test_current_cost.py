"""
    Qovery API

    - Qovery is the fastest way to deploy your full-stack apps on any Cloud provider. - ℹ️ The API is stable and still in development.   # noqa: E501

    The version of the OpenAPI document: 1.0.3
    Contact: support+api+documentation@qovery.com
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import qovery
from qovery.model.cost import Cost
from qovery.model.remaining_credits import RemainingCredits
globals()['Cost'] = Cost
globals()['RemainingCredits'] = RemainingCredits
from qovery.model.current_cost import CurrentCost


class TestCurrentCost(unittest.TestCase):
    """CurrentCost unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCurrentCost(self):
        """Test CurrentCost"""
        # FIXME: construct object with mandatory attributes with example values
        # model = CurrentCost()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()

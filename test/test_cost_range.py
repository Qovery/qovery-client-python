# coding: utf-8

"""
    Qovery API

    - Qovery is the fastest way to deploy your full-stack apps on any Cloud provider. - ℹ️ The API is stable and still in development. 

    The version of the OpenAPI document: 1.0.3
    Contact: support+api+documentation@qovery.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from qovery.models.cost_range import CostRange  # noqa: E501

class TestCostRange(unittest.TestCase):
    """CostRange unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CostRange:
        """Test CostRange
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CostRange`
        """
        model = CostRange()  # noqa: E501
        if include_optional:
            return CostRange(
                min_cost_in_cents = 15000,
                min_cost = 150,
                max_cost_in_cents = 30000,
                max_cost = 300,
                currency_code = 'USD'
            )
        else:
            return CostRange(
                currency_code = 'USD',
        )
        """

    def testCostRange(self):
        """Test CostRange"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

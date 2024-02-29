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

from qovery.models.organization_current_cost import OrganizationCurrentCost  # noqa: E501

class TestOrganizationCurrentCost(unittest.TestCase):
    """OrganizationCurrentCost unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrganizationCurrentCost:
        """Test OrganizationCurrentCost
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrganizationCurrentCost`
        """
        model = OrganizationCurrentCost()  # noqa: E501
        if include_optional:
            return OrganizationCurrentCost(
                plan = 'FREE',
                remaining_trial_day = 56,
                renewal_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                cost = qovery.models.cost.Cost(
                    total_in_cents = 30000, 
                    total = 300, 
                    currency_code = 'USD', )
            )
        else:
            return OrganizationCurrentCost(
        )
        """

    def testOrganizationCurrentCost(self):
        """Test OrganizationCurrentCost"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

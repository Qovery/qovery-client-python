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
from qovery.model.base import Base
from qovery.model.organization_all_of import OrganizationAllOf
from qovery.model.organization_request import OrganizationRequest
from qovery.model.plan_enum import PlanEnum
globals()['Base'] = Base
globals()['OrganizationAllOf'] = OrganizationAllOf
globals()['OrganizationRequest'] = OrganizationRequest
globals()['PlanEnum'] = PlanEnum
from qovery.model.organization import Organization


class TestOrganization(unittest.TestCase):
    """Organization unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testOrganization(self):
        """Test Organization"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Organization()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()

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
from qovery.model.base_response import BaseResponse
from qovery.model.organization_request import OrganizationRequest
from qovery.model.organization_response_all_of import OrganizationResponseAllOf
globals()['BaseResponse'] = BaseResponse
globals()['OrganizationRequest'] = OrganizationRequest
globals()['OrganizationResponseAllOf'] = OrganizationResponseAllOf
from qovery.model.organization_response import OrganizationResponse


class TestOrganizationResponse(unittest.TestCase):
    """OrganizationResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testOrganizationResponse(self):
        """Test OrganizationResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = OrganizationResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()

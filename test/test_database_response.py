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
from qovery.model.base_response import BaseResponse
from qovery.model.database_request import DatabaseRequest
from qovery.model.reference_object import ReferenceObject
globals()['BaseResponse'] = BaseResponse
globals()['DatabaseRequest'] = DatabaseRequest
globals()['ReferenceObject'] = ReferenceObject
from qovery.model.database_response import DatabaseResponse


class TestDatabaseResponse(unittest.TestCase):
    """DatabaseResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDatabaseResponse(self):
        """Test DatabaseResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = DatabaseResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()

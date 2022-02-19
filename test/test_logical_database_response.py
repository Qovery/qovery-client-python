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
from qovery.model.logical_database_request import LogicalDatabaseRequest
from qovery.model.reference_object import ReferenceObject
globals()['BaseResponse'] = BaseResponse
globals()['LogicalDatabaseRequest'] = LogicalDatabaseRequest
globals()['ReferenceObject'] = ReferenceObject
from qovery.model.logical_database_response import LogicalDatabaseResponse


class TestLogicalDatabaseResponse(unittest.TestCase):
    """LogicalDatabaseResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testLogicalDatabaseResponse(self):
        """Test LogicalDatabaseResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = LogicalDatabaseResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()

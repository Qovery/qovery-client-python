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
from qovery.model.environment_response_all_of import EnvironmentResponseAllOf
from qovery.model.environment_response_all_of_cloud_provider import EnvironmentResponseAllOfCloudProvider
from qovery.model.reference_object import ReferenceObject
globals()['BaseResponse'] = BaseResponse
globals()['EnvironmentResponseAllOf'] = EnvironmentResponseAllOf
globals()['EnvironmentResponseAllOfCloudProvider'] = EnvironmentResponseAllOfCloudProvider
globals()['ReferenceObject'] = ReferenceObject
from qovery.model.environment_response import EnvironmentResponse


class TestEnvironmentResponse(unittest.TestCase):
    """EnvironmentResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEnvironmentResponse(self):
        """Test EnvironmentResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = EnvironmentResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()

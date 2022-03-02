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
from qovery.model.environment_variable_request import EnvironmentVariableRequest
from qovery.model.environment_variable_response_all_of import EnvironmentVariableResponseAllOf
from qovery.model.environment_variable_response_all_of_aliased_variable import EnvironmentVariableResponseAllOfAliasedVariable
from qovery.model.environment_variable_response_all_of_overridden_variable import EnvironmentVariableResponseAllOfOverriddenVariable
globals()['BaseResponse'] = BaseResponse
globals()['EnvironmentVariableRequest'] = EnvironmentVariableRequest
globals()['EnvironmentVariableResponseAllOf'] = EnvironmentVariableResponseAllOf
globals()['EnvironmentVariableResponseAllOfAliasedVariable'] = EnvironmentVariableResponseAllOfAliasedVariable
globals()['EnvironmentVariableResponseAllOfOverriddenVariable'] = EnvironmentVariableResponseAllOfOverriddenVariable
from qovery.model.environment_variable_response import EnvironmentVariableResponse


class TestEnvironmentVariableResponse(unittest.TestCase):
    """EnvironmentVariableResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEnvironmentVariableResponse(self):
        """Test EnvironmentVariableResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = EnvironmentVariableResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()

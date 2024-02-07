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

from qovery.models.environment_logs_error import EnvironmentLogsError

class TestEnvironmentLogsError(unittest.TestCase):
    """EnvironmentLogsError unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EnvironmentLogsError:
        """Test EnvironmentLogsError
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EnvironmentLogsError`
        """
        model = EnvironmentLogsError()
        if include_optional:
            return EnvironmentLogsError(
                tag = '',
                user_log_message = '',
                link = '',
                hint_message = '',
                underlying_error = qovery.models.environment_logs_error_underlying_error.EnvironmentLogs_error_underlying_error(
                    message = '', 
                    full_details = '', )
            )
        else:
            return EnvironmentLogsError(
        )
        """

    def testEnvironmentLogsError(self):
        """Test EnvironmentLogsError"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

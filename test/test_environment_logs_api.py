"""
    Qovery API

    - Qovery is the fastest way to deploy your full-stack apps on any Cloud provider. - ℹ️ The API is stable and still in development.   # noqa: E501

    The version of the OpenAPI document: 1.0.1
    Contact: support+api+documentation@qovery.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import qovery
from qovery.api.environment_logs_api import EnvironmentLogsApi  # noqa: E501


class TestEnvironmentLogsApi(unittest.TestCase):
    """EnvironmentLogsApi unit test stubs"""

    def setUp(self):
        self.api = EnvironmentLogsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_list_environment_log(self):
        """Test case for list_environment_log

        List environment deployment logs  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

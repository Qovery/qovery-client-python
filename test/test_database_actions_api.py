"""
    [BETA] Qovery API

    - Qovery is the fastest way to deploy your full-stack apps on any Cloud provider. - ℹ️ The API is in Beta and still in progress. Some endpoints are not available yet.   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support+api+documentation@qovery.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import qovery
from qovery.api.database_actions_api import DatabaseActionsApi  # noqa: E501


class TestDatabaseActionsApi(unittest.TestCase):
    """DatabaseActionsApi unit test stubs"""

    def setUp(self):
        self.api = DatabaseActionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_deploy_database(self):
        """Test case for deploy_database

        Deploy database   # noqa: E501
        """
        pass

    def test_restart_database(self):
        """Test case for restart_database

        Retart database  # noqa: E501
        """
        pass

    def test_stop_database(self):
        """Test case for stop_database

        Stop database  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

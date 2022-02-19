"""
    Qovery API

    - Qovery is the fastest way to deploy your full-stack apps on any Cloud provider. - ℹ️ The API is stable and still in development.   # noqa: E501

    The version of the OpenAPI document: 1.0.2
    Contact: support+api+documentation@qovery.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import qovery
from qovery.api.environment_main_calls_api import EnvironmentMainCallsApi  # noqa: E501


class TestEnvironmentMainCallsApi(unittest.TestCase):
    """EnvironmentMainCallsApi unit test stubs"""

    def setUp(self):
        self.api = EnvironmentMainCallsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_environment(self):
        """Test case for delete_environment

        Delete an environment  # noqa: E501
        """
        pass

    def test_edit_environment(self):
        """Test case for edit_environment

        Edit an environment  # noqa: E501
        """
        pass

    def test_get_environment(self):
        """Test case for get_environment

        Get environment by ID  # noqa: E501
        """
        pass

    def test_get_environment_status(self):
        """Test case for get_environment_status

        Get environment status  # noqa: E501
        """
        pass

    def test_list_environment_links(self):
        """Test case for list_environment_links

        List all URLs of the environment  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

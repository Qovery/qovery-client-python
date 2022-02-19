"""
    Qovery API

    - Qovery is the fastest way to deploy your full-stack apps on any Cloud provider. - ℹ️ The API is stable and still in development.   # noqa: E501

    The version of the OpenAPI document: 1.0.3
    Contact: support+api+documentation@qovery.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import qovery
from qovery.api.environments_api import EnvironmentsApi  # noqa: E501


class TestEnvironmentsApi(unittest.TestCase):
    """EnvironmentsApi unit test stubs"""

    def setUp(self):
        self.api = EnvironmentsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_environment(self):
        """Test case for create_environment

        Create an environment  # noqa: E501
        """
        pass

    def test_get_project_environment_service_number(self):
        """Test case for get_project_environment_service_number

        List total number of services for each environment of the project  # noqa: E501
        """
        pass

    def test_get_project_environment_status(self):
        """Test case for get_project_environment_status

        List environments statuses  # noqa: E501
        """
        pass

    def test_list_environment(self):
        """Test case for list_environment

        List environments  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

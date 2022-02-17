"""
    [BETA] Qovery API

    - Qovery is the fastest way to deploy your full-stack apps on any Cloud provider. - ℹ️ The API is in Beta and still in progress. Some endpoints are not available yet.   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support+api+documentation@qovery.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import qovery
from qovery.api.applications_api import ApplicationsApi  # noqa: E501


class TestApplicationsApi(unittest.TestCase):
    """ApplicationsApi unit test stubs"""

    def setUp(self):
        self.api = ApplicationsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_application(self):
        """Test case for create_application

        Create an application  # noqa: E501
        """
        pass

    def test_get_environment_application_current_instance(self):
        """Test case for get_environment_application_current_instance

        List running instances with CPU and RAM usage for each application  # noqa: E501
        """
        pass

    def test_get_environment_application_current_scale(self):
        """Test case for get_environment_application_current_scale

        List current scaling information for each application  # noqa: E501
        """
        pass

    def test_get_environment_application_current_storage(self):
        """Test case for get_environment_application_current_storage

        List current storage disk usage for each application  # noqa: E501
        """
        pass

    def test_get_environment_application_status(self):
        """Test case for get_environment_application_status

        List all environment applications statuses  # noqa: E501
        """
        pass

    def test_get_environment_application_supported_languages(self):
        """Test case for get_environment_application_supported_languages

        List supported languages  # noqa: E501
        """
        pass

    def test_list_application(self):
        """Test case for list_application

        List applications  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

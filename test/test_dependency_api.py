"""
    Qovery API

    - Qovery is the fastest way to deploy your full-stack apps on any Cloud provider. - ℹ️ The API is stable and still in development.   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support+api+documentation@qovery.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import qovery
from qovery.api.dependency_api import DependencyApi  # noqa: E501


class TestDependencyApi(unittest.TestCase):
    """DependencyApi unit test stubs"""

    def setUp(self):
        self.api = DependencyApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_application_dependency(self):
        """Test case for create_application_dependency

        Add application dependency to this application.  # noqa: E501
        """
        pass

    def test_list_application_dependency(self):
        """Test case for list_application_dependency

        List application dependencies  # noqa: E501
        """
        pass

    def test_remove_application_dependency(self):
        """Test case for remove_application_dependency

        Remove application dependency to this application.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

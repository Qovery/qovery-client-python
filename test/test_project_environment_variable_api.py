"""
    Qovery API

    - Qovery is the fastest way to deploy your full-stack apps on any Cloud provider. - ℹ️ The API is stable and still in development.   # noqa: E501

    The version of the OpenAPI document: 1.0.3
    Contact: support+api+documentation@qovery.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import qovery
from qovery.api.project_environment_variable_api import ProjectEnvironmentVariableApi  # noqa: E501


class TestProjectEnvironmentVariableApi(unittest.TestCase):
    """ProjectEnvironmentVariableApi unit test stubs"""

    def setUp(self):
        self.api = ProjectEnvironmentVariableApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_project_environment_variable(self):
        """Test case for create_project_environment_variable

        Add an environment variable to the project  # noqa: E501
        """
        pass

    def test_create_project_environment_variable_alias(self):
        """Test case for create_project_environment_variable_alias

        Create an environment variable alias at the project level  # noqa: E501
        """
        pass

    def test_create_project_environment_variable_override(self):
        """Test case for create_project_environment_variable_override

        Create an environment variable override at the project level  # noqa: E501
        """
        pass

    def test_delete_project_environment_variable(self):
        """Test case for delete_project_environment_variable

        Delete an environment variable from a project  # noqa: E501
        """
        pass

    def test_edit_project_environment_variable(self):
        """Test case for edit_project_environment_variable

        Edit an environment variable belonging to the project  # noqa: E501
        """
        pass

    def test_list_project_environment_variable(self):
        """Test case for list_project_environment_variable

        List project environment variables  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

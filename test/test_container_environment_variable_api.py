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

from qovery.api.container_environment_variable_api import ContainerEnvironmentVariableApi


class TestContainerEnvironmentVariableApi(unittest.TestCase):
    """ContainerEnvironmentVariableApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ContainerEnvironmentVariableApi()

    def tearDown(self) -> None:
        pass

    def test_create_container_environment_variable(self) -> None:
        """Test case for create_container_environment_variable

        Add an environment variable to the container
        """
        pass

    def test_create_container_environment_variable_alias(self) -> None:
        """Test case for create_container_environment_variable_alias

        Create an environment variable alias at the container level
        """
        pass

    def test_create_container_environment_variable_override(self) -> None:
        """Test case for create_container_environment_variable_override

        Create an environment variable override at the container level
        """
        pass

    def test_delete_container_environment_variable(self) -> None:
        """Test case for delete_container_environment_variable

        Delete an environment variable from a container
        """
        pass

    def test_edit_container_environment_variable(self) -> None:
        """Test case for edit_container_environment_variable

        Edit an environment variable belonging to the container
        """
        pass

    def test_import_container_environment_variable(self) -> None:
        """Test case for import_container_environment_variable

        Import variables
        """
        pass

    def test_list_container_environment_variable(self) -> None:
        """Test case for list_container_environment_variable

        List environment variables
        """
        pass


if __name__ == '__main__':
    unittest.main()

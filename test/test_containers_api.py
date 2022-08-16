"""
    Qovery API

    - Qovery is the fastest way to deploy your full-stack apps on any Cloud provider. - ℹ️ The API is stable and still in development.   # noqa: E501

    The version of the OpenAPI document: 1.0.3
    Contact: support+api+documentation@qovery.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import qovery
from qovery.api.containers_api import ContainersApi  # noqa: E501


class TestContainersApi(unittest.TestCase):
    """ContainersApi unit test stubs"""

    def setUp(self):
        self.api = ContainersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_auto_deploy_container_environments(self):
        """Test case for auto_deploy_container_environments

        NOT YET IMPLEMENTED - Auto deploy containers  # noqa: E501
        """
        pass

    def test_create_container(self):
        """Test case for create_container

        Create a container  # noqa: E501
        """
        pass

    def test_deploy_all_containers(self):
        """Test case for deploy_all_containers

        Deploy containers  # noqa: E501
        """
        pass

    def test_get_environment_container_current_scale(self):
        """Test case for get_environment_container_current_scale

        List current scaling information for each container  # noqa: E501
        """
        pass

    def test_get_environment_container_current_storage(self):
        """Test case for get_environment_container_current_storage

        List current storage disk usage for each containers  # noqa: E501
        """
        pass

    def test_get_environment_container_status(self):
        """Test case for get_environment_container_status

        List all environment container statuses  # noqa: E501
        """
        pass

    def test_list_container(self):
        """Test case for list_container

        List containers  # noqa: E501
        """
        pass

    def test_preview_container_environments(self):
        """Test case for preview_container_environments

        NOT YET IMPLEMENTED - Preview container environments  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

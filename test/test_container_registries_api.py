"""
    Qovery API

    - Qovery is the fastest way to deploy your full-stack apps on any Cloud provider. - ℹ️ The API is stable and still in development.   # noqa: E501

    The version of the OpenAPI document: 1.0.3
    Contact: support+api+documentation@qovery.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import qovery
from qovery.api.container_registries_api import ContainerRegistriesApi  # noqa: E501


class TestContainerRegistriesApi(unittest.TestCase):
    """ContainerRegistriesApi unit test stubs"""

    def setUp(self):
        self.api = ContainerRegistriesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_container_registry(self):
        """Test case for create_container_registry

        Create a container registry  # noqa: E501
        """
        pass

    def test_delete_container_registry(self):
        """Test case for delete_container_registry

        Delete a container registry  # noqa: E501
        """
        pass

    def test_list_available_container_registry(self):
        """Test case for list_available_container_registry

        List supported container registries  # noqa: E501
        """
        pass

    def test_list_container_registry(self):
        """Test case for list_container_registry

        List organization container registries  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
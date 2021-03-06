"""
    Qovery API

    - Qovery is the fastest way to deploy your full-stack apps on any Cloud provider. - ℹ️ The API is stable and still in development.   # noqa: E501

    The version of the OpenAPI document: 1.0.3
    Contact: support+api+documentation@qovery.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import qovery
from qovery.api.container_registry_api import ContainerRegistryApi  # noqa: E501


class TestContainerRegistryApi(unittest.TestCase):
    """ContainerRegistryApi unit test stubs"""

    def setUp(self):
        self.api = ContainerRegistryApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_edit_container_registry(self):
        """Test case for edit_container_registry

        Edit a container registry  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
